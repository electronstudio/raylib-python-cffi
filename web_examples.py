# Written by AI

import os
import shutil

def convert(file_name):
    with open(file_name, "r") as f:
        # Read the lines of the file
        lines = f.readlines()

    # Create a temporary file name
    temp_file_name = file_name + ".tmp"

    # Open the temporary file in write mode
    with open(temp_file_name, "w") as f:
        # Write the first line to define the main() function
        f.write("""# /// script
# dependencies = [
#     "cffi",
#     "inflection",
#     "raylib"
# ]
# ///
import asyncio
import platform
from raylib import *
from pyray import *
async def main():
""")
        # Indent each line of the original file and write it to the temporary file
        for line in lines:
            if "from raylib import *" in line or "from pyray import *" in line:
                pass
            else:
                f.write("    " + line)

            indent = line[:len(line) - len(line.lstrip())]
            if "init_window" in line or "InitWindow" in line:
                f.write(indent + "    platform.window.window_resize()\n")
            if "end_drawing" in line or "EndDrawing" in line:
                f.write(indent + "    await asyncio.sleep(0)\n")




        # Write the last line to call the main() function
        f.write("\nasyncio.run(main())\n")

    # Delete the original file
    os.remove(file_name)

    # Rename the temporary file to the original file name
    os.rename(temp_file_name, file_name)

# Define the directory to start from
start_dir = "examples"

# Define the output directory
output_dir = "webexamples"
os.mkdir(output_dir)

# Loop through all the files and subdirectories
for root, dirs, files in os.walk(start_dir):
    # Loop through the files that match the pattern '*.py'
    for file in files:
        if ((file.startswith("core") or file.startswith("phys") or file.startswith("shapes") or file.startswith("text"))
                and file.endswith(".py")):
            # Get the full path of the file
            file_path = os.path.join(root, file)
            # Get the file name without the extension
            file_name = os.path.splitext(file)[0]
            # Create a new directory with the same name as the file in the output directory
            new_dir = os.path.join(output_dir, file_name)
            os.mkdir(new_dir)
            # Copy the file into the new directory and rename it 'main.py'
            new_file = os.path.join(new_dir, "main.py")
            shutil.copy(file_path, new_file)
            convert(new_file)
            os.system(f"cp -R examples/textures/resources {new_dir}")
            os.system("python3.12 -m pygbag --git --PYBUILD 3.12 --no_opt --can_close 1 --ume_block 0 --template noctx.tmpl --build "+new_file)
            os.system(f"rm -rf {new_dir}/resources")

os.system(f"touch {output_dir}/.nojekyll")

# Open the index.html file in write mode
with open(output_dir+"/index.html", "w") as index_file:

    # Write the HTML header
    index_file.write("<html>\n<head>\n<title>Directory Index</title>\n</head>\n<body>\n")

    # Write the title of the page
    index_file.write("<h1>Directory Index</h1>\n")

    # Write the list of subdirectories
    index_file.write("<ul>\n")
    sub_dirs = os.listdir(output_dir)

    # Sort the list of subdirectories in alphabetical order
    sub_dirs.sort()

    # Loop through the sorted subdirectories
    for sub_dir in sub_dirs:

        # Check if the subdirectory is a directory
        if os.path.isdir(os.path.join(output_dir, sub_dir)):

            # Write the subdirectory name and the link to frank.html
            index_file.write(f"<li><a href='{sub_dir}/build/web'>{sub_dir}</a>")
            #- <a href='{sub_dir}/main.py'>code</a></li>\n")

    # Close the list tag
    index_file.write("</ul>\n")

    # Write the HTML footer
    index_file.write("</body>\n</html>\n")
