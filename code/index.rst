.. _code:

===================================
 Software Development Data Sharing
===================================

As our tools to study the brain become more and more sophisticated, we are
faced with massive amounts of data. Increasingly, scientific research requires
writing software to deal with these growing amounts of data and in order to
apply more sophisticated methods of analysis. However, in order for scientific
results to be reproducible it is essential that we make data available to other
researchers and that we publish the computer code used to generate our
results.

Here are some of my attempts to do that. For more, take a look at my `github
account`__

__ github_



Nitime
------

As a graduate student at Berkeley, I started working on the `nipy`__ project,
aimed at writing reproducible research code for neuroimaging in the `Python`__
programming language). As part of this project, together with others, I built
`Nitime`__, a library for time-series analysis of data from neuroscience
experiments. It contains implementations a high-level representation of time
and of time-series data, as well as algorithms for time-series analysis
(spectral analysis, coherence estimation, event-related analysis, multi-variate
auto-regressive model fitting, and more), convenience classes for analysis and
visualization. This software library is being developed in close collaboration
with `Fernando Perez`__ (to whom I also owe the machinery used to create `this
website <http://fperez.org/code/index.html#how-this-site-is-built>`_) and
several others. The figure below is an example of analysis conducted using
nitime.

__ nipy_
__ whypython_
__ nitime_
__ fperez_


.. image:: event_related_fmri_01.png
   :scale: 60 %
   :target: http://nipy.sourceforge.net/nitime/examples/index.html


Grasshopper data
----------------

I have made a couple of the data sets that I collected at the `ITB`__ available
on the `CRCNS`__ website. You can find the details `here
<http://crcns.org/data-sets/ia>`_. 

__ itb_
__ crcns_

.. include:: links.txt
