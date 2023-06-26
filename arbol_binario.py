class nodo:
    def __init__(self,element:any,parent=None,left=None,right=None) -> None:
        self.element=element
        self.father=parent
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self) -> None:
        self.root=None
        self.height=0  ##altura
        self.weight=0  ##peso
        self.order=0

    def search(self,element:any,current_nodo:nodo)->nodo:
        if current_nodo.element==element:
            return current_nodo
        if  current_nodo.left:
            left=self.search(element,current_nodo.left)
            if left:
             return left
        if  current_nodo.right:
            right=self.search(element,current_nodo.right)
            if right:
                return right
        return None
        
    def _recorrido_preorden(self,node:nodo):
        if node is not None:
            print(node.element)
            self._recorrido_preorden(node.left)
            self._recorrido_preorden(node.right)
    
    def imprimir_preorden(self):
        self._recorrido_preorden(self.root)
        
    def add(self,element,parent=None) -> None:
        new_nodo=nodo(element)
        if self.weight==0:
            self.root=new_nodo
            self.height+=1
            self.weight+=1
        else:
            father=self.search(parent,self.root)
            if not(father):
                raise 'El nodo padre indicado no existe'
            if father.left is None:
                father.left=new_nodo
            elif father.right is None:
                father.right=new_nodo
            else:
                raise Exception('El nodo padre ya tiene dos hijos')
            new_nodo.parent=father
            self.weight+=1
            
if __name__=='__main__':
    a1=BinaryTree()
    a1.add(10)
    a1.add(2,10)
    a1.add(3,10)
    a1.add(7,2)
    a1.add(5,2)
    a1.add(1,3)
    a1.imprimir_preorden()