---
tag: ENB0GT59ZC
kind: definition
name: Strictly singular operator
msc: [47B07, 47L20]
defines: RNX150HS1P
uses: [06GZ956657, 03TM135G0N, M2NEP1K5AE, 8HWGKWD6ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Strictly_singular_operator
---

## Definition

Let $X$ and $Y$ be [[Banach spaces|06GZ956657]], and let $T \colon X \to Y$ be a [[bounded linear map|03TM135G0N]].
The map $T$ is *strictly singular* if for every infinite-dimensional closed subspace $M$ of $X$,
$$\inf \set{\norm{Tx} : x \in M, \ \norm{x} = 1} = 0.$$
Equivalently, no restriction $T|_M$ to an infinite-dimensional closed subspace $M$ is an isomorphism onto its image.

## Remarks

Example: every [[compact operator|M2NEP1K5AE]] is strictly singular.
Indeed, suppose that $T|_M$ had a bounded inverse on $T(M)$.
Then the closed unit ball of $M$ would be the image of a relatively compact set under a bounded map, so it would be compact, and $M$ would be finite-dimensional.
For $1 \le p < q < \infty$, the inclusion $\ell^p \to \ell^q$ is strictly singular but not compact.
Non-example: the identity map of an infinite-dimensional Banach space $X$ is not strictly singular, since it is an isomorphism on $M = X$.
On Hilbert spaces, the strictly singular operators are exactly the compact operators.
For a Banach space $X$, the strictly singular operators from $X$ to $X$ form a closed two-sided ideal of the algebra of bounded operators.
If $F$ is a [[Fredholm operator|8HWGKWD6ZM]] and $S$ is strictly singular, then $F + S$ is Fredholm with the same index.
