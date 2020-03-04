"""A moduke for dealing with BMP bitmap image files."""


def write_grayscale(filename, pixels):
    """Creates and writes a grayscale BMP file.

    Args:
        filename: The name of the BMP file to be created.

        pixels: a rectangular image stored as a sequence of rows.
            Each row must be an iterable series of integers in the
            range 0-255.


    Raises:
        ValueError: If any of the integer values are out of range.
        OsError: If the file could'nt be written.
    """

    #Here improve that all rows have the same length in production code
    height = len(pixels)
    width = len(pixels[0])

    with open(filename, 'wb') as bmp:
        #BMP header
        bmp.write(b'BM')

        size_bookmark = bmp.tell()      #the next four bytes hold the filesize as a 32-bit
        bmp.write(b'\x00\x00\x00\x00')  # little-endian integer. Zero placeholder for now.

        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00')  # Unused 16-bit integer - should be zero

        pixel_offset_bookmark = bmp.tell()  # The next four bytes hold integer offset to the
        bmp.write(b'\x00\x00\x00\x00')      # pixel data. Zero placeholder for now.

        #image Header
        bmp.write(b'\x28\x00\x00\x00')  #Image header size in bytes - 40 decimal
        bmp.write(_int32_to_bytes(width))  # Image width in pixels
        bmp.write(_int32_to_bytes(height))  # Image height in pixels
        bmp.write(b'\x01\x00')              # Number of image planes
        bmp.write(b'\x08\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')
        bmp.write(b'\x00\x00\x00\x00')

        #Color palette - a linear grayscale
        #you can enhace this to make its own function to get these values
        for c in range(256):
            bmp.write(bytes((c,c,c,0)))  #Blue, Green, Red, Zero

        #pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * ((4 -(len(row) % 4)) % 4)
            bmp.write(padding)

        #end of file
        eof_bookmark = bmp.tell()

        #fill in file size placeholders
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        #fill in pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))


def _int32_to_bytes(i):

    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 24 & 0xff))
