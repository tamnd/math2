---
tag: VT2PSXKM50
kind: concept
name: Non-definability proofs by games
aliases: [inexpressibility-by-ehrenfeucht-fraisse-games, non-definability-by-games]
msc: ["03C13", "03C07", "68Q19"]
topics: [N64R1MGDBN]
audience: grad
uses: [2RE7YAZK8R, 72BMYXGFA8, FVEVRE5XNZ, P3B1V182N4, DKFGQTRYZE, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrenfeucht%E2%80%93Fra%C3%AFss%C3%A9_game
    locator: Equivalence and inexpressibility
  - url: https://en.wikipedia.org/wiki/Finite_model_theory
    locator: Characterisation of a class of structures
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Summary

A *non-definability proof by games* shows that a property $P$ of [[structures|983GZBQYT4]] is not expressed by any first-order [[sentence|DKFGQTRYZE]].
For each $n$ it exhibits a structure $\mathcal{A}_n$ with $P$, a structure $\mathcal{B}_n$ without $P$, and a winning strategy for Duplicator in the [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]] $G_n(\mathcal{A}_n, \mathcal{B}_n)$.
A sentence $\sigma$ that expresses $P$ has some [[quantifier rank|FVEVRE5XNZ]] $n$.
By the [[Ehrenfeucht-Fraïssé theorem|72BMYXGFA8]], $\mathcal{A}_n$ and $\mathcal{B}_n$ agree on $\sigma$, which contradicts $\mathcal{A}_n \models P$ and $\mathcal{B}_n \not\models P$.
The method works inside any class of structures, in particular inside the class of finite structures.

## Motivation

The standard proof that a property is not first-order uses the compactness theorem, as in [[these examples|T1S9T0RKHJ]].
Compactness produces infinite models, so it says nothing when only finite structures are allowed.
In [[finite model theory|4XRVJE0KAN]], questions such as "is even size definable" or "is connectivity definable" concern finite structures only.
Games still work there: the structures $\mathcal{A}_n$ and $\mathcal{B}_n$ can be finite, and the theorem holds for them unchanged.

## Notation

One writes $\mathcal{A} \equiv_n \mathcal{B}$ for agreement on sentences of rank at most $n$, and $\mathcal{A} \sim_n \mathcal{B}$ for a win of Duplicator in $G_n$.
A property is a class $K$ of structures closed under isomorphism; it is *first-order definable* in a class $C$ when $K \cap C$ is the class of models in $C$ of one sentence.

## Remarks

### Examples

- Even size is not definable on finite sets or on finite linear orders; see [[this example|N3AC6Y96RZ]].
- Hamiltonicity and having a perfect matching are not definable on finite graphs; see [[this example|W0JEQM6ZTH]].
- Connectivity of finite graphs is not definable, by an interpretation in finite linear orders; see the [[games on linear orders|ZZPXVVZARC]].

### Non-examples

- A single pair of structures with $\mathcal{A} \equiv_n \mathcal{B}$ for one $n$ proves nothing about definability; see [[this non-example|S88FE481WW]].
- Exhibiting $\mathcal{A} \in P$ and $\mathcal{B} \notin P$ with $\mathcal{A} \equiv \mathcal{B}$ also works, but it is the compactness style, and for finite structures it never applies, since elementarily equivalent finite structures are isomorphic.

### Basic properties

- The method is complete: if $P$ is not definable in a class $C$ with a finite relational signature, suitable $\mathcal{A}_n$ and $\mathcal{B}_n$ in $C$ exist for every $n$.
- To prove completeness, fix $n$ and suppose no such pair exists in $C$. Then each class of $\equiv_n$ lies inside $P$ or misses $P$, on $C$. There are finitely many classes, each defined by one sentence, and the disjunction over the classes inside $P$ defines $P$ in $C$.
- Locality theorems of Hanf and of Gaifman give quick strategies for Duplicator on structures that look the same around each point; see [[finite model theory|CBPS8B13S4]].
- Definable reductions transfer the result: if $Q$ is defined from $P$ by first-order formulas and $Q$ is not definable, neither is $P$. This is how connectivity reduces to parity.

### History

The game form of the method is due to Ehrenfeucht, who introduced the games in 1961 to study the completeness of theories.

### Common errors

- To give strategies only for some $n$. The pairs must exist for every $n$.
- To use structures of bounded size. A single sentence describes each finite structure up to isomorphism, so the sizes must grow with $n$.
- To forget that both structures must lie in the class under study, for instance both must be finite graphs.

## Explanations

### L1 human

To show that first-order logic cannot express a property, we play a game.
For each number $n$ we find two structures, one with the property and one without, that no sentence with $n$ nested quantifiers can tell apart.
Any sentence has some number of nested quantifiers, so no sentence can tell all these pairs apart, and no sentence expresses the property.

### L2 human

We prove that "the set has even size" is not first-order on finite sets.

1. Fix $n \ge 1$. Let $\mathcal{A}_n$ be a set of $2n$ elements and $\mathcal{B}_n$ a set of $2n + 1$ elements.
2. Both have at least $n$ elements, so Duplicator wins $G_n$ by [[the game on finite sets|X98C7KEQRV]].
3. A sentence $\sigma$ of rank $n$ that says "even" would hold in $\mathcal{A}_n$ and fail in $\mathcal{B}_n$, against the theorem.

The typical use of the method is inside finite model theory.
A trap is the reduction direction: to transfer non-definability from $Q$ to $P$, $Q$ must be definable from $P$, not the other way around.

### L3 human

The method is the basis of descriptive complexity lower bounds.
First-order logic with order and arithmetic on finite structures captures uniform $\mathrm{AC}^0$.
The game argument shows that parity is not definable with order alone, and the much harder circuit result that [[parity is not in AC0|W6T7X0QCFH]] shows that arithmetic does not help.
Pebble games and Hanf-locality arguments extend the method to finite-variable logics, counting logics and fixed-point logics.
