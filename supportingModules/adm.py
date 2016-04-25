# ----------------------------------------------------------------------------
# Name:         adm.py (Administrative.py)
# Purpose:      This module contains variables for the construction
# 				of a administrative dataset. This module is to be used in
# 				conjunction with create-Base-DataSet/main.py
# Description
# and Examples: Government boundaries:  LGA, Postcodes, Localities, Electoral,
#               Political, Maritime, Mining boundaries: Leases, Exploration,
#               Permits, etc
#
#
# Author:      	Christian Fletcher Smith
#
# Created:     	10/02/2015
# Copyright:   	(c) smithc5 2015
# Version:		2
# ----------------------------------------------------------------------------

# This is the name for the administrative dataset.
ADM_GDB_NAME = "Administrative.gdb"

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

    # Localities -------------------------------------------------------------

    LOCALITIES = r"D:\Location\Localities_Queensland.shp"

    LOCALITIES_FC_NAME = "{}\Localities_Queensland".format(ADM_GDB_NAME)

    LOCALITIES_ALIAS = "Localities Queensland"

    LOCALITIES_DIC = {"source_location": LOCALITIES,
                       "output_name": LOCALITIES_FC_NAME,
                       "alias": LOCALITIES_ALIAS}

'''

# Local Government Area ------------------------------------------------------

LGA = r"\testData\Local_Government_Area\Local_Government_Areas.shp"

LGA_FC_NAME = "{}\Local_Government_Area".format(ADM_GDB_NAME)

LGA_ALIAS = "Local Government Area"

LGA_DIC = {"source_location": LGA,
           "output_name": LGA_FC_NAME,
           "alias": LGA_ALIAS}


# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

ADM_DIC_LIST = [val for name, val in globals().items() if name.endswith('_DIC')]



