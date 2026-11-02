---
tag: BQGK1FHSKB
kind: definition
name: Embedding of structures
msc: [08A05, 03C07]
defines: SCRB74SWQN
uses: [983GZBQYT4, KBXSZC6BV1, 09NWETVTNY, 676H7EGTKJ, PZMGQMDN25]
sources:
  - url: https://en.wikipedia.org/wiki/Embedding
---

## Definition

Let $\sigma$ be a signature and let $\mathbf{A}$ and $\mathbf{B}$ be $\sigma$-[[structures|983GZBQYT4]] with domains $A$ and $B$.
An *embedding* of $\mathbf{A}$ into $\mathbf{B}$ is a map $h \colon A \to B$ such that:

1. $h$ is a [[homomorphism|KBXSZC6BV1]] from $\mathbf{A}$ to $\mathbf{B}$;
2. $h$ is [[injective|09NWETVTNY]];
3. for each relation symbol $R \in \sigma$ of arity $n$ and all $a_1, \dots, a_n \in A$, if $(h(a_1), \dots, h(a_n)) \in R^{\mathbf{B}}$ then $(a_1, \dots, a_n) \in R^{\mathbf{A}}$.

## Remarks

A map $h$ is an embedding if and only if its image is the domain of a [[substructure|676H7EGTKJ]] $\mathbf{C}$ of $\mathbf{B}$ and $h$ is an [[isomorphism|PZMGQMDN25]] from $\mathbf{A}$ to $\mathbf{C}$.
For a signature without relation symbols, clause 3 is empty, and an embedding is an injective homomorphism.

Example: for the signature $\set{+, \cdot, 0, 1}$, the inclusion $\Z \to \Q$ is an embedding, because it is injective and respects sums, products, $0$ and $1$.

Non-example: view graphs as structures with one binary relation.
Let $A$ be the graph with vertices $1, 2$ and no edge, and $B$ the graph with vertices $1, 2$ and one edge between them.
The identity map is an injective homomorphism from $A$ to $B$ but not an embedding, because clause 3 fails for the pair $(1, 2)$.
