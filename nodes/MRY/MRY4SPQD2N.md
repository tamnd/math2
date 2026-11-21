---
tag: MRY4SPQD2N
kind: proof
name: Proof of the uniqueness of the model companion by interleaved chains
msc: ["03C10", "03C25"]
topics: [1A9JSC5YG8]
audience: grad
proves: V9KVDFCXW7
uses: [WSJ2QN9YTY, ERVV6RWNNX, NHCRZ74JHH, CGH8C8EA9N]
methods: [GQHHNV79PA, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Model_complete_theory
    locator: Model companion and model completion
  - book: isbn:9780521587136
---

## Proof

Let $T_1$ and $T_2$ be model companions of $T$.
By symmetry it suffices to show that every model of $T_1$ is a model of $T_2$.

### Mutual model consistency of $T_1$ and $T_2$

1. Let $A \models T_1$. By [[mutual model consistency|WSJ2QN9YTY]] of $T_1$ and $T$, the structure $A$ embeds into some $B \models T$.
2. By mutual model consistency of $T$ and $T_2$, the structure $B$ embeds into some $C \models T_2$.
3. So every model of $T_1$ embeds into a model of $T_2$. In the same way every model of $T_2$ embeds into a model of $T_1$.

### The chain

Let $M \models T_1$, and identify each structure with its image.
Using the first part at each step, build a chain
$$M = M_0 \subseteq N_0 \subseteq M_1 \subseteq N_1 \subseteq M_2 \subseteq \cdots$$
with $M_i \models T_1$ and $N_i \models T_2$ for all $i$.

1. The theory $T_1$ is [[model complete|ERVV6RWNNX]] and $M_i \subseteq M_{i+1}$ are models of $T_1$. So $M_i \preceq M_{i+1}$ for all $i$, and $(M_i)$ is an elementary chain.
2. In the same way $N_i \preceq N_{i+1}$ for all $i$, since $T_2$ is model complete.
3. The two chains have the same union $U = \bigcup_i M_i = \bigcup_i N_i$, since they are interleaved.
4. By the [[elementary chain theorem|NHCRZ74JHH]], $M_i \preceq U$ and $N_i \preceq U$ for all $i$.
5. From $N_0 \preceq U$ and $N_0 \models T_2$ we get $U \models T_2$.
6. From $M = M_0 \preceq U$ we get that $M$ and $U$ satisfy the same sentences. So $M \models T_2$.

So every model of $T_1$ is a model of $T_2$, and by symmetry the two theories have the same models.

## Idea

Climb alternately through models of the two theories.
Model completeness of each theory makes each half of the chain elementary, and the two halves meet in the same union.
So a model of one theory is an elementary substructure of a model of the other.

## Variants

One can replace the chain by one step: if $M \models T_1$, then $M \subseteq N \models T_2$ and $N \subseteq M' \models T_1$ with $M \preceq M'$ give that every universal-existential consequence of $T_2$ holds in $M$, and $T_2$ is axiomatized by such sentences since it is model complete.
This version uses that a model complete theory is equivalent to a set of $\forall\exists$ sentences.
That fact holds because unions of chains of models of a model complete theory are models, by the chain argument above, and by the Chang-Łoś-Suszko theorem.
