import cv2  
#from google.colab.patches import cv2_imshow -> 코랩에서 imshow를 쓰려면 이걸 import해야함
import numpy as np
#import matplotlib.pyplot as plt


path = 'C:/Users/Etoile/Desktop/labyrinth/Array-Maze_test/'
object = 'maze_withball.png'
img_file = path+object
threshold_plane = 192
threshold_ball = 100

#0이 어둡고 255가 밝은거
label_plane = 255 #바닥의 label값을 지정
label_ball = 128
label_wall = 0 


#class
class img2array:
    def __init__(self, img_file):
        img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
        self.img = cv2.resize(img, (120,120), interpolation=cv2.INTER_LANCZOS4)
    def to_array(self):
        return self.img
    def to_label(self):
        IMG = self.img
        for j in range(IMG[0, :].size):
            for i in range(IMG[:, 0].size):
                if IMG[i,j] >= threshold_plane:
                    IMG[i,j] = label_plane
                elif (IMG[i,j] >= threshold_ball) and (IMG[i,j] < threshold_plane):
                    IMG[i,j] = label_ball
                elif IMG[i,j] < threshold_ball:
                    IMG[i,j] = label_wall
        return IMG

#grayscale testing section
IMG = img2array(img_file).to_array()
#cv2.imshow('gray',IMG)

print(IMG) 

#label testing section
IMG2 = img2array(img_file).to_label()
#cv2.imshow('label',IMG2)

print(IMG2)

cv2.waitKey(0)
#save
#np.save(path+'/array_gray.npy',IMG)
#np.save(path+'/array_label.npy',IMG2)
#np.savetxt(path+'/array_maze_ball.txt',IMG, fmt='%d')
np.savetxt(path+'/array_maze_ball_labelled.txt',IMG2, fmt='%d')
#cv2.imwrite(path+'/gray_img.png', IMG)
#cv2.imwrite(path+'/labelled_img.png', IMG2)

#load
# ARRAY = np.load(path+'array.npy')
# print(ARRAY)