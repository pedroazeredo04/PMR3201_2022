from heapq import heappush, heappop
from src.utils import char_to_bin

# global variables
current_linear_tree = ''

class Node:  # Classe que define um no da arvore binaria
    def __init__(self, car=None, freq=None, left=None, right=None):
        self.caracter = car  # caracter caso seja um no terminal
        self.frequencia = freq  # numero de ocorrencias do caracter
        self.left = left  # ponteiro filho da esquerda
        self.right = right  # ponteiro filho da direita

    def __str__(self):  # Utilizado para impressao de um
        if (self.caracter is None):  # objeto tipo Node fora do terminal
            return('0')
        else:
            return('1')  # No terminal (leaf node)

    def __le__(self, other):
        return self.frequencia <= other.frequencia

    def __lt__(self, other):
        return self.frequencia < other.frequencia


class BST:  # Classe que define uma arvore de busca binaria
    def __init__(self, root=None):  # BST (Binary Search Tree)
        self.root = root

    def get_root(self):
        return self.root

    def creates_codification_table_rec(self, p, current_terminal_codification, current_list):
        '''Codificates a tree by traversing the tree from top to bottom.
        When the path goes to right, the function adds a '0' to the codification, and a '1' otherwise.
        
        Parameters
        ----------
        - p: node
          - the tree root
        - current_terminal_codification: string
          - a codifications of the terminals at given moment
        - current_list: array
          - a list that matches each codification with its corresponding terminal at given moment

        Returns
        -------
        - current_list: array
          - dictionary that matches each codification with its corresponding terminal caracter
        '''

        if (p is not None):

            if (p.caracter is not None):  # No terminal
                current_list.append([p.caracter, current_terminal_codification])

            else:  # Fora do terminal
                self.creates_codification_table_rec(
                    p.left, current_terminal_codification + '0', current_list)  # recursao a esquerda
                self.creates_codification_table_rec(
                    p.right, current_terminal_codification + '1', current_list)  # recursao a direita

        return current_list

    def creates_codification_table(self, p):
        '''Codificates a tree by calling creates_codification_table_rec with its right starting parameters.
        
        Parameters
        ----------
        - p: node
          - the tree root

        Returns
        -------
        - creates_codification_table_rec(p, '', []): list
          - dictionary that matches each codification with its corresponding terminal caracter
        '''

        return self.creates_codification_table_rec(p, '', [])

    def linearize_tree_rec(self, p):
        global current_linear_tree
        '''A function that linearizes a tree, by crossing it in preordertraverse
        
        Parameters
        ----------
        - p: node
          - the tree root
        - current_linear_tree: string
          - a global variable that represents the linear tree at given moment

        Returns
        -------
        - current_linear_tree: string
          - the linearized tree after its completion
        '''

        # if (p is not None): condicao comentada pois é redundante

        current_linear_tree += str(p)  # writes '1' or '0', depending if it is a terminal or not

        if p.caracter is not None:  # No terminal
            current_linear_tree += char_to_bin(str(p.caracter))

        else:  # Fora do terminal
            self.linearize_tree_rec(p.left)  # recursao a esquerda
            self.linearize_tree_rec(p.right)  # recursao a direita

        return current_linear_tree
    

def linearize_tree(text):
    '''Linearizes a tree defined by the text huffman codification
    
    Parameters
    ----------
    - text: string
      - the text to be codificated
      
    Returns
    -------
    - linearize_tree_rec(): string
      - the linear form of the tree
    '''

    arvore = BST(create_tree(text))
    raiz = arvore.get_root()

    return arvore.linearize_tree_rec(raiz)


def create_tree(text):
    '''Creates a tree following the Huffman Codification method

    Parameters
    ----------
    - text: string
      - The text that will be turned into a binary tree

    Returns
    -------
    - tuples[1]: Node
      - A node that represents the root of the codification tree
    '''
    tuples = []
    occurrences = []

    for letter in text:
        # Quero adicionar só os caracteres cujos nodes ainda nao foram criados
        if letter not in occurrences:
            current_node = Node(letter, text.count(letter))
            heappush(tuples, (current_node.frequencia, current_node))

            occurrences.append(letter)

    # Enquanto tuples não for uma lista formada apenas pela tupla contendo a raíz da árvore
    while len(tuples) > 1:
        # Calculates
        last_tuple = heappop(tuples)
        second_last_tuple = heappop(tuples)

        # Calculate new_node parameters:
        new_freq = last_tuple[0] + second_last_tuple[0]

        # Calculate new_node and updates nodes list
        new_node = Node(None, new_freq, last_tuple[1], second_last_tuple[1])
        heappush(tuples, (new_node.frequencia, new_node))

    # Return tree root
    return heappop(tuples)[1]


def delinearize_tree(linear_tree, diff_char_num):
    '''A function that constructs a tree based on its linearized form
    
    Parameters
    ----------
    - linear_tree: string
      - the tree in its linear form (a binary number)
    - diff_char_num: int
      - the number of different characters in the tree
      
    Returns
    -------
    - root_node: Node
      - the node that represents the tree root
    '''

    one_count = current_index = 0
    root_node = Node()
    non_terminal_node_list = [root_node]

    while one_count < diff_char_num:

        # first iteration case
        if linear_tree[current_index] == '0' and current_index == 0:
            current_index += 1
            pass

        # new terminal son
        elif linear_tree[current_index] == '1':
            current_char = str(chr(int(linear_tree[current_index + 1: current_index + 9], 2)))

            current_non_term_node = non_terminal_node_list.pop()

            if current_non_term_node.left is None:  # se não existe filho esquerdo
                current_non_term_node.left = (Node(current_char))
                non_terminal_node_list.append(current_non_term_node)

            elif current_non_term_node.left is not None:  # se existe filho esquerdo
                current_non_term_node.right = (Node(current_char))

            one_count += 1
            current_index += 9


        # new non terminal son
        elif linear_tree[current_index] == '0':
            new_node = Node()
            current_non_term_node = non_terminal_node_list.pop()
            
            # caso o nó já tenha filho esquerdo e direito, ele sai da lista
        
            if current_non_term_node.left is not None and current_non_term_node.right is not None:
                non_terminal_node_list.append(new_node)

            # se não existe filho esquerdo e estamos em zero, é adicionado um novo nó na lista
            # e esse nó é declarado como filho do ainda existente na lista "current_non_term_node"
            elif current_non_term_node.left is None:
                current_non_term_node.left = new_node
                non_terminal_node_list.append(current_non_term_node)
                non_terminal_node_list.append(new_node)
            
            # se existe filho direito, o nó pode sair da lista, entrando o novo declarado como direita
            # do velho "current_non_term_node"
            elif current_non_term_node.right is None:
                current_non_term_node.right = new_node
                non_terminal_node_list.append(new_node)

            current_index += 1
            
    return root_node
