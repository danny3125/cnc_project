#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import numpy as np

import rospy
from std_msgs.msg import Float64
img = cv2.imread('/home/peter/mother_board.png')
# rospy.Publisher('/KDD_RoboArm/nozzlebase_controller/command', Float64, queue_size = 1),
# rospy.Publisher('/KDD_RoboArm/nozzle_controller/command', Float64, queue_size = 1)]))

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = (x, img.shape[:2][0]-y)
        print('index: ', xy)
        val = img[y][x][0]
        print('val: ', val)
        coord = pixel2coordinate(xy, val)
        print('3D coordinate: ', coord)
        param[0].publish(coord[0])
        param[1].publish(coord[1])
        param[2].publish(coord[2] - 0.03)
        '''cv2.circle(img, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        img.imshow('image', img)'''

def pixel2coordinate(p_index, val):
    # Gazebo中原點座標與height_map原點間的偏量
    x_offset = -460
    y_offset = -120
    # height_map 中的 0 與真實值之間的偏量
    z_bias = -9.7    
    tf_x = 0.239144/1024
    tf_y = 0.128838/554
    tf_z = 0.014156/110
    
    x = (p_index[0] + x_offset) * tf_x
    y = (p_index[1] + y_offset) * tf_y
    z = (val+z_bias)*tf_z
    
    return(x, y, z)

if __name__=='__main__':
    rospy.init_node('command_fromImg')
    x_publisher = rospy.Publisher('/KDD_RoboArm/x_position_controller/command', Float64, queue_size = 1)
    y_publisher = rospy.Publisher('/KDD_RoboArm/y_position_controller/command', Float64, queue_size = 1) 
    z_publisher = rospy.Publisher('/KDD_RoboArm/z_position_controller/command', Float64, queue_size = 1)
    
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', on_EVENT_LBUTTONDOWN, (x_publisher, y_publisher, z_publisher))
    cv2.imshow('image', img)
    while(True):
        try:
            cv2.waitKey(100)
        except Exception:
            cv2.destroyWindow('image')
            break
    
    cv2.waitKey(0)
    cv2.destroyAllWindow()
