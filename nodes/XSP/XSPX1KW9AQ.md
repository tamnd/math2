---
tag: XSPX1KW9AQ
kind: concept
name: Low-discrepancy sequence
msc: [11K38, 11K36, 65C05]
sources:
  - url: https://en.wikipedia.org/wiki/Low-discrepancy_sequence
same_as:
  wikidata: Q6692743
  wikipedia: Low-discrepancy sequence
---

## Summary

A low-discrepancy sequence is a sequence of points in the unit cube $[0, 1)^s$ whose initial segments fill the cube as evenly as possible.
Evenness is measured by the star discrepancy.
It compares the share of the first $N$ points in each box anchored at the origin with the volume of the box.
For a low-discrepancy sequence the largest difference is of order $(\log N)^s / N$.
For large $N$ this is much smaller than the typical value of order $N^{-1/2}$ for random points.
Such sequences are the point sets of quasi-Monte Carlo integration.
Every low-discrepancy sequence is uniformly distributed in the cube; for $s = 1$ this is [[equidistribution modulo one|XM6DH57BWY]].

## Explanations

### L1 human

Random points tend to clump in some places and leave gaps in others.
A low-discrepancy sequence places each new point in a region that is still empty, so that at every stage the points are spread out evenly.
The simplest example on $[0, 1)$ is the van der Corput sequence $\frac12, \frac14, \frac34, \frac18, \frac58, \frac38, \frac78, \ldots$, obtained by writing $1, 2, 3, \ldots$ in binary and mirroring the digits at the binary point.
In higher dimension, the Halton and Sobol sequences play the same role.
Averages of a function over such points approximate its integral with a smaller error than random points.
