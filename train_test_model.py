import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

import librosa

def listen_to_audio(filename):
    # Load the audio file.
    audio_data = librosa.load(filename, sr=44100)

    # Convert the audio data to a spectrogram.
    spectrogram = librosa.spectrogram(audio_data, n_fft=256, hop_length=128)

    # Normalize the spectrogram.
    spectrogram = spectrogram / np.max(spectrogram)

    # Pad the spectrogram to a fixed size.
    spectrogram = np.pad(spectrogram, [[0, 0], [0, 128 - len(spectrogram[0])], [0, 0]], 'constant')

    # Return the spectrogram.
    return spectrogram

def train_convnet(spectrograms, distances):
    # Create the convnet.
    convnet = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 1)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1, activation='linear')
    ])

    # Compile the convnet.
    convnet.compile(optimizer='adam', loss='mse', metrics=['mae'])

    # Train the convnet.
    convnet.fit(spectrograms, distances, epochs=10)

    return convnet

if __name__ == "__main__":
    # Load the spectrograms and distances.
    spectrograms = []
    distances = []
    for i in range(10):
        filename = f"swing{i + 1}.m4a"
        spectrogram = listen_to_audio(filename)
        spectrograms.append(spectrogram)
        distance = i * 10
        distances.append(distance)

    # Train the convnet.
    convnet = train_convnet(spectrograms, distances)

    # Assess the error of the model on the test set.
    assess_error(convnet, test_spectrograms, test_distances)
