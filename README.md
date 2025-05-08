# 🥣 SoupBytes

A simple CLI tool to reverse bytes in a binary file
Made it just to easily solve some basic CTF forensics challenges
Feel free to use the script in your projects or fork this repo
Also let me know if you encounter any bugs or want any changes!

## Usage

```bash
python3 soupbytes.py -f file.bin          # Reverse entire file
python3 soupbytes.py -f file.bin -n 4     # Reverse every 4 bytes
python3 soupbytes.py -f file.bin -n 8 -o output.bin  # Reverse every 8 bytes to custom file
