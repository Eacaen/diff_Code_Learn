from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class CreatePlateDB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Create Plate',
            self.OK|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            
        GroupBox_2 = FXGroupBox(p=self, text='Title', opts=FRAME_GROOVE)
        fileName = os.path.join(thisDir, 'createPlate.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=GroupBox_2, text='', ic=icon)
        GroupBox_1 = FXGroupBox(p=self, text='Parameters', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='partName:', tgt=form.partNameKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='width:', tgt=form.keyword02Kw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='height:', tgt=form.heightKw, sel=0)
        AFXTextField(p=GroupBox_1, ncols=12, labelText='radius:', tgt=form.radiusKw, sel=0)
