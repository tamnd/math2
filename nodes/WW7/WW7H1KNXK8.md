---
tag: WW7H1KNXK8
kind: concept
name: Jack function
msc: ["05E05", 33C52]
specializes: [PAJEHWXW6M]
sources:
  - url: https://en.wikipedia.org/wiki/Jack_function
same_as:
  wikidata: Q6115970
  wikipedia: Jack function
---

## Summary

Jack functions $J_\lambda^{(\alpha)}$ are [[symmetric functions|PAJEHWXW6M]] indexed by an [[integer partition|0JV30XN73Z]] $\lambda$ and depending on a parameter $\alpha$.
They are fixed by being triangular with respect to the monomial basis and orthogonal for a deformation of the Hall inner product.
For $\alpha = 1$ they are multiples of the [[Schur polynomials|43VFMJCDYJ]], and for $\alpha = 2$ they are the zonal polynomials of multivariate statistics.
They are the limit $q = t^\alpha$, $t \to 1$ of the [[Macdonald polynomials|VYP9PB000X]], and they are eigenfunctions of the Calogero–Sutherland model of quantum particles on a circle.

## Explanations

### L1 human

Schur polynomials are a very good basis of the symmetric polynomials, because they are orthogonal and have a meaning in representation theory.
Jack functions keep the orthogonality but add a dial $\alpha$ that changes the inner product.
As $\alpha$ moves, the basis moves from the elementary symmetric functions ($\alpha = 0$) through the Schur functions ($\alpha = 1$) to the monomial symmetric functions ($\alpha \to \infty$).
For example, in degree $2$ the monic Jack function is $m_{(2)} + \frac{2}{1 + \alpha} m_{(1,1)}$, which equals $s_{(2)} = m_{(2)} + m_{(1,1)}$ at $\alpha = 1$.
