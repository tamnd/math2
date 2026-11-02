---
tag: 8ZSFY9BWME
kind: definition
name: Frölicher space
msc: [58A40]
defines: T0AEF3Z8C9
uses: [0V33BNKZ9S, F45VQ47GPV, 7JS0JFR89E, BFBNQ36QS8]
sources:
  - url: https://en.wikipedia.org/wiki/Fr%C3%B6licher_space
---

## Definition

Let $X$ be a set, let $\mathcal{C}$ be a set of maps $c \colon \R \to X$ and let $\mathcal{F}$ be a set of maps $f \colon X \to \R$.
The triple $(X, \mathcal{C}, \mathcal{F})$ is a *Frölicher space* if both conditions hold.

1. A map $f \colon X \to \R$ lies in $\mathcal{F}$ if and only if $f \circ c$ is a [[smooth function|0V33BNKZ9S]] $\R \to \R$ for every $c \in \mathcal{C}$.
2. A map $c \colon \R \to X$ lies in $\mathcal{C}$ if and only if $f \circ c$ is a smooth function $\R \to \R$ for every $f \in \mathcal{F}$.

The elements of $\mathcal{C}$ are the smooth curves and those of $\mathcal{F}$ the smooth functions.
A map $\Phi \colon X \to Y$ of Frölicher spaces is *smooth* if $\Phi \circ c \in \mathcal{C}_Y$ for every $c \in \mathcal{C}_X$; equivalently, $f \circ \Phi \in \mathcal{F}_X$ for every $f \in \mathcal{F}_Y$.

## Remarks

Example: $X = \R^n$ with $\mathcal{C}$ the smooth curves and $\mathcal{F}$ the smooth functions.
Condition 2 holds, since a curve is smooth when its coordinate functions are.
Condition 1 is a theorem of Boman: a function on $\R^n$ is smooth if it is smooth along every smooth curve.
The same works for every finite-dimensional [[smooth manifold|F45VQ47GPV]].

Non-example: $X = \R$, $\mathcal{C}$ the smooth curves and $\mathcal{F}$ the polynomial functions.
Condition 1 fails: $\sin \circ c$ is smooth for every smooth curve $c$, but $\sin$ is not a polynomial.

Every Frölicher space carries a [[diffeology|7JS0JFR89E]]: its plots are the maps $p$ from open subsets of Euclidean spaces with $f \circ p$ smooth for every $f \in \mathcal{F}$.
Frölicher spaces and smooth maps form a [[cartesian closed category|BFBNQ36QS8]].
