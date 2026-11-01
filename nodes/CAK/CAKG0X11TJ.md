---
tag: CAKG0X11TJ
kind: definition
name: Irreducible ideal
msc: ["13A15"]
defines: 7PDWB550C9
uses: [0GYGHKX834, 0MYSA6MYNA]
sources:
  - url: https://en.wikipedia.org/wiki/Irreducible_ideal
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]].
An [[ideal|0MYSA6MYNA]] $I$ of $R$ is *irreducible* if these two conditions hold:

1. $I \ne R$.
2. For all ideals $J$ and $K$ of $R$ with $I = J \cap K$, one has $I = J$ or $I = K$.

## Remarks

Example: every prime ideal $P$ is irreducible; if $P = J \cap K$ with $a \in J \setminus P$ and $b \in K \setminus P$, then $ab \in J \cap K = P$, a contradiction.
Non-example: $(6)$ in $\Z$ fails clause 2, since $(6) = (2) \cap (3)$ with both terms strictly larger.
In a Noetherian ring, every irreducible ideal is [[primary|V026AAV8E6]].
The converse fails: in $k[x, y]$ over a field $k$, the ideal $(x^2, xy, y^2)$ is primary, but it equals $(x^2, y) \cap (x, y^2)$.
Some authors call an ideal with clause 2 alone meet-irreducible, and then allow $I = R$.

## Explanations

### L1 human

An irreducible ideal is a proper ideal that is not the intersection of two strictly larger ideals.
