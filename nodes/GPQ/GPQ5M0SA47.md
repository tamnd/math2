---
tag: GPQ5M0SA47
kind: definition
name: Gelfand pair
msc: [43A90, 22D10, 43A85]
defines: W38ZDXDVYC
uses: [AHV05ZBCYW, VY0HXD3GC4, 2Z29JN3VES, 0R6EWFKRCF, 0X1JXT47GA]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand_pair
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with a [[Haar measure|VY0HXD3GC4]], and let $K$ be a [[compact|0R6EWFKRCF]] [[subgroup|0X1JXT47GA]] of $G$.
A function $f$ on $G$ is *$K$-bi-invariant* if $f(k_1 g k_2) = f(g)$ for all $g \in G$ and $k_1, k_2 \in K$.
Let $C_c(K \backslash G / K)$ be the space of continuous, compactly supported, $K$-bi-invariant functions on $G$.
It is closed under [[convolution|2Z29JN3VES]].
The pair $(G, K)$ is a *Gelfand pair* if $f_1 * f_2 = f_2 * f_1$ for all $f_1, f_2 \in C_c(K \backslash G / K)$.

## Remarks

Example: $G = \mathrm{SL}_2(\R)$ and $K = \mathrm{SO}(2)$.
Let $\theta(g) = g^{T}$, the transpose, which reverses products and preserves Haar measure.
By the Cartan decomposition $g = k_1 a k_2$ with $a$ diagonal, so $g^{T} = k_2^{-1} a k_1^{-1}$ lies in $K g K$.
So every bi-invariant $f$ satisfies $f \circ \theta = f$, and then $f_1 * f_2 = (f_2 * f_1) \circ \theta = f_2 * f_1$.
This is Gelfand's trick.

Non-example: $G$ a finite non-abelian group and $K = \set{e}$.
Then every function is bi-invariant, and the convolution of the indicators of $\set{a}$ and $\set{b}$ is the indicator of $\set{ab}$.
So the algebra is not commutative when $ab \ne ba$.

Equivalent form: $(G, K)$ is a Gelfand pair exactly when every irreducible unitary representation of $G$ has a space of $K$-fixed vectors of dimension at most $1$.
For finite $G$, this says that the permutation representation of $G$ on functions on $G/K$ is multiplicity-free.
If $(G, K)$ is a Gelfand pair, then $G$ is unimodular.
