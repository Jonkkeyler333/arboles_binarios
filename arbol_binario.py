class nodo:
    def __init__(self,element:any,parent:None,left=None,right=None) -> None:
        self.element=element
        self.father=parent
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self,root) -> None:
        self.root=root
        self.height=0  ##altura
        self.weight=0  ##peso
        self.order=0
    
    def add(self,element) -> None:
        new_nodo=nodo(element)
        if self.weight==0:
            self.root=new_nodo
            self.height+=1
            self.weight
        else:
            pass

            