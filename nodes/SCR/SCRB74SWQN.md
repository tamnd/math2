---
tag: SCRB74SWQN
kind: concept
name: Embedding of structures
msc: ["08A05", "03C07"]
topics: [AY09KYSW81]
audience: ug2
specializes: [KBXSZC6BV1]
uses: [983GZBQYT4, KBXSZC6BV1, 09NWETVTNY, 676H7EGTKJ, PZMGQMDN25]
sources:
  - url: https://en.wikipedia.org/wiki/Embedding
    locator: Universal algebra and model theory
  - book: isbn:9780387987606
    locator: Chapter 1
  - book: isbn:9780521587136
    locator: Chapter 1
---

## Summary

Let $\mathcal{M}$ and $\mathcal{N}$ be [[structures|983GZBQYT4]] for the same signature $L$, with domains $M$ and $N$.
An *embedding* of $\mathcal{M}$ into $\mathcal{N}$ is an [[injective|09NWETVTNY]] map $h \colon M \to N$ that sends each constant $c^{\mathcal{M}}$ to $c^{\mathcal{N}}$, satisfies $h(f^{\mathcal{M}}(a_1, \dots, a_n)) = f^{\mathcal{N}}(h(a_1), \dots, h(a_n))$ for each function symbol $f$, and satisfies $(a_1, \dots, a_n) \in R^{\mathcal{M}} \iff (h(a_1), \dots, h(a_n)) \in R^{\mathcal{N}}$ for each relation symbol $R$.
Equivalently, $h$ is an injective [[homomorphism|KBXSZC6BV1]] that also reflects the relations, or an [[isomorphism|PZMGQMDN25]] of $\mathcal{M}$ onto a [[substructure|676H7EGTKJ]] of $\mathcal{N}$.
Embeddings make exact the idea that one structure "sits inside" another, as $\Z$ sits inside $\Q$.

## Motivation

In algebra we often identify an object with its image under a map: the integers with the integer fractions $n/1$, a group with a subgroup of a symmetric group.
The identification is safe only when the map loses no information.
For operations this means that the map is injective and respects the operations.
For relations it means more: the map must keep both the relation and its failure.
These are the embeddings, and they are exactly the maps that preserve every quantifier-free statement about elements.

## Notation

We write $h \colon \mathcal{M} \hookrightarrow \mathcal{N}$ for an embedding.
A *homomorphism* only needs $h(c^{\mathcal{M}}) = c^{\mathcal{N}}$, the equation for each $f$, and the implication $\bar{a} \in R^{\mathcal{M}} \Rightarrow h(\bar{a}) \in R^{\mathcal{N}}$.
An *isomorphism* is a surjective embedding, and an *automorphism* is an isomorphism of a structure onto itself.
Mathlib uses bundled maps: `L.Hom M N` for homomorphisms (notation `M →[L] N`), `L.Embedding M N` for embeddings (notation `M ↪[L] N`) and `L.Equiv M N` for isomorphisms.

## Remarks

### Examples

- The inclusion of any [[substructure|676H7EGTKJ]] is an embedding.
- The inclusion $\Z \to \Q$ is an embedding of rings in the signature $\set{+, -, \cdot, 0, 1}$; see [[this example|~3ca411f0]].
- The inclusion $(\Z, <) \to (\Q, <)$ and the map $n \mapsto 2n$ from $(\Z, <)$ to itself are embeddings of orders; see [[this example|~e614153d]].
- Cayley's theorem gives an embedding of a group $G$ into the symmetric group on $G$, in the signature $\set{\cdot, {}^{-1}, e}$.

### Non-examples

- The identity map from the graph with two vertices and no edge to the graph with one edge is an injective homomorphism but not an embedding; see [[this non-example|~3e0fe003]].
- The quotient map $\Z \to \Z/2\Z$ is a ring homomorphism but not an embedding, because it is not injective: $0$ and $2$ have the same image.

### Basic properties

- A composition of embeddings is an embedding, and the identity is an embedding.
- An embedding preserves and reflects every quantifier-free formula, preserves existential formulas and reflects universal formulas; see [[embeddings preserve quantifier-free formulas|~9a0a1ffd]].
- So if $\mathcal{M}$ embeds into $\mathcal{N}$ and a universal sentence is true in $\mathcal{N}$, it is true in $\mathcal{M}$.
- A surjective embedding is an isomorphism, and [[isomorphic structures satisfy the same sentences|NDTJ2E895C]].
- In a signature without relation symbols, the embeddings are exactly the injective homomorphisms.

### History

Embeddings of algebraic structures, such as the embedding of an integral domain into its field of fractions, were used in algebra long before model theory.
The notion for structures with relations, where the map must also reflect the relations, is the one used in model theory and in the definition of [[elementary embeddings|CGH8C8EA9N]].

### Common errors

- To take an injective homomorphism of relational structures for an embedding. The map must also reflect the relations.
- To think that an embedding preserves all formulas. The inclusion $(\Z, <) \to (\Q, <)$ is an embedding, but "there is $z$ with $0 < z < 1$" is true in $\Q$ and false in $\Z$.
- To confuse an embedding with an [[elementary embedding|CGH8C8EA9N]], which preserves all formulas.

## Explanations

### L1 human

An embedding places a copy of one structure inside another without losing any information.
Different elements go to different elements, and the operations and relations are kept.
For example, send each whole number $n$ to the fraction $n/1$.
Then $2 + 3 = 5$ becomes $2/1 + 3/1 = 5/1$, and $2 \cdot 3 = 6$ becomes $2/1 \cdot 3/1 = 6/1$.
So the whole numbers sit inside the fractions with the same arithmetic.

### L2 human

We check that $h(n) = 2n$ is an embedding of $(\Z, +, 0)$ into itself.

1. Injective: $2m = 2n$ gives $m = n$.
2. Constant: $h(0) = 0$.
3. Function: $h(m + n) = 2m + 2n = h(m) + h(n)$.
4. There are no relation symbols, so the check is complete.

The image is the substructure $2\Z$, and $h$ is an isomorphism of $\Z$ onto $2\Z$.
The typical use of an embedding is to replace a structure by an isomorphic substructure of a larger one.
A trap: $h$ is not an embedding of $(\Z, +, \cdot, 0, 1)$, because $h(1) = 2 \ne 1$ and $h(1 \cdot 1) = 2 \ne 4 = h(1) \cdot h(1)$.

### L3 human

Embeddings are the monomorphisms of the category of $L$-structures that also reflect relations; in a signature with relations, a monomorphism of the category of structures and homomorphisms need not be an embedding.
Model theory uses a hierarchy of maps: homomorphisms preserve positive existential formulas, embeddings preserve quantifier-free formulas, and [[elementary embeddings|CGH8C8EA9N]] preserve all formulas.
The diagram lemma says that the models of the atomic diagram of $\mathcal{M}$ are the structures into which $\mathcal{M}$ embeds; it appears in the sub-area on [[elementary extensions|2RE7GWWXM5]].
Classes closed under substructures are the classes with universal axioms, by the [[Łoś-Tarski theorem|9RN0KYXNT1]], and embeddings with an amalgamation property lead to [[Fraïssé theory|ZS8X8KS54R]].
