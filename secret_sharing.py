import networkx as nx
import matplotlib.pyplot as plt
import scipy.sparse as sp
import sympy as spsy
from sympy import symbols, interpolate, log

def binary_string_to_graph(binary_string):
    n = len(binary_string)
    row_indices = []
    col_indices = []

    for i in range(n):
        if binary_string[i] == '0':
            for j in range(i + 1, n):
                row_indices.append(i)
                col_indices.append(j)
        elif binary_string[i] == '1':
            for j in range(i):
                row_indices.append(i)
                col_indices.append(j)

    graph = sp.csr_matrix((n, n), dtype=int)
    graph[row_indices, col_indices] = 1

    return graph

def visualize_graph(graph):
    nx_graph = nx.Graph(graph)

    pos = nx.spring_layout(nx_graph)
    nx.draw(nx_graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', width=0.5)

    plt.title("Graph Visualization")
    plt.axis('off')
    plt.show()

def create_binary_matrix(graph, n):
    binary_matrix = sp.lil_matrix((n, n), dtype=int)
    row_indices, col_indices = graph.nonzero()
    for i, j in zip(row_indices, col_indices):
        binary_matrix[i, j] = 1
    return binary_matrix

def binary_to_decimal(binary_row):
    decimal_value = 0
    for bit in binary_row:
        decimal_value = (decimal_value << 1) | bit
    return decimal_value

def retrieve_binary_string(binary_matrix):
    n = binary_matrix.shape[0]
    binary_string = ""

    # Handle the first row
    if all(binary_matrix[0, j] == 0 for j in range(n)):
        binary_string += '1'

    i = 0
    while i < n:
        found = False
        for j in range(i + 1):
            if binary_matrix[i, j] == 1:
                binary_string += '1'
                found = True
                break
        if not found:
            for j in range(i + 1, n):
                if binary_matrix[i, j] == 1:
                    binary_string += '0'
                    break
        i += 1

    # Handle the last row
    if all(binary_matrix[n-1, j] == 0 for j in range(n)):
        binary_string += '0'

    return binary_string

def binary_matrix_to_decimal_list(binary_matrix):
    n = binary_matrix.shape[0]
    decimal_list = []
    for j in range(n):
        decimal_value = 0
        for i in range(n):
            decimal_value += binary_matrix[i, j] * (2 ** i)
        decimal_list.append(decimal_value)
    return decimal_list

def generate_chromatic_polynomial(decimal_list):
    x = spsy.symbols('x')
    chromatic_polynomial = 0
    n = len(decimal_list)

    for i, coeff in enumerate(decimal_list):
        chromatic_polynomial += coeff * (x ** (n - (i+1)))

    return chromatic_polynomial

def calculate_chromatic_values(chromatic_polynomial, n):
    chromatic_values = []
    for x in range(1, n + 1):
        y = chromatic_polynomial.subs('x', x)
        chromatic_values.append(y)
    return chromatic_values

def calculate_chromatic_values(chromatic_polynomial, n):
    chromatic_values = []
    for x in range(1, n + 1):
        y = chromatic_polynomial.subs('x', x)
        chromatic_values.append(y)
    return chromatic_values    