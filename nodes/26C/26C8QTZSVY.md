---
tag: 26C8QTZSVY
kind: definition
name: Low-discrepancy sequence
msc: [11K38, 11K36, 65C05]
defines: XSPX1KW9AQ
uses: [XM6DH57BWY, 0TGV80E6A4]
sources:
  - url: https://en.wikipedia.org/wiki/Low-discrepancy_sequence
---

## Definition

Let $s \ge 1$ be an integer, and let $x_1, x_2, \ldots$ be a sequence of points of $[0, 1)^s$.
For $t = (t_1, \ldots, t_s) \in [0, 1]^s$ let $A_N(t)$ be the number of indices $i \le N$ with $x_i \in [0, t_1) \times \cdots \times [0, t_s)$.
The *star discrepancy* of the first $N$ points is
$$D_N^* = \sup_{t \in [0, 1]^s} \left| \frac{A_N(t)}{N} - t_1 t_2 \cdots t_s \right|.$$
The sequence is a *low-discrepancy sequence* if some constant $c$, independent of $N$, satisfies
$$D_N^* \le c\, \frac{(\log N)^s}{N} \qquad \text{for all } N \ge 2.$$

## Remarks

Example: the van der Corput sequence in base $2$, with $s = 1$, is $x_i = \sum_k a_k 2^{-k-1}$ when $i = \sum_k a_k 2^k$ in binary; its first terms are $\frac12, \frac14, \frac34, \frac18$.
It satisfies $D_N^* = O(\log N / N)$ in [[big O notation|0TGV80E6A4]], so it is a low-discrepancy sequence.
Non-example: the constant sequence $x_i = 0$ has $A_N(t) = N$ for every $t$ with all $t_j > 0$, so $D_N^* = 1$ for all $N$, and the bound fails.
A sequence has $D_N^* \to 0$ if and only if it is uniformly distributed in $[0, 1)^s$; for $s = 1$ this is [[equidistribution modulo one|XM6DH57BWY]].
So every low-discrepancy sequence is uniformly distributed, but the converse fails.
For independent uniform random points, $D_N^*$ is typically of order $N^{-1/2}$ up to logarithmic factors, much larger than $(\log N)^s / N$ for large $N$.
Some authors require the bound only for $N$ large, or use the extreme discrepancy over all boxes, not only those anchored at $0$; this changes only the constant.
