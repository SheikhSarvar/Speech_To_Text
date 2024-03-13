import tkinter as tk
from tkinter import ttk
import speech_recognition as sr

class SpeechToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Speech to Text")
        
        self.label = ttk.Label(root, text="Click 'Start' to begin recording")
        self.label.pack(pady=10)

        self.text_display = tk.Text(root, height=10, width=50)
        self.text_display.pack(pady=10)

        self.start_button = ttk.Button(root, text="Start", command=self.start_recording)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_recording)
        self.stop_button.pack(pady=5)
        self.stop_button.config(state="disabled")

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.recording = False

    def start_recording(self):
        self.recording = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.label.config(text="Recording...")

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.recording:
                try:
                    audio = self.recognizer.listen(source, timeout=1)
                    text = self.recognizer.recognize_google(audio)
                    self.text_display.delete(1.0, tk.END)
                    self.text_display.insert(tk.END, text)
                except sr.WaitTimeoutError:
                    pass
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def stop_recording(self):
        self.recording = False
        self.stop_button.config(state="disabled")
        self.start_button.config(state="normal")
        self.label.config(text="Click 'Start' to begin recording")

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeechToTextApp(root)
    root.mainloop()
