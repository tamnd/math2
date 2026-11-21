---
tag: CWKWP7G6HB
kind: concept
name: Homogeneous structures beyond graphs
aliases: [homogeneous-structures-beyond-graphs, classification-of-homogeneous-structures, homogeneous-partial-orders, homogeneous-tournaments]
msc: ["03C15", "03C50", "06A06", "05C20"]
topics: [ZS8X8KS54R]
audience: research
uses: [H8VM37SSAX, F7PA1RVBCG, HJVRBDQSGG, 0R5HTV7REV, 0FRXBVVR03, V5CKNFP3HC, A22K1X8GKD]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_graph
    locator: Variations
  - book: isbn:9780521587136
---

## Summary

The [[Lachlan-Woodrow theorem|F7PA1RVBCG]] lists all countable [[ultrahomogeneous|H8VM37SSAX]] graphs.
Similar lists exist for other classes of relational structures: partial orders, tournaments, [[directed graphs|0R5HTV7REV]], and permutations viewed as pairs of linear orders.
Each classification answers the question: which amalgamation classes of finite structures of a given kind exist?
Some lists are short, like the four families of homogeneous partial orders, and some are uncountable, like the homogeneous directed graphs.
For several natural classes, such as $3$-uniform hypergraphs, no classification is known.

## Motivation

By [[Fraïssé's theorem|V5CKNFP3HC]], classifying countable homogeneous structures of a given kind is the same as classifying the amalgamation classes of finite structures of that kind.
So each classification is a finite combinatorics problem with an infinite answer.
The resulting lists supply the standard examples of [[$\aleph_0$-categorical|A22K1X8GKD]] structures, of oligomorphic permutation groups, and of [[Fraïssé limits|HJVRBDQSGG]] for structural Ramsey theory.

## Notation

For a relational class, "homogeneous" means ultrahomogeneous in the sense of Fraïssé.
A tournament is a directed graph in which every pair of distinct vertices carries exactly one arc.

## Remarks

### Examples

- The cyclic tournament on $3$ vertices is a finite homogeneous tournament; see [[this example|3GDGCWT2R4]].
- The generic partial order is a countable homogeneous partial order; see [[this example|A0H8Q91FPB]].
- $(\Q, <)$ is homogeneous both as a [[linear order|0FRXBVVR03]] and as a tournament.
- The random tournament, the Fraïssé limit of all finite tournaments, is homogeneous.

### Non-examples

- A finite linear order with at least $2$ elements is not homogeneous; see [[this non-example|KPYTBVVDFS]].
- The partial order $\Z$ with the usual order is not homogeneous, for the same reason as $(\Z, <)$ as a linear order.

### Basic properties

- Partial orders: Schmerl showed that a countable homogeneous partial order is an antichain, a disjoint union of incomparable copies of $(\Q, <)$, a copy of $(\Q, <)$ with each point replaced by an antichain of fixed size, or the generic partial order.
- Tournaments: Lachlan showed that the countable homogeneous tournaments are the one-point tournament, the $3$-cycle, $(\Q, <)$, the local order $S(2)$, and the random tournament.
- Directed graphs: Henson constructed $2^{\aleph_0}$ countable homogeneous directed graphs, and Cherlin classified all of them.
- Permutations: Cameron showed that there are exactly five homogeneous permutations, viewed as sets with two linear orders.

### History

Schmerl's classification of homogeneous partial orders appeared in 1979, and Cherlin's classification of homogeneous directed graphs in 1998.

### Common errors

- To assume every natural class has a countable list. Homogeneous directed graphs come in $2^{\aleph_0}$ isomorphism types.
- To ignore the signature. A linear order viewed as a partial order and as a tournament gives the same structure, but posets and tournaments are classified separately.

## Explanations

### L1 human

Graphs are not the only structures one can ask to be as symmetric as possible.
One can ask the same question for orderings, for tournaments where each pair of players has a winner, and for directed networks.
Each kind has its own short or long list of answers.

### L2 human

We check that an antichain of size $2$ is homogeneous as a partial order.

1. The two elements $a, b$ are incomparable, so the swap $a \leftrightarrow b$ is an automorphism.
2. Any isomorphism between subsets is a partial injection of $\set{a, b}$, and it extends to the identity or to the swap.

The typical use of the classifications is as a source of examples with prescribed properties.
A trap is to forget the finite entries; they are part of each list.

### L3 human

The classifications combine Fraïssé theory with Ramsey-type arguments that show which finite configurations are forced.
Cherlin's classification of homogeneous directed graphs includes Henson's uncountable family, built by forbidding sets of tournaments taken from an infinite antichain under embedding.
For $3$-uniform hypergraphs, only partial results are known, and the full list remains open.
