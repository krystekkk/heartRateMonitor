from video_processor import VideoProcessor
from signal_analyzer import SignalAnalyzer


class PulseDetector:
    def __init__(self, video_path, output_file):
        self.video_path = video_path
        self.output_file = output_file
        self.filter = [0.0043, 0.0129, 0.0349, 0.0583, 0.0684, 0.0583, 0.0349, 0.0129, 0.0043]

    def detect_pulse(self):
        video_processor = VideoProcessor(self.video_path)
        signal_analyzer = SignalAnalyzer(self.filter)

        means = video_processor.process_video()
        filtered_signal = signal_analyzer.filter_signal(means)
        fft_signal = signal_analyzer.calculate_fft(filtered_signal)
        bpm = signal_analyzer.calculate_bpm(fft_signal, len(filtered_signal))

        if bpm:
            with open(self.output_file, 'w') as file:
                file.write(f'Pulse: {bpm} BPMs\\n')
            print(f'Pulse: {bpm} BPMs')
        else:
            print("Unable to detect pulse.")
