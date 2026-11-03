---
tag: QG78SX3DK1
kind: definition
name: AC0
msc: [68Q15, 68Q06]
defines: N1G9S8QC68
uses: [SQXNFGVADX, 5MFZ4VNY6D]
sources:
  - url: https://en.wikipedia.org/wiki/AC0
---

## Definition

A language $L \subseteq \set{0,1}^*$ is in $\mathrm{AC}^0$ if there are a polynomial $p$, an integer $d \ge 1$ and [[Boolean circuits|SQXNFGVADX]] $C_n$ such that, for all $n$:

1. $C_n$ has $n$ inputs, and its gates are NOT gates and AND and OR gates of any fan-in;
2. $C_n$ has at most $p(n)$ gates;
3. every path from an input to the output of $C_n$ passes through at most $d$ gates;
4. for every $x \in \set{0,1}^n$, $C_n(x) = 1$ if and only if $x \in L$.

## Remarks

Example: addition is in $\mathrm{AC}^0$, in the sense that each output bit of the sum of two $n$-bit numbers $a$ and $b$ is computed by such circuits.
The carry into position $i$ is
$$c_i = \bigvee_{j < i} \Big( a_j \wedge b_j \wedge \bigwedge_{j < k < i} (a_k \vee b_k) \Big),$$
which has constant depth and $O(n^2)$ gates, and the sum bit $a_i \oplus b_i \oplus c_i$ adds a constant number of layers.

Non-example: the parity language $\set{x : x \text{ has an odd number of ones}}$ has circuits of depth $O(\log n)$ and size $O(n)$ with fan-in $2$.
But no choice of $p$ and $d$ satisfies clauses 2 and 3 together for it, by the theorem [[parity not in AC0|W6T7X0QCFH]].

The definition above is non-uniform.
Uniform versions ask in addition that $C_n$ be computable from $n$ by a weak machine, such as a logarithmic-time machine; the lower bound for parity holds for both.
