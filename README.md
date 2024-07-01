# Voice-Activated Assistant

This is a cross-platform voice-activated assistant written in Python. It can perform various tasks such as checking the weather, taking screenshots, performing Google and YouTube searches, checking battery status, and more.

## Features

- **Text-to-Speech**: Uses `pyttsx3` for text-to-speech functionality.
- **Voice Recognition**: Uses `speech_recognition` to recognize voice commands.
- **Weather Updates**: Fetches current weather information from `weather.com`.
- **Google and YouTube Search**: Opens search results in the web browser.
- **Screenshot**: Takes and saves screenshots.
- **Battery Status**: Checks and reports the battery status.
- **System Commands**: Can shutdown, restart, and put the computer to sleep.
- **Facebook Messages**: Checks for new Facebook messages (requires credentials).
- **Date and Time**: Reports the current date and time.
- **Wikipedia Search**: Retrieves and speaks Wikipedia summaries.

## Requirements

- Python 3.x
- `pyttsx3`
- `speech_recognition`
- `requests`
- `beautifulsoup4`
- `pyautogui`
- `wikipedia-api`
- `psutil`
- `wolframalpha`
- `fbchat`
- `pyaudio`

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/amariwan/voice-activated-assistant.git
    cd voice-activated-assistant
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Variables**
   Set the following environment variables in your system:
    - `USER_NAME`: Your username.
    - `USER_EMAIL`: Your email for Facebook login.
    - `USER_PASSWORD`: Your password for Facebook login.
    - `WOLFRAM_APP_ID`: Your WolframAlpha app ID.
    - `USER_AGENT`: Your user agent string.

   Example (Linux/macOS):
   ```bash
   export USER_NAME="yourusername"
   export USER_EMAIL="youremail@example.com"
   export USER_PASSWORD="yourpassword"
   export WOLFRAM_APP_ID="yourwolframappid"
   export USER_AGENT="youruseragent"
   ```

   Example (Windows):
   ```powershell
   setx USER_NAME "yourusername"
   setx USER_EMAIL "youremail@example.com"
   setx USER_PASSWORD "yourpassword"
   setx WOLFRAM_APP_ID "yourwolframappid"
   setx USER_AGENT "youruseragent"
   ```

## Usage

1. **Run the Assistant**
    ```bash
    python assistant.py
    ```

2. **Interact with the Assistant**
   - The assistant will greet you and provide the current weather and battery status.
   - Speak commands such as "What is the weather?", "Take a screenshot", "Search Google for Python tutorials", etc.

## Voice Commands

- **Greetings and Info**
  - "Jarvis"
  - "Tell me the date"
  - "Tell me the time"
  - "Thank you"

- **Web Searches**
  - "Open Google"
  - "Google search [query]"
  - "Open YouTube"
  - "YouTube search [query]"

- **System Commands**
  - "Shutdown"
  - "Restart"
  - "Sleep mode"
  - "Take a screenshot"

- **Utilities**
  - "What's the weather?"
  - "Battery percentage"
  - "Check messages"
  - "Username"
  - "Calculate [expression]"
  - "Wikipedia [query]"

## Notes

- Ensure you have a working microphone for voice recognition.
- Facebook message checking requires valid login credentials.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to customize this README further to suit your project’s specific needs.