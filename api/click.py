import wave
import numpy as np
import struct

class Click:
    def __init__(self, A=1, f0=1024, fs=8000.0):
        """
        :int A: amplitude
        :int f0: fundamental frequency
        :float fs: sampling frequency
        """
        self.A = A
        self.f0 = f0
        self.fs = fs

    def create_click(self, length, bpm, beat=4):
        if length <= 0 or bpm <= 0 or beat <= 0:
            return None

        single_beat = self.create_single_click(float(60 / bpm))
        all_click = int(((length * bpm) / (60 * beat))) * single_beat
        self.save_sound(all_click, 16, 1, 'click.wav')

    def create_single_click(self, length):
        """create sin wave
        A: amplitude
        f0: fundamental frequency
        fs: sampling frequency
        length: sound length(second)
        """
        data = []
        # make wave range -1 ~ 1
        for n in np.arange(0.1 * self.fs):
            s = self.A * np.sin(2 * np.pi * self.f0 * n / self.fs)
            # clipping
            if s > 1.0:
                s = 1.0
            if s < -1.0:
                s = -1.0
            data.append(s)
        for n in np.arange((length - 0.1) * self.fs):
            data.append(0)
        data = [int(x * 32767.0) for x in data]

        # change to byte object
        data = struct.pack("h" * len(data), *data)

        return data

    def save_sound(self, data, bit, channel, filename):
        """save sound
        data: sound
        fs: sampling frequency
        bit:
        filename:
        """
        wav = wave.Wave_write("wave_data/" + filename)
        wav.setnchannels(channel)
        wav.setsampwidth(int(bit / 8))
        wav.setframerate(self.fs)
        wav.writeframes(data)
        wav.close()



    # def create_sin_wave(self, length):
    #     """create sin wave
    #     A: amplitude
    #     f0: fundamental frequency
    #     fs: sampling frequency
    #     length: sound length(second)
    #     """
    #     data = []
    #     # make wave range -1 ~ 1
    #     for n in np.arange(length * self.fs):
    #         s = self.A * np.sin(2 * np.pi * self.f0 * n / self.fs)
    #         # clipping
    #         if s > 1.0:
    #             s = 1.0
    #         if s < -1.0:
    #             s = -1.0
    #         data.append(s)
    #     data = [int(x * 32767.0) for x in data]
    #
    #     # change to byte object
    #     data = struct.pack("h" * len(data), *data)
    #
    #     return data
