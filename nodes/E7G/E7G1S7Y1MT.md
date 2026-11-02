---
tag: E7G1S7Y1MT
kind: statement
role: theorem
name: Complexification of a real analytic manifold
msc: [32C09, 32C05]
uses: [Z7H98E1NHP, JSGWAN2RJV]
about: [Z7H98E1NHP]
sources:
  - url: https://en.wikipedia.org/wiki/Complexification
---

## Statement

Let $M$ be a [[real analytic manifold|Z7H98E1NHP]] of dimension $n$ whose topology has a countable basis.
Then there is a [[complex manifold|JSGWAN2RJV]] $X$ of complex dimension $n$ that contains $M$ as a closed subset, with the following property.
Each point $p \in M$ has a holomorphic chart $\varphi \colon U \to \C^n$ of $X$ around $p$ with $\varphi(U \cap M) = \varphi(U) \cap \R^n$.
Moreover $\varphi|_{U \cap M}$ is a real analytic chart of $M$.
Such an $X$ is a complexification of $M$.
It is unique as a germ, in the following sense.
Let $X$ and $X'$ be two complexifications of $M$.
Then there are open neighbourhoods $V \subseteq X$ and $V' \subseteq X'$ of $M$ and a biholomorphic map $V \to V'$ that is the identity on $M$.

## Remarks

The existence is due to Whitney and Bruhat.
Locally, a real analytic chart extends to a holomorphic chart by replacing real variables by complex ones in the convergent power series of the transition maps.
The transition maps of $M$ then extend holomorphically to small complex neighbourhoods.
One glues these local pieces along a neighbourhood of $M$ that is chosen thin enough for the extensions to agree.
Uniqueness follows from the identity theorem: a holomorphic map is determined by its values on a totally real submanifold of maximal dimension.

Examples: $\R^n$ has the complexification $\C^n$.
The circle $S^1 = \set{x^2 + y^2 = 1} \subseteq \R^2$ has the complexification $\set{(z, w) \in \C^2 : z^2 + w^2 = 1}$, which is biholomorphic to $\C \setminus \set{0}$ by $(z, w) \mapsto z + i w$.

By a theorem of Grauert, the complexification $X$ can be chosen to be a Stein manifold.

## Explanations

### L1 human

A real analytic manifold is described by convergent power series in real variables.
Feeding complex numbers into these series gives a complex manifold of the same dimension that contains the real one, as $\C^n$ contains $\R^n$.
Near the real manifold this complex manifold is unique.

### L2 human

Complexification moves problems about real analytic objects to complex analysis, where stronger tools are available.
A real analytic function on $M$ extends to a holomorphic function on a neighbourhood of $M$ in $X$.
With a Stein complexification, Cartan's theorems give many such functions, which leads to Grauert's analytic embedding of $M$ in some $\R^N$.
