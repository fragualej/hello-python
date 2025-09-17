#!/usr/bin/env python3
import whisper
import os
from datetime import datetime

def main():
    print("Loading Whisper model...")
    model = whisper.load_model("medium")  # Options: tiny, base, small, medium, large
    print("Hello, Whisper! Model loaded successfully!")
    
    # Example audio file path (you'll need to provide an actual file)
    audio_file = "audio_02.ogg"
    
    if os.path.exists(audio_file):
        print(f"Transcribing {audio_file}...")
        result = model.transcribe(audio_file)
        print("\nTranscription:")
        print(result["text"])
        
        # Save transcription to file
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamp_filename = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"../output/transcription_{timestamp_filename}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"Transcription generated on: {timestamp}\n")
            f.write(f"Audio file: {audio_file}\n")
            f.write("-" * 50 + "\n\n")
            
            # Split text into lines (approximately 80 characters per line)
            text = result["text"].strip()
            words = text.split()
            lines = []
            current_line = ""
            
            for word in words:
                if len(current_line + " " + word) <= 80:
                    if current_line:
                        current_line += " " + word
                    else:
                        current_line = word
                else:
                    if current_line:
                        lines.append(current_line)
                    current_line = word
            
            if current_line:
                lines.append(current_line)
            
            f.write("\n".join(lines))
        print(f"\nTranscription saved to: {output_file}")
    else:
        print(f"Audio file '{audio_file}' not found.")
        print("Place an audio file in this directory and update the filename.")

if __name__ == "__main__":
    main()