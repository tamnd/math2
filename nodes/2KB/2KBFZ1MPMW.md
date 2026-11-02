---
tag: 2KBFZ1MPMW
kind: definition
name: Amalgamation property
msc: [03C52]
defines: XSCSX39GEZ
uses: [983GZBQYT4, WDVVEYD6AT, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Amalgamation_property
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]], and let $\mathcal{K}$ be a class of [[$L$-structures|983GZBQYT4]] closed under isomorphism.
An embedding is an injective map between $L$-structures that preserves and reflects all functions, relations and constants.
The class $\mathcal{K}$ has the *amalgamation property* if the following holds.
For all $A, B, C \in \mathcal{K}$ and all embeddings $f \colon A \to B$ and $g \colon A \to C$, there are $D \in \mathcal{K}$ and embeddings $f' \colon B \to D$ and $g' \colon C \to D$ with $f' \circ f = g' \circ g$.

## Remarks

The structure $D$ is called an amalgam of $B$ and $C$ over $A$.

Example: the class of finite [[graphs|00C0BR7D7H]] has the amalgamation property.
Given $f$ and $g$, take the disjoint union of $B$ and $C$, identify $f(a)$ with $g(a)$ for each $a \in A$, and add no new edges.
Two vertices of $B$ are adjacent in the result exactly when they are adjacent in $B$, and the same holds for $C$.
So the inclusions of $B$ and $C$ are embeddings, and they agree on $A$.

Non-example: the class of graphs with at most $2$ vertices fails the condition.
Let $A$ be one vertex $a$, let $B$ be an edge $\set{a, b}$, and let $C$ be two non-adjacent vertices $a, c$.
In any amalgam $D$, the images of $b$ and $c$ are distinct, since one is adjacent to the image of $a$ and the other is not.
So $D$ has at least $3$ vertices and is not in the class.

When $A$ may be the empty structure, the amalgamation property implies the joint embedding property: any two members of $\mathcal{K}$ embed into a common member.
