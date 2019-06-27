import wave
import numpy as np

class click:
    def __init__(self, tempo):
        self.tempo = tempo

    def make(self):
        pass


    def create_sin_wave(self, A, f0, fs, length):
        """create sin wave
        A: amplitude
        f0: fundamental frequency
        fs: sampling frequency
        length: sound length(second)
        """
        data = []
        # make wave range -1 ~ 1
        for n in np.arange(length * fs):
            s = A * np.sin(2 * np.pi * f0 * n / fs)
            # clipping
            if s > 1.0:
                s = 1.0
            if s < -1.0:
                s = -1.0
            data.append(s)
        data = [int(x * 32767.0) for x in data]

        return data


    def save_sound(data, fs, bit, channel, filename):
        """save sound
        data: sound
        fs: sampling frequency
        bit:
        filename:
        """
        wf = wave.open(filename, "w")

        wf.setnchannels(channel)
        wf.setsampwidth(bit / 8)
        wf.setframerate(fs)
        wf.writeframes(data)
        wf.close()



