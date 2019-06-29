import wave
import numpy as np
import struct

class click:
    def make(self):
        pass


    def create_sin_wave(A, f0, fs, length):
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

        # change to byte object
        data = struct.pack("h" * len(data), *data)

        return data


    def save_sound(data, fs, bit, channel, filename):
        """save sound
        data: sound
        fs: sampling frequency
        bit:
        filename:
        """
        wav = wave.Wave_write("wave_data/" + filename)
        wav.setnchannels(channel)
        wav.setsampwidth(int(bit / 8))
        wav.setframerate(fs)
        wav.writeframes(data)
        wav.close()

    def join_waves(f_wav_name, b_wav_name, output_name):
        f_wav = wave.open("wave_data/" + f_wav_name, "r")
        b_wav = wave.open("wave_data/" + b_wav_name, "r")

        join_wav = wave.Wave_write("wave_data/" + output_name)

        join_wav.setnchannels(f_wav.getnchannels())
        join_wav.setsampwidth(f_wav.getsampwidth())
        join_wav.setframerate(f_wav.getframerate())

        join_wav.writeframes(f_wav.readframes(f_wav.getnframes()))
        join_wav.writeframes(b_wav.readframes(b_wav.getnframes()))

        f_wav.close()
        b_wav.close()
        join_wav.close()
