from pulse_detector import PulseDetector

if __name__ == "__main__":
    video_path = "sample_video.mov"
    output_file = "pulse.txt"

    detector = PulseDetector(video_path, output_file)
    detector.detect_pulse()
