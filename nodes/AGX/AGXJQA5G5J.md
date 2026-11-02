---
tag: AGXJQA5G5J
kind: definition
name: Pontryagin class
msc: [57R20, 55R40]
defines: DN11FKWN63
uses: [7HACJC0JE2, 6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_class
---

## Definition

Let $E \to B$ be a real vector bundle of rank $n$ over a paracompact space $B$.
Let $E \otimes \C$ be its complexification, the complex vector bundle of rank $n$ with fibers $E_b \otimes_\R \C$.
For $i \ge 0$, the $i$-th *Pontryagin class* of $E$ is
$$p_i(E) = (-1)^i c_{2i}(E \otimes \C) \in H^{4i}(B; \Z),$$
where $c_{2i}$ is the $2i$-th [[Chern class|PAD37GKDPD]].
The total Pontryagin class is $p(E) = 1 + p_1(E) + p_2(E) + \cdots$.

## Remarks

The odd Chern classes of $E \otimes \C$ satisfy $2 c_{2i+1}(E \otimes \C) = 0$, because $E \otimes \C$ is isomorphic to its complex conjugate; this is why only the even ones are used.
Pontryagin classes are natural, so they are [[characteristic classes|7HACJC0JE2]], and $p_i(E) = 0$ for $4i > 2n$, that is, for $i > n/2$.
The Whitney sum formula holds modulo $2$-torsion: $2\bigl(p(E \oplus E') - p(E)\, p(E')\bigr) = 0$.

Example: for the complex projective space $\C P^m$ with generator $a \in H^2(\C P^m; \Z)$, the tangent bundle has $p(T\C P^m) = (1 + a^2)^{m+1}$.
For $m = 2$ this gives $p_1(T\C P^2) = 3a^2$.

Non-example: Pontryagin classes do not detect every nontrivial bundle.
The Möbius line bundle over $S^1$ is not trivial, but $p_1$ lies in $H^4(S^1; \Z) = 0$, so all its Pontryagin classes beyond $p_0$ vanish.

For a smooth manifold $M$, $p_i(M) = p_i(TM)$.
