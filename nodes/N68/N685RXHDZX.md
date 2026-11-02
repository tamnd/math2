---
tag: N685RXHDZX
kind: statement
role: theorem
name: Thom isomorphism
msc: [55R25, 55R40]
uses: [6N7BC70CX0, JX47MS1R1H, 4BVWH0BN28, 0QJJAQ6ZYZ]
about: [6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/Thom_space
---

## Statement

Let $\pi \colon E \to B$ be a real [[vector bundle|P4DZM975BV]] of rank $n$ over a topological space $B$.
Assume it is oriented: each fibre $F_b = \pi^{-1}(b)$ has an [[orientation|0QJJAQ6ZYZ]], given locally by trivializations.
Let $E_0 \subseteq E$ be the complement of the zero section, and $F_{b,0} = F_b \setminus \set{0}$.
Then, in [[singular cohomology|6N7BC70CX0]] with integer coefficients:

1. $H^i(E, E_0) = 0$ for $i < n$.
2. There is a unique class $u \in H^n(E, E_0)$, the *Thom class*, whose restriction to $H^n(F_b, F_{b,0}) \cong \Z$ is the generator given by the orientation of $F_b$, for every $b \in B$.
3. For every $k$, the map $H^k(B) \to H^{k+n}(E, E_0)$, $x \mapsto \pi^*(x) \smile u$, is an isomorphism.

## Remarks

The relative group $H^{k+n}(E, E_0)$ is the cohomology analogue of a [[relative homology|4BVWH0BN28]] group, and $\smile$ is the relative [[cup product|JX47MS1R1H]].
The proof treats a trivial bundle $B \times \R^n$ first, where the result is the Künneth formula with $H^\bullet(\R^n, \R^n \setminus \set{0})$, which is $\Z$ in degree $n$ only.
It then glues local pieces by Mayer–Vietoris arguments and passes to general $B$ by a limit argument.
Without an orientation, the same statement holds with $\Z/2$ coefficients.
For paracompact $B$ one may choose a metric, and then $H^\bullet(E, E_0)$ is the reduced cohomology of the Thom space of the bundle.

Example: for the trivial bundle $B \times \R^n$, $u$ is the pullback of the generator of $H^n(\R^n, \R^n \setminus \set{0})$, and the isomorphism is $H^k(B) \cong H^{k+n}(B \times (\R^n, \R^n \setminus \set{0}))$.

## Explanations

### L1 human

A vector bundle attaches a copy of $\R^n$ to each point of a base space.
Looking at the cohomology of the bundle relative to the part away from the zero section, one finds the cohomology of the base again, shifted up by $n$ degrees.
The shift is given by one special class, the Thom class, which looks like the standard orientation class on each fibre.

### L2 human

The Thom isomorphism is the source of the Euler class: pull the Thom class back along the zero section to get $e \in H^n(B)$.
It leads to the Gysin sequence of a sphere bundle and to Poincaré duality type results for normal bundles.
Thom used it to compute the cohomology of Thom spaces and from that the cobordism ring.
Versions exist for any multiplicative cohomology theory, given a suitable orientation of the bundle.
