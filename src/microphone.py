from threading import Thread
import pyaudio
import numpy as np

class Microphone(Thread):
    def __init__(self):
        self.sampling_rate = 44100      # Sampling rate of the recording device
        self.chunk_size = 4096          # Number of data points to read at a time
        self.refresh_rate = 30          # Updates per second

        # Create the PyAudio object
        self.audio = pyaudio.PyAudio()
        self.audio_stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=self.sampling_rate, input=True,
                                            frames_per_buffer=self.chunk_size)

    # Destructor to gracefully close the audio stream
    def __del__(self):
        self.audio_stream.stop_stream()
        self.audio_stream.close()
        self.audio.terminate()


    # Continually listen for sound input
    def run(self):
        for i in range(10):
            data = np.fromstring(self.audio_stream.read(self.chunk_size), dtype=np.int16)
            print(data)


if __name__ == '__main__':
    mic = Microphone()
