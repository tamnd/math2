---
tag: QJSPWM9F9P
kind: statement
role: theorem
name: Gysin sequence
msc: [55R25, 55R40]
uses: [BJX6QS0ANT, JX47MS1R1H, 6N7BC70CX0, JB7ZBFBA9C, N685RXHDZX, 3VQ2V5HH3R]
about: [3VQ2V5HH3R, BJX6QS0ANT]
sources:
  - url: https://en.wikipedia.org/wiki/Gysin_homomorphism
---

## Statement

Let $\pi \colon E \to B$ be an oriented real vector bundle of rank $n \ge 1$, let $E_0$ be the complement of its zero section, and let $\pi_0 = \pi|_{E_0} \colon E_0 \to B$.
Let $e \in H^n(B; \Z)$ be its [[Euler class|BJX6QS0ANT]].
Then there is a long [[exact sequence|JB7ZBFBA9C]] in integral [[singular cohomology|6N7BC70CX0]]
$$\cdots \to H^i(B) \xrightarrow{\ \smile e\ } H^{i+n}(B) \xrightarrow{\ \pi_0^*\ } H^{i+n}(E_0) \to H^{i+1}(B) \xrightarrow{\ \smile e\ } H^{i+n+1}(B) \to \cdots,$$
where $\smile e$ is the [[cup product|JX47MS1R1H]] with $e$.

## Remarks

The space $E_0$ deformation retracts onto the unit [[sphere bundle|3VQ2V5HH3R]] $S(E)$ of any metric on $E$, so the sequence is often written with $S(E)$, a bundle with fibre $S^{n-1}$.
The proof writes the long exact sequence of the pair $(E, E_0)$, replaces $H^\bullet(E)$ by $H^\bullet(B)$ since $E$ deformation retracts onto $B$, and replaces $H^{\bullet}(E, E_0)$ by $H^{\bullet - n}(B)$ with the [[Thom isomorphism|N685RXHDZX]].
The composite $H^{i}(B) \to H^{i+n}(E, E_0) \to H^{i+n}(E) \cong H^{i+n}(B)$ is then the cup product with $e$.
With $\Z/2$ coefficients the sequence holds without the orientation hypothesis, with the top Stiefel–Whitney class in place of $e$.

Example: the tautological complex line bundle over complex projective space $\C P^m$ has rank $2$ as a real bundle, and its unit sphere bundle is the Hopf map $S^{2m+1} \to \C P^m$.
Since $H^j(S^{2m+1}) = 0$ for $0 < j < 2m+1$, the sequence shows that $\smile e \colon H^i(\C P^m) \to H^{i+2}(\C P^m)$ is an isomorphism for $0 \le i \le 2m - 2$.
With $H^0(\C P^m) = \Z$, this gives $H^\bullet(\C P^m; \Z) \cong \Z[e]/(e^{m+1})$.

## Explanations

### L1 human

A sphere bundle is a space made of spheres, one over each point of a base space.
The Gysin sequence computes the cohomology of the total space from the cohomology of the base and one class, the Euler class, which measures how twisted the bundle is.
If the bundle is a product, the Euler class is zero and the sequence splits into short pieces.

### L2 human

The Gysin sequence is the special case of the Serre spectral sequence for a sphere bundle, where only two rows are nonzero.
It is a standard way to compute cohomology rings of projective spaces, of unit tangent bundles and of lens spaces.
It also shows that an oriented bundle with a nowhere zero section has Euler class zero, because then $\pi_0^*$ is injective in the relevant degree.
