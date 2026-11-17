---
tag: 983GZBQYT4
kind: concept
name: Structure
aliases: [interpretation, model-theoretic-structure]
msc: ["03C07", "03B10"]
topics: [NJDME6F845]
audience: ug2
uses: [WDVVEYD6AT, 0BSJ7RQ9BW, 0EPAT51DXQ, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_(mathematical_logic)
    locator: Definition
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Empty domains
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://builds.openlogicproject.org/
    locator: Syntax and Semantics
same_as:
  wikidata: Q1851710
  wikipedia: Structure (mathematical logic)
---

## Summary

Let $L$ be a [[signature|WDVVEYD6AT]], that is, a set of constant symbols, function symbols and relation symbols, each function and relation symbol with an arity $n \geq 1$.
An $L$-structure $\mathcal{M}$ consists of a nonempty [[set|0BSJ7RQ9BW]] $M$, called the domain or universe of $\mathcal{M}$, and an interpretation of each symbol of $L$ on $M$.
The interpretation of a constant symbol $c$ is an element $c^{\mathcal{M}} \in M$.
The interpretation of an $n$-ary function symbol $f$ is a [[function|0EPAT51DXQ]] $f^{\mathcal{M}} \colon M^n \to M$, defined at every $n$-tuple of $M$.
The interpretation of an $n$-ary relation symbol $R$ is a subset $R^{\mathcal{M}} \subseteq M^n$ of the [[Cartesian power|09CEDJYBKP]] $M^n$.
Structures matter because a first-order formula has no truth value on its own: it becomes true or false only in a structure, and groups, rings, orders and graphs are all structures.

## Motivation

The axiom $\forall x \, \forall y \, (x \cdot y = y \cdot x)$ is a string of symbols.
It is true for the integers under addition and false for the invertible $2 \times 2$ matrices under multiplication.
So the truth of a formula depends on what the symbols mean.
To speak about truth in a precise way, we need a precise notion of "a meaning for each symbol".
A structure is exactly this: one set over which the variables range, and one object of the right type for each symbol.
With this notion, Tarski's definition of [[satisfaction|2RBQPV02AS]] gives each formula a truth value in each structure, and the words [[model|MVCH6N9SNW]], [[validity|5SDS9T8E7J]] and [[logical consequence|1HK0VYWTV7]] get exact meanings.

## Notation

We write a structure with a calligraphic letter $\mathcal{M}$, $\mathcal{N}$ and its domain with the matching italic letter $M$, $N$.
Enderton writes $\mathfrak{A}$ for the structure and $|\mathfrak{A}|$ for its domain.
A structure with a short signature is often written as a tuple, such as $(\Z, +, 0, <)$, with the symbols in a fixed order.
In this tuple notation the same letter often names the symbol and its interpretation, so $+$ means both the symbol of $L$ and the addition of integers.
In Mathlib, `FirstOrder.Language.Structure L M` is a type class on a type `M`, with the fields `funMap` and `RelMap`; constants are function symbols of arity $0$.

Books differ on the empty domain.
This page, Enderton, Mendelson and most textbooks require $M \neq \emptyset$.
Mathlib allows the empty type as a domain, and so does [[inclusive first-order logic|YXYF6JQXBT]].
The choice changes which formulas are [[valid|5SDS9T8E7J]]: $\exists x \, (x = x)$ is valid with nonempty domains and false in the empty structure.

## Remarks

### Examples

1. The [[natural numbers as a structure for the language of arithmetic|~a6c22843]]: the domain $\N = \set{0, 1, 2, \ldots}$, with $0$, the successor $n \mapsto n + 1$, addition, multiplication and the order $<$. Each operation of $\N$ gives a value in $\N$, so each symbol has an interpretation.
2. Each [[group|G5S1M9]] $(G, \cdot, e, {}^{-1})$ is a structure for the signature with one binary function symbol, one constant symbol and one unary function symbol. The group axioms are not part of the definition of a structure; they are sentences that this structure satisfies.
3. A [[directed graph as a structure|~3db99883]]: one binary relation symbol $E$, interpreted as the set of edges. Every subset of $V \times V$ is allowed, so every directed graph with vertex set $V$ is a structure.
4. The field of real numbers $(\R, +, \cdot, 0, 1)$ and the ordered field $(\R, +, \cdot, 0, 1, <)$ are structures for two different signatures. The second one has one more symbol.
5. For the empty signature, a structure is just a nonempty set. Two such structures differ only in the size of the domain.

### Non-examples

1. The real numbers with [[division|~0f8713fc]] do not form a structure for a signature with one binary function symbol. The condition that fails is totality: $1 / 0$ has no value.
2. The natural numbers with $n \mapsto n - 1$ do not form a structure for a signature with one unary function symbol. The condition that fails is that the value lies in the domain: $0 - 1 = -1 \notin \N$.
3. The set $\set{1, 2, 3}$ with a constant symbol $c$ interpreted as $5$ is not a structure. The condition that fails is $c^{\mathcal{M}} \in M$.
4. Under the convention of this page, the empty set with the empty signature is not a structure. The condition that fails is $M \neq \emptyset$.

### Basic properties

1. The same set carries many structures for one signature. For one binary relation symbol and a domain with $n$ elements, there are exactly $2^{n^2}$ structures with that domain, because $R^{\mathcal{M}}$ can be any of the $2^{n^2}$ subsets of $M^2$.
2. Each term $t$ of $L$ gets a value in $M$ once each variable gets a value; see [[satisfaction|2RBQPV02AS]] for the recursive definition.
3. Let $L \subseteq L'$ be two signatures. An $L'$-structure $\mathcal{N}$ gives an $L$-structure $\mathcal{N} \restriction L$, the reduct, with the same domain and with the interpretations of the symbols of $L'$ outside $L$ forgotten. Conversely $\mathcal{N}$ is an expansion of $\mathcal{N} \restriction L$. The [[coincidence lemma|~7b107606]] shows that an $L$-formula has the same truth value in $\mathcal{N}$ and in $\mathcal{N} \restriction L$.
4. Maps between structures that respect the interpretations are [[homomorphisms|KBXSZC6BV1]]; the bijective ones whose inverses are also homomorphisms are [[isomorphisms|PZMGQMDN25]]. [[Isomorphic structures satisfy the same sentences|~5166a0b3]].
5. A subset of $M$ that contains each $c^{\mathcal{M}}$ and is closed under each $f^{\mathcal{M}}$ carries a [[substructure|676H7EGTKJ]], with the restricted interpretations.

### History

Tarski's 1933 work on truth defined truth for formalized languages with one fixed intended meaning.
The definition of truth relative to an arbitrary structure became standard with the work of Tarski and his school in the 1950s, in particular Tarski and Vaught's 1957 paper "Arithmetical extensions of relational systems".
In that period structures were also called relational systems, and Mal'cev called them algebraic systems.

### Common errors

- Confusing a symbol with its interpretation. The symbol $<$ of $L$ has no meaning; the set $<^{\mathcal{M}}$ is a relation on one particular domain.
- Forgetting that a function symbol needs a total function. A partial operation such as division on $\R$ must be modelled as a relation, or on a smaller domain such as $\R \setminus \set{0}$.
- Thinking that a structure must satisfy some axioms. Any interpretation of the right types is a structure; being a group or an order is a property that some structures have.

## Explanations

### L1 human

A formal language has symbols such as $+$, $0$ and $<$, but the symbols alone mean nothing.
A structure picks a set of objects and says what each symbol means for these objects.
For example, take the numbers $0, 1, 2, 3, \ldots$ and let $+$ mean ordinary addition, $0$ mean zero and $<$ mean "is less than".
Then the statement "for each number there is a bigger number" becomes true.
Take instead the numbers $0, 1, 2$ only, with the same meaning of $<$.
Now the same statement is false, because nothing is bigger than $2$.
So the same symbols can describe many different worlds, and each world is one structure.

### L2 human

We check that a small set with an operation is a structure, and we compute in it.
Let $L = \set{+, 0}$, with $+$ a binary function symbol and $0$ a constant symbol.
Let $M = \set{0, 1, 2}$, let $+^{\mathcal{M}}$ be addition modulo $3$, and let $0^{\mathcal{M}} = 0$.

1. The domain $M$ is nonempty, because $0 \in M$.
2. The constant symbol gets the element $0^{\mathcal{M}} = 0$, and $0 \in M$.
3. Addition modulo $3$ is defined for all $9$ pairs in $M^2$, and each value is a remainder modulo $3$, so it lies in $M$. Thus $+^{\mathcal{M}} \colon M^2 \to M$ is a function.
4. So $\mathcal{M} = (\set{0, 1, 2}, +^{\mathcal{M}}, 0)$ is an $L$-structure.
5. With $x$ given the value $2$, the term $(x + x) + 0$ has the value $(2 + 2) \bmod 3 = 1$, and then $(1 + 0) \bmod 3 = 1$.

The typical use is to read an axiom system as a signature plus sentences, and its intended objects as structures for that signature.
A trap is to forget the totality condition: ordinary addition on $\set{0, 1, 2}$ is not an interpretation, because $2 + 2 = 4 \notin M$.

### L3 human

A structure for a signature with only function and constant symbols is an algebra in the sense of [[universal algebra|W82R6N0GM9]], and a structure with only relation symbols is a [[relational structure|MJF9M19E3E]].
The $L$-structures and their homomorphisms form a category, with products, substructures and quotients by congruences, and much of algebra is the study of special classes of structures.
Many-sorted structures have one domain for each sort; they reduce to one-sorted structures with one unary relation for each sort.
In Mathlib a structure is a type class instance on a type, so one type can carry several structures, and the domain may be empty.
Model theory studies structures up to [[elementary equivalence|P3B1V182N4]], the relation of having the same true first-order sentences, and it classifies the [[elementary classes|MEC3ZMC4F1]] of structures.
