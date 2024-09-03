import tensorflow as tf

def classify_image(image_path):
    model = tf.keras.applications.MobileNetV2(weights="imagenet")
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    input_array = tf.keras.preprocessing.image.img_to_array(image)
    input_array = tf.expand_dims(input_array, axis=0)

    # Preprocess the image
    input_array = tf.keras.applications.mobilenet_v2.preprocess_input(input_array)

    # Predict the class
    predictions = model.predict(input_array)
    predicted_class = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)

    return predicted_class
