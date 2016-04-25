# ------------------------------------------------------------------------------
# Name:         mar.py (Marine.py)
# Purpose:      This module contains variables for the construction
#               of a marine dataset. This module is to be used in conjunction
#               with create-Base-DataSet/main.py.
# Description
# and Examples:  Ocean-related data, Marine Charts, Tides, Reefs, Currents
#
# Author:       Christian Fletcher Smith
#
# Created:     	10/02/2015
# Copyright:   	(c) smithc5 2015
# Version:		2
# -----------------------------------------------------------------------------

# This is the name for the marine dataset
MAR_GDB_NAME = "Marine.gdb"

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

    # Great Barrier Reef Coast Marine Park -----------------------------------

    GBRMP = r"D:\GBRMP\Great_Barrier_Reef_coast_marine_park_zoning.shp"

    GBRMP_FC_NAME = "{}\GBR_Coast_Marine_Park_Zoning".format(MAR_GDB_NAME)

    GBRMP_ALIAS = "Great Barrier Reef Coast Marine Park Zoning"

    GBRMP_DIC = {"source_location": GBRMP,
            "output_name": GBRMP_FC_NAME,
            "alias": GBRMP_ALIAS}

'''


# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

MAR_DIC_LIST = [val for name, val in globals().items() if name.endswith('_DIC')]
