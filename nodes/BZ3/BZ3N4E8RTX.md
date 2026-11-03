---
tag: BZ3N4E8RTX
kind: definition
name: NC
msc: [68Q15, 68Q06, 68Q10]
defines: 3QFZN6ZZNC
uses: [SQXNFGVADX, VRZ9H4EZ6V, 5MFZ4VNY6D]
sources:
  - url: https://en.wikipedia.org/wiki/NC_(complexity)
---

## Definition

Let $i \ge 1$.
Consider [[Boolean circuits|SQXNFGVADX]] with AND and OR gates of fan-in $2$ and NOT gates.
A language $L \subseteq \set{0,1}^*$ is in $\mathrm{NC}^i$ if there are a polynomial $p$, a constant $c$ and such circuits $C_n$ such that, for all $n \ge 2$:

1. $C_n$ has $n$ inputs and at most $p(n)$ gates;
2. every path from an input to the output of $C_n$ passes through at most $c (\log n)^i$ gates;
3. for every $x \in \set{0,1}^n$, $C_n(x) = 1$ if and only if $x \in L$;
4. a deterministic Turing machine computes a description of $C_n$ from $1^n$ using space $O(\log n)$.

The class *NC* is $\bigcup_{i \ge 1} \mathrm{NC}^i$.

## Remarks

Example: the parity language $\set{x : x \text{ has an odd number of ones}}$ is in $\mathrm{NC}^1$.
The exclusive or $u \oplus v = (u \wedge \neg v) \vee (\neg u \wedge v)$ uses a constant number of gates and has constant depth.
A balanced binary tree of such blocks over the $n$ inputs has $O(n)$ gates and depth $O(\log n)$, and it is easy to describe in logarithmic space.

Non-example: let $C_n$ be a chain of $n$ exclusive-or blocks.
This family also computes parity, but its depth grows linearly in $n$, so it fails clause 2 for every $i$.

Clause 4 is logspace uniformity; other uniformity conditions give the same class $\mathrm{NC}$.
The known inclusions are $\mathrm{NC}^1 \subseteq$ [[L|VRZ9H4EZ6V]] $\subseteq$ [[NL|7RH189REV7]] $\subseteq \mathrm{NC}^2$ and $\mathrm{NC} \subseteq \mathrm{P}$.
