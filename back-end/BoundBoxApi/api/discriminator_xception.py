from torchvision import transforms, datasets

from PIL import Image
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from .networks import xception
from BoundBox.settings import BASE_DIR
from collections import OrderedDict

target_size = (224, 224)
center_crop_size = 300


class Discriminator:

    def __init__(self, path, mean, std):
        self.model = xception(pretrained=False)
        num_ftrs = self.model.last_linear.in_features
        self.model.last_linear = nn.Linear(num_ftrs, 2)
        device = torch.device('cpu')
        self.mean = mean
        self.std = std
        self.param = torch.load(BASE_DIR + path, map_location=device)
        state_dict = self.fix_model_state_dict(self.param)
        self.model.load_state_dict(state_dict)
        self.model.eval()


    def fix_model_state_dict(self, state_dict):
        new_state_dict = OrderedDict()
        for k, v in state_dict.items():
            name = k
            if name.startswith('module.'):
                name = name[7:]  # remove 'module.' of dataparallel
            new_state_dict[name] = v
        return new_state_dict


    def image_to_tensor(self, img):
        data_transforms = transforms.Compose([
            transforms.CenterCrop(center_crop_size),
            transforms.Resize(target_size),
            transforms.ToTensor(),
            transforms.Normalize(self.mean, self.std)
        ])
        image_tensor = data_transforms(img)[:3, :, :].unsqueeze(0)

        return image_tensor

    def predict(self, file):
        print('upload_file:', file)
        image = Image.open(file)
        with torch.no_grad():
            tensor_image = self.image_to_tensor(image)
            output = self.model(tensor_image)

            # change
            preds_tensor = F.softmax(output, dim=1)
            # end of change
            print(preds_tensor)

            if (np.float(preds_tensor.tolist()[0][0]) > 0.5):
                result = True
            else:
                result = False
            print(result)
        return result
