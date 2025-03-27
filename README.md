Python Version
License
A simple Python script that generates QR codes from text or URLs and saves them as PNG images.

Description
This script uses the qrcode library to create customizable QR codes. The user provides input text (which can be a URL, plain text, or any other data) and specifies the output filename (must include .png extension). The generated QR code is saved as a PNG image with default black-and-white styling.

Features
Generates QR codes from any text input (URLs, messages, etc.)

Adjustable QR code parameters (size, error correction, borders)

Saves output as high-quality PNG images

Simple command-line interface

Installation
Clone this repository:

bash
Copy
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
Install the required dependencies:

bash
Copy
pip install qrcode Pillow
Usage
Run the script from the command line:

bash
Copy
python qr_generator.py
Follow the prompts:

Enter the text or URL you want to encode

Specify the output filename (must end with .png)

The generated QR code will be saved in the same directory as the script.

Example
bash
Copy
$ python qr_generator.py
Introduce un texto o una URL para generar el código QR: https://github.com
Introduce el nombre del código QR que contenga SIEMPRE la extensión .png: github_qr.png
QR code guardado como github_qr.png
Dependencies
Python 3.6+

qrcode library

Pillow (for image handling)

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to contribute by opening issues or pull requests!
