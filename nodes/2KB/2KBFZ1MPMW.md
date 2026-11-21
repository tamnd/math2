---
tag: 2KBFZ1MPMW
kind: definition
name: Amalgamation property
msc: ["03C52"]
topics: [ZS8X8KS54R]
audience: grad
defines: XSCSX39GEZ
uses: [983GZBQYT4, WDVVEYD6AT, 00C0BR7D7H, SCRB74SWQN]
sources:
  - url: https://en.wikipedia.org/wiki/Amalgamation_property
    locator: Definition
  - book: isbn:9780521587136
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]], and let $\mathcal{K}$ be a class of [[$L$-structures|983GZBQYT4]] closed under isomorphism.
An [[embedding|SCRB74SWQN]] is an injective map between $L$-structures that preserves and reflects all functions, relations and constants.
The class $\mathcal{K}$ has the *amalgamation property* if the following holds.
For all $A, B, C \in \mathcal{K}$ and all embeddings $f \colon A \to B$ and $g \colon A \to C$, there are $D \in \mathcal{K}$ and embeddings $f' \colon B \to D$ and $g' \colon C \to D$ with $f' \circ f = g' \circ g$.

## Notation

The structure $D$, with the maps $f'$ and $g'$, is called an *amalgam* of $B$ and $C$ over $A$.
The property is abbreviated AP.
When $f$ and $g$ are inclusions, the condition reads: $B$ and $C$ embed into some $D$ by maps that agree on $A$.

## Remarks

Example: the class of finite [[graphs|00C0BR7D7H]] has the amalgamation property.
Given $f$ and $g$, take the disjoint union of $B$ and $C$, identify $f(a)$ with $g(a)$ for each $a \in A$, and add no new edges.
Two vertices of $B$ are adjacent in the result exactly when they are adjacent in $B$, and the same holds for $C$.
So the inclusions of $B$ and $C$ are embeddings, and they agree on $A$.
The details are in [[this example|XM3EG8TN42]].

Non-example: the class of graphs with at most $2$ vertices fails the condition.
Let $A$ be one vertex $a$, let $B$ be an edge $\set{a, b}$, and let $C$ be two non-adjacent vertices $a, c$.
In any amalgam $D$, the images of $b$ and $c$ are distinct, since one is adjacent to the image of $a$ and the other is not.
So $D$ has at least $3$ vertices and is not in the class.
A less artificial failure, for finite bipartite graphs, is in [[this non-example|7YEX9F1V8D]].

When $A$ may be the empty structure, the amalgamation property implies the [[joint embedding property|59FQ5Q2B8R]]: any two members of $\mathcal{K}$ embed into a common member.

## Explanations

### L1 human

Two structures in the class share a common part.
The amalgamation property says that a third structure in the class holds both of them, with the common part used only once.
Gluing along the shared part is the usual way to build it.

### L2 human

We amalgamate two graphs over an edge.

1. Let $A$ be the edge $\set{a, b}$, let $B$ add a vertex $x$ adjacent to $a$, and let $C$ add a vertex $y$ adjacent to $b$.
2. Glue along $\set{a, b}$: the vertex set is $\set{a, b, x, y}$, with edges $ab$, $ax$ and $by$.
3. No edge joins $x$ and $y$, so $B$ and $C$ are induced subgraphs, and they meet in $A$.

The typical use is to verify one hypothesis of Fraïssé's theorem.
A trap is to add the edge $xy$ for no reason; it is allowed, but it must not break a rule of the class.
