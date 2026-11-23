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

A formula of first-order logic is only a string of symbols until we say what its variables range over and what its symbols mean.
A structure supplies exactly that: one set of objects, and one meaning for each symbol.
Take the sentence $\forall x \, \exists y \, (x < y)$.
Read over the integers with the usual order, the structure $(\mathbb{Z}, <)$, it says that every integer has a larger one, and that is true.
Read over the set $\{0, 1, 2\}$ with the usual order, it is false, because nothing is larger than $2$.
The symbols did not change, only the structure did.

In exact terms, let $L$ be a [[signature|WDVVEYD6AT]]: a set of constant symbols, function symbols and relation symbols, where each function and relation symbol has an arity $n \geq 1$.
An $L$-structure $\mathcal{M}$ consists of a nonempty [[set|0BSJ7RQ9BW]] $M$, the domain of $\mathcal{M}$, together with the following interpretations:
$$c^{\mathcal{M}} \in M, \qquad f^{\mathcal{M}} \colon M^n \to M, \qquad R^{\mathcal{M}} \subseteq M^n,$$
one for each constant symbol $c$, each $n$-ary function symbol $f$ and each $n$-ary relation symbol $R$ of $L$.
Here $f^{\mathcal{M}}$ is a [[function|0EPAT51DXQ]] defined on all of the [[Cartesian power|09CEDJYBKP]] $M^n$.
The [[formal definition|Y6C40MHZZC]] lists these conditions one by one.

## Motivation

The axiom $\forall x \, \forall y \, (x \cdot y = y \cdot x)$ is true for the integers under addition and false for the invertible $2 \times 2$ matrices under multiplication.
So whether a formula is true depends on what its symbols mean, and we need an exact notion of "a meaning for each symbol" before we can speak of truth.
A structure is that notion.
It fixes one domain for all the variables, and one object of the right type for each symbol.

Once structures are in place, Tarski's definition of [[satisfaction|2RBQPV02AS]] gives every formula a truth value in every structure.
The words [[truth|K7XDVK5854]], [[model|MVCH6N9SNW]], [[validity|5SDS9T8E7J]] and [[logical consequence|1HK0VYWTV7]] then get exact meanings, and all of them are statements about structures.
Groups, rings, fields, orders and graphs are all structures for suitable signatures, which is why one theory of truth covers all of algebra at once.

## Notation

We write a structure with a calligraphic letter such as $\mathcal{M}$ or $\mathcal{N}$, and its domain with the matching italic letter $M$ or $N$.
Enderton writes $\mathfrak{A}$ for a structure and $|\mathfrak{A}|$ for its domain.
A structure with a short signature is often written as a tuple, such as $(\mathbb{Z}, +, 0, <)$, with the interpretations in a fixed order.
In a tuple the same sign names the symbol and its meaning, so $<$ is both a symbol of $L$ and the order of the integers.
In Mathlib, `FirstOrder.Language.Structure L M` is a type class on a type `M`, with fields `funMap` and `RelMap`, and a constant is a function symbol of arity $0$.

## Remarks

### Three structures to keep in mind

The standard model of arithmetic is the [[natural numbers with zero, successor, addition, multiplication and order|WP27CABPA4]].
Its domain is $\mathbb{N} = \{0, 1, 2, \ldots\}$, and each operation sends natural numbers to natural numbers, so each function symbol gets a total function.

A [[directed graph is a structure|1VQ21DC4Z8]] for the signature with one binary relation symbol $E$.
The domain is the set of vertices, and $E^{\mathcal{M}}$ is the set of edges.
Any subset of $M^2$ is allowed, so every directed graph is a structure.

A group $(G, \cdot, e, {}^{-1})$ is a structure for a signature with a binary function symbol, a constant symbol and a unary function symbol.
The group axioms play no role in the definition.
They are sentences that some structures of this signature satisfy and others do not.

### What is not a structure

Every failure comes from one of the conditions on the interpretations.
[[Division on the real numbers|MFWJEH5022]] does not interpret a binary function symbol, because $1 / 0$ has no value, so the function is not total.
Subtraction by one, $n \mapsto n - 1$, does not interpret a unary function symbol on $\mathbb{N}$, because $0 - 1 = -1$ lies outside the domain.
On the domain $\{1, 2, 3\}$, a constant symbol cannot be interpreted as $5$, because $c^{\mathcal{M}}$ must lie in $M$.
Finally, the empty set is not a domain under the convention we follow.

### The empty domain

Books differ on whether the domain may be empty.
Enderton, Mendelson and most textbooks require $M \neq \emptyset$, and we do the same.
Mathlib allows an empty type as a domain, and so does [[inclusive first-order logic|YXYF6JQXBT]].
The choice matters, because it changes which sentences are valid.
For example, $\exists x \, (x = x)$ is true in every nonempty structure, but false in an empty one, since there is nothing to serve as $x$.
The [[drinker paradox|8BMQTZZEWB]] is valid for the same reason.

### Many structures on one set

One set carries many structures for the same signature.
For a single binary relation symbol and a domain with $n$ elements, the relation $R^{\mathcal{M}}$ can be any subset of $M^2$, so there are
$$2^{n^2}$$
structures with that domain.
Check: for $n = 2$, the set $M^2$ has $4$ pairs and so $2^4 = 16$ subsets.

Two signatures can also share a domain.
The field $(\mathbb{R}, +, \cdot, 0, 1)$ and the ordered field $(\mathbb{R}, +, \cdot, 0, 1, <)$ are structures for different signatures, and the second has one more symbol.
When $L \subseteq L'$, an $L'$-structure $\mathcal{N}$ gives an $L$-structure $\mathcal{N} \restriction L$, the reduct, by forgetting the extra symbols.
In the other direction, $\mathcal{N}$ is an expansion of its reduct.
The [[coincidence lemma|FM580NZ9W6]] shows that an $L$-formula has the same truth value in both.

### Maps between structures

A map between two $L$-structures that respects the constants, the functions and the relations is a [[homomorphism|KBXSZC6BV1]].
A bijective homomorphism whose inverse is also a homomorphism is an [[isomorphism|PZMGQMDN25]], and [[isomorphic structures satisfy the same sentences|NDTJ2E895C]].
A subset of $M$ that contains every $c^{\mathcal{M}}$ and is closed under every $f^{\mathcal{M}}$ carries a [[substructure|676H7EGTKJ]], with the restricted interpretations.

### Watch out

A symbol is not its interpretation.
The symbol $<$ of $L$ has no meaning on its own, while $<^{\mathcal{M}}$ is a set of pairs from one particular domain.
In $(\mathbb{Z}, <)$ the pair $(1, 2)$ lies in $<^{\mathcal{M}}$, and in a structure where $<$ is read as "greater than" it does not.

A function symbol needs a total function.
Ordinary addition on $\{0, 1, 2\}$ is not an interpretation of $+$, since $2 + 2 = 4$ is not in the domain.
Addition modulo $3$ is an interpretation, since every remainder is $0$, $1$ or $2$.

A structure does not have to satisfy any axioms.
Any interpretations of the right types give a structure, and being a group or an order is a property that some structures have.

### History

Tarski's 1933 paper on the concept of truth defined truth for formalized languages with one fixed intended meaning.
Truth relative to an arbitrary structure became standard through the work of Tarski and his school in the 1950s, for example in the 1957 paper of Tarski and Vaught on arithmetical extensions of relational systems.
In that period structures were often called relational systems.

### Try it

Is $(\mathbb{N}, \max)$ a structure for a signature with one binary function symbol?
Yes: the larger of two natural numbers is a natural number, so $\max \colon \mathbb{N}^2 \to \mathbb{N}$ is total.

How many structures for one unary relation symbol have the domain $\{a, b, c\}$?
A unary relation is any subset of $M$, so there are $2^3 = 8$.

## Explanations

### L1 human

A formal language has symbols such as $+$, $0$ and $<$, and the symbols alone mean nothing.
A structure picks a set of objects and says what each symbol means for these objects.
Take the numbers $0, 1, 2, 3, \ldots$ and let $<$ mean "is less than".
Then "every number has a bigger number" is true.
Now take only the numbers $0, 1, 2$, with the same meaning of $<$.
The same statement is false, because nothing is bigger than $2$.
So one set of symbols can describe many different worlds, and each world is one structure.

### L2 human

We check that a small set with an operation is a structure, and then we compute in it.
Let $L = \{+, 0\}$, with $+$ a binary function symbol and $0$ a constant symbol.
Let $M = \{0, 1, 2\}$, let $+^{\mathcal{M}}$ be addition modulo $3$, and let $0^{\mathcal{M}} = 0$.
The domain is nonempty, and the constant gets the element $0 \in M$.
Addition modulo $3$ is defined on all $9$ pairs of $M^2$, and each value is a remainder modulo $3$, so $+^{\mathcal{M}} \colon M^2 \to M$ is a function.
So $\mathcal{M}$ is an $L$-structure.

Now give $x$ the value $2$ and compute the term $(x + x) + 0$ one step at a time:
$$x + x \mapsto (2 + 2) \bmod 3 = 1, \qquad (x + x) + 0 \mapsto (1 + 0) \bmod 3 = 1.$$
The typical use is to read an axiom system as a signature plus sentences, and its intended objects as structures for that signature.
The trap is totality, as in the Watch out above.

### L3 human

A structure for a signature with only function and constant symbols is an algebra in the sense of [[universal algebra|W82R6N0GM9]], and a structure with only relation symbols is a [[relational structure|MJF9M19E3E]].
The $L$-structures and their homomorphisms form a category, with products, substructures and quotients by congruences.
Many-sorted structures have one domain for each sort, and they reduce to one-sorted structures with a unary relation for each sort.

Model theory studies structures up to [[elementary equivalence|P3B1V182N4]], the relation of having the same true sentences.
This relation is weaker than isomorphism: $(\mathbb{Q}, <)$ and $(\mathbb{R}, <)$ satisfy the same first-order sentences, but no bijection between them exists, since one set is countable and the other is not.
Model theory also classifies the [[elementary classes|MEC3ZMC4F1]], the classes of all models of a set of sentences.
