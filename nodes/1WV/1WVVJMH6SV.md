---
tag: 1WVVJMH6SV
kind: definition
name: Needleman–Wunsch algorithm
msc: [92D20, 68W32, 90C39]
defines: PDVT0XX76A
uses: [G42Y4TPD4N, Q7MXCRQR8X, R3FXF08WBH]
sources:
  - url: https://en.wikipedia.org/wiki/Needleman–Wunsch_algorithm
---

## Definition

Let $a = a_1 \cdots a_m$ and $b = b_1 \cdots b_n$ be strings over an alphabet $\Sigma$.
Let $\sigma \colon \Sigma \times \Sigma \to \R$ be a [[substitution matrix|Q7MXCRQR8X]], and let $g \in \R$ be the score of a letter aligned with a gap.
The *Needleman–Wunsch algorithm* computes the numbers $F(i, j)$, for $0 \le i \le m$ and $0 \le j \le n$, by
$$F(i, 0) = i g, \qquad F(0, j) = j g,$$
$$F(i, j) = \max\bigl( F(i-1, j-1) + \sigma(a_i, b_j),\ F(i-1, j) + g,\ F(i, j-1) + g \bigr) \quad (i, j \ge 1).$$
It returns $F(m, n)$.
An alignment is recovered by a traceback from $(m, n)$ to $(0, 0)$ that at each step moves to a cell attaining the maximum.

## Remarks

By induction on $i + j$, $F(i, j)$ is the maximum score of a global [[alignment|G42Y4TPD4N]] of $a_1 \cdots a_i$ with $b_1 \cdots b_j$, so $F(m, n)$ is the optimal global score.
The table has $(m+1)(n+1)$ cells, each filled in constant time, so time and space are $O(mn)$.
Example: $a = AT$, $b = T$, match $+1$, mismatch $-1$, $g = -1$.
Then $F(1, 1) = \max(0 - 1, -1 - 1, -1 - 1) = -1$ and $F(2, 1) = \max(F(1, 0) + 1, F(1, 1) - 1, F(2, 0) - 1) = \max(0, -2, -3) = 0$.
The traceback gives the alignment $AT$ over ${-}T$ with score $0$.
Affine gap scores, where opening a gap costs more than extending it, need three tables instead of one; this variant is due to Gotoh.
