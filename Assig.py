#!/usr/bin/env python
# coding: utf-8

# # Programming a seismic program

# This notebook goes with the article
# 
# > Bianco, E and M Hall (2015). Programming a seismic program. *CSEG Recorder*, November 2015. 
# 
# 
# Modified by: MSc Jorge Guizar (Formerly at ETH Zurich, Currently: UNAM)

# RULES:
# 
# > WORK IN PAIRS
# 
# > USE REFERENCES IF NEEDED
# 
# > DUE DATE: 1ST OCTOBER 2019 24:00
# 
# > CHECK PRESENTATION
# 
# > jorge.guizaralfaro@gmail.com
# 
# 
# 

# In[35]:


Names:"ALAN DE LA FUENTE BONFIL & KARLA DÍAZ"
    
    


# ## Set up the survey

# Loading the following libraries

# In[36]:


import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
import geopandas as gpd
import pandas as pd
from fiona.crs import from_epsg

get_ipython().run_line_magic('matplotlib', 'inline')


# # Question 1
# Can you descibre each one of the uses of the libraries?
# 
# $\textbf{Answer Here:}$ -NumPy is the fundamental package for scientific computing with Python. It contains among other things:a powerful N-dimensional array object, sophisticated (broadcasting) functions, tools for integrating C/C++ and Fortran code, useful linear algebra, Fourier transform, and random number capabilities. Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases. -Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits. -Shapely: The first premise of Shapely is that Python programmers should be able to perform PostGIS type geometry operations outside of an RDBMS. Not all geographic data originate or reside in a RDBMS or are best processed using SQL. We can load data into a spatial RDBMS to do work, but if there’s no mandate to manage (the “M” in “RDBMS”) the data over time in the database we’re using the wrong tool for the job. The second premise is that the persistence, serialization, and map projection of features are significant, but orthogonal problems. You may not need a hundred GIS format readers and writers or the multitude of State Plane projections, and Shapely doesn’t burden you with them. The third premise is that Python idioms trump GIS (or Java, in this case, since the GEOS library is derived from JTS, a Java project) idioms -Geopandas: make working with geospatial data in python easier. It combines the capabilities of pandas and shapely, providing geospatial operations in pandas and a high-level interface to multiple geometries to shapely. -Pandas:is an open source Python package that provides numerous tools for data analysis. The package comes with several data structures that can be used for many different data manipulation tasks. It also has a variety of methods that can be invoked for data analysis, which comes in handy when working on data science and machine learning problems in Python. -Fiona: can read and write real-world data using multi-layered GIS formats and zipped virtual file systems and integrates readily with other Python GIS packages such as pyproj, Rtree, and Shapely. Fiona is supported only on CPython

# Define some survey parameters:

# In[37]:


xmi = 575000        # Easting of bottom-left corner of grid (m)
ymi = 4710000       # Northing of bottom-left corner (m)
SL = 600            # Source line interval (m)
RL = 600            # Receiver line interval (m)
si = 100            # Source point interval (m)
ri = 100            # Receiver point interval (m)
x = 3000            # x extent of survey (m)
y = 1800            # y extent of survey (m)

epsg = 26911  # A CRS to place it on the earth


# # Question 2
# 
# Can you describe   why the revious paramaters ara important ahd wich acquisiton paramaters can be computed using them? (Topic 1 presentation)
# 
# $\textbf{Answer Here:}$ These parameters are important cause when you design the acquisition, you have to consider the vertical resolution to stablish the receiver and source spacing. in that way: -SL: This is the source line spacing, the source line is a foundamental part of the templete, sources are cordinated to shot at the same time to generate the biggets land movement or presure change in the sea. -RL: this is the receiver line spacing, the receiver´s number tends to be more than sources, cause they have to map all the area. -si: in the source line, source are separated in an interval that could help to avoid coherent noise. -ri: in the receiver line, they need to be near to record all the traces. After stablishing these parameters, you can compute from them: -the box: this is the small area from the template, defined by 2 receiver lines and 2 sources lines. -the bin: this is the small area when the common mid point fall. -also you can determinate the detph in meters you are recording using this parametrs, there many theorias that postulates that the depth is the half of offset max and other says that is the fourth part.

# Now we can compute some properties of the survey:

# In[38]:


rlines = int(y/RL) + 1
slines = int(x/SL) + 1


# In[39]:


rperline = int(x/ri) + 2
sperline = int(y/si) + 2


# In[40]:


shiftx = -si/2.0
shifty = -ri/2.0


# We compute lists of the *x*- and *y*-locations of the receivers and sources with nested loops. We'll use Python's list comprehensions, which are shorthand for `for` loops that generate lists.

# In[41]:


rcvrx, rcvry = zip(*[(xmi + rcvr*ri + shiftx, ymi + line*RL - shifty)
                     for line in range(rlines)
                     for rcvr in range(rperline)])

srcx, srcy = zip(*[(xmi + line*SL, ymi + src*si)
                   for line in range(slines)
                   for src in range(sperline)])


# In[42]:


rcvrs = [Point(x, y) for x, y in zip(rcvrx, rcvry)]
srcs = [Point(x, y) for x, y in zip(srcx, srcy)]


# We can make a list of 'r' and 's' labels then compile into a dataframe.

# In[43]:


station_list = ['r']*len(rcvrs) + ['s']*len(srcs)
survey = gpd.GeoDataFrame({'geometry': rcvrs+srcs, 'station': station_list})
survey.crs = from_epsg(epsg)


# In[44]:


try:
    # Needs geopandas fork: https://github.com/kwinkunks/geopandas
    survey.plot(figsize=(12,12), column='station', cmap="bwr", markersize=20)
except:
    # This will work regardless.
    survey.plot()
plt.grid()
plt.show()


# Make a Station ID row, so we can recognize the stations again.

# In[45]:


sid = np.arange(len(survey))
survey['SID'] = sid


# In[46]:


survey.to_file('data/survey_orig.shp')


# ## Midpoint calculations

# We need midpoints. There is a midpoint between every source-receiver pair.
# 
# Hopefully it's not too inelegant to get to the midpoints now that we're using this layout object thing.

# In[47]:


midpoint_list = [LineString([r, s]).interpolate(0.5, normalized=True)
                 for r in rcvrs
                 for s in srcs]


# As well as knowing the (x,y) of the midpoints, we'd also like to record the distance from each *s* to each live *r* (each *r* in the live patch). This is easy enough to compute:
# 
#     Point(x1, y1).distance(Point(x2, y2))
#  
# Then we can make a list of all the offsets when we count the midpoints into the bins. 

# In[48]:


offsets = [r.distance(s)
           for r in rcvrs
           for s in srcs]


# In[49]:


azimuths = [np.arctan((r.x - s.x)/(r.y - s.y))
            for r in rcvrs
            for s in srcs]


# Make a Geoseries of the midpoints, offsets and azimths:

# In[50]:


midpoints = gpd.GeoDataFrame({'geometry': midpoint_list,
                              'offset': offsets,
                              'azimuth': np.degrees(azimuths),
                              })

midpoints[:5]


# In[51]:


ax = midpoints.plot(markersize=3,figsize=(10,5))


# # Question 3 
# 
# What can you observe from the last plot?
# 
# $\textbf{Answer here:}$ The last plot shows all the midpoints recorded, they are defined by DX/2 and DY/2.

# Save to a shapefile if desired. 

# In[52]:


# midpoints.to_file('midpoints.shp')


# ## Spider plot

# In[53]:


midpoints['offsetx'] = offsets * np.cos(azimuths)
midpoints['offsety'] = offsets * np.sin(azimuths)
midpoints[:5].offsetx  # Easy!


# In[54]:


midpoints.ix[3].geometry.x # Less easy :(


# We need lists (or arrays) to pass into the [matplotlib quiver plot](http://matplotlib.org/examples/pylab_examples/quiver_demo.html). This takes four main parameters: *x, y, u,* and *v*, where *x, y* will be our coordinates, and *u, v* will be the offset vector for that midpoint.
# 
# We can get at the GeoDataFrame's attributes easily, but I can't see how to get at the coordinates in the geometry GeoSeries (seems like a user error — it feels like it should be really easy) so I am resorting to this: 

# In[55]:


x = [m.geometry.x for i, m in midpoints.iterrows()]
y = [m.geometry.y for i, m in midpoints.iterrows()]


# In[56]:


fig = plt.figure(figsize=(12,8))
plt.quiver(x, y, midpoints.offsetx, midpoints.offsety, units='xy', width=2, scale=1/0.025, pivot='mid', headlength=0)
plt.axis('equal')
plt.show()


# # Question 4
# 
# 
# Explain the quiver plot (uppper plot) (http://matplotlib.org/examples/pylab_examples/quiver_demo.html)
# 
# $\textbf{Answer here:}$ The last plot shows all the midpoints recorded, they are defined by DX/2 and DY/2.

# ## Bins

# The bins are a new geometry, related to but separate from the survey itself, and the midpoints. We will model them as a GeoDataFrame of polygons. The steps are:
# 
# 1. Compute the bin centre locations with our usual list comprehension trick.
# 1. Buffer the centres with a square.
# 1. Gather the buffered polygons into a GeoDataFrame.

# In[57]:


# Factor to shift the bins relative to source and receiver points
jig = si / 4.
bin_centres = gpd.GeoSeries([Point(xmi + 0.5*r*ri + jig, ymi + 0.5*s*si + jig)
                             for r in range(2*rperline - 3)
                             for s in range(2*sperline - 2)
                            ])

# Buffers are diamond shaped so we have to scale and rotate them.
scale_factor = np.sin(np.pi/4.)/2.
bin_polys = bin_centres.buffer(scale_factor*ri, 1).rotate(-45)
bins = gpd.GeoDataFrame(geometry=bin_polys)

bins[:3]


# In[90]:


ax = bins.plot(figsize=(5,5))


# ## Spatial join

# Thank you to Jake Wasserman and Kelsey Jordahl for this code snippet, and many pointers. 
# 
# This takes about 20 seconds to run on my iMac, compared to something close to 30 minutes for the old nested loops. 

# In[91]:


def bin_the_midpoints(bins, midpoints):
    b = bins.copy()
    m = midpoints.copy()
    reindexed = b.reset_index().rename(columns={'index':'bins_index'})
    joined = gpd.tools.sjoin(reindexed, m)
    bin_stats = joined.groupby('bins_index')['offset']                      .agg({'fold': len, 'min_offset': np.min})
    return gpd.GeoDataFrame(b.join(bin_stats))


# In[92]:


bin_stats = bin_the_midpoints(bins, midpoints)


# In[93]:


bin_stats[:10]


# # Question 5
# 
# Change the size of the figures to pu it in the report and save it into a jpeg or png (to load ir later in LaTex)
# Add them a colorbar

# In[94]:


ax = bin_stats.plot(column="fold")


# In[95]:


ax = bin_stats.plot(column="min_offset")


# # Dealing with the real world: moving stations

# In[96]:


new_survey = gpd.GeoDataFrame.from_file('data/adjusted.shp')


# Join the old survey to the new, based on SID. 

# In[97]:


complete = pd.merge(survey, new_survey[['geometry', 'SID']], how='outer', on='SID')


# Rename the columns.

# In[66]:


complete.columns = ['geometry', 'station', 'SID', 'new_geometry']


# In[67]:


complete[18:23]


# Calculate the distance each station has moved. We have to use `GeoSeries` to do this, and everything was transformed to ordinary `Series` when we did the join.

# In[68]:


old = gpd.GeoSeries(complete.geometry)
new = gpd.GeoSeries(complete['new_geometry'])

complete['skid'] = old.distance(new)


# In[69]:


complete[15:20]


# Now that we have the new geometry, we can recompute everything, this time from the dataframe rather than from lists.
# 
# First the midpoints.

# In[70]:


rcvrs = complete[complete['station']=='r'][complete['new_geometry'].notnull()]['new_geometry']
srcs = complete[complete['station']!='r'][complete['new_geometry'].notnull()]['new_geometry']

midpoint_list = [LineString([r, s]).interpolate(0.5, normalized=True)
                 for r in rcvrs
                 for s in srcs]


# In[71]:


len(srcs)


# In[72]:


offsets = [r.distance(s)
           for r in rcvrs
           for s in srcs]


# In[73]:


azimuths = [np.arctan((r.x - s.x)/(r.y - s.y))
            for r in rcvrs
            for s in srcs]


# In[74]:


new_midpoints = gpd.GeoDataFrame({'geometry': midpoint_list,
                                  'offset': offsets,
                                  'azimuth': np.degrees(azimuths),
                                  })


# In[77]:


new_stats[:10]


# # Question 7
# 
# Plot the new midpoints (see upper section), the next figure shows the  old  midpoints, show me the new distribution 
# 
# What can you observe?
# 
# $\textbf{Answer here:}$

# In[78]:


#HINT:
ax = midpoints.plot(markersize=3,figsize=(10,5))


# Now we can fill the bins and get the statistics.

# In[79]:


new_stats = bin_the_midpoints(bins, new_midpoints).fillna(-1)


# In[80]:


new_stats.plot(column="fold", figsize=(12,8))
plt.show()


# A quick diff shows how the fold has changed.

# In[81]:


new_stats['diff'] = bin_stats.fold - new_stats.fold
new_stats.plot(column="diff", figsize=(12,8))
plt.show()


# In[82]:


# new_stats.to_file('data/new_stats.shp')


# In[83]:


ax = new_stats.plot(column="min_offset")


# # Question 8
# 
# 
# 
# Last section showed when some receivers are moved
# 
# What can you observe?
# 
# Why do you think that the fold has changed?
# 
# 1-The distribution is not uniform now, it has changed because the number of traces that has the same common midpoint is diferent than the first, if we move the receiver´s number they are going to have drastic changes in the traces for bin generating irregularities in the template.
# 
# 

# # Question 9
# 
# Change the source interval , receiver interval, source line interval and receiver line interval and tell me what can you observe?
# 
# 

# # END

# Grade:

# In[ ]:




