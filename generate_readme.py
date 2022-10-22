from py_simple_barcode import (
    Encoder,
    encode_39,
    make_barcode,
    get_code_39_font_data,
    get_code_39_extended_font_data,
    get_code_39_font_and_extended_font_data,
)
from py_simple_readme import readme_generator

about = """A basic Code 39 barcode generator using PIL and the Libre Barcode 39 font family

Libre Barcode 39 is subject to the Open Font License and can be found at https://fonts.google.com/specimen/Libre+Barcode+39

Libre Barcode 39 Extended Text is subject to the Open Font License and can be found at https://fonts.google.com/specimen/Libre+Barcode+39+Extended+Text

See OFL.txt for font license details."""

command_line_desc = """Command line usage has two modes of operation: Single mode and File mode. In Single mode, a single barcode is generated using the the prompt passed to the command line. In File mode, a file at a provided path serves as a source of the barcode prompts.  """

file_mode_desc = """File mode is useful for batch production of barcodes.
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
"""

single_mode_desc = """Single mode is useful for one-off production of barcodes.
Pass the value to be encoded.
#### Example usage:
`py_simple_barcode.py 120231`
"""

installation_message = """Available on pip - `pip install py_simple_barcode`

Alternatively download py_simple_barcode.py to your project directory and import it."""

manifest_system_desc = """Both Single Mode and File Mode have an optional manifest system that allows for easy tracking with an `output/manifest.json` that maps which barcodes have been generated to their file locations.

Use the `-m` flag to enable the manifest system.

The `-mn` argument will override the default manifest name.

The `-om` argument will cause the script overwrite the previous manifest entirely rather than just adding a new entry, this does not remove the output files from the hard drive."""

command_line_usage = """usage: py_simple_barcode.py [-h] [-e] [-f] [-sc] [-i] [-m] [-o OUTPUT] [-t TYPE] [-s SIZE] [-px PADX] [-py PADY]
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
                        existing json will be updated to include new entries."""

module_desc = """Encoder objects simplify handling multiple barcode sub-types."""

encoder_example = """from py_simple_barcode import Encoder

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
extended_barcode.save("extended_barcode.png")"""

make_barcode_example = """from py_simple_barcode import make_barcode, get_code_39_font_data

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
extended_barcode.save("extended_barcode.png")"""

single_file_usage = """This project was designed with single-file usage in mind.
py_simple_barcode.py relies on only the standard python library and pillow.
The Libre Barcode 39 TrueType Fonts are packaged within the script file in a compressed format."""


example_images = {
    "8675309_extended_lilac": "https://raw.githubusercontent.com/AndrewSpangler/py_simple_barcode/main/examples/8675309_extended_lilac.png",
    "12345_normal_pink": "https://raw.githubusercontent.com/AndrewSpangler/py_simple_barcode/main/examples/12345_normal_pink.png",
    "abcde_normal_mint": "https://raw.githubusercontent.com/AndrewSpangler/py_simple_barcode/main/examples/abcde_normal_mint.png",
    "123456789_extended_turquoise": "https://raw.githubusercontent.com/AndrewSpangler/py_simple_barcode/main/examples/123456789_extended_turquoise.png",
    "abcde_extended_lilac": "https://raw.githubusercontent.com/AndrewSpangler/py_simple_barcode/main/examples/abcde_extended_lilac.png",
}


def generate_readme(tables: dict, changelog: dict):
    name = tables["project"]["name"]
    version = tables["project"]["version"]
    description = tables["project"]["description"]

    gen = readme_generator(title=f"{name} {version}", slogan=description)
    gen.set_changelog(changelog)
    gen.set_slogan(slogan)
    for i in example_images:
        gen.add_image((i, example_images[i]))
    gen.add_heading_1("About")
    gen.add_paragraph(about_text)
    gen.increase_toc_depth()
    gen.add_heading_2("Installation")
    gen.add_paragraph(installation_message)
    gen.decrease_toc_depth()
    gen.add_heading_1("Command Line Usage")
    gen.add_paragraph(command_line_desc)
    gen.add_code_block(command_line_usage)
    gen.increase_toc_depth()
    gen.add_heading_2("Single Mode")
    gen.add_paragraph(single_mode_desc)
    gen.add_heading_2("File Mode")
    gen.add_paragraph(file_mode_desc)
    gen.add_heading_2("Manifest System")
    gen.add_paragraph(manifest_system_desc)
    gen.decrease_toc_depth()
    gen.add_heading_1("Module Usage")
    gen.add_paragraph(module_desc)
    gen.increase_toc_depth()
    gen.add_heading_2("Examples")
    gen.increase_toc_depth()
    gen.add_heading_3("Using the Encoder (the easy way)")
    gen.add_code_block(encoder_example)
    gen.add_heading_3("Using make_barcode directly (the hard way)")
    gen.add_code_block(make_barcode_example)
    gen.decrease_toc_depth()
    gen.add_heading_2("The Encoder")
    handle_class_list([Encoder])
    gen.add_heading_2("Functions")
    handle_function_list(
        [
            make_barcode,
            encode_39,
            get_code_39_font_data,
            get_code_39_extended_font_data,
            get_code_39_font_and_extended_font_data,
        ]
    )
    gen.decrease_toc_depth()
    gen.add_heading_1("Single File Usage")
    gen.add_code_block(single_file_usage)
    return gen.assemble()
