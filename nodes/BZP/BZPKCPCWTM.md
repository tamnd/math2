---
tag: BZPKCPCWTM
kind: statement
role: theorem
name: Larson–Sweedler theorem
msc: [16T05]
uses: [7XFYP0N84H, RJA5026RGX, 8EVP1K2CZH, N8X7XJBKT0]
about: [7XFYP0N84H, RJA5026RGX]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_algebra
---

## Statement

Let $K$ be a field and let $H$ be a finite-dimensional [[Hopf algebra|7XFYP0N84H]] over $K$.
Then:

1. The space of left [[integrals|RJA5026RGX]] in $H$ is one-dimensional over $K$.
2. $H$ is a [[Frobenius algebra|8EVP1K2CZH]].

## Remarks

The proof applies the fundamental theorem of [[Hopf modules|N8X7XJBKT0]] to the dual space $H^*$, which is a Hopf module over $H$.
This gives an isomorphism $H^* \cong (H^*)^{\mathrm{co}H} \otimes H$, and the coinvariants of $H^*$ are the left integrals on $H$.
Comparing dimensions shows that this space is one-dimensional, and the isomorphism $H^* \cong H$ of $H$-modules is the Frobenius property; applying this to $H^*$ gives the statement about integrals in $H$.
Example: for a finite group $G$, the left integrals in $KG$ are the multiples of $\sum_{g \in G} g$.
Indeed, if $\Lambda = \sum_g a_g g$ satisfies $h \Lambda = \Lambda$ for all $h \in G$, then all $a_g$ are equal.
Without finite dimension the conclusion fails: in $K[x]$ with $x$ primitive the only integral is $0$.
The same work shows that the antipode of a finite-dimensional Hopf algebra is bijective.

## Explanations

### L1 human

An integral is a Hopf algebra version of the sum of all elements of a finite group.
The theorem says that, in a finite-dimensional Hopf algebra, such an element always exists and is unique up to a scalar.
It also says that the algebra is Frobenius, a strong symmetry property: as a module over itself it looks like its own dual.

### L2 human

The theorem is the starting point for the structure theory of finite-dimensional Hopf algebras.
Together with it, Larson and Sweedler proved the Hopf algebra form of Maschke's theorem: $H$ is semisimple if and only if $\varepsilon(\Lambda) \ne 0$ for a nonzero left integral $\Lambda$.
For $H = KG$ this gives $\varepsilon(\sum_g g) = \abs{G}$, and so recovers the classical condition that the characteristic of $K$ does not divide $\abs{G}$.
Integrals also define the distinguished group-like elements of $H$ and $H^*$, which appear in Radford's formula for $S^4$.
