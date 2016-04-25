# ----------------------------------------------------------------------------
# Name:         cad.py (Climate.py)
# Purpose:     	This module contains variables for the construction
#               of a climate dataset. This module is to be used in
#               conjunction with create-Base-DataSet/main.py.
# Description
# and Examples: Climate data, Rainfall data, Atmospheric information, etc
#
# Author:       Christian Fletcher Smith
#
# Created:     	10/02/2015
# Copyright:   	(c) smithc5 2015
# Version:		2
# ----------------------------------------------------------------------------

# This is the name for the climate dataset
CLI_GDB_NAME = "Climate.gdb"

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

    # Rainfall Gauge Station -------------------------------------------------

    RAINFALL_STN = r"D:\Climate\Rainfall_Stn.shp"

    RAINFALL_STN_FC_NAME = "{}\Rainfall_Gauge_Station".format(CLI_GDB_NAME)

    RAINFALL_STN_ALIAS = "Rainfall Gauge Station"

    RAINFALL_STN_DIC =  {"source_location": RAINFALL_STN,
                    "output_name": RAINFALL_STN_FC_NAME,
                    "alias":RAINFALL_STN_ALIAS}

'''

# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

CLI_DIC_LIST = [val for name, val in globals().items() if name.endswith('_DIC')]
