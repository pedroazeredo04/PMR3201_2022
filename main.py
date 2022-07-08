from src.encoding_functions import decodes_huf_msg, creates_huf_msg
from src.utils import read, write, read_bytes, write_bytes, bytes_to_str


def main():
    user_option = '0'
    while user_option == '0':

        print('1 - Codificar mensagem')
        print('2 - Decodificar mensagem')
        user_option = input('O que deseja realizar? ')
        
        if user_option != '1' and user_option != '2':
            user_option = '0'
            raise NameError('Texto digitado não contempla as opções oferecidas')
        
        read_message_name = input('Informe o nome do arquivo a ser lido ')
        write_message_name = input('Informe o nome do arquivo que será escrito ')

        if user_option == '1':
            text = read(read_message_name)
            encoded_bytes = creates_huf_msg(text)
            write_bytes(write_message_name, bytes(encoded_bytes))
        
        elif user_option == '2':
            encoded_byte_text = read_bytes(read_message_name)
            encoded_huf_msg = bytes_to_str(encoded_byte_text)
            decoded_huf_msg = decodes_huf_msg(encoded_huf_msg)
            write(write_message_name, decoded_huf_msg)

        print('\nArquivo escrito com sucesso! Encerrando o programa.')

if __name__ == '__main__': main()
