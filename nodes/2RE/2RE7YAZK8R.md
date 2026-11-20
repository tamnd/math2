---
tag: 2RE7YAZK8R
kind: concept
name: Ehrenfeucht-Fraïssé game
aliases: [ehrenfeucht-fraisse-game, ef-game, back-and-forth-game]
msc: ["03C07", "03C13"]
topics: [N64R1MGDBN]
audience: grad
uses: [983GZBQYT4, WDVVEYD6AT, EWB8KXZMCV, FVEVRE5XNZ, P3B1V182N4, 676H7EGTKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrenfeucht–Fraïssé_game
    locator: Main idea
  - book: isbn:9780521587136
    locator: Chapter 3
  - book: isbn:9780387987606
same_as:
  wikidata: Q1300013
  wikipedia: Ehrenfeucht–Fraïssé game
---

## Summary

The Ehrenfeucht-Fraïssé game is a two-player game played on two [[structures|983GZBQYT4]] $\mathcal{A}$ and $\mathcal{B}$ of the same [[signature|WDVVEYD6AT]].
In the game $G_n(\mathcal{A}, \mathcal{B})$ with $n$ rounds, Spoiler picks in each round an element of either structure, and Duplicator answers with an element of the other.
Duplicator wins when the chosen elements $a_i \mapsto b_i$ form a partial isomorphism, that is, they satisfy the same atomic formulas.
The formal definition is [[this definition|1DVRN1T2Z0]].
For a finite relational signature, Duplicator has a winning strategy in $G_n$ exactly when $\mathcal{A}$ and $\mathcal{B}$ agree on all sentences of [[quantifier rank|FVEVRE5XNZ]] at most $n$; this is the [[Ehrenfeucht-Fraïssé theorem|72BMYXGFA8]].
In the infinite game, with one round for each natural number, Duplicator wins exactly when a [[back-and-forth system|EWB8KXZMCV]] exists.
The game is the main tool for showing that a property is [[not first-order definable|VT2PSXKM50]], in particular on finite structures.

## Motivation

To show that a property is not first-order, one must show that no sentence among infinitely many expresses it.
A direct search through sentences is hopeless.
The game replaces it by a concrete task: find, for each $n$, two structures that differ in the property and a strategy for Duplicator in $n$ rounds.
Each round matches one quantifier: Spoiler's move picks a witness for a quantifier in one structure, and Duplicator must find a matching witness in the other.
Switching structures between rounds corresponds to alternating $\exists$ and $\forall$.

## Notation

The game is written $G_n(\mathcal{A}, \mathcal{B})$, $\operatorname{EF}_n(\mathcal{A}, \mathcal{B})$ or $\operatorname{EF}_n[\mathcal{A}, \mathcal{B}]$, and the infinite game $G_\omega(\mathcal{A}, \mathcal{B})$.
The game with given starting tuples is $G_n(\mathcal{A}, \bar a, \mathcal{B}, \bar b)$.
The players are called Spoiler and Duplicator, player I and player II, or $\forall$belard and $\exists$loise.
We write $\mathcal{A} \sim_n \mathcal{B}$ when Duplicator has a winning strategy in $G_n(\mathcal{A}, \mathcal{B})$.

## Remarks

### Examples

- On sets with $m$ and $k$ elements and no structure, Duplicator wins $G_n$ if and only if $m = k$ or both are at least $n$; see [[this example|X98C7KEQRV]].
- Duplicator wins every $G_n$ on $(\Z, <)$ and $(\Z + \Z, <)$, by keeping short distances equal and long distances long; see [[this example|JPE6BXFX3F]].
- On finite linear orders of sizes $m \ne k$, Duplicator wins $G_n$ if and only if $m, k \ge 2^n - 1$; see [[games on linear orders|ZZPXVVZARC]].

### Non-examples

- The one-sided game, in which Spoiler must always play in $\mathcal{A}$, tests only existential sentences; see [[this non-example|S56YBNF2XR]].
- A game whose winning condition only asks that $a_i \mapsto b_i$ be injective ignores the relations, so it tests only cardinality, not the structure.

### Basic properties

- If Duplicator wins $G_{n+1}$, Duplicator wins $G_n$, by playing the first $n$ rounds of a winning strategy.
- Each $\sim_n$ is an equivalence relation: a strategy for $(\mathcal{A}, \mathcal{B})$ and one for $(\mathcal{B}, \mathcal{C})$ compose to one for $(\mathcal{A}, \mathcal{C})$.
- The games are determined: for each $n$, exactly one player has a winning strategy, since the game is finite.
- Duplicator wins $G_\omega$ if and only if $\mathcal{A}$ and $\mathcal{B}$ are partially isomorphic; for countable structures this means isomorphic.
- If Duplicator wins every $G_n$, the structures are [[elementarily equivalent|P3B1V182N4]]. The converse holds for finite relational signatures.

### History

The back-and-forth characterization of elementary equivalence was given by Roland Fraïssé in his thesis, published in 1954.
Andrzej Ehrenfeucht formulated it as a game in a paper of 1961.
The names Spoiler and Duplicator are due to Joel Spencer.
The names Abelard and Eloise were introduced by Wilfrid Hodges.

### Common errors

- To let Duplicator answer in the same structure as Spoiler. Every answer lies in the other structure.
- To check the winning condition only on the last pair. All chosen pairs must form one partial isomorphism together.
- To use the theorem for an infinite signature. With infinitely many unary predicates, structures can agree on all rank $1$ sentences while Spoiler wins in one round; see [[the theorem|72BMYXGFA8]].

## Explanations

### L1 human

Two players look at two structures side by side.
Spoiler wants to show that they are different, and Duplicator wants to show that they look the same.
In each round Spoiler points at an element on one side, and Duplicator points at a matching element on the other side.
After the last round, Duplicator wins if the chosen elements relate to each other in the same way on both sides.
On the linear orders with $3$ and $4$ elements, Duplicator wins with $2$ rounds, and Spoiler wins with $3$.

### L2 human

We play $G_3$ on the orders $\mathcal{A} = (\set{1, 2, 3}, <)$ and $\mathcal{B} = (\set{1, 2, 3, 4}, <)$, and Spoiler wins.

1. Round 1: Spoiler picks $2 \in \mathcal{B}$. If Duplicator answers $1$ or $3$, Spoiler wins in one more round, picking an element below $2$ in $\mathcal{B}$ or above $2$ in $\mathcal{B}$, which has no partner. So Duplicator answers $2 \in \mathcal{A}$.
2. Now $\mathcal{B}$ has two elements above $2$, namely $3$ and $4$, and $\mathcal{A}$ has one, namely $3$.
3. Round 2: Spoiler picks $4 \in \mathcal{B}$, and Duplicator must answer $3 \in \mathcal{A}$.
4. Round 3: Spoiler picks $3 \in \mathcal{B}$, between $2$ and $4$. No element of $\mathcal{A}$ lies between $2$ and $3$, so Spoiler wins.

The typical use of the game is to prove $\mathcal{A} \equiv_n \mathcal{B}$ by exhibiting a strategy for Duplicator.
A trap is to give Duplicator a strategy that wins against one line of play only; it must win against every choice of Spoiler.

### L3 human

The game is the model-theoretic form of [[bisimulation|X27BR4YP2Y]]: the infinite game on two transition systems, with moves only along edges, is the bisimulation game of modal logic.
Variants with pebbles count variables instead of quantifier rank, and they characterize the finite-variable logics $L^k$.
Variants with sets of moves characterize monadic second-order logic, and the Hanf and Gaifman locality theorems give quick strategies for Duplicator on structures that look locally alike.
Through [[game-theoretic semantics|D45Z7HETDA]], a strategy in the evaluation game of a sentence is a proof of truth, and the Ehrenfeucht-Fraïssé game compares two such evaluation games.
