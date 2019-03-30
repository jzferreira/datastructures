#!/bin/python3

class Node:
    '''Classe que representa um item do Linked List'''
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    '''Classe que representa a estrutura de classe LinkedList'''
    def __init__(self, head = None):
        self.head = head
        self.__size = 0

    def is_empty(self):
        return (self.head is None)

    def insert_tail(self, value=None):
        if (value is None):
            return
        #cria um novo Nó com o valor passado
        new_node = Node(data=value)
        #incrementa o tamanho da linked list
        self.__size += 1
        #se a lista estiver vazia, adicione o nome nó como o Head
        if (self.is_empty()):
            self.head = new_node
        else:
            #senão, vamos até o final da Linked List para podermos adicionar
            last = self.head
            while (last.next is not None):
                last = last.next
            last.next = new_node


    def insert_head(self, value=None):
        if (value is None):
            return
        #cria um novo Nó com o valor passado
        new_node = Node(data=value)
        #incrementa o tamanho da linked list
        self.__size += 1
        if (self.is_empty()):
            self.head = new_node
        else:
            #recuperamos o proximo do head
            current = self.head
            self.head = new_node
            self.head.next = current


    def find_node(self, value=None):
        if (value is None):
            return
        if (self.is_empty()):
            print('Linked Lista Vazia\n')
            return None
        else:
            current = self.head
            pos = 0
            while (current is not None):
                if (current.data == value):
                    print(f'{value} foi encontrado na posicao {pos}\n')
                    break
                else:
                    current = current.next
                    pos += 1
            if (current is None):
                print(f'{value} nao esta na lista\n')
                pos = -1
            return current, pos

    
    def update_value(self, value=None, new_value=None):
        if (value is None or new_value is None):
            return
        if (self.is_empty()):
            print('Linked Lista Vazia\n')
        else:
            current = self.head
            while (current is not None):
                if (current.data == value):
                    current.data = new_value
                    break
                else:
                    current = current.next

    def update_value_at_position(self, value=None, pos=-1):
        if (value is None):
            return
        if (pos < 0):
            return
        if(self.is_empty()):
            print('Linked Lista Vazia\n')
        else:
            current = self.head
            index = 0
            while (current is not None):
                if (index == pos):
                    current.data = value
                else:
                    current = current.next
                    index += 1
    

    def delete(self, value):
        if (value is None):
            return
        
        if (self.is_empty()):
            print('Linked Lista Vazia\n')
            return None

        else:
            current = self.head
            prev = None

            #1 caso: o head é o Nó a ser removido
            if (current is not None and current.data == value):
                self.head = current.next
                print(f'{value} foi removido e era o head, o novo head e {self.head.data}\n')
                #incrementa o tamanho da linked list
                self.__size -= 1
                return
            
            #2 caso: o valor a ser deletado está no meio da lista
            # Vamos procurar o valor e salvar o nó anterior visitado
            while (current is not None and current.data != value):
                prev = current
                current = current.next
            
            # se o current Node for diferente de None, então precisamos definir o prev.next
            # com o proximo do current. Assim, removemos o nó
            if (current is not None):
                prev.next = current.next
                self.__size -= 1
                print(f'{value} foi removido\n')
            else:
                # porém, se o current Node for None, porque nao achou
                print(f'{value} nao foi encontrado\n')
            

    def delete_at_position(self, pos=-1):
        if (pos < 0):
            return
        if (self.is_empty()):
            return
        
        if (pos + 1) >= self.size():
            print('Posicao nao encontrada2\n')
        else:
            current = self.head
            prev = None
            # 1 caso: Seja o head a ser removido
            if (pos == 0 and current is not None):
                #remove o HEAD
                self.head = current.next
                self.__size -= 1
                return
            
            #2 caso: seja o caso do index ser maior que zero e menor que o tamanho
            index = 0
            while (current is not None):
                if (index == pos):
                    prev.next = current.next
                    self.__size -= 1
                    break
                else:
                    prev = current
                    current = current.next
                    index += 1
            
            #caso 3: nao achou. Essa parte nao e necessaria pois comparamos antes de entrar no else
            if (current is None):
                print('Posicao não encontrado\n')

    def size(self):
        return self.__size


    def print_list(self):
        if (self.is_empty()):
            print('Linked List esta vazia\n')
        else:
            current = self.head
            while (current is not None):
                print(current.data, end=' -> ')
                current = current.next


LinkedList = LinkedList()
for i in range(1,11):
    LinkedList.insert_tail(i)

LinkedList.print_list()
print()
LinkedList.find_node(11)
LinkedList.delete(10)
print(f'Tamanho da Lista: {LinkedList.size()}\n')
LinkedList.print_list()
LinkedList.delete(1)
LinkedList.print_list()
print(f'Tamanho da Lista: {LinkedList.size()}\n')
LinkedList.insert_head(1)
LinkedList.delete_at_position(1)
LinkedList.print_list()
LinkedList.update_value(1,20)
LinkedList.update_value(50, 30)
print()
LinkedList.print_list()
print()
LinkedList.update_value_at_position(3, 50)
LinkedList.update_value_at_position(30, 50)
print()
LinkedList.print_list()
