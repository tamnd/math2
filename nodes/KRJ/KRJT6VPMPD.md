---
tag: KRJT6VPMPD
kind: definition
name: Smith–Waterman algorithm
msc: [92D20, 68W32, 90C39]
defines: RY3XCJEN2F
uses: [G42Y4TPD4N, Q7MXCRQR8X, R3FXF08WBH]
sources:
  - url: https://en.wikipedia.org/wiki/Smith–Waterman_algorithm
---

## Definition

Let $a = a_1 \cdots a_m$ and $b = b_1 \cdots b_n$ be strings over an alphabet $\Sigma$.
Let $\sigma \colon \Sigma \times \Sigma \to \R$ be a [[substitution matrix|Q7MXCRQR8X]], and let $g < 0$ be the score of a letter aligned with a gap.
The *Smith–Waterman algorithm* computes the numbers $H(i, j)$, for $0 \le i \le m$ and $0 \le j \le n$, by
$$H(i, 0) = H(0, j) = 0,$$
$$H(i, j) = \max\bigl( 0,\ H(i-1, j-1) + \sigma(a_i, b_j),\ H(i-1, j) + g,\ H(i, j-1) + g \bigr) \quad (i, j \ge 1).$$
It returns $\max_{i, j} H(i, j)$.
A local alignment is recovered by a traceback that starts at a cell of maximal value and stops at the first cell with value $0$.

## Remarks

$H(i, j)$ is the maximum score of an alignment of a suffix of $a_1 \cdots a_i$ with a suffix of $b_1 \cdots b_j$, the empty alignment scoring $0$.
So the returned value is the optimal score of a local [[alignment|G42Y4TPD4N]], and time and space are $O(mn)$.
Example: $a = GAT$, $b = CAT$, match $+2$, mismatch $-1$, $g = -2$.
Then $H(1, 1) = \max(0, -1, -2, -2) = 0$, $H(2, 2) = H(1, 1) + 2 = 2$ and $H(3, 3) = H(2, 2) + 2 = 4$, which is the maximum; the traceback gives $AT$ over $AT$.
The method finds meaningful local alignments only when the expected score of a random pair of letters is negative.
Otherwise the best local alignment tends to extend over the whole sequences.
