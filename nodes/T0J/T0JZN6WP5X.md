---
tag: T0JZN6WP5X
kind: concept
name: Moving least squares
msc: [65D10, 41A63, 65D05]
sources:
  - url: https://en.wikipedia.org/wiki/Moving_least_squares
same_as:
  wikidata: Q6927143
  wikipedia: Moving least squares
---

## Summary

Moving least squares builds a smooth function from scattered data in $\R^d$.
At each point $x$ it fits a low-degree polynomial to the data by [[weighted least squares|H5CGZHBR58]], with weights that favour data points close to $x$.
The value of the reconstruction at $x$ is the value of this local fit at $x$.
As $x$ moves, the weights and so the local polynomial change continuously, which gives a smooth global approximation.
It is a basic tool of [[multivariate interpolation|BM703GV34G]] and approximation, of surface reconstruction from point clouds and of meshfree methods for differential equations.

## Explanations

### L1 human

To estimate a value at a point, look at the data near that point.
Fit a simple model such as a plane by least squares, and read off the model at that point.
Do this afresh at every point, always giving more weight to nearby data.
Because the weights change gradually from point to point, the estimates fit together into a smooth surface.
If the model is just a constant, the fit is a weighted average of the data, as in [[inverse distance weighting|QHN67MSH8S]].
The [[definition|9HWTPQHHZK]] gives the formula.
