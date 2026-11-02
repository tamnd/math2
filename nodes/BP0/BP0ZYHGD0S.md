---
tag: BP0ZYHGD0S
kind: statement
role: theorem
name: Oka's normalization theorem
msc: [32C20, 32C35]
uses: [831N2Q4GCB, PN55VEF0J7, M2FAMD9HZN, DSJET02WPR, 0VQYCCQVJ5, GB7M582M5Y]
about: [PN55VEF0J7, M2FAMD9HZN]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_scheme
---

## Statement

Let $X$ be a [[reduced complex space|831N2Q4GCB]] and let $N \subseteq X$ be the set of points of $X$ that are not normal.
Then $N$ is a [[nowhere dense|0VQYCCQVJ5]] [[analytic subset|GB7M582M5Y]] of $X$, and there are a [[normal complex space|PN55VEF0J7]] $\tilde{X}$ and a holomorphic map $\nu \colon \tilde{X} \to X$ such that:

1. $\nu$ is finite, that is, closed with finite fibres, and surjective;
2. $\nu^{-1}(N)$ is nowhere dense in $\tilde{X}$;
3. $\nu$ restricts to a biholomorphic map $\tilde{X} \setminus \nu^{-1}(N) \to X \setminus N$.

The pair $(\tilde{X}, \nu)$ is unique up to a unique isomorphism over $X$; it is the [[normalization|M2FAMD9HZN]] of $X$.

## Remarks

The key step, due to Oka, is that the sheaf $\hat{\mathcal{O}}_X$ of weakly holomorphic functions is a [[coherent analytic sheaf|DSJET02WPR]] of $\mathcal{O}_X$-modules.
A weakly holomorphic function is one that is holomorphic on the regular points and locally bounded.
Then $\tilde{X}$ is the analytic spectrum of the finite $\mathcal{O}_X$-algebra $\hat{\mathcal{O}}_X$.

Example: for the cusp $X = \set{z_1^2 = z_2^3} \subseteq \C^2$, the map $\nu \colon \C \to X$, $t \mapsto (t^3, t^2)$, is the normalization.
It is bijective and finite, $N = \set{0}$, and off $t = 0$ its inverse $(z_1, z_2) \mapsto z_1 / z_2$ is holomorphic.
For the cross $X = \set{z_1 z_2 = 0}$, the normalization is the disjoint union of two copies of $\C$, mapped onto the two axes; here $\nu$ is not injective over $0$.

## Explanations

### L1 human

A singular space can be improved by separating sheets that cross and by opening up pinches, without changing it elsewhere.
The theorem says that this can always be done for complex spaces, and in exactly one natural way.
The result is a normal space that maps onto the original one, with finite fibres.

### L2 human

Normalization reduces many questions about reduced spaces to normal spaces, where the Riemann extension theorem and local irreducibility are available.
For curves the normalization is smooth, so it is a resolution of singularities.
It is the analytic counterpart of the normalization of an integral scheme by integral closure of its rings.
