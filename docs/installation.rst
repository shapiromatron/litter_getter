.. highlight:: shell

============
Installation
============


Stable release
--------------

To install litter_getter, run this command in your terminal:

.. code-block:: console

    pip install litter_getter

This is the preferred method to install litter_getter, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


Development version
-------------------

Clone from the `Github repository`_:

.. code-block:: console

    git clone git://github.com/shapiromatron/litter_getter

Once you have a copy of the source, install with:

.. code-block:: console

    cd litter_getter/
    pip install -e .
    pip install -r requirements_dev.txt
    make test

.. _`Github repository`: https://github.com/shapiromatron/litter_getter
