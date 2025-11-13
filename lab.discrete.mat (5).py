"""Module lab from discrete mathematics"""
import copy

def open_file(pathname:str) -> list[list[str]]:
    """
    Reads a text file and transforms its contet into matrix.
    Args:
        pathname (str): name of path to file.
    Returns:
         list[list[str]] : matrix representing a relation from file.
    """
    matrix_new=[]
    with open(pathname,'r',encoding='UTF-8') as file:
        for line in file:
            line1=line.strip()
            line2=[]
            for i in line1:
                line2.append(i)
            matrix_new.append(line2)
    return matrix_new
def write_file(pathname:str,matrix:list[list[str]]) -> None:
    """
    Writes new matrix to file.
    Args:
        pathname (str): name of path to file.
        matrix list[list[str]] : matrix of relation
    Returns:
        None because function write matrix in file.
    """
    with open(pathname,'w',encoding='UTF-8') as file:
        for i in matrix:
            line=''
            for j in i:
                line+=str(j)+' '
            file.write(line.strip()+'\n')
def symmetrical_relation(matrix:list[list[str]]) -> list[list[str]]:
    """
    Returns the symmetric closure of a given relation matrix.
    Args:
        matrix list[list[str]] : matrix of relation
    Returns:
        list[list[str]] : symmetrical matrix to a given relation
    >>> symmetrical_relation([['0', '1', '0'], ['0', '0', '1'], ['1', '0', '1']])
    [['0', '1', '1'], ['1', '0', '1'], ['1', '1', '1']]
    """
    lenght=len(matrix)
    for i in range(lenght):
        for j in range(lenght):
            if matrix[i][j]=='1':
                matrix[j][i]='1'
    return matrix
def reflexive_relation(matrix:list[list[str]]) -> list[list[str]]:
    """
    Returns the reflexive closure of a given relation matrix.
    Args:
        matrix:list[list[str]] : matrix of relation
    Returns:
        list[list[str]] : reflexive matrix to a given relation
    >>> reflexive_relation([['0', '1', '0'], ['0', '0', '1'], ['1', '0', '1']])
    [['1', '1', '0'], ['0', '1', '1'], ['1', '0', '1']]
    """
    lenght=len(matrix)
    for i in range(lenght):
        matrix[i][i]='1'
    return matrix
def transitive_closure(matrix:list[list[str]]) -> list[list[str]]:
    """
    Returns the transitive closure of a relation matrix using the Warshall algorithm.
    Args:
        matrix:list[list[str]] : matrix of relation
    Returns:
        list[list[str]] : transitive matrix to a given relation
    >>> transitive_closure([['0', '1', '0'], ['0', '0', '1'], ['1', '0', '1']])
    [['1', '1', '1'], ['1', '1', '1'], ['1', '1', '1']]
    >>> transitive_closure([['0', '1', '0'], ['0', '0', '1'], ['0', '0', '1']])
    [['0', '1', '1'], ['0', '0', '1'], ['0', '0', '1']]
    """
    lenght=len(matrix)
    for i in range(lenght):
        for j in range(lenght):
            if i==j:
                pass
            else:
                if matrix[j][i]=='1':
                    for k in range(lenght):
                        if matrix[i][k]=='1':
                            matrix[j][k]='1'
    return matrix
def equivalence_classes(matrix:list[list[str]]) -> list[list[str]]|None:
    """
    Finds equivalence classes of a given equivalence relation matrix.
    Args:
        matrix:list[list[str]] : matrix of relation
     Returns:
        list[list[str]]|None : equivalence_classes to a given relation, if the relation is 
        not eqivalent returns None
    >>> equivalence_classes([['1', '0', '0'], ['0', '1', '1'], ['0', '1', '1']])
    [['0'], ['1', '2'], ['1', '2']]
    >>> equivalence_classes([['0', '1', '0'], ['0', '0', '1'], ['0', '0', '1']])
    >>> equivalence_classes([['0','1'], ['0','0']]) is None
    True
    """
    n=len(matrix)
    if if_transitive(matrix) is True:
        for i in range(n):
            for j in range(n):
                if matrix[i][i]=='0' or (matrix[i][j]=='0' and matrix[j][i]=='1'):
                    return None
        result=[[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if matrix[i][j]=='1':
                    result[i].append(str(j))
        return result
def if_transitive(matrix:list[list[str]]) -> bool:
    """
    Checks if a relation matrix is transitive.
    Args:
        matrix:list[list[str]] : matrix of relation
    Returns:
        bool : True if matrix is transitive and False if not.
    >>> if_transitive([['1', '0', '0'], ['0', '1', '1'], ['0', '1', '1']])
    True
    >>> if_transitive([['0', '1', '0'], ['0', '0', '1'], ['0', '0', '1']])
    False
    """
    matrix1=copy.deepcopy(matrix)
    matrix2= transitive_closure(matrix)
    lenght=len(matrix)
    for i in range(lenght):
        for j in range(lenght):
            if matrix1[i][j]!=matrix2[i][j]:
                return False
    return True
def amount_of_transitive(n:int) -> int:
    """
    Finds the number of transitive relations on a set of n elements.
    Args:
        n (int): set of n elements
    Return:
        int: amount of transitive relations
    >>> amount_of_transitive(2)
    13
    >>> amount_of_transitive(3)
    171
    """
    all_pairs=[]
    for i in range(n):
        for j in range(n):
            all_pairs.append([i,j])
    all_sets=[[]]
    amount=0
    for i in all_pairs:
        new_set=[]
        for j in all_sets:
            new_pair=j+[i]
            new_set.append(new_pair)
        all_sets+=new_set
    for k in all_sets:
        matrix=[[] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if [i,j] in k:
                    matrix[i].append('1')
                else:
                    matrix[i].append('0')
        if if_transitive(matrix) is True:
            amount+=1
    return amount
x=open_file('e.csv')
print(x)
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

