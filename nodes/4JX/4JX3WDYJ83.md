---
tag: 4JX3WDYJ83
kind: definition
name: Markov random field
msc: [62H22, 60G60]
defines: 6W69H3A3G5
uses: [Q3FQAD1BXG, 00C0BR7D7H, 0THJ7416DX, 0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_random_field
---

## Definition

Let $G = (V, E)$ be a finite undirected [[graph|00C0BR7D7H]] and let $X = (X_v)_{v \in V}$ be [[random variables|0PNRKMRC55]].
For $A \subseteq V$ write $X_A = (X_v)_{v \in A}$.
A set $S \subseteq V$ *separates* $A$ from $B$ if every path from a vertex of $A$ to a vertex of $B$ passes through $S$.
Then $X$ is a *Markov random field* with respect to $G$ if it has the global Markov property.
This means: whenever $A, B, S \subseteq V$ are disjoint and $S$ separates $A$ from $B$, $X_A$ and $X_B$ are [[conditionally independent|0THJ7416DX]] given $X_S$.

## Remarks

Two weaker properties are also used.
In the local Markov property, each $X_v$ is conditionally independent of all non-neighbours given its neighbours $X_{N(v)}$.
In the pairwise Markov property, $X_u \perp X_v \mid X_{V \setminus \set{u, v}}$ for all non-adjacent $u \ne v$.
Global implies local implies pairwise, and all three are equivalent when the joint density is strictly positive.
Example: on the path $1 - 2 - 3$, a Markov chain $X_1, X_2, X_3$ is a Markov random field, since $\set{2}$ separates $1$ from $3$ and $X_1 \perp X_3 \mid X_2$.
Non-example: let $X_1, X_2$ be independent fair coins and $X_3 = X_1$.
Then $X_1$ and $X_3$ are dependent given $X_2$, so $X$ is not a Markov random field on this path.
