import os
import cv2
from gfpgan.utils import GFPGANer

images_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'images')
model_dir = os.path.join(os.path.dirname(__file__), 'gfpgan', 'weights')

def handler(data, properties):
    model = properties.get('model')
    upscale = properties.get('upscale')
    weight = properties.get('weight')
    pretrain_model_path = os.path.join(model_dir, model)


    for item in data:
      image = cv2.imread(os.path.join(images_dir, item['image']))

      if model == 'RestoreFormer.pth':
          arch = 'RestoreFormer'
      else:
          arch = 'clean'

      restorer = GFPGANer(
        model_path=pretrain_model_path,
        model_dir=model_dir,
        upscale=int(upscale),
        channel_multiplier=2,
        bg_upsampler=None,
        arch=arch
      )

      _, _, restored_image = restorer.enhance(
        image, has_aligned=False, only_center_face=False, paste_back=True, weight=float(weight)
      )

      cv2.imwrite(os.path.join(images_dir, item['image']), restored_image)

    return data