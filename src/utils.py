def char_to_bin(char):
    '''Converts a character into ascii in 8 bit binary form
    
    Parameters
    ----------
    - char: string
      - the character that is going to be converted

    Returns
    -------
    - bin_ascii: string
      - the 8 bit binary of the character following the ascii convention  
    '''

    bin_ascii = bin(ord(char))[2:]

    missing_to_eight = 8 - len(bin_ascii)

    if missing_to_eight > 0:
        bin_ascii = '0'*missing_to_eight + bin_ascii

    return bin_ascii


def separate_bin_bytes(binary):
    '''Turns a binary text into a list formed by 1 byte integers
    
    Parameters
    ----------
    - binary: string
      - the binary number that is going to be converted into bytes

    Returns
    -------
    - bytes_list: list
      - a list formed by the integers of the bytes of the binary text
    '''

    binary = binary + '0' * (8 - len(binary) % 8) if (len(binary) % 8 != 0) else binary
    # '0' * (8 - len(binary) % 8) is added because it's whats missing for a full byte

    index = 0
    next_index = 8
    bytes_list = []

    while next_index <= len(binary):
        current_byte = int(binary[index:next_index], 2)
        bytes_list.append(current_byte)
        index = next_index
        next_index += 8  # the lenght of a byte

    return bytes_list


def read(file_name):
    '''Function that reads a given file
    
    Parameters
    ----------
    - file_name: string
      - the relative path to the file that is going to be read

    Returns
    -------
    - str_text: string
      - A string containing the content of the file
    '''
    t = open('docs/' + file_name, 'r')
    str_text = t.read()
    t.close()

    return str_text


def read_bytes(file_name):
    '''Function that reads a given file
    
    Parameters
    ----------
    - file_name: string
      - the relative path to the file that is going to be read

    Returns
    -------
    - str_text: string
      - A string containing the content of the file
    '''
    t = open('docs/' + file_name, 'rb')
    str_text = t.read()
    t.close()

    return str_text


def write(file_name, message):
    '''Fcuntion that writes at a given file
    
    Parameters
    ----------
    - file_name: string
      - the relative path to the file that is going to be read
    - message: string
      - the string to be written
    '''
    f = open('docs/' + file_name, 'w')
    f.write(message)
    f.close()


def write_bytes(file_name, message):
    '''Fcuntion that writes at a given file
    
    Parameters
    ----------
    - file_name: string
      - the relative path to the file that is going to be read
    - message: string
      - the string to be written
    '''
    f = open('docs/' + file_name, 'wb')
    f.write(message)
    f.close()


def bytes_to_str(encoded_bytes):
    '''Turns the bytes file read from .huf back into a string
    
    Parameters
    ---
    - encoded_bytes: bytes
      - The bytes text to be turned into a string

    - huf_msg: str
      - The string corresponding to the bytes file
    '''

    huf_msg = ''
    for byte in encoded_bytes:
        if len(bin(byte)[2:]) % 8 != 0:
            binary_byte = '0' * (8 - len(bin(byte)[2:])%8) + bin(byte)[2:]
        else:
            binary_byte = bin(byte)[2:]
        huf_msg += binary_byte
    
    return huf_msg
