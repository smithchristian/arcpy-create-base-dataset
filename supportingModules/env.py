# ----------------------------------------------------------------------------
# Name:         env.py (Environment.py)
# Purpose:     	This module contains variables for the construction
#               of a environmental dataset. This module is to be used in
#               conjunction with create-Base-DataSet/main.py.
# Description
# and Examples: Ecosystem, Biodiversity, Vegetation, Wetlands, Environmental
#               zone boundaries, Flora, Fauna, Ecology studies, Study
#               boundaries, Marine ecology, Water quality, Air Quality, etc
#
# Author:       Christian Fletcher Smith
#
# Created:     	10/02/2015
# Copyright:   	(c) smithc5 2015
# Version:		2
# ---------------------------------------------------------------------------

# This is the name for the environmental dataset
ENV_GDB_NAME = "Environment.gdb"

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

    # Vegetation Management Act High Value Regrowth Vegetation ---------------

    VMA_HVR = r"D:\VMA_HVR\IQ_QLD_VEG_REGROWTH_100K_CUR.shp"

    VMA_HVR_FC_NAME = "{}\VMA_High_Value_Regrowth_Vegetation".format(ENV_GDB_NAME)

    VMA_HVR_ALIAS =  "VMA High Value Regrowth Vegetation"

    VMA_HVR_DIC =  {"source_location": VMA_HVR,
                    "output_name": VMA_HVR_FC_NAME,
                    "alias":VMA_HVR_ALIAS}

'''

# Essential Habitat Map ------------------------------------------------------

ESSENT_HAB_MAP = r"\testData\Essential_Habitat_Maps\Essential_habitat_map.shp"

ESSENT_HAB_MAP_FC_NAME = "{}\Essential_Habitat_Maps_Queensland".format(ENV_GDB_NAME)

ESSENT_HAB_MAP_ALIAS = "Essential Habitat Maps"

ESSENT_HAB_MAP_DIC = {"source_location": ESSENT_HAB_MAP,
                      "output_name": ESSENT_HAB_MAP_FC_NAME,
                      "alias": ESSENT_HAB_MAP_ALIAS}

# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

ENV_DIC_LIST = [val for name, val in globals().items() if name.endswith('_DIC')]
