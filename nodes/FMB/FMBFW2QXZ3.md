---
tag: FMBFW2QXZ3
kind: definition
name: Finite-rank operator
msc: [47B07, 47A05]
defines: Z8FABSYQTS
uses: [03J5RAKB30, 03TM135G0N, 0WSFKKT6FF, 0ZZXSBTR4J]
sources:
  - url: https://en.wikipedia.org/wiki/Finite-rank_operator
---

## Definition

Let $X$ and $Y$ be [[normed spaces|03J5RAKB30]] over $\mathbb{K} = \R$ or $\C$, and let $T \colon X \to Y$ be a [[bounded linear map|03TM135G0N]].
The map $T$ is a *finite-rank operator* if its [[image|0WSFKKT6FF]] $T(X)$ is a finite-dimensional subspace of $Y$.
Its *rank* is the dimension of $T(X)$.

## Remarks

Equivalently, there are $n \ge 0$, bounded linear functionals $f_1, \ldots, f_n$ on $X$ and vectors $y_1, \ldots, y_n \in Y$ with
$$T x = \sum_{k=1}^{n} f_k(x) \, y_k \quad \text{for all } x \in X.$$
Example: for a nonzero bounded linear functional $f$ on $X$ and a nonzero $y \in Y$, the map $x \mapsto f(x) y$ has image $\mathbb{K} y$, so it has rank $1$.
Non-example: the identity map of $\ell^2$ is bounded, but its image $\ell^2$ is infinite-dimensional, so it is not of finite rank.
For linear maps between finite-dimensional spaces, the rank is the usual [[rank of a linear map|0ZZXSBTR4J]].
A bounded finite-rank operator is compact, because bounded subsets of a finite-dimensional normed space are relatively compact.
On Hilbert spaces, every compact operator is a norm limit of finite-rank operators.
On general Banach spaces this can fail; this is the question of the approximation property.
