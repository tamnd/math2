---
tag: SNQVJYWYMB
kind: conjecture
name: Kadison–Kaplansky conjecture
msc: [46L80, 20C07, 46L05]
uses: [PEMNN32A43, JKANN4VBYH, 033DA1WE8Y, DSF8C6QPAG, 14CB5N0FPW, 5FG1BKZXKS, JWJ8YPR7EB]
about: [JKANN4VBYH]
sources:
  - url: https://en.wikipedia.org/wiki/Kaplansky%27s_conjectures
history:
  posed_by: "Richard Kadison and Irving Kaplansky"
---

## Statement

Let $G$ be a [[torsion-free|PEMNN32A43]] discrete group.
Let $C^*_r(G)$ be its reduced [[group C*-algebra|JKANN4VBYH]], the norm closure of the group algebra $\C[G]$ acting on $\ell^2(G)$ by left translations.
The conjecture states that the only [[projections|033DA1WE8Y]] in $C^*_r(G)$, that is, the elements $p$ with $p = p^* = p^2$, are $0$ and $1$.

## Remarks

The hypothesis that $G$ is torsion-free is needed.
If $g \in G$ has finite order $n > 1$, then $p = \frac{1}{n}(1 + g + \cdots + g^{n-1})$ is a projection different from $0$ and $1$.

The conjecture implies the idempotent part of [[Kaplansky's conjectures|DSF8C6QPAG]] for the field $\C$.
Indeed $\C[G] \subseteq C^*_r(G)$, and every idempotent of a C*-algebra is similar to a projection.

The canonical trace $\tau$ on $C^*_r(G)$, given by $\tau(x) = \ip{x \delta_e}{\delta_e}$, is faithful, and $0 \le \tau(p) \le 1$ for every projection $p$.
So it suffices to show that $\tau(p)$ is an integer.
For torsion-free $G$, this integrality follows from surjectivity of the assembly map of the [[Baum–Connes conjecture|14CB5N0FPW]].
In this way the conjecture is known for free groups, by Pimsner and Voiculescu, for torsion-free groups with the [[Haagerup property|5FG1BKZXKS]], and for torsion-free [[hyperbolic groups|JWJ8YPR7EB]].
It is open in general.

## Explanations

### L1 human

A projection is an operator that acts like "keep this part, discard the rest", so it satisfies $p^2 = p$.
In the C*-algebra of a group, an element of finite order produces a projection by averaging over its powers.
The conjecture says that when the group has no elements of finite order, there are no projections except the trivial ones $0$ and $1$.
It is the operator-algebra form of Kaplansky's question about idempotents in group rings.
