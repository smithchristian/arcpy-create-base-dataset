# ----------------------------------------------------------------------------
# Name:         create_index.gdb
# Purpose:      This module contains contains variables and functions for the
#               creation of a html catalogue. This catalogue shows what
#               datasets have been included into the .gdb.
#
# Author:       Christian Fletcher Smith
#
# Created:      10/02/2015
# Copyright:    (c) smithc5 2015
# Version:      2
# ---------------------------------------------------------------------------
import os


def sort_data_layers(dic_list, open_object):
    """ Reads from dictionary, sorts the dictionary and then writes to a file

    Keyword arguments:
       dic_list -- list comprehension used to compile all the dictionaries from
       the dataThemes.
       open_object -- file to write to.
    """
    # Opens file to write to
    open_object.write('\t\t<ul>\n')

    # Sorts contents of dictionary
    sorted_dic_list = sorted(dic_list, key=lambda k: k['alias'])

    # Loops through dictionary contents and writes then to a file
    for i in sorted_dic_list:
        open_object.writelines("\t\t\t<li>{}</li>\n".format(i['alias']))

    # Writes to file
    open_object.write('\t\t</ul>\n')


def create_index(source, adm, cad, cli, env, geo, haz, hum, hyd, lnd, mar, pln,
                 ras, top, trn, utl):
    """ Compiles a html file containing all the layers that are used within the
    construction of the databases.

    Keyword arguments:
       source -- The location to where the .gdb is to be created.
       adm -- list comprehension used to compile all the dictionaries from the adm.py.
       cad -- list comprehension used to compile all the dictionaries from the cad.py.
       cli -- list comprehension used to compile all the dictionaries from the cli.py.
       env -- list comprehension used to compile all the dictionaries from the env.py.
       geo -- list comprehension used to compile all the dictionaries from the geo.py.
       haz -- list comprehension used to compile all the dictionaries from the haz.py.
       hum -- list comprehension used to compile all the dictionaries from the hum.py.
       hyd -- list comprehension used to compile all the dictionaries from the hyd.py.
       lnd -- list comprehension used to compile all the dictionaries from the lnd.py.
       mar -- list comprehension used to compile all the dictionaries from the mar.py.
       pln -- list comprehension used to compile all the dictionaries from the pln.py.
       ras -- list comprehension used to compile all the dictionaries from the ras.py.
       top -- list comprehension used to compile all the dictionaries from the top.py.
       trn -- list comprehension used to compile all the dictionaries from the trn.py.
       utl -- list comprehension used to compile all the dictionaries from the url.py.
    """
    # Output location for the index.html to be saved to
    output = os.path.join(source, 'index.html')

    # Compiles html
    with open(output, 'w')as index:
        index.write('<!DOCTYPE HTML>\n')

        index.write('<html lang = "en">\n')

        # Compile header
        index.write('<head>\n')

        index.write('\t<!-- basic.html -->\n')

        index.write('\t<title>CREATE BASE DATASETS</title>\n')

        index.write('\t<meta charset = "UTF-8" />\n')

        index.write('</head>\n')

        # Compile body
        index.write('<body>\n')

        index.write('\t<h1>CREATE BASE DATASETS</h1>\n')

        index.write('\t<p>This tool has been designed to compile geospatial\n' \
                    'datasets for projects. The datasets created have been\n' \
                    'based on the specifications as outlined in the NWA\n' \
                    'Geospatial Project Directory Structure and File\n' \
                    'Management Documentation.</p>\n')

        index.write('\t<p>The following is a summary of the geodatabases and\n' \
                    'their theme associated layers:<p>\n')

        # Compile and write Administrative datasets list
        index.write('\t<h2>Administrative.gdb</h2>\n')

        sort_data_layers(adm, index)

        # Compile and write Cadastre datasets list
        index.write('\t<h2>Cadastre.gdb</h2>\n')

        sort_data_layers(cad, index)

        # Compile and write Climate datasets list
        index.write('\t<h2>Climate.gdb</h2>\n')

        sort_data_layers(cli, index)

        # Compile and write Environment datasets list
        index.write('\t<h2>Environment.gdb</h2>\n')

        sort_data_layers(env, index)

        # Compile and write Geophysical datasets list
        index.write('\t<h2>Geophysical.gdb</h2>\n')

        sort_data_layers(geo, index)

        # Compile and write Hazards datasets list
        index.write('\t<h2>Hazards.gdb</h2>\n')

        sort_data_layers(haz, index)

        # Compile and write Human datasets list
        index.write('\t<h2>Human.gdb</h2>\n')

        sort_data_layers(hum, index)

        # Compile and write Hydrography datasets list
        index.write('\t<h2>Hydrography.gdb</h2>\n')

        sort_data_layers(hyd, index)

        # Compile and write Landuse datasets list
        index.write('\t<h2>Landuse.gdb</h2>\n')

        sort_data_layers(lnd, index)

        # Compile and write Marine datasets list
        index.write('\t<h2>Marine.gdb</h2>\n')

        sort_data_layers(mar, index)

        # Compile and write Planning datasets list
        index.write('\t<h2>Planning.gdb</h2>\n')

        sort_data_layers(pln, index)

        # Compile and write Raster datasets list
        index.write('\t<h2>Raster.gdb</h2>\n')

        sort_data_layers(ras, index)

        # Compile and write Topography datasets list
        index.write('\t<h2>Topography.gdb</h2>\n')

        sort_data_layers(top, index)

        # Compile and write Transport datasets list
        index.write('\t<h2>Transport.gdb</h2>\n')

        sort_data_layers(trn, index)

        # Compile and write Utilities datasets list
        index.write('\t<h2>Utilities.gdb</h2>\n')

        sort_data_layers(utl, index)

        index.write('</body>\n')

        index.write('</html>')
