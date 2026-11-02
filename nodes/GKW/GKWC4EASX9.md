---
tag: GKWC4EASX9
kind: definition
name: Stiefel–Whitney class
msc: [57R20, 55R40]
defines: JQCK7A210W
uses: [7HACJC0JE2, BE9NJRVDR3, 6N7BC70CX0, JX47MS1R1H]
sources:
  - url: https://en.wikipedia.org/wiki/Stiefel%E2%80%93Whitney_class
---

## Definition

Consider real vector bundles $E \to B$ over paracompact spaces $B$.
The *Stiefel–Whitney classes* are the [[characteristic classes|7HACJC0JE2]] $w_i(E) \in H^i(B; \Z/2\Z)$, $i \ge 0$, in [[singular cohomology|6N7BC70CX0]], that satisfy the following axioms.
Write $w(E) = w_0(E) + w_1(E) + w_2(E) + \cdots$ for the total class.

1. $w_0(E) = 1$, and $w_i(E) = 0$ for $i$ greater than the rank of $E$.
2. Naturality: $w_i(f^* E) = f^* w_i(E)$ for every continuous map $f \colon B' \to B$, and isomorphic bundles have equal classes.
3. Whitney product formula: $w(E \oplus E') = w(E) \smile w(E')$ for the [[Whitney sum|BE9NJRVDR3]] of two bundles over the same base, where $\smile$ is the [[cup product|JX47MS1R1H]].
4. Normalization: for the tautological line bundle $\gamma^1_1$ over $\R P^1$, $w_1(\gamma^1_1)$ is the generator of $H^1(\R P^1; \Z/2\Z) \cong \Z/2\Z$.

There is exactly one family of classes with these properties.

## Remarks

Example: a trivial bundle $B \times \R^n$ is pulled back from a point, so by axiom 2 its total class is $w = 1$.
For the tangent bundle of $\R P^n$, one has $w(T\R P^n) = (1 + a)^{n+1}$, where $a$ generates $H^1(\R P^n; \Z/2\Z)$; for $n = 2$ this gives $w = 1 + a + a^2$.

Non-example: the rule $w(E) = 1$ for every bundle satisfies axioms 1 to 3 but fails axiom 4.

A bundle $E$ is orientable exactly when $w_1(E) = 0$.
An orientable bundle admits a spin structure exactly when also $w_2(E) = 0$.
For a smooth manifold $M$, one writes $w_i(M) = w_i(TM)$.
