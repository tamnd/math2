---
tag: MYKHR82SRT
kind: statement
role: theorem
name: Linear network coding theorem
msc: [94A24, 90B10, 05C21]
uses: [0KFYGSHHF5, 0ZXZ82FTX2, 4HMR4KQ01T]
about: [0KFYGSHHF5]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_network_coding
---

## Statement

Let $G$ be a finite acyclic [[directed graph|0KFYGSHHF5]], with parallel edges allowed.
Each edge carries one symbol of a [[finite field|0ZXZ82FTX2]] $F$ per use.
Let $s$ be a source vertex and let $T$ be a nonempty set of sink vertices.
Let $h \ge 1$ be an integer such that, for every $t \in T$, every set of edges whose removal separates $t$ from $s$ has at least $h$ edges.
Assume that $\abs{F} > \abs{T}$.
Then there is a linear network code over $F$ that multicasts $h$ source symbols to every sink, in the following sense.
Each edge carries an $F$-linear combination of the symbols entering its tail, or of the $h$ source symbols if the tail is $s$.
Each sink $t \in T$ recovers all $h$ source symbols as $F$-linear functions of the symbols on its incoming edges.

## Remarks

The idea of the proof: give each edge leaving a vertex unknown coefficients for its linear combination.
For each sink $t$, the map from the source symbols to the symbols arriving at $t$ is an $h \times h'$ matrix, where $h'$ is the number of edges entering $t$.
Its entries are polynomials in these coefficients.
Choose $h$ edge-disjoint paths from $s$ to $t$, and let $M_t$ be the $h \times h$ submatrix for their last edges.
These paths exist by the [[max-flow min-cut theorem|4HMR4KQ01T]], and routing along them shows that $\det M_t$ is a nonzero polynomial.
The product $\prod_{t \in T} \det M_t$ is a nonzero polynomial whose degree in each coefficient is at most $\abs{T}$, so it has a nonzero value at some point of $F$ when $\abs{F} > \abs{T}$.

Example: the butterfly network has vertices $s, u, v, w, x, t_1, t_2$ and edges $su$, $sv$, $ut_1$, $vt_2$, $uw$, $vw$, $wx$, $xt_1$, $xt_2$, with sinks $T = \set{t_1, t_2}$ and $h = 2$.
The source sends $a \in \F_2$ to $u$ and $b \in \F_2$ to $v$.
With routing alone, the single edge $wx$ carries either $a$ or $b$, so one sink misses a symbol.
If $wx$ carries $a + b$, then $t_1$ receives $a$ and $a + b$ and computes $b$, and $t_2$ receives $b$ and $a + b$ and computes $a$.
So both sinks get two symbols per use, which matches the min-cut.
Here $\abs{F} = \abs{T} = 2$, so the field size condition of the theorem is sufficient but not necessary.

The min-cut hypothesis is necessary: if some sink has a cut of fewer than $h$ edges, at most that many symbols per use can reach it under any coding scheme.

## Explanations

### L1 human

In a network of links, the classical way to move data is to copy and forward packets.
Network coding lets inner nodes mix packets, for example by adding them, before forwarding them.
The theorem says that with mixing by linear combinations, one source can send to many receivers at once.
Each receiver gets data at the largest rate allowed by the bottleneck between the source and that receiver.

### L2 human

Ahlswede, Cai, Li and Yeung showed in 2000 that the multicast capacity equals the smallest of the min-cuts from the source to the sinks.
Li, Yeung and Cai showed that linear codes suffice, and Koetter and Médard gave the algebraic proof with transfer matrices sketched above.
Choosing the coefficients at random from a large field works with high probability, which leads to random linear network coding.
For several sources with different demands, linear codes are not always enough.
