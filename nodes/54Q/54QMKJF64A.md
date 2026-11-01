---
tag: 54QMKJF64A
kind: statement
role: theorem
name: Monodromy theorem
msc: ["30B40"]
uses: [0M3YQJ81NB, 0JDE56HWQ8, 075C629XTH, 0DG0Z72CQD, 0X2FY491PF]
about: [0M3YQJ81NB]
sources:
  - url: https://en.wikipedia.org/wiki/Monodromy_theorem
same_as:
  wikidata: Q4455046
  wikipedia: Monodromy theorem
---

## Statement

Let $D \subseteq \C$ be an open set, let $a, b \in D$, and let $f$ be a [[holomorphic function|0DG0Z72CQD]] on a disc around $a$.
Let $\gamma_0$ and $\gamma_1$ be [[paths|0JDE56HWQ8]] in $D$ from $a$ to $b$.
Let $H \colon [0, 1] \times [0, 1] \to D$ be a homotopy from $\gamma_0$ to $\gamma_1$ with fixed end points, and write $\gamma_s = H(s, \cdot)$.
Assume that $f$ has an [[analytic continuation|0M3YQJ81NB]] along every path $\gamma_s$, $0 \le s \le 1$.
Then the continuations of $f$ along $\gamma_0$ and along $\gamma_1$ agree near $b$.

## Remarks

The idea of the proof is that the continuation along $\gamma_s$ depends continuously on $s$.
For $s'$ close to $s$, the two paths stay close, and the continuations along them use overlapping discs, so they give the same germ at $b$.
Compactness of $[0, 1]$ then passes from $s = 0$ to $s = 1$.
An important consequence concerns a [[simply connected domain|075C629XTH]] $D$.
If $f$ can be continued along every path in $D$ that starts at $a$, then there is a holomorphic function $F$ on $D$ that equals $f$ near $a$.
The homotopy hypothesis is needed.
On $D = \C \setminus \set{0}$, a branch of the [[complex logarithm|0X2FY491PF]] near $a = 1$ continues along every path, but continuation along the unit circle returns to $1$ with the value increased by $2 \pi i$.
The unit circle is not homotopic to a constant path in $D$, so there is no contradiction.

## Explanations

### L1 human

Analytic continuation extends a function step by step along a path.
In general, two paths to the same point can give two different values, as for the logarithm going around $0$.
The monodromy theorem says this cannot happen when one path can be deformed into the other without leaving the region where continuation works.
So on a region without holes, continuation produces a single-valued function.

### L2 human

The theorem is the standard way to construct functions on simply connected domains, such as logarithms and square roots of zero-free holomorphic functions.
It is the analytic form of a topological fact: a covering space over a simply connected space is trivial.
Seen in this way, the continuations of a germ form a Riemann surface spread over the plane.
The theorem says that this surface has only one sheet over a simply connected region.
The monodromy group measures the failure over regions that are not simply connected.
