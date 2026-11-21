---
tag: KHZ1E7RMMQ
kind: concept
name: Bi-interpretability
aliases: [bi-interpretability, bi-interpretable-structures, bi-interpretation]
msc: ["03C07"]
topics: [SZRM3N6BXW]
audience: research
uses: [7R0SJPH37J, C5BWHPHAGA, 983GZBQYT4, CY1TXHF6KQ]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
    locator: Bi-interpretability
  - book: isbn:9780521587136
---

## Summary

Let $M$ and $N$ be [[structures|983GZBQYT4]], let $\Gamma$ be an [[interpretation|7R0SJPH37J]] of $N$ in $M$ with coordinate map $f_\Gamma$, and let $\Delta$ be an interpretation of $M$ in $N$ with coordinate map $f_\Delta$.
Composing the two gives an interpretation of $M$ in $M$, with coordinate map $(\bar a_1, \dots, \bar a_m) \mapsto f_\Delta(f_\Gamma \bar a_1, \dots, f_\Gamma \bar a_m)$, and an interpretation of $N$ in $N$ in the same way.
The pair $(\Gamma, \Delta)$ is a *bi-interpretation* if the graph of the first composite coordinate map is a [[definable set|CY1TXHF6KQ]] of $M$ and the graph of the second is a definable set of $N$.
When the interpretations and the two graphs are definable without parameters, $M$ and $N$ are *$\emptyset$-bi-interpretable*; the exact page is [[this definition|ZA0RN56STN]].
Bi-interpretable structures have the same definable sets up to a definable translation, so bi-interpretability is the right notion of sameness for model theory.

## Motivation

Two structures can interpret each other and still be different.
A pure infinite set $M$ and the structure $M \times M$ with its two projection relations interpret each other, but their automorphism groups are not isomorphic.
The trouble is that going from $M$ to $N$ and back can lose track of the elements: the composite coordinate map may not be definable.
Bi-interpretability asks that the round trip be a definable map in both directions.
Then the two structures carry the same model theory: the same types, the same automorphisms and the same categoricity spectrum.

## Notation

Hodges writes $(\Gamma, \Delta)$ for a bi-interpretation and calls $M$ and $N$ *bi-interpretable* when one exists.
Hodges states the condition with *homotopies* of interpretations: each composite self-interpretation is homotopic to the identity interpretation.
The parameter-free version is often the default, and one then says "bi-interpretable with parameters" for the version over parameters.
In proof theory, a related notion for theories carries the same name; it concerns theories, not structures.

## Remarks

### Examples

- The semiring $(\mathbb{N}, +, \cdot)$ and the ring $(\mathbb{Z}, +, \cdot)$ are $\emptyset$-bi-interpretable, through pairs of natural numbers and sums of four squares; see [[this example|Y7VWHYKY2Z]].
- A field $K$ with at least $3$ elements and its group of affine maps $x \mapsto a x + b$ are bi-interpretable with two parameters; see [[this example|SK131CVMFY]].
- The ring $\mathbb{Z}$ and the field $\mathbb{Q}$ are $\emptyset$-bi-interpretable. Julia Robinson defined $\mathbb{Z}$ in $\mathbb{Q}$, and in $\mathbb{Z}$ the composite map is $(a, b) \mapsto a / b$ on pairs with $b \mid a$, whose graph $a = b \cdot c$ is definable.
- A structure $M$ and an expansion of $M$ by $\emptyset$-definable relations are $\emptyset$-bi-interpretable, by the identity coordinate maps.

### Non-examples

- A pure infinite set $M$ and $(M^2, E_1, E_2)$, where $E_i$ means "same $i$-th coordinate", interpret each other without parameters. For $M$ countable they are not $\emptyset$-bi-interpretable, because the automorphism groups differ; see [[this non-example|GM60Z1JN7Q]].
- The field $\mathbb{C}$ is interpretable in the field $\mathbb{R}$, but $\mathbb{R}$ is not interpretable in $\mathbb{C}$, by stability; see [[this example|E355PSA9SW]].
- The groups $(\mathbb{Z}, +)$ and the ring $(\mathbb{Z}, +, \cdot)$ are not bi-interpretable, since the ring is not interpretable in the group: the first theory is decidable and the second is not.

### Basic properties

- Bi-interpretability is an equivalence relation on structures. For transitivity, the composite of two definable round trips is again a definable map.
- Theories. A $\emptyset$-bi-interpretation turns each model $M'$ of $\operatorname{Th}(M)$ into a model $\Gamma(M')$ of $\operatorname{Th}(N)$, and $\Delta(\Gamma(M'))$ is definably isomorphic to $M'$. So the models of the two theories correspond, with $|M'| = |\Gamma(M')|$ for infinite $M'$.
- Categoricity. By the previous point, $\operatorname{Th}(M)$ is $\kappa$-categorical exactly when $\operatorname{Th}(N)$ is, for each infinite cardinal $\kappa$.
- Stability. $\operatorname{Th}(M)$ is [[stable|T7JW5QY6KR]] exactly when $\operatorname{Th}(N)$ is. This already follows from interpretations in both directions.
- Automorphisms. A $\emptyset$-bi-interpretation gives an isomorphism of the [[automorphism groups|0K1SCPBNKJ]] $\operatorname{Aut}(M)$ and $\operatorname{Aut}(N)$. For countable [[$\omega$-categorical|A22K1X8GKD]] structures the converse holds, with topologies; this is the [[reconstruction theorem|AM0523XJ9D]] of Ahlbrandt and Ziegler.

### History

Ahlbrandt and Ziegler used bi-interpretations in 1986 to study totally categorical theories, and they proved the reconstruction theorem for $\omega$-categorical structures.
Hodges's textbook treats bi-interpretations with the coordinate maps as part of the data.
The notion is now a standard tool in the study of the automorphism groups of countable structures.

### Common errors

- Taking interpretations in both directions for a bi-interpretation. The composite coordinate maps must also be definable, and the pure set example shows that this condition has content.
- Confusing bi-interpretability of structures with [[interpretability between theories|8H03GRMDYG]] in proof theory. There, an interpretation of $T$ in $S$ only needs $S$ to prove the translated axioms of $T$, and no fixed structure is involved.

## Explanations

### L1 human

Two structures are bi-interpretable when each can be built inside the other, and the round trip comes back in a controlled way.
For example, the integers can be built from pairs of natural numbers: the pair $(5, 2)$ stands for $3$, and $(2, 5)$ stands for $-3$.
The natural numbers sit inside the integers as the numbers that are not negative.
If we start with an integer, write it as a pair of natural numbers, and see those as integers again, we get two integers whose difference is the original one.
This round trip is a rule that we can write down, so the two structures are really "the same" for the purpose of logic.

### L2 human

We check the round trip in $\mathbb{N}$ for the bi-interpretation of $\mathbb{N}$ and $\mathbb{Z}$.

1. In $\mathbb{N}$, an integer is a pair $(a, b)$ with coordinate map $f_\Gamma(a, b) = a - b$.
2. In $\mathbb{Z}$, a natural number is an integer $x \ge 0$, with coordinate map $f_\Delta(x) = x$.
3. The round trip in $\mathbb{N}$ starts from a pair $(a, b)$ whose value $a - b$ is in the domain of $\Delta$, so $a \ge b$.
4. The composite coordinate map sends $(a, b)$ to $a - b$, and its graph is $\set{(a, b, c) : a = b + c}$.
5. This graph is defined by the formula $a = b + c$, so the round trip is definable in $\mathbb{N}$.

The typical use is to transfer a property of models from one theory to the other, such as categoricity in a cardinal.
A trap is to forget the second round trip: both composites must be definable, one in each structure.

### L3 human

A bi-interpretation is an equivalence of the categories of models with elementary embeddings, given by formulas, and it identifies the two structures with sorts of a common $M^{\mathrm{eq}}$.
In this sense bi-interpretable structures have the same [[imaginary elements|Q0HM88QQKN]] up to a definable bijection, and the same lattice of definable sets in each sort.
For countable $\omega$-categorical structures, the [[reconstruction theorem|AM0523XJ9D]] turns bi-interpretability into an isomorphism of topological groups, so the model theory is a part of the theory of [[Polish groups|9C1WSBNQX9]].
In arithmetic and set theory, bi-interpretability of theories is studied in its own right, and there the round trips are given by proofs in a theory, not by definable maps in one structure.
