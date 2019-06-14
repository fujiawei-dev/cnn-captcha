from PIL import Image
from pandas import DataFrame


def scan(img):
    temp = []
    width, height = img.size
    for h in range(height):
        for w in range(width):
            pixel = img.getpixel((w, h))
            temp.append(pixel)
    return temp


conv = lambda x: x - 48 if 48 <= x <= 57 else x - 87


def pen(single, labels, file):
    with open(labels) as fp:
        for i, j in enumerate(fp):
            n = ord(j[0])
            img = Image.open(f"{single}/{i // 4}-{i % 4}.png")
            lst = scan(img)
            file.write(', '.join(map(str, lst)) + f', {conv(n)}\n')


def pencil(single, file, num):
    for i in range(num):
        img = Image.open(f"{single}/{i // 4}-{i % 4}.png")
        lst = scan(img)
        file.write(', '.join(map(str, lst)) + '\n')


if __name__ == "__main__":
    single = "captcha/single3"
    # labels = "captcha/labels.csv"
    with open("captcha/learn3.csv", 'w') as file:
        pencil(single, file, 4000)
        # pen(single, labels, file)

