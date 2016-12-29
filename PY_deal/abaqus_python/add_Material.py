# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *

def add_Material():
    import material
 
    name = getInput('Enter model name ', mdb.models.keys()[-1])
    if not name in mdb.models.keys():
        raise ValueError,'mdb.models[%s] not found ' %repr(name)

    m = mdb.models[name].Material('Steel')
    m.Density(table=((7800.0, ), ))
    m.Elastic(table=((200000000000.0, 0.3), 
        ))
    m.Plastic(table=((400000000000.0, 
        0.0), (420000000000.0, 0.02), (500000000000.0, 0.2), (600000000000.0, 
        0.5)))

    m = mdb.models[name].Material(name='Aluminum')
    m.Density(table=((2700.0, ), ))
    m.Elastic(table=((70000000000.0, 0.35), 
        ))


add_Material()

