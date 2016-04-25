# ----------------------------------------------------------------------------
# Name:         lan.py (land use.py)
# Purpose:      This module contains variables for the construction
#               of a land use dataset. This module is to be used in conjunction
#               with create-Base-DataSet/main.py.
# Description
# and Examples: Agricultural land, Land cover, Land use, Visual or Scenic
#               amenity, Strategic Cropping Land, GQAL, Land use studies, etc
#
# Author:       Christian Fletcher Smith
#
# Created:     	10/02/2015
# Copyright:   	(c) smithc5 2015
# Version:		2
# ----------------------------------------------------------------------------

# This is the name for the land use dataset
LND_GBD_NAME = "Landuse.gdb"

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

    # Land use ----------------------------------------------------

    LANDUSE = r"D:\LandUse\Landuse.shp"

    LANDUSE_FC_NAM = "{}\Landuse".format(LND_GBD_NAME)

    LANDUSE_ALIAS = "Land Use"

    LANDUSE_DIC = {"source_location": LANDUSE,
               "output_name": LANDUSE_FC_NAME,
               "alias": LANDUSE_ALIAS}

'''

# Land use --------------------------------------------------------------------

LANDUSE = r"\testData\Land_Use\Regional_land_use_categories_South_East_Queensland.shp"

LANDUSE_FC_NAME = "{}\Regional_land_use_categories_South_East_Queensland".format(LND_GBD_NAME)

LANDUSE_ALIAS = "Regional land use categories South East Queensland"

LANDUSE_DIC = {"source_location": LANDUSE,
               "output_name": LANDUSE_FC_NAME,
               "alias": LANDUSE_ALIAS}

# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

LND_DIC_LIST = [val for name, val in globals().items() if name.endswith('_DIC')]