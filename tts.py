import os
from elevenlabs import generate, play, save, voices, set_api_key
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ELEVEN_API_KEY")

if not api_key:
    print("API key not found. Please check your API.")
    exit()

set_api_key(api_key)

def list_voices():
    all_voices = voices()
    print("\n Available Voices:")
    for i, voice in enumerate(all_voices):
        print(f"{i}. {voice.name}")
    return all_voices

def get_voice_choice(voices):
    try:
        choice = int(input("\nSelect voice (number): "))
        if 0 <= choice < len(voices):
            return voices[choice]
    except ValueError:
        pass
    print(" Invalid input. Using default voice.")
    return voices[0]

def main():
    print(" Welcome to Text-to-Speech conversion App")
    text = input(" Enter text to convert to speech:\n> ").strip()

    if not text:
        print(" You didn't enter anything.")
        return

    all_voices = list_voices()
    selected_voice = get_voice_choice(all_voices)

    print(f"\n Generating voice using '{selected_voice.name}'...")

    try:
        audio = generate(text=text, voice=selected_voice)
        save(audio, "output/tts_output.wav")
        play(audio)
        print(" Done! Audio saved to 'tts_output.wav'")
    except Exception as e:
        print(f" Something went wrong: {e}")

if __name__ == "__main__":
    main()
