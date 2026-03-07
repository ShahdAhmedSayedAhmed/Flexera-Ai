import time
import threading
import pyttsx3


class VoiceFeedback:

    def __init__(self, rate=150, volume=0.9, cooldown=3.0, voice_gender='female'):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

        self._set_voice_gender(voice_gender)

        self.enabled = True
        self.is_speaking = False
        self.last_messages = {}
        self.cooldown = cooldown
        self.lock = threading.Lock()

    def _set_voice_gender(self, gender='female'):
        """Set voice to female or male"""
        voices = self.engine.getProperty('voices')

        target_gender = gender.lower()
        selected_voice = None

        for voice in voices:
            voice_id_lower = voice.id.lower()
            voice_name_lower = voice.name.lower() if voice.name else ""

            if target_gender == 'female':
                if any(keyword in voice_id_lower or keyword in voice_name_lower
                       for keyword in ['female', 'woman', 'zira', 'hazel', 'susan', 'samantha']):
                    selected_voice = voice
                    break
            elif target_gender == 'male':
                if any(keyword in voice_id_lower or keyword in voice_name_lower
                       for keyword in ['male', 'man', 'david', 'mark', 'alex']):
                    selected_voice = voice
                    break

        if selected_voice is None and len(voices) > 1:
            selected_voice = voices[1] if target_gender == 'female' else voices[0]
        elif selected_voice is None and len(voices) > 0:
            selected_voice = voices[0]

        if selected_voice:
            self.engine.setProperty('voice', selected_voice.id)
            print(f"Voice set to: {selected_voice.name or selected_voice.id}")

    def set_voice(self, gender):
        """Change voice gender at runtime"""
        self._set_voice_gender(gender)

    def list_available_voices(self):
        """List all available voices on the system"""
        voices = self.engine.getProperty('voices')
        print("\nAvailable voices:")
        for i, voice in enumerate(voices):
            print(f"  {i}: {voice.name} ({voice.id})")
        return voices

    def speak(self, text, force=False):
        if not self.enabled or not text:
            return False

        current_time = time.time()

        with self.lock:
            if not force and text in self.last_messages:
                if current_time - self.last_messages[text] < self.cooldown:
                    return False
            self.last_messages[text] = current_time

        thread = threading.Thread(target=self._speak_thread, args=(text,))
        thread.daemon = True
        thread.start()
        return True

    def _speak_thread(self, text):
        self.is_speaking = True
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            pass
        finally:
            self.is_speaking = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def clear_cooldown(self):
        with self.lock:
            self.last_messages.clear()

    def stop(self):
        try:
            self.engine.stop()
        except:
            pass
