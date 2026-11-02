---
tag: M9HEZ5X3FX
kind: definition
name: Unbounded operator
msc: [47A05, 47B25]
defines: KRJX5RA0PW
uses: [03J5RAKB30, 00YC1D652K, 0NRYHJPQG2, 03TM135G0N]
sources:
  - url: https://en.wikipedia.org/wiki/Unbounded_operator
    locator: Definitions and basic properties
---

## Definition

Let $X$ and $Y$ be [[normed spaces|03J5RAKB30]] over $\R$ or $\C$.
An *unbounded operator* (or *linear operator*) $T$ from $X$ to $Y$ is a pair consisting of
1. a [[linear subspace|00YC1D652K]] $D(T)$ of $X$, the *domain* of $T$, and
2. a [[linear map|0NRYHJPQG2]] $T \colon D(T) \to Y$.

Two such operators $S$ and $T$ are equal when $D(S) = D(T)$ and $Sx = Tx$ for all $x \in D(T)$.
The operator $T$ is an *extension* of $S$, written $S \subseteq T$, when $D(S) \subseteq D(T)$ and $Tx = Sx$ for all $x \in D(S)$.

## Remarks

Example: on $X = Y = L^2(0, 1)$, let $D(T)$ be the space of continuously differentiable functions on $[0, 1]$, and let $Tf = f'$.
This is linear, so $T$ is an unbounded operator.
It is not bounded: $f_n(x) = \sin(n \pi x)$ has $\norm{f_n} = 1/\sqrt{2}$, while $\norm{T f_n} = n \pi / \sqrt{2}$.

Non-example: the rule $f \mapsto f'$ is not an operator with domain all of $L^2(0, 1)$, since many elements of $L^2(0, 1)$ have no derivative in $L^2(0, 1)$.

Every [[continuous linear map|03TM135G0N]] $X \to Y$ is an unbounded operator with domain $X$; the word "unbounded" means "not necessarily bounded".
Sums and products are defined on the natural domains: $D(S + T) = D(S) \cap D(T)$ and $D(ST) = \set{x \in D(T) : Tx \in D(S)}$.
