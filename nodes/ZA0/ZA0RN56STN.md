---
tag: ZA0RN56STN
kind: definition
name: Bi-interpretability
aliases: [bi-interpretability-definition, bi-interpretation-definition]
msc: ["03C07"]
topics: [SZRM3N6BXW]
audience: research
defines: KHZ1E7RMMQ
uses: [C5BWHPHAGA, CY1TXHF6KQ, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
    locator: Bi-interpretability
  - book: isbn:9780521587136
---

## Definition

Let $M$ be an $L$-[[structure|983GZBQYT4]] and let $N$ be an $L'$-structure.
Let $\Gamma$ be an $n$-dimensional [[interpretation|C5BWHPHAGA]] of $N$ in $M$, with domain $D_\Gamma = \partial_\Gamma(M^n)$ and coordinate map $f_\Gamma : D_\Gamma \to N$.
Let $\Delta$ be an $m$-dimensional interpretation of $M$ in $N$, with domain $D_\Delta = \partial_\Delta(N^m)$ and coordinate map $f_\Delta : D_\Delta \to M$.

1. The *composite in $M$* is the map $h_M$ with domain the set of tuples $(\bar a_1, \dots, \bar a_m) \in D_\Gamma^m$ with $(f_\Gamma \bar a_1, \dots, f_\Gamma \bar a_m) \in D_\Delta$. It is given by $h_M(\bar a_1, \dots, \bar a_m) = f_\Delta(f_\Gamma \bar a_1, \dots, f_\Gamma \bar a_m)$, and it maps a subset of $M^{n m}$ onto $M$.
2. The *composite in $N$* is the map $h_N$ with domain the set of tuples $(\bar b_1, \dots, \bar b_n) \in D_\Delta^n$ with $(f_\Delta \bar b_1, \dots, f_\Delta \bar b_n) \in D_\Gamma$. It is given by $h_N(\bar b_1, \dots, \bar b_n) = f_\Gamma(f_\Delta \bar b_1, \dots, f_\Delta \bar b_n)$, and it maps a subset of $N^{m n}$ onto $N$.

The pair $(\Gamma, \Delta)$ is a *bi-interpretation* between $M$ and $N$ if the graph of $h_M$ is a [[definable set|CY1TXHF6KQ]] in $M$ and the graph of $h_N$ is a definable set in $N$.
The structures $M$ and $N$ are *bi-interpretable* if a bi-interpretation between them exists.
They are *$\emptyset$-bi-interpretable* if $\Gamma$ and $\Delta$ are interpretations without parameters and the two graphs are $\emptyset$-definable.
When parameters are allowed in the interpretations and in the two graphs, $M$ and $N$ are *bi-interpretable with parameters*.

## Notation

The composite $h_M$ is the coordinate map of an interpretation of $M$ in $M$, the composite of $\Gamma$ and $\Delta$.
So the condition says that this self-interpretation of $M$ is definably isomorphic to the identity interpretation, and similarly for $N$.
Hodges calls the condition a homotopy between the composite and the identity interpretation.
Books that do not keep coordinate maps phrase the condition with the isomorphism from $M$ to the doubly interpreted copy of $M$, which must be definable.

## Remarks

The composites depend on the coordinate maps, and not only on the formulas.
Changing $f_\Gamma$ by an automorphism of $N$ can change whether $h_M$ is definable.

Interpretations in both directions are not enough for a bi-interpretation.
For a countable pure set $M$ and $N = (M^2, E_1, E_2)$, both interpretations exist, but no choice makes the composites definable; see [[this non-example|GM60Z1JN7Q]].

Example: $(\mathbb{N}, +, \cdot)$ and $(\mathbb{Z}, +, \cdot)$ are $\emptyset$-bi-interpretable; see [[this example|Y7VWHYKY2Z]].

## Explanations

### L1 human

Suppose that each of two structures can be built from pieces of the other.
Then each element can make a round trip: we build it from pieces of the other structure, and then build those pieces from pieces of the first.
The two structures are bi-interpretable when the round trip, in each direction, is a rule that the structure itself can state.

### L2 human

We compute the composite in $N$ for the bi-interpretation of $M = \mathbb{N}$ and $N = \mathbb{Z}$.

1. $\Delta$ interprets $\mathbb{N}$ in $\mathbb{Z}$ as the set of $x$ with $x \ge 0$, with $f_\Delta(x) = x$.
2. $\Gamma$ interprets $\mathbb{Z}$ in $\mathbb{N}$ by pairs, with $f_\Gamma(a, b) = a - b$.
3. In $\mathbb{Z}$, the composite domain is the set of pairs $(x, y)$ with $x \ge 0$ and $y \ge 0$, and $h_N(x, y) = f_\Gamma(x, y) = x - y$.
4. Its graph is defined by $x \ge 0 \wedge y \ge 0 \wedge z = x - y$, where $x \ge 0$ means that $x$ is a sum of four squares.

The typical use is to check the two graphs, one formula in each structure.
A trap is to mix up the dimensions: the composite in $M$ has $n m$ coordinates, not $n + m$.
