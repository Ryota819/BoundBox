from torchvision import transforms, datasets

from PIL import Image
import numpy as np
import torch
import torch.nn as nn
from .networks import resnet
from BoundBox.settings import BASE_DIR

target_size = (224, 224)
model = resnet(pretrained=False, depth=50)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 2)
device = torch.device('cpu')


class Discriminator:

  def __init__(self):
    self.model = model
    self.param = torch.load(BASE_DIR + '/api/model/resnet-50.pth', map_location='cpu')
    self.model = model.load_state_dict(self.param, strict=False)

  def image_to_tensor(img):
    data_transforms = transforms.Compose([
      transforms.Resize(target_size), 
      transforms.ToTensor()
    ])
    image_tensor = data_transforms(img)[:3, :, :].unsqueeze(0)

    return image_tensor

  # def decode_predictions(results):
  #   categories = ['kita', 'other']
  #   results = results[0]
  #   return list({'name': category, 'ratio': np.float(result)} for category, result in zip(categories, results))

  def predict(self, file):
    print('upload_file:',file)
    image = Image.open(file)
    tensor_image = Discriminator.image_to_tensor(image)
    model.eval()
    output = model(tensor_image)
    softmax = nn.Softmax(dim=1)
    preds_tensor = softmax(output)
    # sorted_result = Discriminator.decode_predictions(preds_tensor.tolist())
    print(np.float(preds_tensor.tolist()[0][0]))
    if (np.float(preds_tensor.tolist()[0][0]) > 0.7):
        result = True
    else:
        result = False
    print(result)
    return result
