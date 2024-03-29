# py_simple_barcode 0.2.0<a name="mark0"></a>

***A small Code 39 barcode generator using PIL and the Libre Barcode 39 font family***

![8675309_extended_lilac](https://raw.githubusercontent.com/AndrewSpangler/py_simple_barcode/main/examples/8675309_extended_lilac.png)

![12345_normal_pink](https://raw.githubusercontent.com/AndrewSpangler/py_simple_barcode/main/examples/12345_normal_pink.png)

![abcde_normal_mint](https://raw.githubusercontent.com/AndrewSpangler/py_simple_barcode/main/examples/abcde_normal_mint.png)

![123456789_extended_turquoise](https://raw.githubusercontent.com/AndrewSpangler/py_simple_barcode/main/examples/123456789_extended_turquoise.png)

![abcde_extended_lilac](https://raw.githubusercontent.com/AndrewSpangler/py_simple_barcode/main/examples/abcde_extended_lilac.png)

- [About](#mark1)
	- [Installation](#mark2)
- [Command Line Usage](#mark3)
	- [Single Mode](#mark4)
	- [File Mode](#mark5)
	- [Manifest System](#mark6)
- [Module Usage](#mark7)
	- [Examples](#mark8)
		- [Using the Encoder (the easy way)](#mark9)
		- [Using make_barcode directly (the hard way)](#mark10)
	- [The Encoder](#mark11)
		- [Encoder](#mark12)
	- [Functions](#mark13)
		- [make_barcode](#mark14)
		- [encode_39](#mark15)
		- [get_code_39_font_data](#mark16)
		- [get_code_39_extended_font_data](#mark17)
		- [get_code_39_font_and_extended_font_data](#mark18)
- [Single File Usage](#mark19)
- [Changelog](#mark20)
	- [0.0.0](#mark21)
	- [0.2.0](#mark22)

---

# About<a name="mark1"></a>[^](#mark0)

A basic Code 39 barcode generator using PIL and the Libre Barcode 39 font family

Libre Barcode 39 is subject to the Open Font License and can be found at https://fonts.google.com/specimen/Libre+Barcode+39

Libre Barcode 39 Extended Text is subject to the Open Font License and can be found at https://fonts.google.com/specimen/Libre+Barcode+39+Extended+Text

See OFL.txt for font license details.

## Installation<a name="mark2"></a>[^](#mark1)

Available on pip - `pip install py_simple_barcode`

Alternatively download py_simple_barcode.py to your project directory and import it.

# Command Line Usage<a name="mark3"></a>[^](#mark0)

Command line usage has two modes of operation: Single mode and File mode. In Single mode, a single barcode is generated using the the prompt passed to the command line. In File mode, a file at a provided path serves as a source of the barcode prompts.  

```python
usage: py_simple_barcode.py [-h] [-e] [-f] [-sc] [-i] [-m] [-o OUTPUT] [-t TYPE] [-s SIZE] [-px PADX] [-py PADY]
                          [-fg FOREGROUND] [-bg BACKGROUND] [-mn MANIFEST_NAME] [-om]
                          value

positional arguments:
  value                 Value or text file with one entry per line to encode. Set -f flag for file mode.

options:
  -h, --help            show this help message and exit
  -e, --extended        Set flag to use extended font. Extended font has a text label below it.
  -f, --file            Set flag to load from text file at path specified by value.
  -sc, --skip_check     Set flag to skip check to see if barcode file already exists
  -i, --ignore_duplicates
                        Set flag to ignore error normally raised on duplicate barcode names being found in the barcode
                        file. File Mode only.
  -m, --manifest        Set flag to generate / update barcode manifest json.
  -o OUTPUT, --output OUTPUT
                        Set to specify output directory name. Defaults to "output"
  -t TYPE, --type TYPE  Set to specify output file type (without filetype) / directory name. Defaults to .png
  -s SIZE, --size SIZE  Set to specify barcode font size. Defaults to 50
  -px PADX, --padx PADX
                        Set to specify barcode x-padding. Defauts to 10
  -py PADY, --pady PADY
                        Set to specify barcode y-padding. Defauts to 10
  -fg FOREGROUND, --foreground FOREGROUND
                        Set to specify barcode foreground in RGBA hexadecimal. Defaults to "#000000FF"
  -bg BACKGROUND, --background BACKGROUND
                        Set to specify barcode background in RGBA hexadecimal. Defaults to "#FFFFFFFF"
  -mn MANIFEST_NAME, --manifest_name MANIFEST_NAME
                        Set to override default manifest name.
  -om, --overwrite_manifest
                        Set to overwrite an existing barcode manifest json (losing current entries), by default an
                        existing json will be updated to include new entries.
```
## Single Mode<a name="mark4"></a>[^](#mark3)

Single mode is useful for one-off production of barcodes.
Pass the value to be encoded.
#### Example usage:
`py_simple_barcode.py 120231`


## File Mode<a name="mark5"></a>[^](#mark3)

File mode is useful for batch production of barcodes.
File mode, as the name suggests, uses a test file with one barcode to generate per line.
To enable file mode use the `-f` flag.
A basic commenting system allows comments prefixed by "#"
Example barcode file format:

```
# Comments are supported
900213
900214
900215 # Mid-line comments are supported too.
900216

# Empty lines are ignored.

900217
900218
900219
```

#### Example usage:
`py_simple_barcode.py -f barcodes.txt`


## Manifest System<a name="mark6"></a>[^](#mark3)

Both Single Mode and File Mode have an optional manifest system that allows for easy tracking with an `output/manifest.json` that maps which barcodes have been generated to their file locations.

Use the `-m` flag to enable the manifest system.

The `-mn` argument will override the default manifest name.

The `-om` argument will cause the script overwrite the previous manifest entirely rather than just adding a new entry, this does not remove the output files from the hard drive.

# Module Usage<a name="mark7"></a>[^](#mark0)

Encoder objects simplify handling multiple barcode sub-types.

## Examples<a name="mark8"></a>[^](#mark7)

### Using the Encoder (the easy way)<a name="mark9"></a>[^](#mark8)

```python
from py_simple_barcode import Encoder

# Instantiate Encoder with custom background color
encoder = Encoder(background = (200, 200, 255, 255))

# Make standard barcode
barcode = encoder.make_barcode("8675309")

# Show the barcode in a window
barcode.show()

# Save barcode
barcode.save("barcode.png")

# Repeat process for extended barcode
extended_barcode = encoder.make_extended_barcode("8675309")
extended_barcode.show()
extended_barcode.save("extended_barcode.png")
```
### Using make_barcode directly (the hard way)<a name="mark10"></a>[^](#mark8)

```python
from py_simple_barcode import make_barcode, get_code_39_font_data

# Custom background
background = (200, 200, 255, 255)

# Load normal font from library
font = get_code_39_font_data()

# Make standard barcode
barcode = make_barcode("8675309", font, background=background)

# Show the barcode in a window
barcode.show()

# Save barcode
barcode.save("barcode.png")

# Repeat the process for extended barcode
extended_font = get_code_39_extended_font_data()
extended_barcode = make_barcode("8675309", extended_font, background=background)
extended_barcode.show()
extended_barcode.save("extended_barcode.png")
```
## The Encoder<a name="mark11"></a>[^](#mark7)

### Encoder<a name="mark12"></a>[^](#mark11)
> **Encoder object to set overridable defaults and hold loaded font data. Setting a value in a method will temporarily overide the default.**
> 
> ```py
> class Encoder(object):
> 	def __init__(self, default_size: int = 50, default_padx: int = 10, default_pady: int = 10, default_background: tuple = (255, 255, 255, 255), default_foreground: tuple = (0, 0, 0, 255)):
> 		...
> 	def make_barcode(self, val: str, size: int = None, padx: int = None, pady: int = None, background: tuple = None, foreground: tuple = None):
> 		"""Make normal barcode, returns a PIL Image object."""
> 	def make_extended_barcode(self, val: str, size: int = None, padx: int = None, pady: int = None, background: tuple = None, foreground: tuple = None):
> 		"""Make extended barcode, returns a PIL Image object."""
> ```
## Functions<a name="mark13"></a>[^](#mark7)

### make_barcode<a name="mark14"></a>[^](#mark13)
> **Core barcode generation function, returns a PIL Image object.**
> 
> ```python
def make_barcode(val: str, font: _io.BytesIO, size: int = 50, padx: int = 10, pady: int = 10, background: tuple = (255, 255, 255, 255), foreground: tuple = (0, 0, 0, 255)):
> 	...
> ```
### encode_39<a name="mark15"></a>[^](#mark13)
> **Makes a string ready for the Code 39 font, returns a String.**
> 
> ```python
def encode_39(val: str):
> 	...
> ```
### get_code_39_font_data<a name="mark16"></a>[^](#mark13)
> **Returns a BytesIO file object containing the loaded normal Code 39 font. Takes no arguments.**
> 
> ```python
def get_code_39_font_data():
> 	...
> ```
### get_code_39_extended_font_data<a name="mark17"></a>[^](#mark13)
> **Returns a BytesIO file object containing the loaded extended Code 39 font. Takes no arguments.**
> 
> ```python
def get_code_39_extended_font_data():
> 	...
> ```
### get_code_39_font_and_extended_font_data<a name="mark18"></a>[^](#mark13)
> **Returns a tuple of BytesIO file objects containing the normal and extended fonts. Takes no arguments.**
> 
> ```python
def get_code_39_font_and_extended_font_data():
> 	...
> ```
# Single File Usage<a name="mark19"></a>[^](#mark0)

```python
This project was designed with single-file usage in mind.
py_simple_barcode.py relies on only the standard python library and pillow.
The Libre Barcode 39 TrueType Fonts are packaged within the script file in a compressed format.
```
# Changelog<a name="mark20"></a>[^](#mark0)

## 0.0.0<a name="mark21"></a>[^](#mark20)

Push

## 0.2.0<a name="mark22"></a>[^](#mark20)

Move to new build system.

