
class Node :
    def __init__(self,value):
        self.value = value
        self.count = 1

    def __eq__(self, object) :
        return self.value == object.value

    def __gt__(self,object):
        return self.count>=object.count 

    def __lt__(self, object):
        return (self.value<=object.value)    
       
    def __str__(self) :
        return '\''+ self.value+'\'' 

    def __repr__(self):
        return '\''+ self.value +'\''    

class Graph:
    def __init__(self) :
       self.graph = {}
       self.count = 0

    def add_node(self,node:Node):
        self.graph[node.value] = []

    def add_edge(self,node_x:Node,node_y:Node):
        try:
            if (self.graph[node_x.value].__contains__(node_y) ):
                for x in self.graph[node_x.value]:
                    if (x.value==node_y.value):
                        x.count=node_y.count+1
            else:
                self.graph[node_x.value].append(node_y)            
        except:
            self.graph[node_x.value]=[node_y]

    def create_graph_intput(self,text_token):
        for i in range(len(text_token)):
            if(i==(len(text_token)-1)):
                self.add_node(Node(text_token[i]))
            if(i==0):
                self.add_node(Node(text_token[i]))
            else:
                self.add_edge(Node(text_token[i-1]),Node(text_token[i]))

    def create_graph_output(self,text_token):
        for i in reversed(range(len(text_token))):
            if(i==(len(text_token)-1)):
                self.add_node(Node(text_token[i]))
            if(i==0):
                self.add_node(Node(text_token[i]))
            else:
                self.add_edge(Node(text_token[i]),Node(text_token[i-1]))

    def sort_graph(self):
        for node in self.graph:
            x=sorted(self.graph[node], key=lambda Node: Node.count)
            yield (x)

    #ordena por cantidad de veces que aparece
    def sort_key(self,key):
        return sorted(self.graph[key.value],reverse=True, key=lambda Node: Node.count)
        

    def __str__(self) :
        tex=""
        for node in self.graph:
            for ady in self.graph[node]:
                tex=tex + (node + "---->"+ str(ady)+'(' + str(ady.count) + ')') + '\n'
        return tex

    def __iter__(self):
        for node in self.graph.keys():
            yield  self.graph[node]


text="La cantidad de información que inunda las plataformas de internet y redes sociales crece exponencialmente. Para los negocios, de internet este flujo representa un reto y una oportunidad cuando buscan  promoverse, proteger su imagen y sobresalir en la era de exceso de información. Las herramientas para de reconocimiento de imágenes pueden ser la clave para abrir el liberar el potencial escondido dentro de la creciente cantidad de imágenes en línea."
tex_token = text.split()

grapo=Graph()
grapo.create_graph_intput(tex_token)

print(grapo.sort_key(Node("de")))

