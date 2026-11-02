---
tag: 5WA6FC4JQD
kind: definition
name: E-infinity operad
msc: [55P48, 18M75]
defines: T78YG90VVT
uses: [0RJMNEN3BJ, 0YSE802YCQ, R5WP8Z69Q8, 0CNQXVBHCX]
sources:
  - url: https://en.wikipedia.org/wiki/E∞-operad
---

## Definition

An *operad* $\mathcal{O}$ in [[topological spaces|0CNQXVBHCX]] consists of spaces $\mathcal{O}(n)$ for $n \ge 0$ and the following data.
There is a right [[action|0YSE802YCQ]] of the [[symmetric group|0RJMNEN3BJ]] $\Sigma_n$ on each $\mathcal{O}(n)$ and an identity element $1 \in \mathcal{O}(1)$.
There are continuous composition maps
$$\mathcal{O}(k) \times \mathcal{O}(j_1) \times \cdots \times \mathcal{O}(j_k) \to \mathcal{O}(j_1 + \cdots + j_k),$$
which are associative, unital and equivariant in the standard sense.
An operad $\mathcal{O}$ is an *$E_\infty$ operad* if, for every $n \ge 0$:

1. the space $\mathcal{O}(n)$ is [[contractible|R5WP8Z69Q8]], and
2. the action of $\Sigma_n$ on $\mathcal{O}(n)$ is free.

## Remarks

Often one also asks the action to be nice enough that $\mathcal{O}(n) \to \mathcal{O}(n)/\Sigma_n$ is a principal $\Sigma_n$-bundle, so that $\mathcal{O}(n)/\Sigma_n$ is a model of $B\Sigma_n$.

Example: the linear isometries operad, with $\mathcal{L}(n)$ the space of linear isometric embeddings $(\R^\infty)^n \to \R^\infty$ and composition by composing maps.
Each $\mathcal{L}(n)$ is contractible, and $\Sigma_n$ acts by permuting the $n$ copies of $\R^\infty$.
The action is free: an isometric embedding sends the $n$ summands to mutually orthogonal subspaces, so it is not invariant under a nontrivial permutation.

Example: the Barratt–Eccles operad has $\mathcal{O}(n) = E\Sigma_n$, which is contractible with a free $\Sigma_n$-action.

Non-example: the commutative operad, with $\mathcal{O}(n)$ a single point for every $n$, satisfies clause 1 but not clause 2 when $n \ge 2$, since $\Sigma_n$ fixes the point.
Its algebras are strictly commutative monoids, which are too restrictive in homotopy theory.
