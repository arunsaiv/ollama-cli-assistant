import requests
import threading
import itertools
import sys
import time
import json

# Spinner function
def spinner(stop_event):
    for frame in itertools.cycle(["|", "/", "-", "\\"]):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\r🤖 AI is thinking... {frame}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 40 + "\r")  # Clear the line

def run_ollama_chat():
    print("🤖 Welcome to Ollama CLI Assistant (Streaming Mode Enabled)")

    model = input("🔍 Enter model name (default: llama3): ").strip() or "llama3"

    while True:
        prompt = input("\n💬 You: ")
        if prompt.lower() in ["exit", "quit"]:
            print("👋 Exiting...")
            break

        # Start spinner
        stop_event = threading.Event()
        spin_thread = threading.Thread(target=spinner, args=(stop_event,))
        spin_thread.start()

        try:
            with requests.post(
                "http://localhost:11434/api/generate",
                json={"model": model, "prompt": prompt, "stream": True},
                stream=True,
            ) as response:
                stop_event.set()
                spin_thread.join()

                if response.status_code != 200:
                    print(f"\n❌ Error: {response.status_code} - {response.text}")
                    continue

                print("\n🧠 AI: ", end="", flush=True)
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line.decode("utf-8"))
                        print(data.get("response", ""), end="", flush=True)
                print()  # New line at the end
        except requests.exceptions.RequestException as e:
            stop_event.set()
            spin_thread.join()
            print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    run_ollama_chat()