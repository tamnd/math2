---
tag: SYVXQQK57V
kind: statement
role: theorem
name: Lusternik–Schnirelmann theorem
msc: [55M25, 54H25]
uses: [T62369RFH6, 0WQ19TJV24]
about: [T62369RFH6]
sources:
  - url: https://en.wikipedia.org/wiki/Lusternik–Schnirelmann_theorem
same_as:
  wikidata: Q25098919
  wikipedia: Lusternik–Schnirelmann theorem
---

## Statement

Let $n \ge 0$ and let $A_1, \ldots, A_{n+1}$ be closed subsets of the [[$n$-sphere|T62369RFH6]] $S^n \subset \R^{n+1}$ with $A_1 \cup \cdots \cup A_{n+1} = S^n$.
Then some $A_i$ contains a pair of antipodal points $x$ and $-x$.

## Remarks

The theorem follows from the [[Borsuk–Ulam theorem|QHJ0GBQE2E]].
We may assume that every $A_i$ is nonempty, by replacing an empty one with a copy of a nonempty one.
Let $f(x) = (d(x, A_1), \ldots, d(x, A_n)) \in \R^n$, where $d(x, A)$ is the [[distance from $x$ to $A$|0WQ19TJV24]], and choose $x$ with $f(x) = f(-x)$.
If some coordinate of $f(x)$ is $0$, then $x$ and $-x$ both lie in the closed set $A_i$; otherwise neither lies in $A_1 \cup \cdots \cup A_n$, so both lie in $A_{n+1}$.
The same conclusion holds when all the $A_i$ are open.

Example: for $n = 1$, if the circle is the union of two closed sets, one of them contains two opposite points.

The number $n + 1$ cannot be raised to $n + 2$.
Project the facets of a regular $(n+1)$-simplex centred at the origin radially onto $S^n$.
This covers $S^n$ by $n + 2$ closed sets, none of which contains an antipodal pair.

## Explanations

### L1 human

If you paint a sphere with $n + 1$ colours, where each colour region is closed, then some colour appears at two opposite points.
On an ordinary globe, painted with three colours, some colour is used at two antipodal places.

### L2 human

The theorem is one of several equivalent forms of the Borsuk–Ulam theorem, and it can be proved from it and conversely.
It gives a short proof of Kneser's conjecture on the chromatic number of Kneser graphs.
More generally, covering and coincidence statements of this kind are a main entry point of topological methods in combinatorics.
