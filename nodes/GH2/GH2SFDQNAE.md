---
tag: GH2SFDQNAE
kind: definition
name: Digital topology
msc: [68U03, 68U10]
defines: 456E0RCQR1
uses: [00C0BR7D7H, 01VVP10MWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Digital_topology
---

## Definition

Let $p = (p_1, p_2)$ and $q = (q_1, q_2)$ be distinct points of $\Z^2$.

1. $p$ and $q$ are *$4$-adjacent* if $\abs{p_1 - q_1} + \abs{p_2 - q_2} = 1$.
2. $p$ and $q$ are *$8$-adjacent* if $\max(\abs{p_1 - q_1}, \abs{p_2 - q_2}) = 1$.
3. For $k \in \set{4, 8}$, a *$k$-path* in a set $S \subseteq \Z^2$ is a finite sequence of points of $S$ in which consecutive points are $k$-adjacent.
4. $S$ is *$k$-connected* if any two points of $S$ are joined by a $k$-path in $S$; the maximal $k$-connected subsets of $S$ are its *$k$-components*.

*Digital topology* is the study of such adjacency, connectedness and separation notions on $\Z^2$ and their analogues on $\Z^n$.
For each $k$, the $k$-adjacency makes $S$ a [[graph|00C0BR7D7H]] whose [[connected components|01VVP10MWJ]] are the $k$-components of $S$.

## Remarks

Example: $S = \set{(0, 0), (1, 1)}$ is $8$-connected, since the two points are $8$-adjacent.
Non-example: the same $S$ is not $4$-connected, because $\abs{0 - 1} + \abs{0 - 1} = 2$ and $S$ has no other points.
Let $S = \set{(1, 0), (0, 1), (-1, 0), (0, -1)}$.
With $8$-adjacency for $\Z^2 \setminus S$, the point $(0, 0)$ is $8$-adjacent to $(1, 1) \in \Z^2 \setminus S$, so the complement is $8$-connected and the "curve" $S$ encloses nothing.
With $4$-adjacency for the complement, $(0, 0)$ is a $4$-component by itself, so $S$ separates it from the outside.
For this reason one pairs $8$-adjacency for a set with $4$-adjacency for its complement, or the reverse.
The Khalimsky topology on $\Z$ is a genuine topology: the sets $\set{2n + 1}$ and $\set{2n - 1, 2n, 2n + 1}$ for $n \in \Z$ form a base, and $\Z$ is connected in it.
