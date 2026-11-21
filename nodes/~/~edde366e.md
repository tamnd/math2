---
tag: ~edde366e
kind: concept
name: Hyperimaginaries
aliases: [hyperimaginaries, hyperimaginary, hyperimaginary-element, elimination-of-hyperimaginaries]
msc: ["03C45"]
topics: [SZRM3N6BXW]
audience: research
uses: [~25317890, ~f002ea16, EYTTQZ0E1S, 9V71Q3SD1G, 0G8VEZ3WTK, T7JW5QY6KR, 1NR3HAWG9D]
sources:
  - book: isbn:9780521119559
  - book: isbn:9780521763240
---

## Summary

Let $T$ be a complete theory with [[monster model|EYTTQZ0E1S]] $\mathbb{M}$.
A *hyperimaginary* is a class $\bar a / E$ of an [[equivalence relation|0G8VEZ3WTK]] $E$ on small tuples that is defined by a partial [[type|9V71Q3SD1G]] over $\emptyset$, rather than by one formula.
Hyperimaginaries extend [[imaginary elements|~25317890]], which are the classes of $\emptyset$-definable relations.
A hyperimaginary is *eliminable* if it is interdefinable with a sequence of imaginaries, and $T$ *eliminates hyperimaginaries* if all of them are eliminable.
The exact page is [[this definition|~bba20a81]].

## Motivation

Imaginaries suffice for most of stability theory, where canonical bases of types are sequences of imaginaries.
Beyond stable theories, natural objects are fixed by the automorphisms that fix a type-definable class, and no sequence of imaginaries need have the same stabilizer.
Canonical bases of types in simple theories are of this kind.
Hyperimaginaries give names to these objects, so that closure operators and canonical bases can be formed in the same way as with imaginaries.
Elimination of hyperimaginaries is then the statement that nothing beyond $\mathbb{M}^{\mathrm{eq}}$ is needed.

## Notation

A hyperimaginary is written $e = \bar a_E$ or $\bar a / E$.
Its definable closure $\operatorname{dcl}(e)$ is the set of hyperimaginaries fixed by every automorphism that fixes $e$.
Its bounded closure $\operatorname{bdd}(e)$ is the set of hyperimaginaries with a small orbit under those automorphisms.
Hyperimaginaries do not form a structure: there is no sort for them, and they are handled through automorphisms and types.

## Remarks

### Examples

- Every imaginary $\bar a / E$ with $E$ a $\emptyset$-definable relation is a hyperimaginary.
- Every small tuple $\bar a$, finite or infinite, is a hyperimaginary for the relation of equality.
- In a non-archimedean real closed field, the class of $a$ for the relation "infinitely close" is a hyperimaginary; see [[this example|~99697a21]].
- The intersection of a decreasing chain of definable equivalence relations, each splitting every class in two, has eliminable hyperimaginaries; see [[this example|~fc1ebceb]].
- The finest bounded $\emptyset$-type-definable equivalence relation $E_{\mathrm{KP}}$ on $n$-tuples exists, and its classes are the Kim-Pillay strong types. They are bounded hyperimaginaries.

### Non-examples

- In a real closed field, "at finite distance" is an equivalence relation that is not type-definable; see [[this example|~decee435]].
- In a nonstandard model of [[Presburger arithmetic|4W0E9G7PPV]], the relation $x - y \in \mathbb{Z}$ is not type-definable. If it were, its complement, defined by the formulas $x - y \neq n$, would also be type-definable, so the relation would be definable by [[compactness|1NR3HAWG9D]]. Then the set $\set{x \ge 0 : x - 0 \in \mathbb{Z}}$ of standard nonnegative elements would be a definable set with no maximum and bounded above, which is impossible in a model of Presburger arithmetic.

### Basic properties

- If $\pi(\bar x, \bar y)$ defines an equivalence relation on finite tuples, compactness gives formulas $\varphi_i$ in $\pi$, reflexive and symmetric, such that for each $i$ some $j$ has $\varphi_j \circ \varphi_j \subseteq \varphi_i$, and $E$ is the intersection of the $\varphi_i$.
- If $E$ is bounded, it has at most $2^{|T| + |\alpha|}$ classes on $\alpha$-tuples, so boundedness does not depend on the monster.
- An automorphism fixes $e = \bar a / E$ exactly when it maps $\bar a$ into the class $e$.
- If $E$ is an intersection of $\emptyset$-definable equivalence relations $E_i$, each on finitely many of the coordinates, then $\bar a / E$ is interdefinable with the sequence $(\bar a / E_i)_i$.
- In a [[stable theory|T7JW5QY6KR]], every $\emptyset$-type-definable equivalence relation is such an intersection, so stable theories eliminate hyperimaginaries. In a stable theory, $E_{\mathrm{KP}}$ is the intersection of the $\emptyset$-definable equivalence relations with finitely many classes.

### History

Pillay and Poizat proved in 1987 that, in a stable theory, type-definable equivalence relations are intersections of definable ones.
Hart, Kim and Pillay introduced hyperimaginaries in their work on canonical bases in simple theories, published in 2000.
Buechler, Pillay and Wagner proved in 2001 that supersimple theories eliminate hyperimaginaries.

### Common errors

- Taking a type-definable relation on finite tuples for a definable one. Its classes are imaginaries only when one formula defines it.
- Taking an $\emptyset$-invariant relation for a type-definable one. Invariance under automorphisms is weaker, as the non-examples show.
- Reading elimination of hyperimaginaries as "every type-definable class is definable". Elimination only asks for interdefinability with some sequence of imaginaries.

## Explanations

### L1 human

Imaginary elements name the groups of a sorting rule given by one test.
Hyperimaginaries name the groups of a sorting rule given by infinitely many tests, all of which must pass.
For example, two numbers are "infinitely close" when they pass the tests "closer than $1$", "closer than $\tfrac12$", "closer than $\tfrac13$", and so on.
The hope, called elimination of hyperimaginaries, is that each such group can be named by an infinite list of ordinary imaginary names.

### L2 human

We check that the relation of a decreasing chain of definable relations has eliminable classes.

1. Let $E_0 \supseteq E_1 \supseteq \cdots$ be $\emptyset$-definable equivalence relations, and $E = \bigcap_n E_n$.
2. $E$ is type-defined by $\set{E_n(\bar x, \bar y) : n \in \mathbb{N}}$.
3. Let $e = \bar a / E$ and $d = (\bar a / E_n)_n$. An automorphism $\sigma$ fixes $d$ exactly when $E_n(\sigma \bar a, \bar a)$ for all $n$.
4. That is the condition $E(\sigma \bar a, \bar a)$, which says that $\sigma$ fixes $e$.
5. So $e$ and $d$ have the same stabilizer, and they are interdefinable.

The typical use is to reduce a question about $\bar a / E$ to the imaginaries $\bar a / E_n$.
A trap is to forget that a type-definable relation need not be such an intersection, outside stable theories.

### L3 human

In a simple theory, types over boundedly closed sets have canonical bases, and Hart, Kim and Pillay showed that these exist as hyperimaginaries.
Elimination of hyperimaginaries makes each canonical base interdefinable with a sequence of imaginaries, as in stable theories.
Bounded hyperimaginaries give the Kim-Pillay strong types.
The Lascar strong types refine them, and a theory is *G-compact* when the two notions agree.
In a stable theory, both notions agree with Shelah's strong types.
