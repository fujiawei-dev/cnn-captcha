from PIL import Image


def regularized(img):
    width, height = img.size
    for h in range(height):
        for w in range(width):
            pixel = img.getpixel((w, h))
            if 42 <= pixel <= 43:
                pixel = 0
            else:
                pixel = 255
            img.putpixel((w, h), pixel)
    return img


def cut(img):
    width, height = img.size
    new = img.crop((4, 1, width - 20, height - 5))
    w, h = new.size
    l = w // 4
    return [new.crop((i * l, 0, (i + 1) * l, h)) for i in range(4)]


def img_to_single(intact, single, num):
    for i in range(num):
        img = Image.open(f"{intact}/{i}.png")
        imgs = cut(regularized(img))
        for j in range(4):
            imgs[j].save(f"{single}/{i}-{j}.png")


if __name__ == "__main__":
    intact = "captcha/unknown"
    single = "captcha/single3"
    num = 1000
    img_to_single(intact, single, num)
