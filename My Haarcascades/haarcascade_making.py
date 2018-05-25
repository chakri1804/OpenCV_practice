import cv2
import numpy as np
import os

############## Making POS samples into grayscale and 
############## resizing given a sample data folder
list1 = os.listdir('pos')
for x in list1:
    print(x)
    gray = cv2.imread('pos/arduino.png',0)
    resized_image = cv2.resize(gray, (46,34))
    cv2.imwrite('pos/0001.png',resized_image)
    pass
##############
##############


############## Making NEG samples into grayscale and 
############## resizing given a sample data folder
list1 = os.listdir('neg')
for x in list1:
    print(x)
    gray = cv2.imread('neg/'+str(x),0)
    resized_image = cv2.resize(gray, (200,200))
    cv2.imwrite('neg/'+str(x),resized_image)
    pass
##############
##############



############## Removing Ugly broken useless images
# def find_uglies():
#     match = False
#     for file_type in ['neg']:
#         for img in os.listdir(file_type):
#             for ugly in os.listdir('uglies'):
#                 try:
#                     current_image_path = str(file_type)+'/'+str(img)
#                     ugly = cv2.imread('uglies/'+str(ugly))
#                     question = cv2.imread(current_image_path)
#                     if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
#                         print('That is one ugly pic! Deleting!')
#                         print(current_image_path)
#                         os.remove(current_image_path)
#                 except Exception as e:
#                     print(str(e))
##############

############## creating the coordinates file
def create_pos_n_neg():
    for file_type in ['pos','neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 46 33\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
##############

create_pos_n_neg()