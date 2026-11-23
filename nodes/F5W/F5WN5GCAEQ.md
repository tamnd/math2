---
tag: F5WN5GCAEQ
kind: example
name: A refined frame that is not descriptive
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
not_instance_of:
  - target: GGG7BB78JB
    note: the finite and cofinite sets on the natural numbers give a refined general frame that is not compact, so it is not descriptive
uses: [6W9MEGN982]
sources:
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Types of frames
---

## Example

Let $W = \mathbb{N}$ with the relation $<$, and let $A$ be the family of all finite subsets and all cofinite subsets of $\mathbb{N}$.
We show that $\mathfrak{g} = (\mathbb{N}, <, A)$ is a general frame that is differentiated and tight, but not compact.
So $\mathfrak{g}$ is refined, and it is not a [[descriptive frame|6W9MEGN982]].

1. Unions and complements: a union of two finite sets is finite, a union with a cofinite set is cofinite, and complement swaps finite and cofinite sets.
2. The operator on finite sets: if $X$ is finite with largest element $m$, then $m_<(X) = \{0, \dots, m - 1\}$, which is finite.
   Also $m_<(\emptyset) = \emptyset$.
3. The operator on cofinite sets: a cofinite $X$ has elements above every $w$, so $m_<(X) = \mathbb{N}$, which is cofinite.
4. Differentiated: for $u \neq v$, the finite set $\{u\}$ is admissible, contains $u$ and misses $v$.
5. Tight: let $u < v$ fail, so $v \le u$.
   Take $a = \{v\}$.
   Then $m_<(a) = \{0, \dots, v - 1\}$, which does not contain $u$.
6. The finite intersection property: the sets $C_n = \mathbb{N} \setminus \{0, \dots, n\}$ are cofinite, so admissible.
   Finitely many of them, with largest index $k$, all contain $k + 1$.
7. Not compact: every $k$ lies outside $C_k$, so $\bigcap_n C_n = \emptyset$.

## Remarks

The example shows that compactness is a condition of its own, not a consequence of refinement.
The complex algebra $\mathfrak{g}^*$ is the finite-cofinite algebra of $\mathbb{N}$ with the operator $m_<$.
Its ultrafilters are the principal ones, one for each $n$, and one more, the ultrafilter $\infty$ of all cofinite sets.
So the dual descriptive frame adds a point at infinity.

We can compute the relation at the new point from the definition of the dual.
For every cofinite $b$, the set $m_<(b) = \mathbb{N}$ is cofinite, so $\infty$ sees itself, and every $n$ sees $\infty$.
The point $\infty$ does not see any $n$, because $m_<(\{n\}) = \{0, \dots, n-1\}$ is finite and so not in $\infty$.
A frame with a point at infinity of this kind is the shape behind van Benthem's example of [[Kripke incompleteness|W67YJQTT50]].

## Explanations

### L1 human

Take the numbers $0, 1, 2, \dots$ and allow only regions that are finite or that miss finitely many numbers.
The regions "all numbers above $n$" are allowed, and any few of them overlap.
But no number lies in all of them, so the regions shrink to nothing.
Descriptive frames forbid exactly this kind of vanishing, and this frame has it.

### L2 human

We follow the shrinking regions for a few steps.
The first three are
$$C_0 = \{1, 2, \dots\}, \qquad C_1 = \{2, 3, \dots\}, \qquad C_2 = \{3, 4, \dots\},$$
and they have the common point $3$.
In general $C_0, \dots, C_n$ have the common point $n + 1$, but no number $k$ lies in $C_k$.
So the whole family has no common point.
The typical use of such frames is to build general frames that validate a logic while their Kripke frames do not.
Watch out: here tightness and differentiation can be checked with singletons only because every singleton is admissible.
