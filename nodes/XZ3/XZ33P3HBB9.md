---
tag: XZ33P3HBB9
kind: concept
name: Radial basis function interpolation
msc: [65D12, 41A05, 41A63]
specializes: [BM703GV34G]
sources:
  - url: https://en.wikipedia.org/wiki/Radial_basis_function_interpolation
same_as:
  wikidata: Q65063433
  wikipedia: Radial basis function interpolation
---

## Summary

Radial basis function interpolation fits scattered data in $\R^d$ with a combination of translates of one [[radial basis function|ZBSXSTQM2J]].
There is one translate centred at each data point.
The coefficients solve a square linear system whose matrix collects the values of the radial function at all pairwise distances.
For many radial functions, such as the Gaussian and the inverse multiquadric, this matrix is invertible for every set of distinct points in every dimension.
This makes it one of the main methods of [[multivariate interpolation|BM703GV34G]], free of the restrictions on point position that polynomial interpolation has.

## Explanations

### L1 human

Place a bump at each data point, all of the same shape, and choose their heights so that the sum of the bumps passes through all the data values.
Finding the heights means solving a linear system with one equation per data point.
In one dimension with the function $\varphi(r) = r$, the sum of shifted copies of $\abs{x - x_j}$ is a piecewise linear function, which gives the broken line through the data.
The [[definition|NH59FNJQG1]] writes down the system.
