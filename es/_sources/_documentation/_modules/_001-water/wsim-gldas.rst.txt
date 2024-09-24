.. Author: Akshay Mestry <xa@mes3.dev>
.. Created on: Friday, September 13 2024
.. Last updated on: Tuesday, September 24 2024

===============================================================================
WSIM-GLDAS
===============================================================================

.. title-hero::
    :icon: fa-solid fa-water
    :summary:
        Acquisition, Exploration and Integration with Water Security Indicator
        Model - Global Land Data Assimilation System (WSIM-GLDAS).

.. tags:: modules, water-module, open-science-101, research

.. contributors::
    :prefix: Authored by
    :timestamp: June 03, 2024

    - Josh Brinks
    - test@test.com
    - https://github.com/

    - Elaine Famutimi
    - test@test.com
    - https://github.com/

In this comprehensive lesson, you will embark on an immersive journey that
combines advanced data acquisition, pre-processing, and exploration of vital
water security data. Specifically, you will retrieve the **Water Security
Indicator Model - Global Land Data Assimilation System (WSIM-GLDAS)** dataset,
available from NASA's **Socioeconomic Data and Applications Center (SEDAC)**.
This dataset provides crucial insights into water anomalies, such as droughts
and floods, and will serve as the foundation for your analysis.

.. figure:: https://svs.gsfc.nasa.gov/vis/a010000/a012900/a012950/
    SierraNevada_tmo_2014018_lrg_16x9_1024x576.jpg
    :alt: A true color satellite image of California shows drought.
    :class: height-450 object-fit-center

    This true color satellite image of California illustrates regions
    experiencing water stress such as droughts. Visual representations like
    this are essential for understanding the spatial distribution of water
    security risks and guiding decision-making processes to manage limited
    freshwater resources. [#nasa_svs_1]_

As you progress through this lesson, you will be guided step by step through
several pre-processing tasks designed to help you make sense of this complex
data. You will learn not only how to handle and subset the WSIM-GLDAS dataset
but also how to enhance its value by integrating it with other globally
recognized datasets. In particular, you will incorporate the **geoBoundaries**
dataset, which offers global administrative boundary data, and the **Gridded
Population of the World** dataset, a vital resource for understanding how
human populations are affected by water anomalies.

Through the lesson, you'll engage in a series of data manipulations and
visualizations, gaining practical skills in handling large-scale geospatial
data. These advanced visualizations will empower you to reveal patterns in
precipitation deficits and surpluses, providing a clearer understanding of how
water-related events impact specific regions. Ultimately, by the end of the
lesson, you'll have a complete workflow in place to retrieve, process, and
visualize complex data, arming you with the tools to explore critical water
security issues affecting communities around the globe.

.. carousel::
    :show_controls:
    :show_fade:

    .. image:: ../../_assets/modules/water/data-flow/viz-1.webp
    .. image:: ../../_assets/modules/water/data-flow/viz-2.webp
    .. image:: ../../_assets/modules/water/data-flow/viz-3.webp
    .. image:: ../../_assets/modules/water/data-flow/viz-4.webp
    .. image:: ../../_assets/modules/water/data-flow/viz-5.webp

.. dropdown:: Learning Objectives

    By the end of this lesson, you will have developed a solid understanding
    of the technical and analytical skills needed to work with complex
    datasets in the field of water security. You will have gained the ability
    to:

    - **Retrieve WSIM-GLDAS Data.** Confidently access the WSIM-GLDAS dataset
      from the NASA SEDAC website, ensuring you can efficiently acquire the
      necessary data for analysis.
    - **Access Administrative Boundaries.** Use the geoBoundaries API to
      retrieve up-to-date global administrative boundary data, allowing you to
      contextualize the WSIM-GLDAS dataset within specific regional borders.
    - **Subset WSIM-GLDAS Data.** Learn how to filter and subset the WSIM-GLDAS
      data for specific regions and time periods, enabling you to focus on
      areas of particular interest in your analysis.
    - **Visualize Geospatial Data.** Create insightful geospatial
      visualizations that highlight patterns of precipitation deficits,
      helping you to communicate complex findings with clarity and precision.
    - **Save Pre-Processed Data.** Export your pre-processed NetCDF-formatted
      files to disk, giving you the ability to save and share your refined
      datasets for future use or collaboration.
    - **Explore Data Visually.** Master advanced data visualization techniques,
      including the creation of histograms, choropleths, and time series maps,
      to explore patterns and trends within the dataset.
    - **Integrate Population Data.** Combine the WSIM-GLDAS data with Gridded
      Population of the World data to analyze how water anomalies intersect
      with population distribution, providing valuable insights into the human
      impacts of water security issues.
    - **Summarize Data with Zonal Statistics.** Utilize zonal statistics to
      summarize the WSIM-GLDAS and population raster data, providing an
      analytical overview of how water shortages or surpluses affect specific
      regions and communities.
    
    Through these objectives, you will not only gain proficiency in handling
    complex geospatial data but also develop a deeper understanding of how
    these datasets can be leveraged to solve real-world challenges,
    particularly in the realm of water security and population impacts.

-------------------------------------------------------------------------------
Introduction
-------------------------------------------------------------------------------

The **Water cycle**, also known as the **Hydrologic cycle**, refers to the
continuous movement and circulation of water across, above, and below the
Earth's surface. It is a fundamental process that sustains life, ensuring that
water is recycled and made available through precipitation, evaporation, and
condensation (NOAA, 2019 [#]_). However, human activities in recent decades
|html-dash| such as the emission of greenhouse gases, land-use alterations,
the construction of dams and reservoirs, and the extraction of groundwater
|html-dash| have increasingly disrupted the natural flow of this cycle
(IPCC, 2023 [#]_). These anthropogenic influences have had significant and
far-reaching consequences on various processes tied to oceans, groundwater
systems, and land surfaces. As a result, extreme events like droughts and
floods are becoming more frequent and intense (Zhou, 2016 [#]_).

.. carousel::
    :show_captions_below:
    :show_controls:
    :show_fade:
    :show_indicators:

    .. figure:: ../../_assets/modules/water/greenhouse-effect.webp
        :alt: Impact of Human Activities on the Water Cycle

        Impact of Human Activities on the Water Cycle. Human activities such as
        greenhouse gas emissions, deforestation, and dam construction are
        altering the natural flow of the water cycle, leading to environmental
        imbalances. [#freepik_1]_

    .. figure:: ../../_assets/modules/water/pollution-factory-emisions.webp
        :alt: Impact of Human Activities on the Water Cycle

        Impact of Human Activities on the Water Cycle. Human activities such
        as greenhouse gas emissions, deforestation, and dam construction are
        altering the natural flow of the water cycle, leading to environmental
        imbalances. [#freepik_2]_

Drought, which occurs when precipitation deficits persist over time, is
characterized by prolonged dry periods that lead to severe water shortages.
The cascading effects of drought are felt across ecosystems, agriculture, and
human communities, often creating feedback loops that exacerbate environmental
stresses (Rodgers, 2023 [#]_). For instance, California is notorious for
recurrent droughts, but prolonged dry spells, coupled with sustained high
temperatures, severely reduced the replenishment of fresh water to key water
bodies like the **Klamath River**. From 2003 to 2014, the state experienced
extreme water shortages that had devastating effects. These shortages
significantly impacted California's Central Valley, a vital agricultural
region responsible for producing 80% of the world's almonds. The droughts also
caused ecological distress by triggering declines in `Chinook salmon
<https://www.fisheries.noaa.gov/species/chinook-salmon>`_ populations, as the
lack of fresh water led to heat stress and disease outbreaks among the fish,
affecting the Klamath basin tribal groups, who rely heavily on these salmon
for sustenance (Guillen, 2002 [#]_; Bland, 2014 [#]_).

.. figure:: https://ca-times.brightspotcdn.com/dims4/default/15e8000/
    2147483647/strip/true/crop/4032x3024+0+0/resize/840x630!/quality/90/?
    url=https://california-times-brightspot.s3.amazonaws.com/1e/a1/
    eb76da6f4c5a9ad847549d2b3fa9/tsfxbams.jpeg
    :alt: Indigenous Communities and Water Resources.
    :class: height-450 object-fit-center

    Indigenous Communities and Water Resources. The Klamath basin tribal groups
    depend on the Chinook salmon for their livelihood, but water shortages and
    environmental stress have led to a significant decline in salmon
    populations. [#klamath_death]_

To better understand and quantify such changes in water availability and their
implications, datasets like the **Water Security (WSIM-GLDAS) Monthly Grids,
v1 (1948 - 2014)** are invaluable. This particular dataset offers detailed
insights into freshwater surpluses and deficits across the globe, tracking
them monthly over a 66-year period from January 1948 to December 2014
(ISciences & CIESIN-Columbia University, 2022b [#isciences]_).

The WSIM-GLDAS dataset organizes its data by **thematic variables** such as
temperature, runoff, soil moisture, precipitation, and evapotranspiration, as
well as temporal aggregation periods (e.g., 1-month, 3-month, 6-month, and
12-month intervals). This structure allows for comprehensive exploration of
water-related anomalies across various timescales. The data files, stored in
**NetCDF (.nc)** format, contain time-dimensioned :term:`raster` layers, each
representing one of the **804 months** in the dataset. Some variables even
contain multiple attributes with their own time series. It is important to
note that because the dataset is vast and consists of multiple layers,
downloading and handling the files can be resource-intensive, possibly leading
to memory issues on some computers.

This dataset represents what is known as **"Big Data"**, requiring advanced
tools and techniques to analyze and draw meaningful conclusions from. By
working with this dataset, students and researchers will gain practical
experience dealing with complex, large-scale data, while also exploring
critical water security issues at a global level.

-------------------------------------------------------------------------------
About the Data
-------------------------------------------------------------------------------

For this lesson, we will work with the **WSIM-GLDAS dataset** focusing on the
**Composite Anomaly Twelve-Month Return Period NetCDF file**. This file
includes **water deficit**, **surplus**, and **composite anomaly** variables,
each with a 12-month integration period. The integration period refers to the
timeframe over which anomaly values are averaged. In this case, the 12-month
integration averages water-related anomalies like droughts and floods over a
year, providing a high-level overview of water deficits, surpluses, and
combined anomalies. This helps in understanding yearly trends, and once we've
identified key time periods of interest, we can refine our analysis using the
**3-months** or **1-month** integration periods.

We'll start by downloading the file directly from the SEDAC website. The
`dataset documentation <https://sedac.ciesin.columbia.edu/downloads/docs/water/
water-wsim-gldas-v1-documentation.pdf>`_ highlights the composite variables as
essential elements of WSIM-GLDAS, which integrate the return periods of
multiple water-related parameters into composite indices of overall water
surpluses and deficits (ISciences & CIESIN-Columbia University, 2022a
[#isciences]_). These composite anomaly files provide data in terms of return
periods, indicating how often anomalies such as droughts or floods occur. For
example, a deficit return period of 25 suggests a drought so severe that it
would only occur once every 25 years.

.. dropdown:: Downloading the Dataset

    - Visit the `SEDAC <https://sedac.ciesin.columbia.edu/>`_ website.
    - You can navigate through themes, datasets, or collections on the
      platform. For this exercise, use the search bar to look up "**wsim**."
    - Locate and select the Water Security (WSIM-GLDAS) Monthly Grids, v1
      (1948-2014) dataset.
    - When you're ready, go to the **Data Download** tab. You'll need to sign
      in using your NASA EarthData account.
      :doc:`Learn more <../../_tutorials/_001-basics/accounts>` |chevron-right|
    - Once logged in, find the Composite Class and select the **Variable
      Composite Anomaly Twelve-Month Return Period** for download.

-------------------------------------------------------------------------------
Loading the Dataset
-------------------------------------------------------------------------------

.. tab-set::
    :sync-group: programming-language

    .. tab-item:: R-Programming |badge-beta|
        :sync: r-programming

        ...

    .. tab-item:: Python
        :sync: python

        After downloading the **WSIM-GLDAS** file to your local machine, the
        next step is to prepare your **Python environment** by installing and
        loading the necessary **packages**. This is an essential part of
        ensuring your system is ready to handle the data processing
        efficiently. This installation process makes it easier to manage
        dependencies.

        .. code-block:: console

            python3 -m pip install \
                exactextract \
                geopandas \
                numpy \
                pandas \
                plotnine \
                rasterio \
                requests \
                rioxarray \
                xarray

        Once the packages are installed and you have the
        ``composite_anom_12mo.nc`` file in your working directory, it's time
        to begin reading the file. We will be using
        :external+xarray:py:mod:`xarray`, let's start by importing it.

        .. include:: water-module-001/cell-1.rst

        The below code is configuring :external+xarray:py:mod:`xarray` options
        and :external+ipython:py:mod:`IPython` display settings to control the
        behavior of data representation and plotting in Jupyter notebooks.

        .. include:: water-module-001/cell-2.rst

        .. dropdown:: Code Explanation

            #. :external+xarray:py:class:`xarray.set_options`

                This ``class`` used to set global options that affect the
                behavior of ``xarray`` operations. Here's what each option
                does:

                - :python:`keep_attrs=True.` This ensures that metadata are
                  preserved when performing operations on ``xarray`` objects.
                  By default, many ``xarray`` operations drop attributes, but
                  setting this to :python:`True` prevents that.
                - :python:`display_expand_attrs=False.` This controls the
                  display of attributes in the ``xarray`` object's
                  representation. Setting this to :python:`False` keeps the
                  attribute section collapsed when printing an ``xarray``
                  object.
                - :python:`display_expand_coords=False.` This option controls
                  whether coordinate variables are expanded (shown in detail)
                  when displaying an ``xarray`` object. Setting it to
                  :python:`False` collapses the coordinate details.
                - :python:`display_expand_data=False.` Similar to the previous
                  options, this collapses the data section of the ``xarray``
                  object when printing. This can make the display of large
                  datasets more manageable.
                - :python:`display_expand_data_vars=False.` This option
                  collapses the display of data variables in the output of an
                  ``xarray`` dataset, keeping it neater for large datasets.

            .. tip::

                These options help manage how ``xarray`` data structures are
                displayed in Jupyter notebooks, making them more concise by
                collapsing various sections (attributes, coordinates, data,
                and data variables).

            2. **%config InlineBackend.figure_format="retina"**

                This is an IPython **magic** command that configures the way
                figures (like plots) are displayed in Jupyter notebooks. This
                sets the figure resolution to "retina," which produces
                high-resolution plots for better visual quality, especially on
                displays with high pixel density (like MacBooks with Retina
                displays). This is commonly used in Jupyter notebooks to make
                plots look crisper.

        Using the :external+xarray:py:func:`xarray.open_dataset` function,
        read the file and print the dataset.

        .. include:: water-module-001/cell-3.rst
        |

The output reveals that the dataset consists of five attributes: ``deficit``,
``deficit_cause``, ``surplus``, ``surplus_cause``, and ``both`` (a combination
of ``surpluses`` and ``deficits``. Additionally, it has three dimensions:
``longitude`` and ``latitude`` (spatial extents on the x/y axes) and ``time``
as the third dimension.

In total, this amounts to **4020 individual** raster layers (calculated as 5
attributes multiplied by **804 time steps/months**). This is a clear
indication of just how extensive and complex the dataset is, and further
reinforces the importance of efficient data handling.

-------------------------------------------------------------------------------
Attribute Selection of Reducing Complexity
-------------------------------------------------------------------------------

Now that we've loaded the dataset, let's focus on reducing the size and
complexity of the data by selecting only the variables we need. This process
is known as **Attribute Selection**. In this example, we'll focus on the
``deficit`` variable, which represents drought conditions, and the ``crs``
variable, which contains spatial reference information (i.e., coordinate
reference system).

Why leave out other variables? Well, this decision depends on the specific
goals of your analysis. Since we already know that this dataset covers
12-months, we can safely omit the integration variable, which tracks the time
period.

.. tab-set::
    :sync-group: programming-language

    .. tab-item:: R-Programming |badge-beta|
        :sync: r-programming

        ...

    .. tab-item:: Python
        :sync: python

        ...

        In this code block, we use double brackets to subset the dataset and
        extract only the variables we're interested in |html-dash| ``deficit``
        and ``crs``. This step is crucial for efficiently managing memory when
        working with large datasets. By reducing the number of variables, we
        make the data easier to handle, especially if you're performing
        intensive operations later on.

        After subsetting the data, it's always a good practice to inspect the
        result to make sure everything looks as expected. When you print
        ``wsim_gldas`` again, you should see that the dataset now contains
        only two variables: ``deficit`` and ``crs``. This reduction in
        variables helps streamline the dataset and ensures that we're only
        working with the most relevant information.

By focusing on **deficit**, which is vital for understanding drought
conditions, and retaining the **crs** information for spatial analysis, we can
move forward confidently, knowing that we've optimized the dataset for our
needs.

This step-by-step guide not only reduces the dataset to a more manageable size
but also maintains the critical information needed for your analysis. The goal
here is to simplify the workflow while ensuring you have everything required
to proceed.

-------------------------------------------------------------------------------
Time Selection for Improved Data Efficiency
-------------------------------------------------------------------------------

In this section, we'll delve into how to further refine the dataset by
selecting a specific time range that aligns with your analysis goals.
Narrowing down the temporal range helps reduce the overall size of the
dataset, making it more manageable and focused. This process will also allow
us to focus on key moments in the data, which is essential when analyzing
time-series datasets.

Why Focus on a Specific Temporal Range?
===============================================================================

Large datasets often contain data spanning many years, and while this can be
beneficial for certain analyses, it can also make the file unnecessarily large
and difficult to work with. By specifying a temporal range of interest, we can
isolate the most relevant portions of the dataset. In this case, we're
interested in the period from **December 2000** to **December 2014**, and by
selecting data from these years, we make the file smaller and more manageable.

The dataset we're using, **WSIM-GLDAS**, aggregates the ``deficit`` (drought)
variable over a 12-month period. This means that each time step in the dataset
represents an average of the deficit over the previous 12 months. As a result,
if we focus on the December months, we'll obtain annual averages for the
deficit, which provides a clear picture of how drought conditions evolved year
by year.

Let's dive into the step-by-step process for selecting this time range.

.. tab-set::
    :sync-group: programming-language

    .. tab-item:: R-Programming |badge-beta|
        :sync: r-programming

        ...

    .. tab-item:: Python
        :sync: python

        To start, we need to create a list of dates corresponding to every
        December between **2000** and **2014**. This will ensure that we're
        selecting a yearly snapshot of the drought **deficit** during this
        period. We'll achieve this using the powerful **Pandas** library,
        which is excellent for handling time series data.

        ...

        Now that we've generated the sequence of dates, the next step is to
        apply this list to the dataset and select only the data for the
        specified months. This is where we use
        :external+xarray:py:meth:`xarray.DataArray.sel` method to subset the
        dataset.

        ...

        By passing the list of dates, keeps, into the
        :external+xarray:py:meth:`xarray.DataArray.sel` method, we're telling
        :external+xarray:py:mod:`xarray` to extract only the data for the
        corresponding time steps. This reduces the time dimension of the
        dataset to 15 time steps |html-dash| one for each December from
        **2000** to **2014**. This step is crucial in reducing the overall
        size of the dataset while ensuring we retain the annual averages for
        the deficit variable.

        At this point, we've successfully reduced the dataset to focus on the
        deficit variable over the desired time range (2000-2014). Now that we
        have a more manageable dataset, it's often helpful to visualize the
        data. Visualizations can give you a clearer understanding of patterns
        and trends, especially when dealing with time-series data related to
        spatial variables like ``deficit``.

        We'll use Xarray's built-in plotting functionality to create a quick
        visualization of the deficit over time.

        ...

Although we've already reduced the dataset significantly by focusing on a
single variable and a specific time range, there may still be situations where
you want to narrow it down even further. For example, you might only be
interested in analyzing a particular geographic region, such as a country or a
state. By limiting the spatial extent, you can make the dataset even smaller
and more targeted to your specific area of interest.

In future steps, we'll explore how to subset the dataset spatially, allowing
you to focus on the regions that matter most for your analysis.

By specifying a temporal range and visualizing the deficit data, we've taken
important steps to optimize the dataset for analysis. This approach not only
reduces the size of the file, making it easier to handle, but also ensures
that we're focusing on the most relevant time period. In the next steps, we
can explore how to further refine the dataset by limiting the spatial extent
to specific regions.

-------------------------------------------------------------------------------
Spatial Selection of a Geographic Area of Interest
-------------------------------------------------------------------------------

In data analysis, especially when working with spatial datasets, we often need
to focus on a specific geographic region. Whether it's for better performance,
easier data handling, or simply because you're interested in a particular
area, spatial selection is an essential tool.

In this case, we'll be cropping our dataset, WSIM-GLDAS, to a specific
geographic region using the boundary of the United States and further refining
it to just Texas. This reduces the amount of data we're working with, making
it smaller, easier to manage, and more focused for analysis.

.. dropdown:: Methods for Cropping Spatial Data

    - **Bounding Box.** This method uses specific geographic coordinates
      (longitude and latitude) that define the extent of the area you wish to
      select. Example: You provide the xmin, ymin, xmax, and ymax coordinates
      to specify the rectangular area you want to crop.
    - **Raster Object.** You can also use another raster dataset to crop your
      target dataset by matching its extent to that of the provided raster.
    - **Vector Boundary.** Another common method is to crop the dataset using
      a vector boundary |html-dash| a shapefile or GeoJSON that defines a
      geographic or political boundary (e.g., country, state, province).

In this example, we will use a vector boundary in GeoJSON format to crop our
raster data. This method is particularly useful when working with well-defined
areas like states or countries.

To begin, we need to obtain a vector boundary that represents the geographic
area we are interested in. We will use the geoBoundaries API to fetch this
data. The geoBoundaries API allows us to access vector boundaries for
countries and their subdivisions, such as states or provinces. This data can
be retrieved in various formats, including GeoJSON, which is a widely used
format for geographic data.

For this example, we'll be working with the United States and specifically
focusing on Administrative Level 1 (ADM1), which corresponds to the State
level.

The API URL structure is as follows:
https://www.geoboundaries.org/api/current/gbOpen/ISO3/LEVEL/

- **ISO3.** This is the three-letter country code (for the U.S., it's "USA").
- **LEVEL.** This defines the administrative level (in this case, "ADM1" for
  states).

Why Focus on a Specific Temporal Range?
===============================================================================

Large datasets often contain data spanning many years, and while this can be
beneficial for certain analyses, it can also make the file unnecessarily large
and difficult to work with. By specifying a temporal range of interest, we can
isolate the most relevant portions of the dataset. In this case, we're
interested in the period from **December 2000** to **December 2014**, and by
selecting data from these years, we make the file smaller and more manageable.

The dataset we're using, **WSIM-GLDAS**, aggregates the ``deficit`` (drought)
variable over a 12-month period. This means that each time step in the dataset
represents an average of the deficit over the previous 12 months. As a result,
if we focus on the December months, we'll obtain annual averages for the
deficit, which provides a clear picture of how drought conditions evolved year
by year.

Let's dive into the step-by-step process for selecting this time range.

.. tab-set::
    :sync-group: programming-language

    .. tab-item:: R-Programming |badge-beta|
        :sync: r-programming

        ...

    .. tab-item:: Python
        :sync: python

        We'll use the requests library to access this data and the geopandas library to handle the GeoJSON file.

        ...

        The JSON response from the geoBoundaries API contains a variety of information, but what we need is the direct link to the GeoJSON file. This link is found in the gjDownloadURL field (typically located in item 29 of the response).

        We'll now use geopandas to load and visualize the GeoJSON data.

        ...

        The GeoJSON we retrieved contains the boundaries for all U.S. states and territories, including places like Alaska, Hawaii, and Puerto Rico. For this demonstration, we're going to focus on the contiguous United States (i.e., the 48 mainland states), so we'll need to exclude certain regions from our dataset.

        ...

        For more detailed analysis, we might want to focus on a specific state. In this example, let's focus on Texas.

        ...

        This snippet extracts Texas by filtering the shapeName column for any entries that contain the word "Texas". We can then visualize just the Texas boundary.

        Now that we have the vector boundary for Texas, we can use it to crop the WSIM-GLDAS dataset. This process is called spatial clipping, where the raster data is cropped to the extent of the Texas boundary. For this, we'll use rioxarray, a library built on top of Xarray and Rasterio that provides geospatial raster operations.

        First, we need to ensure the dataset has the correct Coordinate Reference System (CRS), which we can set to EPSG: 4326, a common geographic coordinate system.

        ...

        Now that we've successfully clipped the dataset to the extent of Texas, we can visualize the results. We'll plot the last time step in the dataset (December 2014) and overlay it with the Texas boundary to verify our processing.

        ...

        This plot provides a clear view of the deficit anomaly within Texas over time, with color variations showing the severity of drought conditions.

        Finally, we can save both the processed raster data (WSIM-GLDAS) and the vector boundary (Texas) to disk. This is useful for sharing with colleagues, conducting further analysis, or storing the data for future use.

        ...

The resulting dataset is significantly smaller (1.6 MB compared to the original 1.7 GB), making it much more manageable for further analysis, especially in cloud environments or workshops.

This completes the process of spatially selecting and processing your data, allowing you to focus on the region and variable of interest.     

.. rubric:: References
    :heading-level: 2

.. [#] NOAA. 2019. `"Water Cycle." <https://www.noaa.gov/education/
    resource-collections/freshwater/water-cycle>`_ National Oceanic;
    Atmospheric Administration.
.. [#] IPCC. 2023. `"Climate Change 2021 the Physical Science Basis" <https://
    ciesin-geospatial.github.io/TOPSTSCHOOL-water/m101-wsim-gldas.html#ref-
    intergovernmentalpanelonclimatechange2023>`_, June.
.. [#] Zhou, Haddeland, T. 2016. `"Human-Induced Changes in Global Water
    Cycle." <https://ciesin-geospatial.github.io/TOPSTSCHOOL-water/m101-wsim-
    gldas.html#ref-Zhou2016>`_ Geophysical Monograph Series.
.. [#] Rodgers, Alison Ince. 2023. `"Understanding Droughts." <https://
    ciesin-geospatial.github.io/TOPSTSCHOOL-water/m101-wsim-gldas.html#ref-
    Rodgers2023>`_ National Geographic Society.
.. [#] Guillen, George. 2002. `"Klamath River Fish Die-Off." <https://
    ciesin-geospatial.github.io/TOPSTSCHOOL-water/m101-wsim-gldas.html#ref-
    guillen2002>`_ Mortality Report AFWO-01-03. Arcata, CA: U.S. Fish &
    Wildlife Service.
.. [#] Bland, Alastair. 2014. `"California Drought Has Wild Salmon Competing
    with Almonds for Water." <https://www.npr.org/sections/thesalt/2014/08/21/
    342167846/california-drought-has-wild-salmon-competing-with-almonds-for-
    water>`_ National Public Radio.
.. [#isciences] ISciences, and Center For International Earth Science
    Information Network-CIESIN-Columbia University. 2022a. `"Documentation for
    the Water Security Indicator Model - Global Land Data Assimilation System
    (WSIM-GLDAS) Monthly Grids, Version 1." <https://doi.org/10.7927/
    X7FJ-JJ41>`_ Palisades, NY: NASA Socioeconomic Data; Applications Center
    (SEDAC).

.. rubric:: Attributions
    :heading-level: 2

.. [#freepik_1] Image by `freepik - 13 <https://www.freepik.com/free-photo/
    pollution-concept-factory-emisions_18268018.htm#fromView=search&page=1&
    position=13&uuid=6b870993-1f14-4765-b9bb-ef68514a09d3>`_
.. [#freepik_2] Image by `freepik - 26 <https://www.freepik.com/free-photo/
    pollution-concept-factory-emisions_18268011.htm#fromView=search&page=1&
    position=26&uuid=6b870993-1f14-4765-b9bb-ef68514a09d3>`_
.. [#klamath_death] Our Klamath Basin Water Crisis `article <https://ca-times.
    brightspotcdn.com/dims4/default/15e8000/2147483647/strip/true/crop/
    4032x3024+0+0/resize/840x630!/quality/90/?url=https://california-times-
    brightspot.s3.amazonaws.com/1e/a1/eb76da6f4c5a9ad847549d2b3fa9/tsfxbams.
    jpeg>`_
.. [#nasa_svs_1] A true color satellite `image <https://svs.gsfc.nasa.gov/
    12950/#media_group_325749>`_ of California shows drought in the region
    which corresponds with decreases in freshwater reserves
