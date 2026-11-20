---
tag: CGH8C8EA9N
kind: concept
name: Elementary embedding
msc: ["03C07"]
topics: [2RE7GWWXM5]
audience: ug2
uses: [983GZBQYT4, WDVVEYD6AT, HYJ10AF6RT, K7XDVK5854, SCRB74SWQN]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Elementary embeddings
  - book: isbn:9780387987606
    locator: Chapter 2
  - book: isbn:9780521587136
---

## Summary

Let $L$ be a [[signature|WDVVEYD6AT]], and let $\mathcal{M}$ and $\mathcal{N}$ be $L$-[[structures|983GZBQYT4]] with domains $M$ and $N$.
A map $h \colon M \to N$ is an *elementary embedding* of $\mathcal{M}$ into $\mathcal{N}$ when, for every $L$-[[formula|HYJ10AF6RT]] $\varphi(x_1, \dots, x_n)$ and all $a_1, \dots, a_n \in M$,
$$\mathcal{M} \models \varphi(a_1, \dots, a_n) \iff \mathcal{N} \models \varphi(h(a_1), \dots, h(a_n)).$$
The formula $x_1 = x_2$ shows that $h$ is injective, and the atomic formulas show that $h$ is an [[embedding|SCRB74SWQN]].
The case $n = 0$ shows that $\mathcal{M}$ and $\mathcal{N}$ satisfy the same sentences.
Elementary embeddings are the maps that first-order logic cannot detect, so they are the natural maps between models in model theory.

## Motivation

An embedding keeps the quantifier-free properties of elements, but it can change the properties that use quantifiers.
The inclusion of $(\Z, <)$ into $(\Q, <)$ is an embedding, but "there is an element between $0$ and $1$" is false in $\Z$ and true in $\Q$.
For many arguments we want a larger structure that changes nothing that a formula can say about the old elements.
Then a fact about the old elements can be proved in the larger structure and moved back.
For example, nonstandard analysis uses a field ${}^*\R$ with an elementary embedding of the real field, and the transfer of facts between the two fields is exactly elementarity.
Elementary embeddings make this idea exact.

## Notation

We write $h \colon \mathcal{M} \preceq \mathcal{N}$ or $h \colon \mathcal{M} \to_{e} \mathcal{N}$ for an elementary embedding.
When $h$ is an inclusion, $\mathcal{M}$ is an [[elementary substructure|8WZF9SBP39]] of $\mathcal{N}$, written $\mathcal{M} \preceq \mathcal{N}$.
Some books say *elementary map* or *elementary monomorphism*.
In Mathlib the elementary embeddings form the type `L.ElementaryEmbedding M N`, with the notation `M ↪ₑ[L] N`.
In set theory, an elementary embedding $j \colon V \to M$ of the universe into a class is a different, class-sized notion; it belongs to the theory of large cardinals.

## Remarks

### Examples

- Every [[isomorphism|PZMGQMDN25]] is an elementary embedding, because [[isomorphisms preserve the truth of formulas|NDTJ2E895C]].
- The inclusion of $(\Q, <)$ into $(\R, <)$ is elementary; see [[this example|~89a66bd3]].
- Every embedding of one algebraically closed field into another is elementary, for example $\overline{\Q} \subseteq \C$; see [[this example|~4bfe8f6c]].
- If $T$ is a [[model complete theory|YR6HCMABTE]], then every embedding between two models of $T$ is elementary; this is the definition of model completeness.
- The diagonal map of a structure into an [[ultrapower|AX9Q86GB8M]] is elementary, by Łoś's theorem.

### Non-examples

- The inclusion of $(2\Z, <)$ into $(\Z, <)$ is an embedding, and the two orders are isomorphic, but the inclusion is not elementary; see [[this non-example|~65feae4d]].
- The map $n \mapsto n + 1$ from $(\N, <)$ to $(\N, <)$ is an embedding, but $0$ is the least element and its image $1$ is not.
- The inclusion $\Z \to \Q$ of rings is an embedding, but $\exists y \, (y + y = 1)$ is false in $\Z$ and true in $\Q$.

### Basic properties

- An elementary embedding is an embedding, and its image is an elementary substructure of $\mathcal{N}$ that is isomorphic to $\mathcal{M}$.
- The composition of two elementary embeddings is elementary, and the identity map is elementary.
- If $g \colon \mathcal{N} \to \mathcal{P}$ and $g \circ h$ are elementary, then $h$ is elementary, since $\mathcal{N} \models \varphi(h(\bar a))$ and $\mathcal{P} \models \varphi(g(h(\bar a)))$ agree.
- If $\mathcal{M}$ embeds elementarily into $\mathcal{N}$, then $\mathcal{M}$ and $\mathcal{N}$ are [[elementarily equivalent|P3B1V182N4]], so they are models of the same complete theory.
- The structures into which $\mathcal{M}$ embeds elementarily are the models of its elementary diagram, by the [[diagram lemmas|~4a49d7ae]].
- The union of a chain of elementary embeddings is elementary over each member, by the [[elementary chain theorem|~26b49e10]].

### History

The notions of elementary extension and elementary substructure were introduced by Alfred Tarski and Robert Vaught in a paper of 1957.
The same paper proved the [[Tarski-Vaught test|60SA99BER7]] and the elementary chain theorem.

### Common errors

- To think that an embedding of two elementarily equivalent structures is elementary. The inclusion $(2\Z, <) \subseteq (\Z, <)$ is a counterexample.
- To check only sentences. Elementarity is about formulas with parameters from $M$, which is much stronger than $\mathcal{M} \equiv \mathcal{N}$.
- To forget that the map must be defined on all of $M$. A map on a subset that preserves formulas is a [[partial elementary map|~7e54c18a]].

## Explanations

### L1 human

An ordinary embedding copies a structure into another one and keeps the operations and relations.
An elementary embedding keeps much more: every first-order statement about some elements is true before the map exactly when it is true after the map.
The inclusion of the fractions into the real numbers, with the order "less than", is elementary.
The map that adds $1$ to each natural number keeps the order, but it is not elementary.
The number $0$ is the smallest number, and its image $1$ is not the smallest number.

### L2 human

We show that the inclusion $h$ of $(\N_{>0}, <)$, the positive integers, into $(\N, <)$ is not elementary.

1. Let $\varphi(x)$ be the formula $\forall y \, \neg (y < x)$, "$x$ is the least element".
2. In $(\N_{>0}, <)$ no element is less than $1$, so $(\N_{>0}, <) \models \varphi(1)$.
3. In $(\N, <)$ we have $0 < 1$, so $(\N, <) \models \neg\varphi(1)$.
4. So $h(1) = 1$ satisfies $\varphi$ in one structure and fails it in the other, and $h$ is not elementary.

The two orders are isomorphic by $n \mapsto n - 1$, so they satisfy the same sentences.
The typical use of an elementary embedding is to prove a statement about elements of $\mathcal{M}$ inside a larger, richer structure $\mathcal{N}$.
A trap is to test elementarity only with sentences: the test above needs the parameter $1$.

### L3 human

The $L$-structures with elementary embeddings form a category, and each connected part of it lies inside the models of one complete theory.
This category has directed colimits, by the elementary chain theorem, and it has the amalgamation property, by the [[elementary amalgamation theorem|~c9e11fa5]].
These two facts are the starting point of the monster model of a complete theory and of abstract elementary classes.
An elementary embedding preserves complete types, so it is the global form of a partial elementary map; the sub-areas on [[types and saturated models|Z772KEC9BY]] and [[back-and-forth methods|N64R1MGDBN]] build elementary embeddings one element at a time.
In set theory the same word names embeddings $j \colon V \to M$ of the universe into a transitive class, and a nontrivial one exists exactly when there is a [[measurable cardinal|AKBWT323RQ]].
