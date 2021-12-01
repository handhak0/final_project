def segmentation(filename) :
    from tensorflow.keras import Input
    from model import u_net
    import cv2

    import tensorflow as tf
    import numpy as np

    import os
    # 실행
    input_img = Input(shape=(256, 256, 3), name='img')
    model = u_net.get_u_net(input_img, num_classes=19)
    model.summary()
    model.load_weights('C:/Users/sonso/Desktop/Git/멀티캠퍼스/04.FinalProject/손학영/Face_segmentation/1125_1250-unet.h5')


    # 실행
    color_list = [[0, 0, 0], [204, 0, 0], [255, 140, 26], [204, 204, 0],
                  [51, 51, 255], [204, 0, 204], [0, 255, 255],
                  [255, 204, 204], [102, 51, 0], [255, 0, 0],
                  [102, 204, 0], [255, 255, 0], [0, 0, 153], [0, 0, 204],
                  [255, 51, 153], [0, 204, 204], [0, 51, 0], [255, 153, 51], [0, 204, 0]]

    def change_3ch(prediction, image):
        """
        Change image chanel to 3 chanel

        :param prediction: predicted output of the model.
        :type prediction: array
        :param mask: true masks of the images.
        :type mask: array
        :param image: original image.
        :type image: array

        """
        tmp_image = (image * 255.0).astype(np.uint8)
        im_base = np.zeros((256, 256, 3), dtype=np.uint8)
        for idx, color in enumerate(color_list):
            im_base[prediction == idx] = color
        return im_base

    # 이미지 불러오기
    # img_file  = 'C:/Users/sonso/Desktop/Git/멀티캠퍼스/04.FinalProject/손학영/Face_segmentation/test.jpg'
    # img_file = '../static/input/test.jpg'
    # img_file = r'C:\Users\sonso\Desktop\Git\멀티캠퍼스\04.FinalProject\손학영\Face_segmentation\test.jpg'
    # filename = 'test.jpg'

    img_file = 'C:/Users/sonso/Desktop/Git/멀티캠퍼스/04.FinalProject/손학영/static/input/' + filename

    stream = open(img_file.encode("utf-8") , "rb")
    bytes = bytearray(stream.read())
    numpyArray = np.asarray(bytes, dtype=np.uint8)


    img = cv2.imdecode(numpyArray ,cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img / 255.0
    img = tf.image.random_brightness(img, max_delta=0.5)

    dst = cv2.resize(np.float32(img), dsize=(256, 256)) #, interpolation=cv2.INTER_AREA)
    dst = tf.stack([dst])

    predictions = model.predict(dst)
    predictions = np.argmax(predictions, axis=-1)

    pred = change_3ch(predictions[0], dst[0].numpy())
    save_path = f'C:/Users/sonso/Desktop/Git/멀티캠퍼스/04.FinalProject/손학영/Face_segmentation/temp/{filename}'
    extension = os.path.splitext(save_path)[1]

    result, encoded_img = cv2.imencode(extension, pred)

    if result:
        with open(save_path, mode='w+b') as f:
            encoded_img.tofile(f)


# cv2.imwrite(save_path, pred)

# if __name__ == "__main__" :
#     pass


# segmentation()