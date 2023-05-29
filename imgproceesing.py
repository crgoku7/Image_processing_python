from PIL import Image
import time
import numpy as np
#import pysimplegui #DISPLAYING MODIFIED IMAGES
class ImageProcess:
    def __init__(self, img_matrix):
        self.img_data = img_matrix
        self.img_h = np.shape(img_matrix)[0]
        self.img_w = np.shape(img_matrix)[1]
    def GS_average(self):
        self.grey_data = np.zeros((self.img_h,self.img_w))
        for i in range(self.img_h):
            for j in range(self.img_w):
                self.grey_data[i][j] = np.sum(self.img_data[i][j])/3
    def GS_luminousity(self):
        self.grey_data = np.zeros((self.img_h,self.img_w))
        for i in range(self.img_h):
            for j in range(self.img_w):
                self.grey_data[i][j] = (0.3*self.img_data[i][j][0]+0.59*self.img_data[i][j][1]+0.11*self.img_data[i][j][2])
    
    def Blue_gaussian(self, kernel_size):
        if(kernel_size%2==0):
            kernel_size +=1
        kernel = np.ones((kernel_size, kernel_size))
        sum_v = 0
        for i in range(kernel_size):
            for j in range(kernel_size):
                val = 1#abs(i-blur_size/2) + abs(j-blur_size/2)
                kernel[i][j] = 1/pow(2,val)
                sum_v+= kernel[i][j]
        print(kernel)


    

while(True):#input("SCAN IMAGE(Y/N?)")=="Y"
    #file_name = input("ENTER IMAGE PATH:")
    file_name = "tiger.bmp"
    img = Image.open(file_name)
    img_matrix = np.array(img)
    image = ImageProcess(img_matrix)
    image.GS_average()
    grey = Image.fromarray(image.grey_data)
    image.Blue_gaussian(3)
    """if grey.mode != 'RGB':
        grey  = grey.convert("RGB")
    grey.save("image.bmp")
    break"""
        

