---
tag: E2EM9ZYCZS
kind: definition
name: Regular function
msc: [14A10]
defines: 4M94FZH9Y8
uses: [JERVQT4C12, EQSHJPE7H8, A4H4CZ2V35, 02BH3MCBQB, 2C3PAQ7H50, G9WB27VWP7, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Morphism_of_algebraic_varieties
---

## Definition

Let $k$ be an algebraically closed field.

1. Let $X$ be a quasi-affine variety, that is, a nonempty open subset of an [[affine variety|JERVQT4C12]] in $k^n$. A function $f \colon X \to k$ is *regular at* $p \in X$ if the following holds. There are an [[open|02BH3MCBQB]] neighbourhood $U \subseteq X$ of $p$ and polynomials $g, h \in k[x_1, \dots, x_n]$ such that $h$ has no zero on $U$ and $f = g/h$ on $U$.
2. Let $X$ be a [[quasi-projective variety|EQSHJPE7H8]] in $\mathbb{P}^n$. A function $f \colon X \to k$ is *regular at* $p \in X$ if the following holds. There are an open neighbourhood $U \subseteq X$ of $p$ and [[homogeneous polynomials|2C3PAQ7H50]] $g, h \in k[x_0, \dots, x_n]$ of the same degree. The polynomial $h$ has no zero on $U$, and $f = g/h$ on $U$.

In both cases, $f$ is *regular* on $X$ if it is regular at every point of $X$.

## Remarks

In case 2, $g/h$ is a well-defined function on $U$, because $g$ and $h$ have the same degree $d$ and so $g(\lambda a)/h(\lambda a) = g(a)/h(a)$.
A regular function is [[continuous|0VGFHTM75Y]] when $k$ is identified with $\mathbb{A}^1$ with its Zariski topology.

Example: on $X = k \setminus \set{0}$, the function $f(x) = 1/x$ is regular, with $g = 1$ and $h = x$ on $U = X$.

Non-example: the function on $k$ given by $f(0) = 1$ and $f(x) = 0$ for $x \ne 0$ is not regular at $0$.
Near $0$ it would equal $g/h$ on a nonempty open set, so $g$ would vanish on a cofinite set and hence be $0$, which contradicts $f(0) = 1$.

On an affine variety $X$, the ring of regular functions on all of $X$ equals the [[coordinate ring|G9WB27VWP7]] $k[X]$; this uses Hilbert's Nullstellensatz.
On a [[projective variety|A4H4CZ2V35]], every regular function on the whole variety is constant.
