---
tag: A2T1HDC0VN
kind: definition
name: Shannon–Fano coding
msc: [94A45, 94A29, 68P30]
defines: G0S748GZCX
uses: [GNB3T6TD0M, 0D6J4B671D, Y86E072V0V]
sources:
  - url: https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding
---

## Definition

Let $x_1, \dots, x_n$ be the symbols of a finite source, $n \ge 2$, with [[probabilities|0D6J4B671D]] $p_1 \ge p_2 \ge \dots \ge p_n > 0$.
The name *Shannon–Fano coding* covers two constructions of a binary [[prefix code|GNB3T6TD0M]] $C$.

1. *Shannon's method.* Put $\ell_i = \ceil{\log_2 (1/p_i)}$ and $F_i = \sum_{j < i} p_j$. The codeword $C(x_i)$ is the string of the first $\ell_i$ binary digits of $F_i$ after the point.
2. *Fano's method.* Split the list $x_1, \dots, x_n$ into an initial part and a final part whose total probabilities are as close as possible. Codewords of the first part begin with $0$ and those of the second part with $1$. Repeat on each part with more than one symbol, appending further digits.

## Remarks

Both methods give a prefix code.
Shannon's method has expected length $L < \mathrm{H}(p) + 1$, where $\mathrm{H}(p)$ is the [[Shannon entropy|Y86E072V0V]] in bits.
For Shannon's method, the numbers $F_j$ with $j > i$ differ from $F_i$ by at least $p_i \ge 2^{-\ell_i}$, so their first $\ell_i$ digits differ from those of $F_i$.
Example: for $p = (1/2, 1/4, 1/8, 1/8)$, Shannon's method gives $F = (0, 1/2, 3/4, 7/8)$ and lengths $1, 2, 3, 3$.
The binary expansions $0.0$, $0.10$, $0.110$, $0.111$ give the codewords $0, 10, 110, 111$.
Fano's method splits $\set{x_1} \mid \set{x_2, x_3, x_4}$ first and gives the same code.
Non-example: for $p = (0.35, 0.17, 0.17, 0.16, 0.15)$, the optimal code with lengths $1, 3, 3, 3, 3$ is not a Fano code.
Its first split, $0.35$ against $0.65$, is less balanced than the split $0.52$ against $0.48$ that Fano's method takes.
Fano's code here has expected length $2.31$, the optimal one $2.30$.
