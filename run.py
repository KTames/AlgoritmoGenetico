#!encoding=utf-8
from probabilistic import Probabilistic
from image import ImageData

if __name__ == "__main__":
    rows = 10
    columns = 10

    images = [ImageData("imgs/guacamaya.jpg"), ImageData("imgs/Beach.jpg"), ImageData("imgs/imagen.jpg")]
    probabilistic = Probabilistic(images, rows, columns)
    sectors = probabilistic.choose_samples()
