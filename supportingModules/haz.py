# ----------------------------------------------------------------------------
# Name:         haz.py (Hazards.py)
# Purpose:      This module contains variables for the construction
#               of a hazard dataset. This module is to be used in
#               conjunction with create-Base-DataSet/main.py.
# Description
# and Examples: Hazards to human and environmental health: Hazardous materials
#               Pollutants, NPI data, Contaminated land, Disease data, Pests,
#               Noise-related data, Waste storage, etc
#
# Author:       Christian Fletcher Smith
#
# Created:      10/02/2015
# Copyright:    (c) smithc5 2015
# Version:      2
# ----------------------------------------------------------------------------

# This is the name for the hazard dataset
HAZ_GDB_NAME = "Hazards.gdb"

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

    # Erosion Areas ----------------------------------------------------------

    ERO_AREAS= r"D:\Hazards\Erosion_Areas.shp"

    ERO_AREAS_FC_NAME = "{}\Erosion_Areas".format(HAZ_GDB_NAME)

    ERO_AREAS_ALIAS =  "Erosion Areas"

    ERO_AREAS_DIC =  {"source_location": ERO_AREAS,
                      "output_name": ERO_AREAS_FC_NAME,
                      "alias": ERO_AREAS_ALIAS}

'''

# Erosion Prone Area All Components -----------------------------------------

EROS_PRONE_AREAS = r"\testData\Essential_Habitat_Maps\Essential_habitat_map.shp"

EROS_PRONE_AREAS_FC_NAME = "{}\Erosion_Prone_Area".format(HAZ_GDB_NAME)

EROS_PRONE_AREAS_ALIAS = "Erosion Prone Area"

EROS_PRONE_AREAS_DIC = {"source_location": EROS_PRONE_AREAS,
                        "output_name": EROS_PRONE_AREAS_FC_NAME,
                        "alias": EROS_PRONE_AREAS_ALIAS}

# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

HAZ_DIC_LIST = [val for name, val in globals().items() if name.endswith('_DIC')]