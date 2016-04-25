# ----------------------------------------------------------------------------
# Name:         geo.py (Geophysical.py)
# Purpose:      This module contains variables for the construction
#               of a geophsyical dataset. This module is to be used in
#               conjunction with create-Base-DataSet/main.py.
# Description
# and Examples: Geological data, Soils data, Groundwater data, Borehole
#               information, Minerals, Oil & Gas data, Fossil fuels, Natural
#               resources, Tectonic activity, Gravity data, Erosion, Land
#               stability, Acid Sulphate soils, Salinity, etc
#
# Author:       Christian Fletcher Smith
#
# Created:     	10/02/2015
# Copyright:   	(c) smithc5 2015
# Version:		2
# ----------------------------------------------------------------------------

# This is the name for the geophysical dataset
GEO_GDB_NAME = "Geophysical.gdb"

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

    # Detailed Solid Geology - Queensland ------------------------------------

    GEO_SOLID = r"D:\Geology\Solid_Geology.shp

    GEO_SOLID_FC_NAME = "{}\Detailed_Solid_Geology_QLD".format(GEO_GDB_NAME)

    GEO_SOLID_ALIAS = "Detailed Solid Geology - QLD"

    GEO_SOLID_DIC = {"source_location": GEO_SOLID,
                     "output_name": GEO_SOLID_FC_NAME,
                     "alias": GEO_SOLID_ALIAS}

'''
# Detailed Surface Geology - Queensland ----------------------------------------

GEO_SURFACE = r"\testData\Surface_Geology_Queensland\QLD_GEOLOGY_2012_EDN_ROCK_UN.shp"

GEO_SURFACE_FC_NAME = "{}\Surface_Geology_QLD".format(GEO_GDB_NAME)

GEO_SURFACE_ALIAS = "Surface Geology - Queensland"

GEO_SURFACE_DIC = {"source_location": GEO_SURFACE,
                 "output_name": GEO_SURFACE_FC_NAME,
                 "alias": GEO_SURFACE_ALIAS}


# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

GEO_DIC_LIST =[val for name, val in globals().items() if name.endswith('_DIC')]


