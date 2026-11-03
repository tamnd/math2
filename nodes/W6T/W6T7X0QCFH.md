---
tag: W6T7X0QCFH
kind: statement
role: theorem
name: Parity is not in AC0
msc: [68Q17, 68Q06]
uses: [N1G9S8QC68, SQXNFGVADX]
about: [N1G9S8QC68, 4PGX7PHJCK]
sources:
  - url: https://en.wikipedia.org/wiki/AC0
---

## Statement

Let $\mathrm{PARITY}_n \colon \set{0,1}^n \to \set{0,1}$ be the function $x \mapsto x_1 \oplus \cdots \oplus x_n$, which is $1$ exactly when $x$ has an odd number of ones.

1. The language $\set{x \in \set{0,1}^* : \mathrm{PARITY}_{\abs{x}}(x) = 1}$ is not in [[AC0|N1G9S8QC68]].
2. More precisely, consider [[Boolean circuits|SQXNFGVADX]] with NOT gates and AND and OR gates of unbounded fan-in.
For every $d \ge 2$ there is $\varepsilon_d > 0$ such that, for all large $n$, every such circuit of depth $d$ for $\mathrm{PARITY}_n$ has at least $2^{\varepsilon_d n^{1/(d-1)}}$ gates.

## Remarks

Part 1 was proved by Furst, Saxe and Sipser and independently by Ajtai, and part 2 is due to Håstad.
The proof uses random restrictions: fix each input at random to $0$ or $1$, except for a small random set of inputs left free.
Håstad's switching lemma says that after such a restriction a small-width DNF becomes, with high probability, a small-width CNF.
Then one layer of the circuit can be merged into the next.
After $d - 2$ rounds the circuit depends on few of the free variables.
But the restriction of parity to the free variables is still parity or its negation, and it depends on all of them.

The bound in part 2 is sharp up to the constant $\varepsilon_d$: parity has depth-$d$ circuits of size $2^{O(n^{1/(d-1)})}$.
The constant depth is necessary: with depth $O(\log n)$, a balanced tree of exclusive-or blocks computes parity with $O(n)$ gates.

## Explanations

### L1 human

Parity asks whether the number of ones in a bit string is odd.
Circuits with a fixed number of layers and many-input AND and OR gates can do much, but they cannot compute parity unless they are huge.
The reason is that parity changes whenever any single input bit changes, while shallow AND and OR circuits are stable under fixing most of their inputs.

### L2 human

This was one of the first unconditional lower bounds for a natural model of computation.
It separates $\mathrm{AC}^0$ from $\mathrm{NC}^1$, since parity is in [[NC|3QFZN6ZZNC]] at level $1$.
Razborov and Smolensky gave a second proof by approximating $\mathrm{AC}^0$ circuits with low-degree polynomials over a finite field.
Their method also shows that counting modulo a prime $q$ is not in $\mathrm{AC}^0$ with gates counting modulo a different prime $p$.
The proof is natural in the sense of the [[natural proofs barrier|THPBBYSDP1]], which explains why such methods do not reach general circuits.
