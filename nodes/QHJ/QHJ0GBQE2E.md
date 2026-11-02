---
tag: QHJ0GBQE2E
kind: statement
role: theorem
name: Borsuk–Ulam theorem
msc: [55M25, 55M20]
uses: [T62369RFH6, 0VGFHTM75Y, TMFG2P912R]
about: [T62369RFH6]
sources:
  - url: https://en.wikipedia.org/wiki/Borsuk–Ulam_theorem
same_as:
  wikidata: Q848092
  wikipedia: Borsuk–Ulam theorem
---

## Statement

Let $n \ge 1$ and let $f \colon S^n \to \R^n$ be a [[continuous map|0VGFHTM75Y]] on the [[$n$-sphere|T62369RFH6]] $S^n \subset \R^{n+1}$.
Then there is a point $x \in S^n$ with $f(x) = f(-x)$.

## Remarks

An equivalent form says that there is no continuous odd map $g \colon S^n \to S^{n-1}$, that is, no map with $g(-x) = -g(x)$ for all $x$.
Indeed, if $f(x) \neq f(-x)$ for all $x$, then $g(x) = (f(x) - f(-x)) / \norm{f(x) - f(-x)}$ is such a map.
One proof uses the fact that an odd map $S^{n-1} \to S^{n-1}$ has odd [[degree|TMFG2P912R]].
The restriction of an odd map $S^n \to S^{n-1}$ to the equator is an odd map that extends over a hemisphere.
So it is null-homotopic and has degree $0$, a contradiction.

Example: for $n = 1$, let $h(x) = f(x) - f(-x)$ on the circle.
Then $h(-x) = -h(x)$, so $h$ takes values of both signs or vanishes, and by the intermediate value theorem it has a zero.

Example of use: at any moment there are two antipodal points on the Earth with the same temperature and the same air pressure, if both are continuous functions on $S^2$.
The theorem fails for maps $S^n \to \R^{n+1}$: the inclusion $S^n \subset \R^{n+1}$ takes different values at $x$ and $-x$.

## Explanations

### L1 human

If you squash a sphere flat into a space of one dimension less, two opposite points of the sphere always land on the same spot.
For a balloon pressed flat onto a table, some pair of opposite points ends up one on top of the other.

### L2 human

The theorem is the starting point of the use of topology in combinatorics and geometry.
It implies the ham sandwich theorem, the Lusternik–Schnirelmann covering theorem, and Lovász's computation of the chromatic number of Kneser graphs.
Its combinatorial counterpart is [[Tucker's lemma|PADZ7D9KBT]], from which it can also be proved.
