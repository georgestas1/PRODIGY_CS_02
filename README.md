# Keylogger Program README

## Overview

This is a simple keylogger program written in Python. It records all key presses and logs them to a text file named `key_log.txt`. The program uses the `pynput` library to capture keyboard events and `tkinter` to ask the user for permission before starting the keylogging process. It also allows the user to stop the keylogger by pressing the key combination `Ctrl + Shift + X`.

## Features

- Logs all key presses, including special keys like `Enter`, `Space`, `Tab`, `Backspace`, etc.
- Displays a permission dialog before starting the keylogger.
- Stops the keylogger when the `Ctrl + Shift + X` combination is pressed.
- Saves the logs to `key_log.txt` with timestamps for each key press.
- Supports various special keys and handles key release events.

## Prerequisites

To run this program, you need to have Python installed on your system. Additionally, the following Python packages are required:

- `pynput`: Used to capture keyboard input.
- `tkinter`: Used to display the permission pop-up.

You can install the required libraries using the following command:

```bash
pip install pynput
```

## How to Use

1. **Clone or download the repository** containing the program.
    ```bash
    git clone https://github.com/georgestas1/PRODIGY_CS_04
    ```
    
2. **Run the program**:

   ```bash
   python keylogger.py
   ```

3. When the program starts, a **permission pop-up** will appear asking for your consent to log keystrokes.

4. Once permission is granted, the keylogger will start capturing all keystrokes.

5. **Stop the keylogger** at any time by pressing `Ctrl + Shift + X`.

6. The keystrokes will be saved in `key_log.txt` in the same directory as the program.

## Key Presses

The following special keys are logged with custom labels:

- `[ENTER]`
- `[SPACE]`
- `[TAB]`
- `[BACKSPACE]`
- `[ESC]`
- `[SHIFT]`
- `[CTRL]`
- `[ALT]`
- `[CAPS_LOCK]`
- `[DELETE]`
- `[HOME]`
- `[END]`
- `[PAGE_UP]`
- `[PAGE_DOWN]`
- `[LEFT_ARROW]`
- `[RIGHT_ARROW]`
- `[UP_ARROW]`
- `[DOWN_ARROW]`

## Exit Key Combination

To stop the keylogger, press the following key combination:

```
Ctrl + Shift + X
```

Once all keys in the combination are pressed simultaneously, the program will stop, and the log file will be saved.

## Log File

All keystrokes are saved with timestamps in `key_log.txt` in the following format:

```
2024-10-16 18:34:22,123: [KEY_PRESSED]
```

Each new session starts with a header indicating the session start time:

```
---- New Session Started at YYYY-MM-DD HH:MM:SS ----
```

## Security Disclaimer

This program is intended for educational purposes only. Ensure that you have permission before using it on any system. Unauthorized use of keyloggers can violate privacy and security laws.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [pynput](https://pypi.org/project/pynput/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)
