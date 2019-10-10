from pytorch_app import target_size
from torchvision import transforms, datasets
import torchvision.models as models
from skimage import io
from PIL import Image
import numpy as np
import torch
import torch.nn as nn
import os
import networks

#model_name = os.path.abspath('kitagwa-resnet-50.h5')
#print("model:", model_name)
#model = models.resnet50(num_classes=2)
model = networks.resnet(pretrained=False, depth=50)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)
device = torch.device('cpu')

class Discriminator:

  def __init__(self):

    #self.model = KerasApp(weights='imagenet')
    self.model = model
    self.param = torch.load('./model/resnet-50.pth', map_location='cpu')
    self.model = model.load_state_dict(self.param, strict=False)

  def image_to_tensor(img):
    data_transforms = transforms.Compose([
      transforms.Resize(target_size), 
      transforms.ToTensor()
    ])
    image_tensor = data_transforms(img)[:3, :, :].unsqueeze(0)

    return image_tensor

  def decode_predictions(results):
    categories = ['kitagwa', 'other']
    results = results[0]
    result_with_labels = list({'name': category, 'ratio': np.float(result)} for category, result in zip(categories, results))
    return result_with_labels
    
  def predict(self, file):
    print('upload_file:',file)
    image = Image.open(file)
    tensor_image = Discriminator.image_to_tensor(image)
    model.eval()
    output = model(tensor_image)
    softmax = nn.Softmax(dim=1)
    preds_tensor = softmax(output)
    sorted_result = Discriminator.decode_predictions(preds_tensor.tolist())
    return sorted_result
