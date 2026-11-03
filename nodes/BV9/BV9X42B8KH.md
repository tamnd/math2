---
tag: BV9X42B8KH
kind: definition
name: Polar code
msc: [94B05, 94A24]
defines: SAVK6PAFQ5
uses: [E85KREWV60, 0N7ENQRCXN, B9C5RBFATB, A83CYGDXFG, ESYMTB37YG]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_code_(coding_theory)
---

## Definition

Let $n \ge 1$, $N = 2^n$, and let $F = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ over $\F_2$, with $n$-fold [[Kronecker power|0N7ENQRCXN]] $F^{\otimes n}$, an $N \times N$ matrix.
Let $W$ be a binary-input memoryless [[channel|B9C5RBFATB]].
Let $u_1, \dots, u_N$ be independent uniform bits, let $x = u F^{\otimes n}$, and send each $x_j$ through $W$ to get $y_j$.
For $1 \le i \le N$, the synthetic channel $W_N^{(i)}$ has input $u_i$ and output $(y_1, \dots, y_N, u_1, \dots, u_{i-1})$.
Let $1 \le K \le N$, and let $A \subseteq \set{1, \dots, N}$ be a set of $K$ indices $i$ for which the [[mutual information|A83CYGDXFG]] $I(W_N^{(i)})$ between input and output is largest.
The *polar code* of length $N$ and dimension $K$ for $W$ is
$$C = \set{u F^{\otimes n} : u \in \F_2^N, \ u_i = 0 \text{ for all } i \notin A}.$$

## Remarks

The coordinates $u_i$ with $i \in A$ carry the message, and the others are frozen to $0$.
Many authors multiply $F^{\otimes n}$ by the bit-reversal permutation matrix; this permutes the coordinates of the codewords.
The standard decoder is successive cancellation: it estimates $u_1, u_2, \dots, u_N$ in this order, each $u_i$ with $i \in A$ from $y$ and the earlier estimates, with $O(N \log N)$ operations.
Choosing $A$ requires computing or estimating the reliabilities of the $W_N^{(i)}$; for the [[binary erasure channel|ESYMTB37YG]] they follow from the recursion $\varepsilon \mapsto 2\varepsilon - \varepsilon^2$ and $\varepsilon \mapsto \varepsilon^2$.

Example: $N = 2$, so $x = (u_1 + u_2, u_2)$.
On the binary erasure channel with erasure probability $\varepsilon$, $W_2^{(1)}$ is an erasure channel with probability $2\varepsilon - \varepsilon^2$ and $W_2^{(2)}$ one with probability $\varepsilon^2$.
For $K = 1$, $A = \set{2}$ and the polar code is $\set{(0, 0), (1, 1)}$, the [[repetition code|PZV5HW9BT7]] of length $2$.

Non-example: for $N = 2$ and $K = 1$, the code $\set{u F : u_2 = 0} = \set{(0, 0), (1, 0)}$ uses the worse synthetic channel, so it is not the polar code; its second coordinate carries no information.
