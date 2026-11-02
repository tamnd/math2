---
tag: B4Z8C36HEB
kind: definition
name: Linear system of divisors
msc: [14C20]
defines: GHRPE8CXJ9
uses: [A4H4CZ2V35, FHV05ZK99F, 7JCF2TE3V5]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_system_of_divisors
---

## Definition

Let $X$ be a normal [[projective variety|A4H4CZ2V35]] over an algebraically closed field $k$, and let $D$ be a [[Cartier divisor|FHV05ZK99F]] on $X$.
Two Cartier divisors are *linearly equivalent* if their difference is principal.
The *complete linear system* $\abs{D}$ is the set of effective Cartier divisors on $X$ that are linearly equivalent to $D$.
Let $V = H^0(X, \mathcal{O}_X(D))$, a finite-dimensional vector space, where $\mathcal{O}_X(D)$ is the [[invertible sheaf|7JCF2TE3V5]] of $D$.
Each nonzero $s \in V$ has a divisor of zeros $(s)_0 \in \abs{D}$, and $s \mapsto (s)_0$ gives a bijection between $(V \setminus \set{0})/k^*$ and $\abs{D}$.
A *linear system* is a subset of $\abs{D}$ of the form $\set{(s)_0 : s \in W \setminus \set{0}}$ for a linear subspace $W \subseteq V$.
Its dimension is $\dim W - 1$.

## Remarks

The *base locus* of a linear system is the intersection of the supports of all its divisors; the system is *base-point-free* if the base locus is empty.

Example: on $X = \mathbb{P}^n_k$ with $D$ a hyperplane, $V$ is the space of linear forms in $n+1$ variables.
So $\abs{D}$ is the set of all hyperplanes, a linear system of dimension $n$, and it is base-point-free.

Non-example: on $\mathbb{P}^1_k$, the set of divisors $\set{p, \; p + q}$ for two points $p, q$ is not a linear system.
The two divisors have degrees $1$ and $2$, so they are not linearly equivalent and do not lie in one $\abs{D}$.

A base-point-free linear system of dimension $r$, with a basis $s_0, \dots, s_r$ of $W$, gives a morphism $X \to \mathbb{P}^r_k$, $x \mapsto [s_0(x) : \dots : s_r(x)]$.
