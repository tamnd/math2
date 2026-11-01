---
tag: PHA1S6GQGV
kind: definition
name: Motzkin number
msc: [05A15, 11B83]
defines: PB0DSH9XCG
uses: [040WY0TT2G]
sources:
  - url: https://en.wikipedia.org/wiki/Motzkin_number
---

## Definition

Let $n \ge 0$ be an integer.
A *Motzkin path* of length $n$ is a [[lattice path|040WY0TT2G]] $(p_0, p_1, \ldots, p_n)$ in $\Z^2$ with these properties:

1. $p_0 = (0, 0)$ and $p_n = (n, 0)$;
2. each step $p_i - p_{i-1}$ is one of $U = (1, 1)$, $D = (1, -1)$ and $H = (1, 0)$;
3. each point $p_i$ has second coordinate at least $0$.

The *Motzkin number* $M_n$ is the number of Motzkin paths of length $n$.

## Remarks

Example: the Motzkin paths of length $3$ are $HHH$, $UDH$, $HUD$ and $UHD$, so $M_3 = 4$.
Non-example: the path $HDU$ ends at $(3, 0)$ but fails clause 3, because after two steps it is at height $-1$.

The first values are $M_0, \ldots, M_7 = 1, 1, 2, 4, 9, 21, 51, 127$.
Splitting a path at its first step gives the recurrence
$$M_{n+1} = M_n + \sum_{k=0}^{n-1} M_k M_{n-1-k}.$$
The [[generating function|0PHAC833JF]] $M(z) = \sum_n M_n z^n$ satisfies $M = 1 + z M + z^2 M^2$, hence
$$M(z) = \frac{1 - z - \sqrt{1 - 2z - 3z^2}}{2 z^2}.$$
Choosing the positions of the $H$ steps gives $M_n = \sum_{k} \binom{n}{2k} C_k$, where $C_k$ is the [[Catalan number|0YWZJEABB2]].
The Motzkin paths without $H$ steps are the [[Dyck words|0YTJ3RN3GE]].
