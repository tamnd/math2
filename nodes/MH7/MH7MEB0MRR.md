---
tag: MH7MEB0MRR
kind: statement
role: theorem
name: Morse inequalities
msc: [57R70, "58E05"]
uses: [F45VQ47GPV, KPQ96640ZJ, M0Q5CFJ7ZH, ST71ZV3FES, RNDDWDAFJ5]
about: [KPQ96640ZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Morse_theory
---

## Statement

Let $M$ be a compact [[smooth manifold|F45VQ47GPV]] without boundary, of dimension $n$, and let $f \colon M \to \R$ be a [[Morse function|KPQ96640ZJ]].
For $0 \le k \le n$, let $c_k$ be the number of critical points of $f$ of index $k$.
Let $F$ be a field, and let $b_k = \dim_F H_k(M; F)$ be the $k$-th [[Betti number|ST71ZV3FES]] of $M$ over $F$, where $H_k$ is [[singular homology|M0Q5CFJ7ZH]].
Then:

1. (weak Morse inequalities) $c_k \ge b_k$ for every $k$;
2. (strong Morse inequalities) $\sum_{i=0}^{k} (-1)^{k-i} c_i \ge \sum_{i=0}^{k} (-1)^{k-i} b_i$ for every $k$;
3. $\sum_{k=0}^{n} (-1)^k c_k = \sum_{k=0}^{n} (-1)^k b_k = \chi(M)$, where $\chi(M)$ is the [[Euler characteristic|RNDDWDAFJ5]] of $M$.

## Remarks

The idea of the proof: as $c$ increases, the sublevel set $\set{f \le c}$ changes up to homotopy only when $c$ crosses a critical value.
At such a value it changes by attaching one cell of dimension $k$ for each critical point of index $k$.
So $M$ is homotopy equivalent to a CW complex with $c_k$ cells of dimension $k$.
The inequalities follow from the cellular chain complex of this CW complex.
The strong inequalities imply the weak ones, by adding the inequalities for $k$ and $k - 1$.
Item 3 is the Euler characteristic of the CW complex, computed once from cells and once from homology.
Example: the height function on an upright torus has $c_0 = 1$, $c_1 = 2$, $c_2 = 1$, and the torus has $b_0 = 1$, $b_1 = 2$, $b_2 = 1$, so all inequalities are equalities.
Consequence: every Morse function on a closed orientable surface of genus $g$ has at least $2g + 2$ critical points.

## Explanations

### L1 human

A Morse function needs at least as many critical points of each index as the manifold has holes of that dimension.
For example, any nice height function on a doughnut has at least one bottom, one top, and two saddles.
Topology forces critical points to exist.

### L2 human

The inequalities are the first quantitative link between the analysis of a function and the topology of its domain.
They can be used in two directions.
They bound the number of critical points of a function, as in Morse's results on geodesics.
They also bound Betti numbers, once one constructs a function with few critical points.
A Morse function for which all inequalities are equalities is called perfect.
Morse homology refines the inequalities by building a chain complex on the critical points whose homology is $H_*(M)$.
