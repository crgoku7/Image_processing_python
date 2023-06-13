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
    
    def Blur_gaussian(self, kernel_size):
        img_data = self.img_data
        #GS_luminousity()#ADD FUNCTIONALITY HERE
        blur_data = np.zeros(np.shape(img_data))
        if(kernel_size%2==0):
            kernel_size +=1
        kernel = np.ones((kernel_size, kernel_size))
        sum_v = 0
        for i in range(kernel_size):
            for j in range(kernel_size):
                val = abs(i-kernel_size//2) + abs(j-kernel_size//2)
                kernel[i][j] = 1/pow(2,val)
                sum_v+= kernel[i][j]
        print(kernel)
        for i in range(len(img_data)):
            b_sum = 0
            x = i//self.img_w
            y = i%self.img_w
            for j in range(-1*kernel_size//2, kernel_size//2):
                for k in range(-1*kernel_size//2, kernel_size//2):
                    br_sum = (kernel[j+kernel_size//2][k+kernel_size//2])*img_data[(y+j)//self.img_h][(x+k)//self.img_w][0]
                    bg_sum = (kernel[j+kernel_size//2][k+kernel_size//2])*img_data[(y+j)//self.img_h][(x+k)//self.img_w][1]
                    bb_sum = (kernel[j+kernel_size//2][k+kernel_size//2])*img_data[(y+j)//self.img_h][(x+k)//self.img_w][2]
            blur_data[y][x][0] = br_sum
            blur_data[y][x][1] = bg_sum
            blur_data[y][x][2] = bb_sum
        




    

while(True):#input("SCAN IMAGE(Y/N?)")=="Y"
    #file_name = input("ENTER IMAGE PATH:")
    file_name = "tiger.bmp"
    print("Starting")
    inp = int(input("Again?"))
    img = Image.open(file_name)
    img_matrix = np.array(img)
    image = ImageProcess(img_matrix)
    #image.GS_average()
    #grey = Image.fromarray(image.grey_data)
    image.Blur_gaussian(inp)
    img.blur_data.save("blur.bmp")
    
    """if grey.mode != 'RGB':
        grey  = grey.convert("RGB")
    grey.save("image.bmp")
    break"""
        

