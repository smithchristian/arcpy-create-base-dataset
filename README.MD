# create-base-dataset

This project is designed to create base datasets for projects utilising ArcGIS 10.x , Arcpy and Python. The term "base" in the title, refers to baseline/basic dataset which would contain generic GIS layers (e.g. Roads, Railway line, Watercouses) needed to start a project.

### Description of Project Contents


    create-base-datasets
    |   +-- createbasedatasets.tbx
    |   +-- __init__.py
    |   +-- LICENCE.TXT
    |   +-- main.py
    |   +-- README.MD
    |   +-- _supportingModules
    |   |   +-- __init__.py
    |   |   +-- adm.py
    |   |   +-- cad.py
    |   |   +-- cli.py
    |   |   +-- env.py
    |   |   +-- geo.py
    |   |   +-- haz.py
    |   |   +-- hum.py
    |   |   +-- hyd.py
    |   |   +-- lnd.py
    |   |   +-- mar.py
    |   |   +-- pln.py
    |   |   +-- ras.py
    |   |   +-- top.py
    |   |   +-- utl.py
    |   |   +-- create_index.py
    |   +-- _testData
    |   |   +-- _Baseline_Roads_and_Tracks
    |   |   +-- Default.gdb
    |   |   +-- _Drainage_Line_Major
    |   |   +-- _Erosion_Prone_Area
    |   |   +-- _Essential_Habitat_Maps
    |   |   +-- _Heritage_Register_Boundaries_Queensland
    |   |   +-- _Land_Use
    |   |   +-- _Local_Government_Area
    |   |   +-- _Project_Area
    |   |   +-- _Property_Boundaries_Queensland
    |   |   +-- _Surface_Geology_Queensland

**createbasedatasets.tbx:**

This ArcGIS toolbox acts as the interface for this project. In order to use this tool, you will need to have [ESRI's ArcGIS Desktop](http://www.esri.com/software/arcgis/arcgis-for-desktop) installed. For more information regarding the use of an ArcToolbox, please visit ["Using the ArcToolbox window"](http://resources.arcgis.com/EN/HELP/MAIN/10.2/index.html#//003q0000001m000000).

**main.py:**

This module is the main module for this project. This module pulls in the variables from the dataTheme modules and generates the necessary base datasets.

**supportingModules:**

This folder contains the two different themed modules used to support this project: data Themes and catalogue generation.

**supportingModules - Data Theme:**

The following modules are used to populate the geodatabases. Each theme contains a short description of the GIS layers to be included and documentation on how to populate the modules variables. The current themes include:

+ **adm.py (Administrative.py):**

    This module contains variables for the construction of a administrative dataset.

+ **cad.py (Cadastre.py):**

    This module contains variables for the construction of a cadastre dataset.

+ **cli.py (Climate.py):**

    This module contains variables for the construction of a climate dataset.

+ **env.py (Environment.py):**

    This module contains variables for the construction of a environmental dataset.

+ **geo.py (Geophysical.py):**

    This module contains variables for the construction of a geophysical dataset.

+ **haz.py (Hazards.py):**

    This module contains variables for the construction of a hazard dataset.

+ **hum.py (Human.py):**

    This module contains variables for the construction of a human dataset.

+ **hyd.py (Hydrography.py):**

    This module contains variables for the construction of a hydrography dataset.

+ **lnd.py (Land use.py):**

    This module contains variables for the construction of a landuse dataset.

+ **mar.py (Marine.py):**

    This module contains variables for the construction of a marine dataset.

+ **pln.py (Planning.py):**

    This module contains variables for the construction of a planning dataset.

+ **ras.py (Raster.py):**

    This module contains variables for the construction of a Raster dataset.

+ **top.py (Topography.py):**

    This module contains variables for the construction of a topography dataset.

+ **trn.py (Transport.py):**

    This module contains variables for the construction of a transport network dataset.

+ **utl.py (Utilities.py):**

    This module contains variables for the construction of a utilities dataset.

**supportingModules - catalogue generation:**

This module is used to generate a html catalogue.

+ **create_index.py:**

    This module is used to generate a html report listing the geodatabases created by this project and their contents.

**testData**

    This directory contains shapefiles to be used in testing the application. All the data used for the testing can be found on [Queensland Spatial Catalogue - QSpatial](http://qldspatial.information.qld.gov.au/catalogue/custom/index.page).

### Requirements

In order to run this project the following is required:

+ [ESRI's ArcGIS Desktop](http://www.esri.com/software/arcgis/arcgis-for-desktop), and
+ [Python 2.7x](https://www.python.org/download/releases/2.7/)


### Installation

1. Ensure that you have the required software prior to using this tool - see Requirements section.
2. Download and unzip or create a clone of this repository onto your system.
3. Open ArcGis Desktop 10.x session.
4. Once ArcGis Desktop is open, Open ArcToolbox.
5. Once the ArcToolbox window/tab has open, add the createbasedatasets.tbx from this project.
6. The toolboxes help documentation has been populated with information to assist in the tools use.

### How to use the test data

1. Open ArcGIS Desktop 10.x.
2. Open ArcToolbox.
3. If the Create base datasets toolbox is not present, follow the installation steps, then open the Create base dataset tool.
4. In the Clip Feature field, use the shapefile located here: “\create-base-dataset \testData\Project_Area\Project_Clip_Extent_Test_Only.shp”.
5. In the Output folder path field, you can either specify your own output folder or use this location “\create-base-dataset \testData\Test_Results”.
6. You can check on and off the .gdb that you would like created, but for the first time, I would suggest leaving them all checked on.
7. Click OK.

### Final set up

1. Open main.py, on line 38, change the variable path to the location where you Deault.gdb is currently stored.
2. You will need to populate the various data themes with the source data that you wish to include in your base datasets. Each data theme module will include instructions on how to add new layer variables.

