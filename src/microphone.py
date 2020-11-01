import time
import pyaudio


if __name__ == '__main__':
    pa = pyaudio.PyAudio()
    stream_in = pa.open(
            rate=48000,
            channels=2,
            format=pyaudio.paInt16,
            input=True,
            input_device_index=2,
            frames_per_buffer=1024)

    print('Recording')
    input_audio = stream_in.read(5 * 48000)
    print('Finished')
