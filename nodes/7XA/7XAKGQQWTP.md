---
tag: 7XAKGQQWTP
kind: concept
name: Position operator
msc: ["81Q10", "47B25"]
sources:
  - url: https://en.wikipedia.org/wiki/Position_operator
same_as:
  wikidata: Q903835
  wikipedia: Position operator
---

## Summary

The position operator is the [[observable|DF5RN297GE]] that corresponds to the position of a particle.
On [[$L^2(\R)$|SASP14MA1Z]] it multiplies a wave function by the coordinate: $(X\psi)(x) = x\psi(x)$.
It is an [[unbounded|KRJX5RA0PW]] [[self-adjoint operator|0NEGN5CRSC]] with spectrum $\R$ and no eigenvalues.
Its spectral projections are multiplications by indicator functions, which is why $\abs{\psi}^2$ is the probability density of the position.

## Explanations

### L1 human

To ask "where is the particle?", quantum mechanics uses the operator that multiplies the wave function by $x$.
Its average value in a state is $\int x \abs{\psi(x)}^2 \, dx$, the mean position under the density $\abs{\psi}^2$.
For $\psi(x) = \pi^{-1/4} e^{-x^2/2}$ this average is $0$, by symmetry.
No wave function has an exact position, because $x\psi(x) = a\psi(x)$ for all $x$ would force $\psi = 0$ away from the single point $a$.
