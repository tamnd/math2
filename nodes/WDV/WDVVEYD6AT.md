---
tag: WDVVEYD6AT
kind: concept
name: Signature
aliases: [vocabulary, similarity-type, first-order-language]
msc: ["03C07", "03B10"]
topics: [PSRDJXRW53]
audience: ug2
uses: [MSXX2P86CY, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Signature_(logic)
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
  - url: https://builds.openlogicproject.org/
    locator: "Chapter: Syntax and Semantics"
same_as:
  wikidata: Q741810
  wikipedia: Signature (logic)
---

## Summary

A signature lists the non-logical symbols of a first-order language: function symbols, relation symbols and constant symbols, each with its [[arity|MSXX2P86CY]].
It fixes what one can talk about, before any axioms are chosen.
Terms, formulas and [[structures|983GZBQYT4]] are always taken over a given signature.
Other names are vocabulary, similarity type and language, and in Mathlib it is called a first-order language.

## Motivation

The same set $\mathbb{Z}$ can be studied as a group, as a ring or as an ordered set.
Each view uses different symbols, and so different statements are possible.
In the signature $\set{<}$ the sentence $\forall x \, \exists y \, (x < y)$ makes sense, but the sentence $\forall x \, (x \cdot 1 = x)$ does not.
The signature makes this choice explicit.
It also lets one state results for all languages at once, such as the [[compactness theorem|1NR3HAWG9D]].

## Notation

1. A signature is written $\sigma$, $\tau$, $L$ or $\mathcal{L}$. This site writes $\sigma$, and "$\sigma$-term" and "$\sigma$-formula" for the terms and formulas over $\sigma$.
2. The arity of a symbol $s$ is $\operatorname{ar}(s)$. Arities are often listed in order, for example "$\set{+, \cdot, 0}$ with arities $2, 2, 0$".
3. Some books write a signature as a tuple of arities, such as $(2, 2, 1, 0, 0)$ for rings.
4. In Mathlib a signature is `FirstOrder.Language`, a pair of families `Functions n` and `Relations n` of symbols indexed by the arity $n$.

## Remarks

### Examples

1. The signature of rings is $\set{+, \cdot, -, 0, 1}$ with arities $2, 2, 1, 0, 0$.
2. The signature of ordered sets is $\set{<}$, with one binary relation symbol.
3. The signature of set theory is $\set{\in}$, with one binary relation symbol.
4. The signature of graphs is $\set{E}$, with one binary relation symbol for adjacency.
5. [[Groups in two signatures|~8aea4994]]: $\set{\cdot, e, {}^{-1}}$ and $\set{\cdot}$ give the same groups, but different substructures.
6. [[A constant for each real number|~0d363af5]] gives an uncountable signature, used to describe $\mathbb{R}$ inside its own language.
7. The empty signature has no symbols. Its formulas are built from equations $x = y$ alone, and they talk only about the number of elements.
8. More examples are on the page of [[standard first-order languages|~1cac8c60]].

### Non-examples

1. [[One symbol for unary and binary minus|~c53e6eb1]] is not a signature: each symbol has exactly one arity, and the double use destroys unique readability.
2. "A binary operation $\cdot$ that is associative" is not a signature. Associativity is an axiom, and a signature holds only symbols and arities.
3. The equality symbol $=$ is not part of a signature in most books. It is a logical symbol, with a fixed meaning in every structure.
4. The set $\set{+, \cdot}$ without arities is not a signature. The same letter $+$ could be binary in one language and ternary in another.

### Basic properties

1. When $\sigma$ is countable, there are countably many $\sigma$-terms and $\sigma$-formulas. In general there are $\max(\abs{\sigma}, \aleph_0)$ of each.
2. When $\sigma \subseteq \sigma'$, every $\sigma$-formula is a $\sigma'$-formula. A $\sigma'$-structure gives a $\sigma$-structure by forgetting the extra symbols, its reduct, and $\sigma$-formulas have the same truth in both.
3. Every signature can be replaced by a relational one: a function symbol $f$ of arity $n$ becomes a relation symbol $R_f$ of arity $n + 1$ for the graph of $f$.
4. The substructures and the homomorphisms of structures depend on the signature, not only on the underlying sets.

### History

Birkhoff's paper of 1935 on abstract algebras studied algebras through their operations and arities, which universal algebra calls the type of an algebra.
Model theory, built by Tarski and others in the 1950s, extended the idea to relation symbols, and some books call a signature a similarity type.
The word "signature" became standard later, and finite model theory often says "vocabulary".

### Common errors

1. A student treats a symbol and its interpretation as the same thing. The symbol $+$ is a mark in $\sigma$, and addition on $\mathbb{Z}$ is one possible meaning for it.
2. A student puts axioms into the signature. A signature has no axioms, and a set of axioms over $\sigma$ is a [[first-order theory|92SWXST1ZM]].
3. A student assumes that a group in the signature $\set{\cdot}$ has the same substructures as in $\set{\cdot, e, {}^{-1}}$. It does not, as the example of [[groups in two signatures|~8aea4994]] shows.

## Explanations

### L1 human

Before writing axioms for groups, one has to say which symbols are allowed.
For groups, one may take a binary symbol $\cdot$, a unary symbol ${}^{-1}$ and a constant $e$.
This list of symbols with their numbers of arguments is the signature.
The axioms, such as associativity, come later and are not part of the signature.
For example, $x \cdot e$ uses only allowed symbols, but $x + e$ does not, because $+$ is not in the list.

### L2 human

We replace the function symbol $\cdot$ of groups by a relation symbol, as in property 3.

1. Let $M$ be a ternary relation symbol, and read $M(x, y, z)$ as "$x \cdot y = z$".
2. One axiom says that $M$ is the graph of a function: $\forall x \, \forall y \, \exists z \, (M(x, y, z) \land \forall w \, (M(x, y, w) \to w = z))$.
3. The term $x \cdot (y \cdot z)$ has no direct translation, because the new signature has no function symbols.
4. The equation $x \cdot (y \cdot z) = w$ becomes $\exists u \, (M(y, z, u) \land M(x, u, w))$, with a new variable $u$ for the inner value.
5. Each formula over $\set{\cdot}$ translates in this way, and the translation has the same truth in each group.

The typical use of relational signatures is in finite model theory and in proofs where terms get in the way.
A trap: without the axiom of step 2, a structure for $\set{M}$ need not come from any binary operation.

### L3 human

A signature is the data of a first-order language, and the logic itself is the same for all signatures.
This uniformity lets model theory state the compactness and the [[Löwenheim-Skolem theorem|484M0TZ1S7]] once, with the size of the signature as a parameter.
Many proofs change the signature: Henkin's proof of completeness adds new constants, Skolemization adds function symbols, and a Morleyization adds one relation symbol per formula.
The elementary diagram of a structure $\mathcal{M}$ uses the signature $\sigma$ with one new constant for each element of $M$.
In Mathlib this expansion is `FirstOrder.Language.withConstants`, written `L[[A]]`.
[[Many-sorted logic|~4886a7ff]] uses signatures that also list the sorts, and each symbol has a sort for each argument and for its value.
In categorical logic a signature generates a free category of terms, and a theory over it gives a Lawvere theory or a hyperdoctrine.
