---
tag: SERN6CRVWW
kind: concept
name: Monadic predicate calculus
aliases: [first-order-monadic-predicate-logic, monadic-first-order-logic, monadic-logic, monadic-predicate-logic]
msc: ["03B10", "03B25"]
topics: [E4AVTNWE9E]
audience: ug2
uses: [086QKPF0A6, HYJ10AF6RT, 983GZBQYT4, QN7M1JCGT9, 5SDS9T8E7J]
sources:
  - wikipedia: en:8015680@r1371775840
    locator: Monadic predicate calculus
    note: adopted
    mention: wikipedia://en/8015680
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Monadic_predicate_calculus
    locator: lead section
same_as:
  wikidata: Q6897882
  wikipedia: Monadic predicate calculus
inventory: [5SSXBYC1X5]
---

## Summary

Take the sentence $\forall x \, (P(x) \to Q(x)) \wedge \exists x \, P(x) \wedge \exists x \, \neg Q(x)$.
Each atom talks about one element at a time, so a structure matters only through how many elements lie in each of the four regions of a Venn diagram for $P$ and $Q$.
Two elements, one in $P \cap Q$ and one outside both, make the sentence true.

The monadic predicate calculus is the fragment of [[first-order logic|086QKPF0A6]] whose signature consists only of unary relation symbols $P_1, \ldots, P_k$, with no function symbols and no constant symbols.
So each atomic [[formula|HYJ10AF6RT]] has the form $P_i(x)$ for a variable $x$, or $x = y$ when the logic includes equality.
The fragment is decidable: an algorithm decides whether a monadic sentence is [[satisfiable|QN7M1JCGT9]] or [[valid|5SDS9T8E7J]].
It is the classical example of a decidable fragment, and a single binary relation symbol already makes first-order logic undecidable.

## Motivation

Much of ordinary reasoning is about properties of one object at a time.
The syllogism "every man is mortal, every Greek is a man, so every Greek is mortal" uses three properties and no relations between objects.
In first-order logic it becomes $\forall x \, (G(x) \to H(x)) \wedge \forall x \, (H(x) \to D(x)) \to \forall x \, (G(x) \to D(x))$.
Boole and Venn treated such reasoning as calculation with sets, and a [[Venn diagram|0KCT6DPXJK]] decides it by inspecting regions.
The monadic predicate calculus is the exact first-order form of this calculus of classes, and its decidability explains why the diagrams work.

## Notation

For a structure $\mathcal{A}$ and an element $a$, the type of $a$ is the set $\{ i : a \in P_i^{\mathcal{A}} \}$.
There are $2^k$ possible types, one for each region of a Venn diagram of $k$ sets.
For a type $\tau \subseteq \{ 1, \ldots, k \}$, the formula $\tau(x)$ is $\bigwedge_{i \in \tau} P_i(x) \wedge \bigwedge_{i \notin \tau} \neg P_i(x)$.
The quantifier rank of a formula is the largest number of nested quantifiers in it.
Some books write MFO or $\mathrm{FO}^1$ for the fragment, and some distinguish the case "with equality" from the case "without equality".

## Remarks

### Examples

The syllogism of the motivation is a valid monadic sentence, as [[the syllogism Barbara as a monadic sentence|PRG93K4Z81]] shows.
The sentence of the summary is monadic and satisfiable with two elements, and [[deciding a monadic sentence by types|8TCDB2FMXC]] works it out.
The sentence $\exists x \, \exists y \, \exists z \, (x \neq y \wedge x \neq z \wedge y \neq z)$ says "there are at least three elements", and it is monadic with equality and $k = 0$.
The sentence $\forall x \, (P(x) \vee \neg P(x))$ is monadic and valid, because each element is in $P$ or not in $P$.

### Non-examples

[[A sentence with only infinite models|KH3ZG4RXAW]] uses a binary relation symbol $<$, so it is not monadic.
It also shows that the finite model property fails outside the monadic fragment.

The sentence $\forall x \, P(f(x))$ uses a function symbol $f$, so it is not monadic, although $f$ takes one argument.

A sentence of monadic second-order logic, such as $\exists X \, \forall x \, X(x)$, quantifies over sets.
It belongs to [[second-order logic|G6X7SZSNC5]], not to the monadic predicate calculus.

### Basic properties

A satisfiable monadic sentence with $k$ predicates and quantifier rank $q$ has a model with at most $\max(q, 1) \cdot 2^k$ elements, and with at most $2^k$ elements when there is no equality.
This is the [[finite model property of the monadic predicate calculus|AS0NHQMAKA]].
So satisfiability and validity of monadic sentences are decidable: the algorithm checks the finitely many structures up to that size.

A monadic structure is determined, up to isomorphism, by the number of elements of each type.
A sentence of quantifier rank $q$ can only count each type up to $q$.

Adding one binary relation symbol makes validity undecidable, by the strong form of [[Church's theorem|VA6BNNY2YC]].
Adding one unary function symbol destroys the finite model property: "$f$ is injective and not surjective" has only infinite models.

### History

Löwenheim proved in 1915 that the monadic fragment is decidable, in the same paper that contains the first form of the [[Löwenheim-Skolem theorem|484M0TZ1S7]].
Behmann gave in 1922 a decision procedure by elimination of quantifiers, which also covers quantification over the unary predicates.
The [[Entscheidungsproblem|DJNYM72Z4G]] of Hilbert and Ackermann asked for an extension of such procedures to all of first-order logic, and Church and Turing showed in 1936 that none exists.

### Watch out

"Monadic" does not mean "with one variable".
A monadic sentence may use many variables, and only the relation symbols are restricted to one argument.

Remember equality when you compute the size bound.
Without equality, $2^k$ elements suffice.
With equality, the sentence "there are at least $q$ elements" has rank $q$ and needs $q$ elements even for $k = 0$.

Do not confuse the monadic predicate calculus with monadic second-order logic.
The second allows quantifiers over sets, and with a binary relation symbol it is undecidable, since it contains first-order logic.

## Explanations

### L1 human

In the monadic predicate calculus, every statement talks about properties of single objects, like "is red" or "is round".
A collection of objects then splits into groups by which properties each object has: red and round, red and not round, and so on.
With two properties there are four groups, and a statement can only ask which groups are empty or how many members they have, up to a small number.
So to test a statement, one can try all small collections, and this test always ends.
For example, "if everything red is round and something is red, then something is round" is true in every collection.

### L2 human

We decide whether $\sigma = \forall x \, (P(x) \to Q(x)) \wedge \exists x \, (P(x) \wedge \neg Q(x))$ is satisfiable.

1. The predicates are $P$ and $Q$, so $k = 2$ and there are four types: $PQ$, $P\bar{Q}$, $\bar{P}Q$ and $\bar{P}\bar{Q}$, where a bar means "not".
2. The first conjunct says that no element has type $P\bar{Q}$.
3. The second conjunct says that some element has type $P\bar{Q}$.
4. The two conditions contradict each other, so no structure satisfies $\sigma$.
5. The finite model property confirms this by a finite search.
   The sentence $\sigma$ has no equality and $k = 2$, so it suffices to check the structures with at most $4$ elements, and none of them is a model.

The typical use of the monadic predicate calculus is to check syllogisms and statements about classes.
A trap is to add a relation such as "is a parent of": the statement is then no longer monadic, and the finite search is no longer a complete method.

### L3 human

The monadic fragment is the simplest of the decidable classes of the classical decision problem, which also include the [[decidable prefix classes|ZF79MZRQ8V]], the [[two-variable fragment|S7C3C7DJRF]] and the [[guarded fragment|Y7YS1C3GAE]].
Each of these has a form of the finite model property, and each fails as soon as one adds enough binary structure to code a grid or a Turing machine.
Monadic second-order logic over unary predicates alone is still decidable, by Behmann's elimination.
Monadic second-order logic over the successor relation on $\mathbb{N}$ is decidable by the automata method, as [[Büchi's theorem on S1S|YPDXVTH5JR]] shows.
