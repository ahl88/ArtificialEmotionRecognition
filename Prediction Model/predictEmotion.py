import tensorflow as tf
import keras
import numpy as np
import librosa
import sys

#filePath = sys.argv[1]
#fileName = sys.argv[2]

model = tf.keras.models.load_model('C:\\Users\\drkdfr\\Desktop\\django_final\\Emotion_Voice_Detection_Model_REAL.h5')
data, sampling_rate = librosa.load('C:\\Users\\drkdfr\\Desktop\\django_final\\03-01-01-01-01-01-01.wav')
mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
x = np.expand_dims(mfccs, axis=1)
x = np.expand_dims(x, axis=0)
predictions = model.predict_proba(x)
print (predictions*100)

