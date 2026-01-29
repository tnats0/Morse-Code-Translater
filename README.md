# Morse Code Translater

A terminal-based Python application that translates text to Morse code and vice versa with animated visual effects.

## Features

- **Text to Morse Translation**: Convert English text to Morse code format
- **Morse to Text Translation**: Decode Morse code back to readable English
- **Animated Output**: Character-by-character typing animation for visual appeal


## Project Structure

```
Morse-Code-Translater/
├── main.py              # Entry point - handles user menu and navigation
├── translater.py        # Core translation logic (text ↔ Morse)
├── values.py            # Morse code dictionary mapping (A-Z, 0-9, punctuation)
├── words_morse.py       # Utility functions for word-level Morse processing
├── anim_type.py         # Terminal animation utilities (typing, deleting, clearing)
├── README.md            # This file
└── .gitattributes       # Git configuration
```

## File Descriptions

| File | Purpose |
|------|---------|
| **main.py** | Application entry point with menu loop and user input handling |
| **translater.py** | `translate_to_morse()` and `translate_to_text()` functions |
| **values.py** | Bidirectional dictionary: `morse_dict` (char→morse) and `reverse_morse_dict` (morse→char) |
| **words_morse.py** | Helper functions for processing Morse code words and spacing |
| **anim_type.py** | Reusable animation functions: `typing_animation()`, `deleting()`, `clear()` |

## How It Works

### Text → Morse Code
1. User enters English text in main menu
2. `translater.py` converts each character using `values.py` dictionary
3. Characters separated by spaces, words separated by " / "
4. Output displayed with typing animation via `anim_type.py`

### Morse Code → Text
1. User enters Morse code (spaces between characters, " / " between words)
2. `translater.py` reverses the lookup using `reverse_morse_dict`
3. Reconstructs original text
4. Animated display of decoded message

## Requirements

### Python Version
- Python 3.7+

### Dependencies
None - uses only Python standard library (`time`, `os`, `sys`)

### Optional
- `colorama` (for enhanced terminal colors on Windows)

## Installation & Usage

### Setup
```bash
# Navigate to project directory
cd Morse-Code-Translater

# Run the application
python main.py
```

### Usage Example
```
=== MORSE CODE TRANSLATER ===
1. Text to Morse Code
2. Morse Code to Text
3. Exit

Select option: 1
Enter text: HELLO
[Animated output]
.... . .-.. .-.. ---
```

## Animation Features

The project uses custom terminal animations from `anim_type.py`:

- **typing_animation(text, delay=0.05)** - Types text character-by-character
- **deleting(count)** - Backspaces and removes characters
- **clear()** - Clears entire terminal screen (cross-platform)

### Example
```python
from anim_type import typing_animation, clear

clear()
typing_animation("Welcome to Morse Code Translater!", delay=0.03)
```

## Morse Code Format

- **Dot** = `.`
- **Dash** = `-`
- **Character separator** = Space
- **Word separator** = `/`

### Example
```
HELLO WORLD
↓
.... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

## Key Functions

### translater.py
```python
translate_to_morse(text: str) → str
translate_to_text(morse_code: str) → str
```

### values.py
```python
morse_dict = {'A': '.-', 'B': '-...', ...}  # Char to Morse
reverse_morse_dict = {'.-': 'A', '-...': 'B', ...}  # Morse to Char
```

## Limitations

- Supports A-Z, 0-9, and basic punctuation only
- Input is case-insensitive (converts to uppercase internally)
- Unsupported characters are skipped or marked as unknown


## License

Open source - feel free to use and modify for educational purposes.