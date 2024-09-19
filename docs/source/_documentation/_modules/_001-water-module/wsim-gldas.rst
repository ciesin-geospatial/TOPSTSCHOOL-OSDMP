.. Author: Akshay Mestry <xa@mes3.dev>
.. Created on: Friday, September 13 2024
.. Last updated on: Thursday, September 19 2024

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
Acquiring the Data
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

.. dropdown:: Downloading Data

    - Visit the `SEDAC <https://sedac.ciesin.columbia.edu/>`_ website.
    - You can navigate through themes, datasets, or collections on the
      platform. For this exercise, use the search bar to look up "**water
      security wsim**."
    - Locate and select the Water Security (WSIM-GLDAS) Monthly Grids, v1
      (1948-2014) dataset. Take a few moments to review the dataset's overview
      and documentation.
    - When you're ready, go to the **Data Download** tab. You'll need to sign
      in using your NASA EarthData account.
    - Once logged in, find the Composite Class and select the **Variable
      Composite Anomaly Twelve-Month Return Period** for download.

-------------------------------------------------------------------------------
Reading the Data
-------------------------------------------------------------------------------

.. tab-set::
    :sync-group: programming-language

    .. tab-item:: R-Programming |badge-beta|
        :sync: r-programming

        After downloading the **WSIM-GLDAS** file to your local machine, the
        next step is to prepare your **R environment** by installing and
        loading the necessary **R packages**. This is an essential part of
        ensuring your system is ready to handle the data processing
        efficiently.

        .. code-block:: r

            install.packages('stars')
            install.packages('terra')
            install.packages('sf')
            install.packages('cubelayer')
            install.packages('lubridate')
            install.packages('httr')
            install.packages('data.table')
            install.packages('exactextractr')
            install.packages('ggplot2')
            install.packages('kableExtra')

        Once the packages are set up and you have the ``composite_12mo.nc``
        file in your working directory, it's time to begin reading the file.
        Using the :r:`stars::read_stars()` function, you can read the file into
        R. Importantly, adding the argument :r:`proxy = TRUE` during this
        process is a key step, as it allows you to inspect the essential
        elements of the file without fully loading it into memory. This
        technique helps manage large, multi-dimensional datasets by only
        loading the metadata initially, which prevents your system from being
        overwhelmed, especially if it has limited memory. Multidimensional
        :term:`raster` datasets, like this one, can be enormous, and reading
        the entire file into memory at once could bring your computer to a
        halt.

        .. code-block:: r
            :emphasize-lines: 2

            # read in the 12 month integration WSIM-GLDAS file with stars
            wsim_gldas_anoms <- stars::read_stars(
                "data/composite_12mo.nc",
                proxy = TRUE
            )

        Once the initial read is complete, you can use the :r:`print()` command
        to view the file's basic structure and content.

        .. code-block:: r

            # check the basic info
            print(wsim_gldas_anoms)

    .. tab-item:: Python
        :sync: python

        After downloading the **WSIM-GLDAS** file to your local machine, the
        next step is to prepare your **Python environment** by installing and
        loading the necessary **packages**. This is an essential part of
        ensuring your system is ready to handle the data processing
        efficiently. This installation process makes it easier to manage
        dependencies.

        .. code-block:: console

            python3 -m pip install xarray \
                                   rioxarray \
                                   rasterio \
                                   pandas \
                                   geopandas
                                   exactextractr \
                                   numpy \
                                   calendar \
                                   requests \
                                   plotnine

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
               behavior of ``xarray`` operations. Here's what each option does:

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

        The output reveals that the dataset consists of five attributes:
        ``deficit``, ``deficit_cause``, ``surplus``, ``surplus_cause``, and
        ``both`` (a combination of ``surpluses`` and ``deficits``.
        Additionally, it has three dimensions: ``longitude`` and ``latitude``
        (spatial extents on the x/y axes) and ``time`` as the third dimension.

In total, this amounts to **4020 individual** raster layers (calculated as 5
attributes multiplied by **804 time steps/months**). This is a clear
indication of just how extensive and complex the dataset is, and further
reinforces the importance of efficient data handling.

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
