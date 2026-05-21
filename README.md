# Password-Generator

## Overview
A command line password generator with clipboard support. 

This simple tool randomly generates a unique strong password.
Once executed, the program generates a strong password between 12 and 128 characters long and copies the output to the user's clipboard for a limited time - ready to be used.

## Installation

### Requirements

- Python 3.12.3+
- pip

### Clone the repository

```bash
git clone https://github.com/katana-gh/password-generator.git
cd password-generator
```

### Install dependencies

```bash
pip install pyperclip
```

## Usage

Run the program by specifying the password's <length> <optional time>:

```bash
python3 main.py <length> <time>
```

### Example
```bash
python3 main.py 20 15
```

**Output:**
```
CJ985<#C#=5^aVC<a9<^
```

Creates a strong password of 20 characters and copies it to the clipboard for 15 seconds. (note: Password does NOT remove from enabled clipboard history)
If the given length is below 12 or above 128, the length defaults to the closest defined boundary.
If no time argument is specified, the password is removed from clipboard after 30 seconds.

## License

This project is licensed under the MIT License.
