import numpy as np


class SignalAnalyzer:
    def __init__(self, filter):
        self.filter = filter

    def filter_signal(self, signal):
        return np.convolve(signal, self.filter, 'same')

    def calculate_fft(self, signal):
        fft_result = abs(np.fft.fft(signal))
        fft_result[0] = 0
        return fft_result

    def calculate_bpm(self, fft_signal, frame_count, frame_rate=30):
        fourier_mean = np.mean(fft_signal[:100])
        fourier_pos = []
        fourier_values = []

        for i in range(100):
            if fft_signal[i] > fourier_mean:
                fourier_pos.append(i)
                fourier_values.append(round(fft_signal[i], 5))

        frequencies = []
        for i in range(len(fourier_pos)):
            frequencies.append(round((fourier_pos[i] * 30.0) / frame_count, 5))

        bpm = []
        for i in range(len(frequencies)):
            bpm.append(round(frequencies[i] * 60, 5))

        factors = {}
        for i in range(len(bpm)):
            if frequencies[i] >= 1:
                factors[((fourier_values[i] * bpm[i]) / frequencies[i])] = bpm[i]

        if factors:
            max_ = max(factors.keys())
            return factors[max_]
        else:
            return None
