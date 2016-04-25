# ----------------------------------------------------------------------------
# Name:         utl.py (Utilities.py)
# Purpose:      This module contains variables for the construction
#               of a utilities dataset. This module is to be used in
#               conjunction with create-Base-DataSet/main.py.
# Description
# and Examples: Water, Wastewater, Stormwater, Sewer, Electricity,
#               Gas reticulation, Data & Communication networks,
#
# Author:       Christian Fletcher Smith
#
# Created:     	10/02/2015
# Copyright:   	(c) smithc5 2015
# Version:		2
# ---------------------------------------------------------------------------

# This is the name for the utilities dataset
UTL_GDB_NAME = "Utilities.gdb"

'''
The following information outlines the variable structure for each feature
in order to be used correctly within main.py.

NOTE: The * used in the information below is to indicate a user defined
name.

Feature variable structure:

    # Layer Name ----------------------------------------------------------

    * -- This is the source location of the layer to be clipped.

    *_FC_NAME -- This is the .gdb name and feature class name for the layer to
            be used. The user only needs to populate text after the '{}\', as
            '{}\' is formatted to use the variable ADM_GDB_NAME.

    *_ALIAS -- This is the alias name to be displayed within ArcGIS.

    *_DIC -- The dictionary is used to store all the features variables which
            will be imported into main.py as required.

example:

    # Electrical Network -----------------------------------------------------

    ELEC_NET = r"D:\Utilities\Electrial.shp"

    ELEC_NET_FC_NAME = "{}\Electrical_Network".format(UTL_GDB_NAME)

    ELEC_NET_ALIAS = "Electrical Network"

    ELEC_NET_DIC = {"source_location": ELEC_NET,
            "Output_name": ELEC_NET_FC_NAME,
            "alias": ELEC_NET_ALIAS}

'''

# TODO: need to add in layer variables

# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

UTL_DIC_LIST = [val for name, val in globals().items() if name.endswith('_DIC')]
