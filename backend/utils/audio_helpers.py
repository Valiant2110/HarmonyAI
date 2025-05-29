import librosa
import numpy as np

def extract_features(file_path: str) -> np.ndarray:
    """
    Extract audio features (MFCCs) from file for mood classification.
    """
    y, sr = librosa.load(file_path, sr=None)  # Load audio file with original sampling rate
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfccs_mean = np.mean(mfccs.T, axis=0)  # Average over time frames
    return mfccs_mean
