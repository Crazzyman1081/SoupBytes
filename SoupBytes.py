#!/usr/bin/env python3
import argparse
import os

def rev(input_path, output_path, chunk_size=None):
    file_size = os.path.getsize(input_path)
    
    with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
        if chunk_size is None:
            data = f_in.read()
            f_out.write(data[::-1])
            print(f"Reversed the entire file: {file_size} bytes")
        else:
            total_chunks = 0
            while chunk := f_in.read(chunk_size):
                f_out.write(chunk[::-1])
                total_chunks += 1
            print(f"Reversed every {chunk_size} bytes in {total_chunks} chunks")

def main():
    parser = argparse.ArgumentParser(
        description="Reverse bytes in a file either entirely or in fixed-size chunks."
    )
    parser.add_argument('-f', '--file', required=True, help='  Input file path')
    parser.add_argument('-o', '--output', default='output.bin', help='  Output file path')
    parser.add_argument('-n', '--chunk', type=int, help='  Chunk size in bytes to reverse (e.g. 2, 4, 8)')

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' does not exist.")
        return

    rev(args.file, args.output, args.chunk)

if __name__ == '__main__':
    main()
