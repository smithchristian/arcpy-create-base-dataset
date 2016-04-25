# ----------------------------------------------------------------------------
# Name:           main.py
# Purpose:        This script creates a base datasets for projects by
#                 clipping features to a specified extent
#
# Author:         smithc5
#
# Created:        10/02/2015
# Copyright:      (c) smithc5 2015
# Version:        2
# ArcGIS Licenses: ArcGIS for Desktop Basic
# ----------------------------------------------------------------------------

import os
import sys
import traceback

import arcpy

from supportingModules import adm
from supportingModules import cad
from supportingModules import cli
from supportingModules import env
from supportingModules import geo
from supportingModules import haz
from supportingModules import hum
from supportingModules import hyd
from supportingModules import lnd
from supportingModules import mar
from supportingModules import pln
from supportingModules import ras
from supportingModules import top
from supportingModules import trn
from supportingModules import utl
from supportingModules import create_index

# Creates workspace
arcpy.env.workspace = r"\testData\Default.gdb"

# Sets the overwrite ability to false
arcpy.env.overwriteOutput = False

# Used to store the user input to the location of the clipping shapefile.
CLIP_FEATURE_CLASS = arcpy.GetParameterAsText(0)

# The location to where the .gdb is to be created
GDB_DATABASE_OUTPUT_PATH = arcpy.GetParameterAsText(1)

# Boolean used to determine if existing .gdb needs deleting.
DEL_EXT_GDB = arcpy.GetParameterAsText(2)


'''
FORMAT: *_SELECTION = arcpy.GetParameterAsText(*)
e.g ADM_SELECTION = arcpy.GetParameterAsText(2)

The following variables are used to store a boolean indicating if a user
wants a particular .gdb created or not.
'''

ADM_SELECTION = arcpy.GetParameterAsText(3)

CAD_SELECTION = arcpy.GetParameterAsText(4)

CLI_SELECTION = arcpy.GetParameterAsText(5)

ENV_SELECTION = arcpy.GetParameterAsText(6)

GEO_SELECTION = arcpy.GetParameterAsText(7)

HAZ_SELECTION = arcpy.GetParameterAsText(8)

HUM_SELECTION = arcpy.GetParameterAsText(9)

HYD_SELECTION = arcpy.GetParameterAsText(10)

LND_SELECTION = arcpy.GetParameterAsText(11)

MAR_SELECTION = arcpy.GetParameterAsText(12)

PLN_SELECTION = arcpy.GetParameterAsText(13)

RAS_SELECTION = arcpy.GetParameterAsText(14)

TOP_SELECTION = arcpy.GetParameterAsText(15)

TRN_SELECTION = arcpy.GetParameterAsText(16)

UTL_SELECTION = arcpy.GetParameterAsText(17)

'''
The following information outlines the variable structure
for the below variables.

FORMAT: *_FINAL_LIST = [*_SELECTION, *.*_GDB_NAME, *.*_DIC_LIST]

e.g ADM_FINAL_LIST = [ADM_SELECTION,adm.ADM_GDB_NAME,adm.ADM_DIC_LIST]

Keyword arguments:
    *_SELECTION --  The users selection (boolean) for creating a .gdb.
    *.*_GDB_NAME -- The name of the .gdb to be created.
    *.*_DIC_LIST -- The dictionary list containing the data's location,
                    name and alias.
'''

ADM_FINAL_LIST = [ADM_SELECTION, adm.ADM_GDB_NAME, adm.ADM_DIC_LIST]

CAD_FINAL_LIST = [CAD_SELECTION, cad.CAD_GDB_NAME, cad.CAD_DIC_LIST]

CLI_FINAL_LIST = [CLI_SELECTION, cli.CLI_GDB_NAME, cli.CLI_DIC_LIST]

ENV_FINAL_LIST = [ENV_SELECTION, env.ENV_GDB_NAME, env.ENV_DIC_LIST]

GEO_FINAL_LIST = [GEO_SELECTION, geo.GEO_GDB_NAME, geo.GEO_DIC_LIST]

HAZ_FINAL_LIST = [HAZ_SELECTION, haz.HAZ_GDB_NAME, haz.HAZ_DIC_LIST]

HUM_FINAL_LIST = [HUM_SELECTION, hum.HUM_GDB_NAME, hum.HUM_DIC_LIST]

HYD_FINAL_LIST = [HYD_SELECTION, hyd.HDY_GDB_NAME, hyd.HYD_DIC_LIST]

LND_FINAL_LIST = [LND_SELECTION, lnd.LND_GBD_NAME, lnd.LND_DIC_LIST]

MAR_FINAL_LIST = [MAR_SELECTION, mar.MAR_GDB_NAME, mar.MAR_DIC_LIST]

PLN_FINAL_LIST = [PLN_SELECTION, pln.PLN_GDB_NAME, pln.PLN_DIC_LIST]

RAS_FINAL_LIST = [RAS_SELECTION, ras.RAS_GDB_NAME, ras.RAS_DIC_LIST]

TOP_FINAL_LIST = [TOP_SELECTION, top.TOP_GDB_NAME, top.TOP_DIC_LIST]

TRN_FINAL_LIST = [TRN_SELECTION, trn.TRN_GDB_NAME, trn.TRN_DIC_LIST]

UTL_FINAL_LIST = [UTL_SELECTION, utl.UTL_GDB_NAME, utl.UTL_DIC_LIST]


''''
FINAL_LIST =[]

Is a list comprehension used to compile a list of all the *_FINAL_LISTs.
This list will be passed to the main function for the creations and
population of the gdb.
'''

FINAL_LIST = [val for name, val in globals().items()
              if name.endswith('_FINAL_LIST')]

# Functions


def check_if_gdb_exist(database_filepath):
    """ Checks to see the if .gdb exist. If true, the .gdb is deleted.
    The idea of this function is remove old .gdb and replace it with
    updated ones.

    Keyword arguments:
       database_filepath -- Full file path to the .gdb
    """
    # Prints message to screen.
    arcpy.AddMessage("....Checking to see if .gdb exist")

    # Check to see if the file path exist. If true, the file is deleted.
    if arcpy.Exists(database_filepath):

        # Deletes file
        arcpy.Delete_management(database_filepath)

        # Prints message to screen
        arcpy.AddMessage(".......Existing .gdb - Deleted")


def delete_gdb_selection(del_ext_gdb, gdb_db_output_path, gdb_name):
    """ Deletes existing .gdb if "Delete .gdb" select box is checked

    Keyword arguments:
        del_ext_gdb -- Boolean indicating deletion of .gdb required
        gdb_db_output_path -- Directory path to .gdb
        gdb_name -- Name of the .gdb
    """

    if str(del_ext_gdb) == "true":

        # Full file name for the .gdb to be created
        database_filepath = os.path.join(gdb_db_output_path, gdb_name)

        # Checks to see if .gdb already exist.
        check_if_gdb_exist(database_filepath)

    else:

        pass


def create_gdb(data_base_location, data_base_name):
    """ Creates the .gdb to store the feature classes

    Keyword arguments:
        data_base_location -- Location of .gdb to store feature classes
        data_base_name -- Name of the .gdb
    """

    # Prints message to screen
    arcpy.AddMessage("....Starting Creating New Database")

    # Creates the .gdb
    arcpy.CreateFileGDB_management(data_base_location, data_base_name)

    # Prints message to screen
    arcpy.AddMessage(".......Finished Creating Database")


def create_feature(dictionary_list, clip_extent, gdb_output):
    """ Clips the feature and assigns the alias

    Keyword arguments:
       dictionary_list -- List containing dictionary of features to clip.
       clip_extent -- Feature used to clip other features.
       gdb_output -- The file path where the .gdb will be stored\saved.
    """

    for dic in dictionary_list:

        # File path to the source file to be clipped.
        source_location = dic["source_location"]

        # File path location to save the clipped features.
        output_name = os.path.join(gdb_output, dic["output_name"])

        # Alias name to be assigned to the newly clipped feature.
        alias = dic["alias"]

        # Prints message to screen.
        arcpy.AddMessage("....Starting Creating {} Feature".format(alias))

        # Function used to clip features.
        arcpy.Clip_analysis(source_location, clip_extent, output_name)

        # Function used to assign alias.
        arcpy.AlterAliasName(output_name, alias)

        # Prints message to screen.
        arcpy.AddMessage("........Finished Creating {} Feature".format(alias))


def main():
    """ Main function for creating gdb
    """

    try:
        # Prints message to screen
        arcpy.AddMessage("....Creating HTML index")
        create_index.create_index(GDB_DATABASE_OUTPUT_PATH, adm.ADM_DIC_LIST,
                                  cad.CAD_DIC_LIST, cli.CLI_DIC_LIST,
                                  env.ENV_DIC_LIST, geo.GEO_DIC_LIST,
                                  haz.HAZ_DIC_LIST, hum.HUM_DIC_LIST,
                                  hyd.HYD_DIC_LIST, lnd.LND_DIC_LIST,
                                  mar.MAR_DIC_LIST, pln.PLN_DIC_LIST,
                                  ras.RAS_DIC_LIST, top.TOP_DIC_LIST,
                                  trn.TRN_DIC_LIST, utl.UTL_DIC_LIST)
        # Prints message to screen.
        arcpy.AddMessage("........Finished Creating HTML index")

        for item in FINAL_LIST:

            # Separates items into designated variables.
            selection, gdb_name, theme_dic_list = item

            # Check to see if user wants .gdb created.
            if str(selection) == "true":

                # If delete existing .gdb box is checked, delete existing .gdb
                delete_gdb_selection(DEL_EXT_GDB, GDB_DATABASE_OUTPUT_PATH,
                                     gdb_name)

                # Function for creating .gdb
                create_gdb(GDB_DATABASE_OUTPUT_PATH, gdb_name)

                # Function for populating .gdb with feature classes.
                create_feature(theme_dic_list, CLIP_FEATURE_CLASS,
                               GDB_DATABASE_OUTPUT_PATH)

            else:

                # If selection = false, continue loop
                continue

    except:

        tb = sys.exc_info()[2]

        tbinfo = traceback.format_tb(tb)[0]

        pymsg = "{}\n{}\n {}\n{}\n\t{}: {}\n".format("PYTHON ERRORS:",
                                                     "Traceback Info:",
                                                     tbinfo, "Error Info:",
                                                     str(sys.exc_type),
                                                     str(sys.exc_value))

        msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"

        arcpy.AddError(msgs)

        arcpy.AddError(pymsg)

        print msgs

        print pymsg

        arcpy.AddMessage(arcpy.GetMessages(1))

        print arcpy.GetMessages(1)


if __name__ == '__main__':
    main()
