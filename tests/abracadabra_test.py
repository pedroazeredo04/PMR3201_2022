from ..src.encoding_functions import creates_huf_msg, decodes_huf_msg
import src.utils

text = src.utils.read('abracadabra.txt')
print(f'O texto lido foi: {text}')

encoded_bytes = creates_huf_msg(text)
print(f'O texto codificado em bytes foi: {encoded_bytes}')

decoded_bytes = src.utils.bytes_to_str(encoded_bytes)

decoded_text = decodes_huf_msg(decoded_bytes)
print(f'O texto decodificado foi: {decoded_text}')
