---
tag: FFH90QRFFJ
kind: definition
name: Cellular homology
msc: [55N10, 55U15]
defines: W4DG4WCQ5W
uses: [5W95QFHXPR, 4BVWH0BN28, M0Q5CFJ7ZH, TMFG2P912R, 1DDYB6VVSR]
sources:
  - url: https://en.wikipedia.org/wiki/Cellular_homology
---

## Definition

Let $X$ be a [[CW complex|5W95QFHXPR]] with $n$-skeleton $X^n$ for $n \ge 0$, and put $X^{-1} = \emptyset$.
The *cellular chain group* in degree $n$ is the [[relative homology|4BVWH0BN28]] group $C_n^{\mathrm{CW}}(X) = H_n(X^n, X^{n-1})$, taken in [[singular homology|M0Q5CFJ7ZH]] with integer coefficients.
Let $\partial$ be the connecting map of the pair $(X^n, X^{n-1})$, and let $j$ be induced by the inclusion of pairs.
The *cellular boundary map* $d_n \colon C_n^{\mathrm{CW}}(X) \to C_{n-1}^{\mathrm{CW}}(X)$ is the composite
$$H_n(X^n, X^{n-1}) \xrightarrow{\ \partial\ } H_{n-1}(X^{n-1}) \xrightarrow{\ j\ } H_{n-1}(X^{n-1}, X^{n-2}).$$
Then $d_{n-1} \circ d_n = 0$, so these groups and maps form a chain complex.
The *cellular homology* $H_n^{\mathrm{CW}}(X)$ is the homology of this chain complex in degree $n$.

## Remarks

The group $H_n(X^n, X^{n-1})$ is free abelian with one generator $e_\alpha$ for each $n$-cell $e_\alpha$ of $X$.
In this basis, $d_n(e_\alpha) = \sum_\beta d_{\alpha\beta} e_\beta$, where $d_{\alpha\beta}$ is the [[degree|TMFG2P912R]] of the map $S^{n-1} \to X^{n-1} \to S^{n-1}$ given by the attaching map of $e_\alpha$ followed by the collapse of everything outside $e_\beta$.
The basic theorem is that $H_n^{\mathrm{CW}}(X) \cong H_n(X)$ for all $n$.

Example: the [[real projective plane|1DDYB6VVSR]] $\R P^2$ has one cell in each of the dimensions $0$, $1$, $2$.
The $2$-cell is attached by a map of degree $2$ onto the $1$-skeleton $S^1$, so $d_2 = 2$, and $d_1 = 0$ because the $1$-cell is a loop.
The cellular chain complex is $\Z \xrightarrow{2} \Z \xrightarrow{0} \Z$, which gives $H_0 = \Z$, $H_1 = \Z/2$ and $H_2 = 0$.

Non-example: the definition needs a CW structure, that is, a filtration by skeleta in which each $X^n$ comes from $X^{n-1}$ by attaching $n$-cells.
For an arbitrary increasing chain of subspaces, the groups $H_n(X^n, X^{n-1})$ need not vanish outside degree $n$, and the homology of the resulting complex need not be the homology of $X$.
