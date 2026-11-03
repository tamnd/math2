---
tag: HN46KHEZYA
kind: definition
name: Lin–Kernighan heuristic
msc: [90C27, 90C59]
defines: 3GZCWKX4A0
uses: [XJRHJX2241, 0HF30P75G4, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Lin%E2%80%93Kernighan_heuristic
---

## Definition

Let $V$ be a finite set of at least $4$ cities with symmetric distances $c(u, v) = c(v, u) \ge 0$.
A *tour* is a [[Hamiltonian cycle|0HF30P75G4]] on $V$, and its length is the sum of $c$ over its edges.
For a tour $T$, a *Lin–Kernighan chain* is a sequence of distinct vertices $t_1, t_2, \dots, t_{2k}$ with these properties, for $i = 1, \dots, k$:

1. The edge $x_i = \set{t_{2i-1}, t_{2i}}$ belongs to $T$, and for $i < k$ the edge $y_i = \set{t_{2i}, t_{2i+1}}$ does not.
2. No $x_i$ equals any $y_j$.
3. The partial gain $G_i = \sum_{j \le i} \big( c(x_j) - c(y_j) \big)$ is positive for $i < k$.
4. Deleting $x_1, \dots, x_i$ from $T$ and adding $y_1, \dots, y_{i-1}$ and $\set{t_{2i}, t_1}$ gives a tour $T_i$.

The *Lin–Kernighan heuristic* is the following [[algorithm|9DMSG5HAQX]] for the [[travelling salesman problem|XJRHJX2241]].

1. Start with any tour $T$.
2. For a choice of $t_1$, build a chain step by step, as long as possible. At each step choose an edge $y_i$ that keeps the partial gain positive.
3. If some tour $T_i$ along the chain is shorter than $T$, replace $T$ by the shortest such $T_i$ and go back to step 2.
4. Otherwise try other choices of $t_1$, $t_2$ and $t_3$; when none gives an improvement, return $T$.

## Remarks

Writing $\ell$ for length, $\ell(T_i) = \ell(T) - \big( G_{i-1} + c(x_i) - c(t_{2i}, t_1) \big)$.
So the method searches among $i$-opt moves for all $i$ while keeping the work low, because the positive gain rule prunes most chains.
The returned tour is locally optimal for these moves, but it need not be a shortest tour.

Example: for $k = 2$, the chain removes $x_1, x_2$ and adds $y_1$ and $\set{t_4, t_1}$, a $2$-opt move.
Take four points at the corners $(0,0), (1,0), (1,1), (0,1)$ of a unit square, with the crossing tour through $(0,0), (1,1), (1,0), (0,1)$ of length $2 + 2\sqrt{2}$.
Removing the two diagonals and adding two sides gives a gain of $2\sqrt{2} - 2 > 0$ and the square tour of length $4$.

Non-example: plain $2$-opt local search uses only chains with $k = 2$, so it is not the Lin–Kernighan heuristic.
Its local optima can be longer than those of Lin–Kernighan, since deeper exchanges are not tried.

Practical versions add rules, such as candidate lists of nearby cities for $y_i$ and bounded backtracking.
