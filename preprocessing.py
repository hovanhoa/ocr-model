import os
import cv2
import numpy as np


def preprocessing(img_path):
    # Read image using opencv
    img = cv2.imread(img_path)

    # Extract the file name without the file extension
    file_name = os.path.basename(img_path).split('.')[0]
    file_name = file_name.split()[0]

    # Create a directory for outputs
    # output_path = os.path.join('output_images')
    # if not os.path.exists(output_path):
    #     os.makedirs(output_path)

    # Rescale the image, if needed.
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    # save_path = os.path.join(output_path, file_name + "_1_rescale"+ ".png")
    # cv2.imwrite(save_path, img)

    # Converting to gray scale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # save_path = os.path.join(output_path, file_name + "_2_gray_scale"+ ".png")
    # cv2.imwrite(save_path, img)

    # Removing Shadows
    rgb_planes = cv2.split(img)
    result_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        result_planes.append(diff_img)
    img = cv2.merge(result_planes)
    # save_path = os.path.join(output_path, file_name + "_3_remove_shadow"+ ".png")
    # cv2.imwrite(save_path, img)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1) # increases the white region in the image 
    img = cv2.erode(img, kernel, iterations=1) # erodes away the boundaries of foreground object
    # save_path = os.path.join(output_path, file_name + "_4_remove_noise"+ ".png")
    # cv2.imwrite(save_path, img)

    # Apply blur to smooth out the edges
    # img = cv2.GaussianBlur(img, (1, 1), 0)
    # save_path = os.path.join(output_path, file_name + "_5_blur"+ ".png")
    # cv2.imwrite(save_path, img)

    # Apply threshold to get image with only b&w (binarization)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # save_path = os.path.join(output_path, file_name + "_6_threshold"+ ".png")
    # cv2.imwrite(save_path, img)

    # Save the filtered image in the output directory
    # save_path = os.path.join(output_path, file_name + "_7_done" + ".png")
    # cv2.imwrite(save_path, img)

    return img
