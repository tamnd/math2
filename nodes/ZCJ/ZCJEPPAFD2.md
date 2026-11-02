---
tag: ZCJEPPAFD2
kind: definition
name: Varifold
msc: [49Q15, 49Q20]
defines: N3QA80M44M
uses: [HZNEQQBCW4, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Varifold
---

## Definition

Let $U \subseteq \R^n$ be an [[open set|02BH3MCBQB]] and let $0 \le m \le n$.
Let $G(n, m)$ be the Grassmannian of $m$-dimensional linear subspaces of $\R^n$, with its usual compact metric topology.
An *$m$-dimensional varifold* in $U$ is a [[Radon measure|HZNEQQBCW4]] $V$ on the locally compact space $U \times G(n, m)$.
The *weight* of $V$ is the Radon measure $\norm{V}$ on $U$ given by $\norm{V}(A) = V(A \times G(n, m))$.

## Remarks

Example: let $M \subseteq U$ be an $m$-dimensional $C^1$ submanifold that is a closed subset of $U$, with tangent plane $T_x M$ at $x \in M$.
Let $\mathcal{H}^m$ be the $m$-dimensional [[Hausdorff measure|Q1TGZK8RN6]], which is surface area on $M$.
Set $V(B) = \mathcal{H}^m(\set{x \in M : (x, T_x M) \in B})$ for Borel sets $B \subseteq U \times G(n, m)$.
This is a Borel measure that is finite on compact sets, since $M$ has locally finite area, so $V$ is a varifold; its weight is $\mathcal{H}^m$ restricted to $M$.
More generally, a [[rectifiable set|7N0GFMW05R]] with a positive density function gives a *rectifiable varifold*.
Non-example: counting measure on a countable dense subset of $U \times G(n, m)$ is not finite on compact sets with interior, so it is not a Radon measure and not a varifold.
