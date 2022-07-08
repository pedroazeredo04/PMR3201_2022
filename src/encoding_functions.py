from src.tree_functions import BST, create_tree, linearize_tree, delinearize_tree
from src.utils import separate_bin_bytes


def encodes_text(text):
    '''Encodes a text following huffman codification method
    
    Parameters
    ----------
    - text: string
      - the text to be codificated
      
    Returns
    -------
    - codificated_text: string
      - the text turned into binary though huffman codification
    '''

    arvore = BST(create_tree(text))
    raiz = arvore.get_root()

    tabela = arvore.creates_codification_table(raiz)

    codificated_text = ''

    for letter in text:
        for tupla in tabela:
            if letter == tupla[0]:
                codificated_text += str(tupla[1])

    return codificated_text


def creates_huf_msg(text):
    '''Function that turns a text into the form requested by the .huf file.
    The form consists of a byte organization:
    First 3 bytes: number of different characters in the original text
    Next 4 bytes: string referring to the size of the codificated message
    Next n bytes: string referring to the linearized tree
    Rest of the bytes: the message itself, in binary

    Parameters
    ----------
    - text: string
      - the text that is going to be written into the .huf file.

    Returns
    -------
    - huf_msg_list: list
      - A list that contains the bytes of the huffman message.
      It is formed by the byte organization explained above.
    '''

    huf_msg_list = []
    encoded_msg = encodes_text(text)

    # writes first 3 bytes:
    # string of algarisms representing the number of different characters in the message
    diff_alg = ''

    for letter in text:
        if letter not in diff_alg:
            diff_alg += letter

    first_bytes_base = '00' + str(len(diff_alg))

    byte1 = int(first_bytes_base[-3])
    byte2 = int(first_bytes_base[-2])
    byte3 = int(first_bytes_base[-1])

    huf_msg_list += [byte1, byte2, byte3]

    # writes next 4 bytes (number of bytes of encoded message):
    # na pratica, the lenght of the encoded message
    second_bytes_base = '000' + str(len(encoded_msg))

    byte1 = int(second_bytes_base[-4])
    byte2 = int(second_bytes_base[-3])
    byte3 = int(second_bytes_base[-2])
    byte4 = int(second_bytes_base[-1])

    huf_msg_list += [byte1, byte2, byte3, byte4]

    # writes preordertraverse bytes:
    # a series of '0' and '1' that represents the linearized tree
    linearized_tree = linearize_tree(text)
    huf_msg_list += separate_bin_bytes(linearized_tree + encoded_msg)

    return huf_msg_list


def decodes_huf_msg(text):
    '''Decodes a text written in binary encoded by the huffman codification method
    The text must be structured in the following way:
    1. First 3 bytes: number of different characters in the original text
    2. Next 4 bytes: string referring to the size of the codificated message
    3. Next n bytes: string referring to the linearized tree
    4. Rest of the bytes: the message itself, in binary
    
    Parameters
    ----------
    - text: str
      - the encoded text that is going to be decoded. 
      it is written in 8 bit binary
    
    Returns
    -------
    - decoded_text: str
      - the decoded text
    '''

    # first 3 bytes:
    # (different characters number)
    diff_char_num = ''
    for i in range(3):
        diff_char_num += str(int(text[i*8:(i+1)*8], 2))
    diff_char_num = int(diff_char_num)
    text = text[24:]

    # next 4 bytes:
    # (number of bits of the encoded message nb)
    bits_num = ''
    for i in range(4):
        bits_num += str(int(text[i*8:(i+1)*8], 2))
    bits_num = int(bits_num)
    text = text[32:]
    
    # next n bytes:
    # the linearized tree
    i = one_num = 0
    while one_num < diff_char_num:
        if text[i] == '1':
            i += 9
            one_num += 1
        elif text[i] == '0':
            i += 1

    # the message bytes:
    linear_tree = text[:i]

    text = text[i:i + bits_num]

    tree = BST(delinearize_tree(linear_tree, diff_char_num))
    no_atual = tree.get_root()

    decoded_text = ''

    for i in range(len(text)):

        # forA do terminal
        if text[i] == '0':
            no_atual = no_atual.left

        elif text[i] == '1':
            no_atual = no_atual.right

        if no_atual.caracter != None:  # no terminal
            decoded_text += no_atual.caracter
            no_atual = tree.get_root()

    return decoded_text
