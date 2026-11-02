---
tag: EJD3C6QW9T
kind: definition
name: Stein manifold
msc: [32Q28, "32E10"]
defines: HMCD0JBFST
uses: [JSGWAN2RJV, 507C34W0ZT, 0R6EWFKRCF, CD6SMMZSW8, 03PPNCM9GG]
sources:
  - url: https://en.wikipedia.org/wiki/Stein_manifold
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] of complex dimension $n$ that is [[second countable|03PPNCM9GG]], and let $\mathcal{O}(X)$ be the algebra of [[holomorphic functions|507C34W0ZT]] on $X$.
For a [[compact set|0R6EWFKRCF]] $K \subseteq X$, its [[holomorphically convex hull|CD6SMMZSW8]] is
$$\widehat{K} = \set{x \in X : \abs{f(x)} \le \sup_{K} \abs{f} \text{ for all } f \in \mathcal{O}(X)}.$$
The manifold $X$ is a *Stein manifold* if:

1. $X$ is holomorphically convex: $\widehat{K}$ is compact for every compact $K \subseteq X$.
2. $X$ is holomorphically separable: for all $x \ne y$ in $X$ there is $f \in \mathcal{O}(X)$ with $f(x) \ne f(y)$.

## Remarks

Some authors add a third condition: at every point $x$ there are $f_1, \dots, f_n \in \mathcal{O}(X)$ that form local coordinates near $x$.
This condition follows from the first two.
Example: $X = \C^n$ is Stein.
The coordinate functions separate points.
The hull $\widehat{K}$ is closed, and $\abs{z_j} \le \max_K \abs{z_j}$ on $\widehat{K}$ for each $j$.
So $\widehat{K}$ lies in a compact polydisc, and it is compact.
Non-example: a compact connected complex manifold $X$ of positive dimension is not Stein.
Every $f \in \mathcal{O}(X)$ is constant, by the maximum principle, so clause 2 fails.
A domain in $\C^n$ is a Stein manifold if and only if it is a domain of holomorphy.
