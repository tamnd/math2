---
tag: CY1TXHF6KQ
kind: concept
name: Definable set
msc: ["03C07", "03C40"]
topics: [AY09KYSW81]
audience: ug2
uses: [983GZBQYT4, HYJ10AF6RT, 1WTCZB4DVB, DSQ17TNW1C, NDTJ2E895C]
sources:
  - url: https://en.wikipedia.org/wiki/Definable_set
    locator: Definition; Invariance under automorphisms
  - url: https://en.wikipedia.org/wiki/Model_theory
    locator: Definable sets
  - book: isbn:9780387987606
    locator: Section 1.3
same_as:
  wikidata: Q2895824
  wikipedia: Definable set
---

## Summary

Let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]] with domain $M$, and let $A \subseteq M$.
A set $X \subseteq M^n$ is *definable over $A$* when there are a first-order [[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n, y_1, \dots, y_m)$ and parameters $\bar{b} \in A^m$ with $X = \set{\bar{a} \in M^n : \mathcal{M} \models \varphi(\bar{a}, \bar{b})}$.
For $A = \emptyset$ the set is *$\emptyset$-definable*, or definable without parameters; for $A = M$ it is simply *definable*.
Definable sets are closed under Boolean operations, products and projections, and every [[automorphism|DSQ17TNW1C]] that fixes $A$ pointwise maps each $A$-definable set onto itself.
Definable sets are the main objects of modern model theory, and their behavior, for example in o-minimal or stable structures, measures how complicated a structure is.

## Motivation

Algebraic geometry studies the sets cut out by polynomial equations, and real algebraic geometry adds inequalities.
Both are cases of definable sets: in the field $\C$, the definable sets are the sets built from zero sets of polynomials by Boolean operations and projections.
A model-theoretic result about definable sets, such as quantifier elimination, then says which shapes these sets can have.
For instance, Tarski's theorem for the real field says that the projection of a semialgebraic set is semialgebraic.

## Notation

Common notations for the set defined by $\varphi(\bar{x}, \bar{b})$ are $\varphi(M, \bar{b})$ and $\varphi(\mathcal{M}^n, \bar{b})$.
Mathlib writes `A.Definable L s` for a set `s : Set (α → M)` that is definable over `A : Set M`; this is `Set.Definable`, and the same predicate is bound on the [[definition node|1DQ1M6ZWS4]].
A function $f \colon M^n \to M$ is *definable* when its graph is a definable subset of $M^{n+1}$.

## Remarks

### Examples

- The successor relation in $(\Z, <)$; see [[this example|P50P8AZNEE]].
- The even numbers in $(\N, +)$; see [[this example|JY67Q6H6H9]].
- The order in the field of reals, by $\exists z \, (y = x + z \cdot z \land \neg(x = y))$; see [[this example|TCJZNK8PT2]].
- Divisibility and the primes in $(\N, +, \cdot)$; see [[this example|BD4PEHWBRX]].
- In $(\Z, <, 0)$ the set $\set{1}$ is $\emptyset$-definable; see [[this example|~0804090f]].

### Non-examples

- The positive integers in $(\Z, +)$; see [[this non-example|9ZGWM7XXJ5]].
- The order in $(\Z, +)$; see [[this non-example|~8dc06e57]].
- The set $\set{0}$ in $(\R, <)$ without parameters, since $x \mapsto x + 1$ is an automorphism that moves it.

### Basic properties

- If $X, Y \subseteq M^n$ are $A$-definable, so are $X \cup Y$, $X \cap Y$, $M^n \setminus X$, $X \times Y$ and the projection of $X$ to any set of coordinates.
- If $\sigma$ is an automorphism of $\mathcal{M}$ that fixes $A$ pointwise, then $\sigma(X) = X$ for every $A$-definable $X$; this follows from [[isomorphism invariance|NDTJ2E895C]].
- The converse fails. In $(\N, +, \cdot, 0, 1)$ each $n$ is the value of the term $1 + \cdots + 1$, so the identity is the only automorphism and every subset of $\N$ is invariant; but there are only countably many formulas, hence countably many definable sets, and uncountably many subsets of $\N$.
- Images and preimages of definable sets under definable functions are definable.

### History

Tarski gave a precise definition of definable sets of real numbers in a paper of 1931.
Tarski's quantifier elimination for real closed fields, with an independent proof by Seidenberg published in 1954, describes the definable sets of the real field as the semialgebraic sets.

### Common errors

- To forget parameters. A set may be definable with parameters and not without them, as $\set{0}$ in $(\R, <)$ shows.
- To use automorphisms to prove definability. Automorphism invariance is necessary for $\emptyset$-definability, and in general not sufficient.
- To confuse definability in a structure with definability in a substructure or a reduct; the formulas range over the whole domain of the structure in question.

## Explanations

### L1 human

A definable set is a set that you can describe by a first-order formula in the language of the structure.
In the field of real numbers, the set of nonnegative numbers is definable by the formula "$x$ is a square", that is, $\exists y \, (y \cdot y = x)$.
The unit circle is definable by $x \cdot x + y \cdot y = 1$.
In the ordered set $(\R, <)$ without parameters, no single number can be defined, because a shift $x \mapsto x + c$ preserves the order.

### L2 human

We show that the function $f(x) = x^{-1}$ for $x \ne 0$, with $f(0) = 0$, is $\emptyset$-definable in the field $(\R, +, \cdot, 0, 1)$.

1. The graph of $f$ is $\set{(x, y) : (x = 0 \land y = 0) \lor x \cdot y = 1}$.
2. For $x \ne 0$, $x \cdot y = 1$ holds exactly for $y = x^{-1}$; for $x = 0$, $x \cdot y = 1$ fails for every $y$, and $y = 0$ is the only value allowed.
3. So the formula $(x = 0 \land y = 0) \lor x \cdot y = 1$ defines the graph, and $f$ is definable.

The typical use of automorphisms is the opposite direction: to show that a set is not definable.
A trap is to write a "formula" that quantifies over subsets or natural numbers; such a description does not show first-order definability.

### L3 human

The family of all definable sets of a structure, with Boolean operations and projections, is the main invariant studied by geometric model theory.
In an [[o-minimal|QS8ZBPAFJN]] structure, the definable subsets of the line are finite unions of points and intervals, and stability and [[NIP|RS09CRTDRA]] are conditions on the combinatorics of definable families; see also [[stable theories|2T8HMVV8SB]].
Quotients of definable sets by definable equivalence relations, the imaginaries, and interpretations between structures are treated in the sub-area on [[interpretations|SZRM3N6BXW]].
