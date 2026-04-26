# Password-Generator

## A CLI tool to create strong passwords. 

This simple tool randomly generates a unique strong password.
Once executed, the program generates a strong password between 12 and 128 characters long and copies the output to the user's clipboard - ready to be used.

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

Run the program by specifying the password's length:

```bash
python3 main.py <length>
```

### Example
```bash
python3 main.py 20
```

**Output:**
```
CJ985<#C#=5^aVC<a9<^
```

Creates a strong password of 20 characters and copies it to the clipboard.
If the given length is below 12 or above 128, the length defaults to the closest defined boundary.

## License

This project is licensed under the MIT License.
