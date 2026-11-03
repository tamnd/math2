---
tag: 189XXD6TPC
kind: problem
name: Earthquake location problem
msc: [86A15, 86A22, 65K10]
uses: [1ED8R29JZR, 0BYTQ4X1HC, PCMW7KN5P4]
about: [PCMW7KN5P4]
sources:
  - url: https://en.wikipedia.org/wiki/Epicenter
history:
  posed_by: "Ludwig Geiger"
  first_stated: "1910"
  notes: "Geiger gave the first iterative method to find the hypocentre and origin time from arrival times."
---

## Problem

Let seismic stations be at known points $x_1, \dots, x_N$ of $\R^3$.
Let $T(x, h)$ be the travel time of a seismic phase from a source at $h \in \R^3$ to a station at $x$.
This function is given by a known velocity model.
Let $t_i$ be the observed arrival time of the phase at station $i$.
The *earthquake location problem* asks for the hypocentre $h$ and the origin time $t_0 \in \R$ that best explain the data.
Usually this is meant in the [[least squares|0BYTQ4X1HC]] sense:
$$\min_{h,\, t_0} \sum_{i=1}^{N} \bigl(t_i - t_0 - T(x_i, h)\bigr)^2.$$
The epicentre is the point of the Earth's surface above the hypocentre $h$.

## Remarks

There are four unknowns, so at least four arrival times are needed, and more are used in practice to average out errors in picks and in the model.
The problem is nonlinear in $h$.
Geiger's method solves it by linearising $T$ around a trial location and solving the linear least squares problem for the correction, which is the Gauss–Newton iteration.
Take a homogeneous medium of speed $c$ in the plane.
The difference of the arrival times at two stations fixes the difference of the distances to them.
So the epicentre lies on a branch of a hyperbola with these stations as foci.
The depth and the origin time trade off against each other when all stations are far away compared with the depth, which makes the depth the least well determined coordinate.
The answer depends on the velocity model through the [[travel-time curves|1ED8R29JZR]], so errors in the model bias the location; relative methods that locate many events together reduce this bias.
The problem is a basic example of an [[inverse problem|PCMW7KN5P4]] in seismology.

## Explanations

### L1 human

When an earthquake happens, its waves reach nearby seismometers first and distant ones later.
From the arrival times at many stations, one can work backwards to find where and when the earthquake started.
It is like finding where a thunderclap came from by comparing when different people heard it.
