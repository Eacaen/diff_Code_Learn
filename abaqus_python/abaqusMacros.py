# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def add_Material():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Steel')
    mdb.models['Model-1'].materials['Steel'].Density(table=((7800.0, ), ))
    mdb.models['Model-1'].materials['Steel'].Elastic(table=((200000000000.0, 0.3), 
        ))
    mdb.models['Model-1'].materials['Steel'].Plastic(table=((400000000000.0, 
        0.0), (420000000000.0, 0.02), (500000000000.0, 0.2), (600000000000.0, 
        0.5)))
    mdb.models['Model-1'].Material(name='Altium')
    mdb.models['Model-1'].materials['Altium'].Density(table=((2700.0, ), ))
    mdb.models['Model-1'].materials['Altium'].Elastic(table=((70000000000.0, 0.35), 
        ))


