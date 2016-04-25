# ----------------------------------------------------------------------------
# Name:         trn.py (Transport.py)
# Purpose:      This module contains variables for the construction
#               of a transport network dataset. This module is to be used in
#               conjunction with create-Base-DataSet/main.py.
# Description
# and Examples: Roads, Ferry & Shipping routes, Rail, Tunnels, Air routes,
#               Aeronautical charts and data, etc
#
# Author:       Christian Fletcher Smith
#
# Created:     	10/02/2015
# Copyright:   	(c) smithc5 2015
# Version:		2
# ----------------------------------------------------------------------------

# This is the default name for the transport dataset
TRN_GDB_NAME = "Transport.gdb"

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

    # Road Network -----------------------------------

    RDNETWORK = r"D:\Transport\Roads.shp"

    RDNETWORK_FC_NAME = "{}\Road_Network".format(TRN_GDB_NAME)

    RDNETWORK_ALIAS = "Road Network"

    RDNETWORK_DIC = {"source_location": RDNETWORK,
            "output_name": RDNETWORK_FC_NAME,
            "alias": RDNETWORK_ALIAS}

'''

# Base Line Roads and Tracks -------------------------------------------------

BASELINE_RD_TRK = r"\testData\Baseline_Roads_and_Tracks\Baseline_roads_and_tracks.shp"

BASELINE_RD_TRK_FC_NAME = "{}\Baseline_Roads_and_Tracks".format(TRN_GDB_NAME)

BASELINE_RD_TRK_ALIAS = "Baseline Roads and Tracks"

BASELINE_RD_TRK_DIC = {"source_location": BASELINE_RD_TRK,
                       "output_name": BASELINE_RD_TRK_FC_NAME,
                       "alias": BASELINE_RD_TRK_ALIAS}


# ----------------------------------------------------------------------------
# DO NOT ADD LAYER VARIABLES BELOW THIS LINE!
#
# The following list comprehension is designed to compile all the dictionaries
# from the above layers into a single list. This list is imported into main.py
# when required.
# ----------------------------------------------------------------------------

TRN_DIC_LIST = [val for name, val in globals().items() if name.endswith('_DIC')]
