class nodo:
    def __init__(self,element:any,parent=None,left=None,right=None) -> None:
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

    def search(self,element:any,current_nodo=None)->nodo:
        if not(current_nodo):
            current_nodo=self.root
        if current_nodo.element==element:
            return current_nodo
        left=self.search(element,current_nodo.left)
        if left:
            return left
        right=self.search(element,current_nodo.right)
        if right:
            return right
        
    def add(self,element,parent=None) -> None:
        new_nodo=nodo(element,parent)
        if self.weight==0:
            self.root=new_nodo
            self.height+=1
            self.weight+=1
        else:
            if parent.left is not(None):
                parent.left=new_nodo
            else:
                parent.right=new_nodo
            new_nodo.parent=parent
            self.weight+=1
            
            