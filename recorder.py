import streamlit as st
import sounddevice as sd
import numpy as np
import wavio

st.title("Record and Upload Audio")

duration = 5  # seconds
fs = 44100  # Sample rate

if st.button("Record Audio"):
    st.write("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()
    st.write("Recording complete.")
    wavio.write("recorded_audio.wav", recording, fs, sampwidth=2)
    st.download_button("Download Audio", open("recorded_audio.wav", "rb"), "recorded_audio.wav")
