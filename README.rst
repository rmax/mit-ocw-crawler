============================
MIT's OpenCourseWare Crawler
============================

:Author: Rolando Espinoza La fuente <darkrho@gmail.com>

About
=====

MIT's `OpenCourseWare`_ is an excellent resource of knowledge.
This crawler helps to fetch all courses information, like
materials' download links.


Requirements
============

 - `Scrapy`_

Usage Example
=============

First, choose a department at MIT's `OpenCourseWare`_. Then figure out the
``DEPARTMENT_ID`` which is part of the department's url. In this case
we will choose the `Nuclear Science and Engineering`_ department using
``nuclear-engineering`` as DEPARTMENT_ID.

Finally run ``scrapy-ctl.py`` to crawl and fetch all courses information.

 * To only crawl all courses::

    $ ./scrapy-ctl.py crawl materials --set DEPARTMENT_ID=nuclear-engineering

 * To store results in a CSV file::

    $ ./scrapy-ctl.py crawl materials --set DEPARTMENT_ID=nuclear-engineering --set EXPORT_FORMAT=csv --set EXPORT_FILE=materials.csv

 * To store urls for later usage in a download manager::

    $ ./scrapy-ctl.py crawl materials --set DEPARTMENT_ID=nuclear-engineering --set EXPORT_FORMAT=csv --set EXPORT_FILE=materials.csv --set EXPORT_FIELDS=download_url
    $ wget -i materials.csv


.. _Scrapy: http://www.scrapy.org/
.. _OpenCourseWare: http://ocw.mit.edu/
.. _Nuclear Science and Engineering: http://ocw.mit.edu/courses/nuclear-engineering/
