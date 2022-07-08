from src.encoding_functions import creates_huf_msg, decodes_huf_msg
import src.utils

print('1 - abracadabra.txt')
print('2 - dickens.txt')
print('3 - Alice1.txt')

a = input('Escolha o arquivo a ser testado: ').strip()

if a == '1':
    text = src.utils.read('abracadabra.txt')
elif a == '2':
    text = src.utils.read('dickens.txt')
elif a == '3':
    text = src.utils.read('Alice1.txt')
else:
    raise NameError('Opção inválida escolhida. Encerrando o teste.')

print(f'O texto lido foi: {text}\n')

encoded_bytes = creates_huf_msg(text)
decoded_bytes = src.utils.bytes_to_str(encoded_bytes)

is_print_encoded_text = input('Deseja printar o texto codificado? [yN] ').strip().lower()

if is_print_encoded_text == 'y':
    print(f'O texto codificado, em binário, é: {decoded_bytes}\n')

decoded_text = decodes_huf_msg(decoded_bytes)
print(f'A decodificação do binário resultou em: {decoded_text}')
