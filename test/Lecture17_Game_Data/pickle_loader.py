class NPC :
    def __init__ (self,name, _x, _y):
        self.name, self.x, self.y = name, _x, _y

import pickle

with open('npc.pickle', 'rb') as f:
    npc_list = pickle.load(f)


for npc in npc_list:
    print(npc.name, npc.x, npc.y)