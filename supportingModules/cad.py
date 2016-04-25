# ----------------------------------------------------------------------------
# Name:         cad.py (Cadastre.py)
# Purpose:     	This module contains contains variables for the construction
#               of a cadastre dataset. This module is to be used in conjunction
#               with create-Base-DataSet/main.py
# Description
# and Examples: DCDB data: monthly updates
#               Geodetic: Survey control, etc
#
# Author:       Christian Fletcher Smith
#
# Created:     	10/02/2015
# Copyright:   	(c) smithc5 2015
# Version:		2
# ----------------------------------------------------------------------------

# This is the name for the cadastre dataset
CAD_GDB_NAME = "Cadastre.gdb"

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

    # Property Boundaries ----------------------------------------------------

    PROPERTY_BRDY = r"D:\Property_Boundaries_Queensland\QLD_CADASTRE_DCDB.shp"

    PROPERTY_BRDY_FC_NAME = "{}\Property_Boundaries_QLD".format(CAD_GDB_NAME)

    PROPERTY_BRDY_ALIAS = "Property Boundaries"

    PROPERTY_BRDY_DIC = {"source_location": PROPERTY_BRDY,
                       "Output_name": PROPERTY_BRDY_FC_NAME,
                       "alias": PROPERTY_BRDY_ALIAS}

'''

# Property Boundaries Queensland ---------------------------------------------

DCDB = r"\testData\Property_Boundaries_Queensland\QLD_CADASTRE_DCDB.shp"

DCDB_FC_NAME = "{}\Property_Boundaries_QLD".format(CAD_GDB_NAME)

DCDB_ALIAS = "Property Boundaries Queensland"

DCDB_DIC = {"source_location": DCDB,
            "output_name": DCDB_FC_NAME,
            "alias": DCDB_ALIAS}


# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

CAD_DIC_LIST = [val for name, val in globals().items() if name.endswith('_DIC')]
