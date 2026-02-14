import time
import threading


class CameraRecorder(threading.Thread):

    def __init__(self):
        super().__init__()

        self.recording_signal = threading.Event()
        self.stop_signal = threading.Event()
        self.daemon = True

    def run(self):
        """
        
        """
        print("[Camera] Ready, waiting for motion...")

        while not self.stop_signal.is_set():

            # tunggu signal true
            self.recording_signal.wait(timeout=1)

            if self.recording_signal.is_set():
                print("[Camera] MOTION DETECTED! Recording started...")

                self.record_video()

                # clear signal setelah selesai
                self.recording_signal.clear()
                print("[Camera] recording stopped. Waiting for next motion...")

    def record_video(self):
        """
        
        """
        for i in range(5):
            print(f"[Camera] Recording frame {i}...")
            time.sleep(0.5)

    def trigger_recording(self):
        """
        
        """
        self.recording_signal.set() # set signal ke True

    def stop(self):
        """
        
        """
        self.stop_signal.set()


if __name__ == "__main__":

    # start camera thread
    camera = CameraRecorder()
    camera.start()

    # simulate motion detector
    time.sleep(2)
    print("[Motion Detector] Motion detected!")
    camera.trigger_recording()

    time.sleep(8)

    print("[Motion Detector] Motion detected again !")
    camera.trigger_recording()

    time.sleep(8)

    # stop
    camera.stop()
    camera.join()
    print("camera stoppedd !")
