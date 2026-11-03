---
tag: 6E0DCB1NF1
kind: statement
role: theorem
name: Bloch–Lichtenbaum spectral sequence
msc: ["19E15", 19D45, 14C25]
uses: [V1BB32NY3G, 04C5ZBG1WT, GG8AYV847V, 5GVFZWMWC8]
about: [V1BB32NY3G, 5GVFZWMWC8]
sources:
  - url: https://en.wikipedia.org/wiki/Motivic_cohomology
---

## Statement

Let $F$ be a [[field|04C5ZBG1WT]].
Write $CH^j(F, m)$ for the higher Chow groups of $\operatorname{Spec} F$, so that $CH^j(F, m) = H^{2j - m}(F, \Z(j))$ is [[motivic cohomology|V1BB32NY3G]].
Write $K_n(F)$ for the [[algebraic K-groups|5GVFZWMWC8]] of $F$.
Then there is a strongly convergent [[spectral sequence|GG8AYV847V]]
$$E_2^{p, q} = CH^{-q}(F, -p - q) \Longrightarrow K_{-p-q}(F).$$

## Remarks

Bloch and Lichtenbaum built it from a tower of spectra made of K-theory of the algebraic simplices with supports on cycles in good position.
For a field, $CH^j(F, m) = 0$ when $j > m$, so the nonzero terms satisfy $p \le 0$ and $q \le 0$.
The term $E_2^{0, -n} = CH^n(F, n) \cong K^M_n(F)$ gives the edge map from Milnor K-theory to Quillen K-theory.
Example: in total degree $1$, the only nonzero term is $E_2^{0,-1} = CH^1(F, 1) \cong F^\times$, and the spectral sequence recovers $K_1(F) \cong F^\times$.
Rationally the spectral sequence degenerates at $E_2$.

## Explanations

### L1 human

For a field, the K-groups are glued together from higher Chow groups, which are built from algebraic cycles on simplices.
The spectral sequence makes this precise.
In low degrees it gives back the familiar facts that $K_0(F) = \Z$ and $K_1(F) = F^\times$.

### L2 human

This was the first motivic spectral sequence, and it was later extended from fields to all smooth varieties.
It is the analogue for fields of the Atiyah–Hirzebruch spectral sequence in topology.
Together with the comparison of motivic and étale cohomology, it is a route from the Bloch–Kato conjecture to the Quillen–Lichtenbaum conjecture.
