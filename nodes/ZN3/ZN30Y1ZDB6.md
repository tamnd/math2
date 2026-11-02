---
tag: ZN30Y1ZDB6
kind: concept
name: Discrete Laplace operator
msc: [39A12, 39A14, 05C50]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_Laplace_operator
same_as:
  wikidata: Q451881
  wikipedia: Discrete Laplace operator
---

## Summary

The discrete Laplace operator is the analogue of the [[Laplacian|0E0B6RA8K0]] for functions on a grid or on the vertices of a graph.
At each point it adds up the differences between the values at the neighbours and the value at the point.
On the grid $h\Z^d$ it gives the standard finite difference approximation of $\sum_i \partial^2 u / \partial x_i^2$.
On a finite graph it is, up to sign, the [[Laplacian matrix|TN6M6DVZRP]], and it links random walks, electrical networks and discrete harmonic functions.

## Explanations

### L1 human

Ask at each point how much its value differs from the values around it.
If the point sits in a dip, its neighbours are higher, and the discrete Laplacian there is positive.
If it sits on a bump, the discrete Laplacian is negative.
On the integers, $u(m) = m^2$ gives $(m+1)^2 - 2m^2 + (m-1)^2 = 2$ at every point, just as the second derivative of $x^2$ is $2$.
