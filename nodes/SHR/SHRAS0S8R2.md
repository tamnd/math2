---
tag: SHRAS0S8R2
kind: statement
role: proposition
name: Gelfand's trick
msc: ["43A90", "22D10"]
uses: [AHV05ZBCYW, VY0HXD3GC4, W38ZDXDVYC]
about: [W38ZDXDVYC]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand_pair
---

## Statement

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with a left [[Haar measure|VY0HXD3GC4]], and let $K$ be a compact subgroup of $G$.
Suppose that there is a continuous automorphism $\theta$ of $G$ with $\theta^2 = \mathrm{id}$ such that
$$\theta(g) \in K g^{-1} K \quad \text{for every } g \in G.$$
Then the algebra $L^1(K \backslash G / K)$ of integrable functions $f$ with $f(k_1 g k_2) = f(g)$ for $k_1, k_2 \in K$ is commutative under convolution.
In other words, $(G, K)$ is a [[Gelfand pair|W38ZDXDVYC]].

## Remarks

Proof idea.
The modular function $\Delta$ is trivial on the compact group $K$, so the hypothesis gives $\Delta(\theta(g)) = \Delta(g)^{-1}$; an involutive automorphism preserves Haar measure and $\Delta$, so $\Delta = 1$ and $G$ is unimodular.
For a bi-$K$-invariant function $f$ write $f^\theta = f \circ \theta$ and $f^\vee(g) = f(g^{-1})$; the hypothesis gives $f^\theta = f^\vee$.
Since $\theta$ is an automorphism, $(f_1 * f_2)^\theta = f_1^\theta * f_2^\theta$, and by unimodularity $(f_1 * f_2)^\vee = f_2^\vee * f_1^\vee$.
Comparing these gives $f_1^\vee * f_2^\vee = f_2^\vee * f_1^\vee$ for all bi-invariant $f_1, f_2$, and $f \mapsto f^\vee$ is a bijection of $L^1(K \backslash G / K)$.

Examples.
For $G$ abelian and $K = \set{e}$, take $\theta(g) = g^{-1}$.
For $G = \mathrm{SL}(2, \R)$ and $K = \mathrm{SO}(2)$, take $\theta(g) = (g^{T})^{-1}$: writing $g = k_1 a k_2$ with $a$ diagonal, one finds $\theta(g) = k_1 a^{-1} k_2 \in K g^{-1} K$.
The same argument with the Cartan decomposition $G = K A K$ shows that $(G, K)$ is a Gelfand pair for every connected semisimple Lie group $G$ with finite centre and maximal compact subgroup $K$.

## Explanations

### L1 human

A Gelfand pair is a group with a compact subgroup for which a certain convolution algebra is commutative.
Checking commutativity directly is hard.
Gelfand's trick replaces it by finding a symmetry of the group that sends each element to its inverse, up to multiplying by elements of $K$ on both sides.

### L2 human

The trick is the standard way to prove that the pairs coming from Riemannian symmetric spaces are Gelfand pairs, with $\theta$ the Cartan involution.
Once $(G, K)$ is a Gelfand pair, the theory of [[spherical functions|BKZNC76RC8]] and the [[spherical transform|E06PG40SVD]] applies.
The same idea for a finite group $G$ and subgroup $K$ shows that the permutation representation on $G / K$ is multiplicity free.
