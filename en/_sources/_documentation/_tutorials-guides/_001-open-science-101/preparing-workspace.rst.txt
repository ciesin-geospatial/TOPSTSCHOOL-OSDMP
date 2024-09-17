.. Author: Akshay Mestry <xa@mes3.dev>
.. Created on: Wednesday, September 11 2024
.. Last updated on: Thursday, September 12 2024

===============================================================================
Workspace Setup
===============================================================================

.. title-hero::
    :icon: fa-brands fa-python
    :summary:
        Equip yourself with the essential tools required for efficient coding,
        data analysis, and collaboration in Open Science. This guide will walk
        you through installing and configuring the key tools you'll need.

.. tags:: getting-started, open-science-101, preparing-workspace

.. contributors::
    :prefix: Put together by
    :location: Chicago, IL

    - Akshay Mestry
    - xa@mes3.dev
    - https://github.com/xames3/

In the world of :term:`Open Science`, collaboration and innovation go
hand-in-hand. Scientists, researchers, and contributors from across the globe
come together to share data, insights, and breakthroughs. However, this
collaboration requires more than just ideas |html-dash| it requires the right
set of tools. These tools serve as the backbone for everything from coding and
data analysis to version control and publishing. Without them, the journey
from concept to contribution would be slow, error-prone, and often
overwhelming.

.. dropdown:: What Are These Tools?

    In this context, tools refer to a collection of software programs,
    platforms, and environments that allow you to efficiently work with code,
    manage versions, handle data, and even collaborate in real time. Each tool
    plays a specific role in the research and development process, addressing
    different challenges:

    - :term:`Version Control System (VCS)` like Git allow you to track changes
      in code, ensuring you never lose work and can collaborate seamlessly with
      others.
    - :term:`Integrated Development Environment (IDE)` like Visual Studio Code provide a
      space to write, debug, and test code with features that make your
      workflow faster and more intuitive.
    - :term:`Data processing tools` like Jupyter Notebook facilitate
      interactive data analysis, letting you run code in chunks, visualize
      outputs, and document results in one place.
    - :term:`Package managers` like Conda help you manage software libraries
      and environments, ensuring that you're working with the right versions
      of the tools for your project.

    These tools are more than just software |html-dash| they are the enablers
    of :term:`Open Science`. They streamline workflows, reduce friction, and
    help build a shared language across diverse disciplines. By mastering
    these tools, you become empowered to focus more on your research and less
    on the technical overhead. They allow you to engage in the spirit of Open
    Science |html-dash| transparently, collaboratively, and efficiently.

.. dropdown:: Why These Tools Are Needed?

    Imagine trying to contribute to a global research project without a
    :term:`Version Control System (VCS)`. Every small change would need to be
    communicated manually, resulting in conflicting edits, lost progress, and
    massive inefficiencies. Or think about analyzing vast datasets without the
    help of specialized software |html-dash| it would be an overwhelming task
    that could consume precious time and energy. These tools solve exactly
    these types of problems:

    - **Faster Workflows.** Automate repetitive tasks and offering smart
      suggestions.
    - **Enhance Collaboration.** Allowing teams to work on the same projects
      without stepping on each other's toes.
    - **Security.** Maintain a history of changes and protecting your work
      from accidental loss.

In essence, these tools equip you with the digital infrastructure to excel in
the world of :term:`open research`, and the best part? Most of them are free
and open-source, aligning perfectly with the principles of Open Science.

-------------------------------------------------------------------------------
Integrated Development Environments (IDEs)
-------------------------------------------------------------------------------

Integrated Development Environments (IDEs) are powerful tools designed to
simplify the process of writing, testing, and debugging code. An IDE provides
a cohesive workspace where all essential features |html-dash| such as a text
editor, debugger, compiler, and version control |html-dash| are bundled into a
single platform. For programmers and data scientists, an IDE can significantly
boost productivity by offering intelligent code completion, syntax
highlighting, and project management tools.

.. admonition:: Common Misconceptions
    :class: danger

    - **IDEs Are Only for Professional Programmers.** Many assume that IDEs
      are complicated and reserved for advanced users, but the truth is that
      modern IDEs like Visual Studio Code are beginner-friendly and versatile.
    - **IDEs Are Resource-Intensive.** Another misconception is that IDEs are
      slow and consume a lot of system resources. While some older IDEs might
      have been resource-heavy, newer ones like Visual Studio Code are
      lightweight and optimized for performance across various platforms.
    - **You Only Need a Text Editor.** While text editors can suffice for
      writing code, an IDE offers much more |html-dash| debugging tools,
      project management, and integrated version control, making the
      development process more streamlined and efficient.

To begin this journey into mastering the essential tools for Open Science,
we'll start with one of the most popular and powerful IDEs available: **Visual
Studio Code**.

Whether you're writing Python scripts, working on Jupyter notebooks, or
managing documentation, Visual Studio Code provides a feature-rich yet
lightweight environment tailored to your needs. It's highly customizable and
integrates smoothly with version control, making it the perfect starting point
for any coding or data analysis tasks you'll encounter in NASA's :term:`TOPS`
:term:`SCHOOL` program.

.. tab-set::
    :sync-group: operating-system

    .. tab-item:: Windows
        :sync: windows

        - Download the latest Visual Studio Code for `Windows <https://code.
          visualstudio.com/sha/download?build=stable&os=win32-arm64-user>`_,
          run the installer and select your preferences.

        .. admonition:: Pro Tip
            :class: tip

            Make sure to check the box for "**Add to PATH**" if you want to
            access Visual Studio Code from the command line.

        - Click :guilabel:`&Install` and wait for the process to complete.
          Once done, click :guilabel:`&Finish` to launch Visual Studio Code
          for the first time.

    .. tab-item:: macOS
        :sync: macos

        - Download the latest Visual Studio Code for `macOS <https://code.
          visualstudio.com/sha/download?build=stable&os=darwin-universal>`_,
          open the ``.dmg`` file and drag the Visual Studio Code app to your
          Applications folder.

        - Open Visual Studio Code, press :kbd:`Command+Shift+P`,
          and type: ``Shell Command``, select the option to Install.

    .. tab-item:: Linux (Ubuntu/Debian-based) |badge-beta|
        :sync: linux

        - Open a terminal and run the following command to update your
          system's package index:
     
          .. code-block:: bash

                sudo apt update \
                && apt upgrade \
                && apt install \
                    software-properties-common
                    apt-transport-https
                    wget

.. tab-set::
    :sync-group: operating-system

    .. tab-item:: Windows
        :sync: windows

        Windows Stuff

    .. tab-item:: macOS |badge-beta|
        :sync: macos

        macOS Stuff

    .. tab-item:: Linux |badge-beta|
        :sync: linux

        Linux Stuff
