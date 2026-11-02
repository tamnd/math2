---
tag: JFP2DGMNXT
kind: statement
role: theorem
name: Jacobi triple product
msc: [11F27, 33D15, 05A30]
uses: [Y1X8ZZQ7VM, RZ0Z2BTMT4]
about: [2F5CYQJVAF, Y1X8ZZQ7VM]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_triple_product
same_as:
  wikidata: Q507393
  wikipedia: Jacobi triple product
---

## Statement

Let $q, z \in \C$ with $\abs{q} < 1$ and $z \ne 0$.
Then
$$\prod_{m=1}^{\infty} \left(1 - q^{2m}\right) \left(1 + z q^{2m-1}\right) \left(1 + z^{-1} q^{2m-1}\right) = \sum_{n=-\infty}^{\infty} q^{n^2} z^n.$$
Equivalently, with the [[q-Pochhammer symbol|Y1X8ZZQ7VM]], $(q; q)_\infty\, (z; q)_\infty\, (q/z; q)_\infty = \sum_{n \in \Z} (-1)^n q^{\binom{n}{2}} z^n$.

## Remarks

Proof idea: call the product $F(z)$; it is holomorphic on $\C \setminus \set{0}$, so it has a Laurent expansion $\sum_n c_n z^n$.
The product satisfies $F(q^2 z) = (q z)^{-1} F(z)$, which forces $c_n = q^{n^2} c_0$.
The constant $c_0 = 1$ can be found by specializing $z$, for instance with Gauss's or Euler's identities, or by a limit argument.
Example: substituting $q \mapsto q^{3/2}$ and $z \mapsto -q^{1/2}$ in the first form gives [[Euler's pentagonal number theorem|R587SR9GNV]] $(q; q)_\infty = \sum_{n \in \Z} (-1)^n q^{n(3n-1)/2}$.
With $z = 1$ the first form gives $\sum_{n \in \Z} q^{n^2} = \prod_{m \ge 1} (1 - q^{2m})(1 + q^{2m-1})^2$, a product for a [[theta function|2F5CYQJVAF]].
The condition $\abs{q} < 1$ is needed for the [[infinite product|RZ0Z2BTMT4]] and the series to converge.

## Explanations

### L1 human

The triple product identity says that a certain infinite product equals a sum of powers $q^{n^2}$, one for each integer $n$.
The sum side is a theta function, so the identity turns theta functions into products.
Products are good for counting partitions, sums are good for computing, and the identity lets one pass between them.

### L2 human

It is the basic identity behind the product formulas for the Jacobi theta functions and the [[Dedekind eta function|MX3CVYMNDV]].
It is a limiting case of [[Ramanujan's 1psi1 summation|RK6DCJVJCR]].
Together with its relative, the [[quintuple product identity|PZR6RC79ED]], it gives many partition identities, and it is a step in proofs of the [[Rogers–Ramanujan identities|M24H4GJPPW]].
In Lie theory it is the Macdonald identity for the affine root system of type $A_1^{(1)}$.
