import cv2
import numpy as np

def blur_center(image_path, width, height, sigmaX=25):
    # Read the image
    image = cv2.imread(image_path)

    # Get the dimensions of the image
    img_height, img_width = image.shape[:2]

    # Find the center coordinates of the image
    center_x = int(img_width / 2)
    center_y = int(img_height / 2)

    # Create a copy of the image for processing
    blurred_image = image.copy()

    # Blur the central region of the image
    start_x = center_x - int(width / 2)
    end_x = center_x + int(width / 2)
    start_y = center_y - int(height / 2)
    end_y = center_y + int(height / 2)

    blurred_image[start_y:end_y, start_x:end_x] = cv2.GaussianBlur(blurred_image[start_y:end_y, start_x:end_x], (0, 0), sigmaX=sigmaX)

    return blurred_image
# def blur_center(image_path, width, height, border_radius, sigmaX=25):
#     # Read the image
#     image = cv2.imread(image_path)

#     # Get the dimensions of the image
#     img_height, img_width = image.shape[:2]

#     # Find the center coordinates of the image
#     center_x = int(img_width / 2)
#     center_y = int(img_height / 2)

#     # Create a mask for the blur region with border radius
#     mask = np.zeros((height, width), dtype=np.uint8)
#     cv2.ellipse(mask, (int(width/2), int(height/2)), (int(width/2), int(height/2)), 0, 0, 360, (255), -1)

#     # Apply Gaussian blur to the mask
#     mask = cv2.GaussianBlur(mask, (border_radius, border_radius), sigmaX)

#     # Normalize the mask to the range [0, 1]
#     mask = mask / 255.0

#     # Resize the mask to match the image size
#     mask = cv2.resize(mask, (img_width, img_height))

#     # Convert the image to float32 to support alpha channel
#     image = image.astype(np.float32) / 255.0

#     # Apply alpha blending to create a blurred border with border radius
#     blurred_image = image * (1 - mask[..., np.newaxis]) + cv2.GaussianBlur(image, (border_radius, border_radius), sigmaX) * mask[..., np.newaxis]

#     # Convert the image back to uint8
#     blurred_image = (blurred_image * 255).astype(np.uint8)

#     return blurred_image