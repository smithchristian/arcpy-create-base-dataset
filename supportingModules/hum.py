# ----------------------------------------------------------------------------
# Name:         hum.py (Human.py)
# Purpose:      This module contains variables for the construction
#               of a human dataset. This module is to be used in
#               conjunction with create-Base-DataSet/main.py.
# Description
# and Examples: Pertaining to the human social environment: Cultural
#               Heritage, Native Title, Historical importance, Archaeological,
#               Population,Employment, Census, Demographic, Economic,
#               Education, Recreation, Tourism, Crime, etc
#
# Author:       Christian Fletcher Smith
#
# Created:      10/02/2015
# Copyright:    (c) smithc5 2015
# Version:      2
# ---------------------------------------------------------------------------

# This is the name for the human dataset
HUM_GDB_NAME = "Human.gdb"

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

    # Heritage Areas ---------------------------------------------------------

    HERIT_AREAS= r"D:\Human\Heritage_Areas.shp"

    HERIT_AREAS_FC_NAME = "{}\Heritage_Areas".format(HUM_GDB_NAME)

    HERIT_AREAS_ALIAS =  "Heritage Areas"

    HERIT_AREAS_DIC =  {"source_location": HERIT_AREAS,
                      "output_name": HERIT_AREAS_FC_NAME,
                      "alias": HERIT_AREAS_ALIAS}

'''


# Queensland Heritage Register Boundaries ------------------------------------

QLD_HERIT_REG = r"\testData\Heritage_Register_Boundaries_Queensland\Queensland_heritage_register_boundaries.shp"

QLD_HERIT_REG_FC_NAME = "{}\Heritage_Register_Boundaries_QLD".format(HUM_GDB_NAME)

QLD_HERIT_REG_ALIAS = "Heritage Register Boundaries - QLD"

QLD_HERIT_REG_DIC = {"source_location": QLD_HERIT_REG,
                     "output_name": QLD_HERIT_REG_FC_NAME,
                     "alias": QLD_HERIT_REG_ALIAS}

# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

HUM_DIC_LIST = [val for name, val in globals().items() if name.endswith('_DIC')]