import pandas as pd
from tensorflow.keras import layers, optimizers, Sequential, utils, models
from PIL import Image

from preprocess import regularized, cut
from scan import scan


def predict(captcha):
    imgs = cut(regularized(Image.open(captcha)))
    data = [scan(img) for img in imgs]
    x = pd.DataFrame(data) / 255.0
    x = x.values.reshape(-1, 21, 12, 1)
    model = models.load_model('captcha_model', compile=True)
    conv = lambda x: chr(x + 48 if 0 <= x <= 9 else x + 87)
    return list(map(conv, model.predict_classes(x)))


if __name__ == "__main__":
    captcha = 'captcha/unknown/0.png'
    print(predict(captcha))
