class node:

    def __init__(self, identity, label, parents, children):
        '''
        identity: int; its unique id in the graph
        label: string;
        parents: int->int dict; maps a parent node's id to its multiplicity
        children: int->int dict; maps a child node's id to its multiplicity
        '''
        self.id = identity
        self.label = label
        self.parents = parents
        self.children = children

    def __str__(self) :
        return f'ID: {self.id} , Label: {self.label} , Parents: {self.parents} , Children = {self.children }'

    def __repr(self) :
        return __str__(self)

    def copy(self) :
        return node(self.id, self.label, self.parents, self.children)

    def get_id(self) :
        return self.id 

    def get_label(self) :
        return self.label 

    def get_parents(self) :
        return self.parents 
    
    def get_children(self) :
        return self.children

    def set_id(self, a) :
        self.id = a 

    def set_label(self, a) :
        self.label = a

    def set_parent_ids(self, a) :
        self.parents = a

    def set_children_ids(self, a) :
        self.children = a

    def add_child_id(self, a) : 
        self.children.update(a)

    def add_parent_id(self, a) :
        self.parent.update(a)



class open_digraph: # for open directed graph

    def __init__(self, inputs, outputs, nodes,):
        '''
        inputs: int list; the ids of the input nodes
        outputs: int list; the ids of the output nodes
        nodes: node iter;
        '''
        self.inputs = inputs
        self.outputs = outputs
        self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict

    def __str__(self) :
        return f'Inputs : {self.inputs} , Outputs : { self.outputs} , Nodes : {self.nodes} '

    def __repr__(self) :
        return __str__(self)

    def copy(self) :
        return open_digraph(self.inputs.copy(), self.outputs.copy(), [n.copy() for n in self.nodes.values()])

    def get_input_ids(self) : 
        return self.inputs

    def get_output_ids(self) :
        return self.outputs

    def get_id_node_map(self) :
        return self.nodes 

    def get_nodes(self) :
        return self.nodes.values()

    def get_node_ids(self) :
        return self.nodes.keys()

    def get_node_by_id(self, i ) :
        return self.nodes[i]

    def get_notes_by_ids(self, l ) :
        return [self.nodes[i] for i in l]

    def set_input_ids(self, a) :
        self.inputs = a

    def set_output_ids(self, a) :
        self.outputs = a

    def add_input_id(self, a) :
        self.inputs.append(a)

    def add_output_id(self, a) :
        self.outputs.append(a)   

    def new_id(self) :
        cpt = 0
        while (cpt in self.nodes ): 
                cpt+= 1
        return cpt 
            
                
                

    @classmethod
    def __empty__(cls) :
        return cls([],[],[])     
