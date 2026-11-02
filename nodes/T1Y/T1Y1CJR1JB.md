---
tag: T1Y1CJR1JB
kind: concept
name: Spectral element method
msc: [65N35, 65N30, 65M70]
specializes: [98GZ9DVHTA]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_element_method
same_as:
  wikidata: Q7575186
  wikipedia: Spectral element method
---

## Summary

The spectral element method is a [[finite element method|98GZ9DVHTA]] that uses high-degree polynomials on a few large elements.
Its nodes and quadrature come from a [[spectral method|MYV657YRDW]].
On each element, usually a quadrilateral or hexahedron, the basis consists of [[Lagrange polynomials|Y7KSGE97GK]] at the Gauss–Lobatto–Legendre points.
It combines the geometric flexibility of finite elements with the fast convergence of spectral methods for smooth solutions.
It was introduced by Anthony Patera for fluid dynamics, and is widely used in seismology and in simulations of turbulent flow.
See the [[definition|8PQ405CKA3]].

## Explanations

### L1 human

Cut the domain into a few blocks, and on each block use a polynomial of high degree, such as degree $8$.
Neighbouring blocks agree along their common edges, so the whole approximation is continuous.
The polynomial on each block is stored by its values at special points that cluster near the block edges.
Using the same points for the integrals makes the mass matrix diagonal, which makes time stepping cheap.
