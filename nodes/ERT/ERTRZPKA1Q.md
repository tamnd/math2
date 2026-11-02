---
tag: ERTRZPKA1Q
kind: definition
name: Lattice homomorphism
msc: [06B05]
defines: BNVRR925X8
uses: [WH4SFAACAS, J2T75ATRV5, 0A7KV2WB7A]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_(order)
---

## Definition

Let $(L, \vee, \wedge)$ and $(M, \vee, \wedge)$ be [[lattices|WH4SFAACAS]].
A *lattice homomorphism* is a map $f \colon L \to M$ such that, for all $x, y \in L$:

1. $f(x \vee y) = f(x) \vee f(y)$;
2. $f(x \wedge y) = f(x) \wedge f(y)$.

If $L$ and $M$ are bounded lattices, a *bounded lattice homomorphism* also satisfies $f(0) = 0$ and $f(1) = 1$.

## Remarks

A lattice homomorphism is [[monotone|0A7KV2WB7A]]: if $x \le y$ then $x \vee y = y$, so $f(x) \vee f(y) = f(y)$, that is, $f(x) \le f(y)$.
A bijective lattice homomorphism is a lattice isomorphism, and its inverse is again a lattice homomorphism.
A bijection between lattices is a lattice isomorphism exactly when it and its inverse are monotone.
Example: every monotone map between two chains is a lattice homomorphism, since join and meet in a chain are $\max$ and $\min$, and monotone maps preserve both.
Non-example: let $N = \set{\emptyset, \set{1}, \set{2}, \set{1, 2, 3}}$, a lattice under $\subseteq$ in which $\set{1} \vee \set{2} = \set{1, 2, 3}$.
The inclusion map of $N$ into the power set of $\set{1, 2, 3}$ is monotone and preserves meets.
It fails clause 1, because the join of $\set{1}$ and $\set{2}$ in the power set is $\set{1, 2} \ne \set{1, 2, 3}$.
