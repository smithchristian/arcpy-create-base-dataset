# -----------------------------------------------------------------------------
# Name:         hyd.py (Hydrography.py)
# Purpose:      This module contains variables for the construction
#               of a hydrography dataset. This module is to be used in
#               conjunction with create-Base-DataSet/main.py.
# Description
# and Examples: Land-based water resources, Lakes, Rivers & Waterways,
#               Hydrology, Water quality, Flood data, Catchment, boundaries,
#               Flood modelling, etc
#
# Author:       Christian Fletcher Smith
#
# Created:     	10/02/2015
# Copyright:   	(c) smithc5 2015
# Version:		2
# -----------------------------------------------------------------------------

# This is the name for the hydrography dataset
HDY_GDB_NAME = "Hydrography.gdb"

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

    # Drainage Line - All ----------------------------------------------------

    DRAINAGE_LINE_ALL = r"D:\Water\QLD_WATERCOURSE_LINES.shp"

    DRAINAGE_LINE_ALL_FC_NAME = "{}\Drainage_Line_All".format(HDY_GDB_NAME)

    DRAINAGE_LINE_ALL_ALIAS = "Drainage Line - All"

    DRAINAGE_LINE_ALL_DIC = {"source_location": DRAINAGE_LINE_ALL,
                            "output_name": DRAINAGE_LINE_ALL_FC_NAME,
                            "alias": DRAINAGE_LINE_ALL_ALIAS}

'''

# Drainage Line - Major ------------------------------------------------------

DRAINAGE_LINE_MAJOR = r"\testData\Drainage_Line_Major\QLD_MAJOR_WATERCOURSE_LINES.shp"

DRAINAGE_LINE_MAJOR_FC_NAME = "{}\Drainage_Line_Major".format(HDY_GDB_NAME)

DRAINAGE_LINE_MAJOR_ALIAS = "Drainage Line - Major"

DRAINAGE_LINE_MAJOR_DIC = {"source_location": DRAINAGE_LINE_MAJOR,
                           "output_name": DRAINAGE_LINE_MAJOR_FC_NAME,
                           "alias": DRAINAGE_LINE_MAJOR_ALIAS}

# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

HYD_DIC_LIST = [val for name, val in globals().items() if name.endswith('_DIC')]
