---
tag: XM3EG8TN42
kind: example
name: Free amalgamation of finite graphs
aliases: [free-amalgamation-of-finite-graphs]
msc: ["03C15", "05C63"]
topics: [ZS8X8KS54R]
audience: grad
instance_of: [XSCSX39GEZ]
uses: [XSCSX39GEZ, 2KBFZ1MPMW, 00C0BR7D7H, 0EREPBVG2G, SCRB74SWQN]
sources:
  - url: https://en.wikipedia.org/wiki/Amalgamation_property
    locator: Examples
  - book: isbn:9780521587136
---

## Example

Let $\mathcal{G}$ be the class of finite [[graphs|00C0BR7D7H]], in the signature with one symmetric irreflexive binary relation $E$.
We show that $\mathcal{G}$ has the [[amalgamation property|XSCSX39GEZ]].

1. Let $f \colon A \to B$ and $g \colon A \to C$ be [[embeddings|SCRB74SWQN]] of finite graphs.
2. Replace $B$ and $C$ by isomorphic copies so that $f$ and $g$ are inclusions and $B \cap C = A$.
3. Let $D$ have vertex set $B \cup C$, and let $xy$ be an edge of $D$ when it is an edge of $B$ or an edge of $C$.
4. For $x, y \in B$, the pair $xy$ is an edge of $C$ only if $x, y \in A$; then it is an edge of $C$ exactly when it is an edge of $A$, hence of $B$.
5. So $B$ is an [[induced subgraph|0EREPBVG2G]] of $D$, and in the same way $C$ is one.
6. The inclusions $B \to D$ and $C \to D$ agree on $A$, so $D$ is an amalgam.

## Remarks

The graph $D$ is the *free amalgam* of $B$ and $C$ over $A$: no edge joins $B \setminus A$ to $C \setminus A$.
The images of $B$ and $C$ meet only in $A$, so the amalgamation is strong.
Adding all edges between $B \setminus A$ and $C \setminus A$ also gives an amalgam, so amalgams are not unique.
The free amalgam never creates a new triangle or a new clique, so the same construction proves AP for finite $K_n$-free graphs.
The Fraïssé limit of $\mathcal{G}$ is the [[Rado graph|RMXR0FEF54]].

## Explanations

### L1 human

Two finite graphs share a common part.
Lay them side by side, glue the shared part together, and draw no new lines.
Each original graph sits inside the result exactly as before.
That is all that amalgamation asks.

### L2 human

We glue two paths over a vertex.

1. Let $A = \set{a}$, let $B$ be the path $a - b - c$, and let $C$ be the edge $a - d$.
2. The free amalgam has vertices $a, b, c, d$ and edges $ab$, $bc$, $ad$.
3. The induced subgraph on $\set{a, b, c}$ is the path, and on $\set{a, d}$ it is the edge.

The typical use is to verify the hypothesis of Fraïssé's theorem for a class of graphs defined by forbidden cliques.
A trap is to apply free amalgamation to a class with a global rule, such as bipartite graphs, where gluing can create an odd cycle.
