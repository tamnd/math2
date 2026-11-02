---
tag: ABSRB2KXA6
kind: concept
name: Quasi-Monte Carlo method
msc: [65D30, 11K45, 65C05]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-Monte_Carlo_method
same_as:
  wikidata: Q7269435
  wikipedia: Quasi-Monte Carlo method
---

## Summary

A quasi-Monte Carlo method approximates an integral over the unit cube $[0, 1]^s$ by an average of the integrand at deterministic points.
The points are spread evenly: they come from a [[low-discrepancy sequence|XSPX1KW9AQ]].
It keeps the simple form of [[Monte Carlo integration|DAR3QJ5H7Y]], an equal-weight average, but replaces random points by structured ones.
For integrands of bounded variation, the Koksma–Hlawka inequality bounds the error by the variation of the integrand times the discrepancy of the points.
This gives an error of order $(\log N)^s / N$ instead of $N^{-1/2}$.
Quasi-Monte Carlo methods are widely used in computational finance and in high-dimensional integration.

## Explanations

### L1 human

Monte Carlo integration averages a function at random points, and random points leave gaps and clusters.
Quasi-Monte Carlo uses points that are placed deliberately to avoid gaps, like a carefully raked lawn instead of scattered seeds.
For example, to integrate $f$ over $[0, 1]$ one can average $f$ at $\frac12, \frac14, \frac34, \frac18, \frac58, \ldots$, the van der Corput points.
For smooth functions of not too many variables, the error then shrinks almost like $1/N$ rather than $1/\sqrt N$.
The price is the loss of a simple statistical error estimate, which randomized versions of the method restore.
