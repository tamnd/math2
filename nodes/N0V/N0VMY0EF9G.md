---
tag: N0VMY0EF9G
kind: example
name: n-vector model
msc: [82B20, 82B27]
instance_of: [PAEME5EQRM]
uses: [00C0BR7D7H, GYNMZ9201M]
sources:
  - url: https://en.wikipedia.org/wiki/N-vector_model
same_as:
  wikidata: Q1959618
  wikipedia: N-vector model
---

## Example

Let $n \ge 1$ be an integer, let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]], let $J > 0$ and let $\beta \ge 0$ be the inverse temperature.
A configuration assigns to each vertex $x$ a unit vector $s_x$ of $\R^n$, that is, a point of the sphere $S^{n-1}$.
Its energy is
$$H(s) = -J \sum_{\set{x, y} \in E} s_x \cdot s_y.$$
The *$n$-vector model* on $G$ is the probability measure on $(S^{n-1})^V$ with density $e^{-\beta H(s)} / Z$ with respect to the product of the uniform measures.
Here $Z$ is the normalizing constant.

## Remarks

For $n = 1$ the sphere $S^0$ is $\set{-1, +1}$ and the model is the [[Ising model|R0KGM32QN6]] without field.
For $n = 2$ it is the [[XY model|J53AT590R9]] and for $n = 3$ the [[classical Heisenberg model|B9N542W1CN]].
The energy is invariant under the orthogonal group $O(n)$ acting on all spins at once, so physicists also call it the $O(n)$ model.
H. Eugene Stanley introduced the family in 1968 to study how critical behaviour depends on $n$.
In the limit $n \to \infty$ its free energy approaches that of the [[spherical model|SXE93C9RHC]].

## Explanations

### L1 human

This is one model with a dial $n$.
At each site sits an arrow of length one in $n$-dimensional space, and neighbouring arrows like to align.
Turning the dial gives the Ising model, the XY model and the Heisenberg model as special cases, so they can be studied together.
