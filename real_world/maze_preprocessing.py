import cv2  
import numpy as np
#import matplotlib.pyplot as plt

from Ball_tracking import masking

class ImagePreprocess:
    '''
    Class for preprocessing images
    Args:
        img_size : 
        threshold_plane
        threshold_ball
    '''
    def __init__(self, img_size=(480,640), threshold_plane=192, threshold_ball=100):
        self.img_size = img_size
        self.masker = masking()

        # Thresholds
        self.threshold_plane = threshold_plane
        self.threshold_ball = threshold_ball
        self.label_plane = 255 # label of floor
        self.label_ball = 128
        self.label_wall = 0 
    
    def to_label(self, img):
        IMG = cv2.resize(img, (120,120), interpolation=cv2.INTER_LANCZOS4)
        for j in range(IMG[0, :].size):
            for i in range(IMG[:, 0].size):
                if IMG[i,j] >= self.threshold_plane:
                    IMG[i,j] = self.label_plane
                elif (IMG[i,j] >= self.threshold_ball) and (IMG[i,j] < self.threshold_plane):
                    IMG[i,j] = self.label_ball
                elif IMG[i,j] < self.threshold_ball:
                    IMG[i,j] = self.label_wall
        return IMG
    
    
#    def get_ball(self, img):
        


if __name__=="__main__":
    cam = cv2.VideoCapture(1)

    assert cam.isOpened(), "Webcam is not connected"

    while cam.isOpened():
        status, frame = cam.read()

        #framer = img2array(frame)
        #img = framer.to_array()
        #print(img)

        #img2 = framer.to_label()
        #print(img2)
        if status:
            IMG = cv2.resize(frame, (480,480), interpolation=cv2.INTER_LANCZOS4)
            cv2.imshow("img", IMG)
            cv2.imshow('frame', frame[:, 80: 560])

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

# #grayscale testing section
# IMG = img2array(img_file).to_array()
# #cv2.imshow('gray',IMG)

# print(IMG) 

# #label testing section
# IMG2 = img2array(img_file).to_label()
# #cv2.imshow('label',IMG2)

# print(IMG2)

# cv2.waitKey(0)
# #save
# #np.save(path+'/array_gray.npy',IMG)
# #np.save(path+'/array_label.npy',IMG2)
# #np.savetxt(path+'/array_maze_ball.txt',IMG, fmt='%d')
# np.savetxt(path+'/array_maze_ball_labelled.txt',IMG2, fmt='%d')
# #cv2.imwrite(path+'/gray_img.png', IMG)
# #cv2.imwrite(path+'/labelled_img.png', IMG2)

# #load
# # ARRAY = np.load(path+'array.npy')
# # print(ARRAY)