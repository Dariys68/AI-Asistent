import tensorflow as tf


def create_model(input_shape):
    (tf.keras.Sequential([

        tf.keras.layers.Dense(128, activation='relu', input_shape=input_shape),

        tf.keras.layers.Dense(64, activation='relu'),

        tf.keras.layers.Dense(10, activation='softmax')

    ])).compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=input_shape),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])