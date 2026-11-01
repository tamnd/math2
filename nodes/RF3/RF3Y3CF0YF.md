---
tag: RF3Y3CF0YF
kind: definition
name: Carleson measure
msc: [30H10, 42B35]
defines: SQHGJ9C0QE
uses: [8G5ABXRK85]
sources:
  - url: https://en.wikipedia.org/wiki/Carleson_measure
---

## Definition

Let $\mathbb{D}$ be the open [[unit disc|8G5ABXRK85]] and $\mathbb{T}$ the unit circle.
For an arc $I \subseteq \mathbb{T}$ of length $\ell(I)$, the *Carleson box* over $I$ is
$$S(I) = \set{r \zeta : \zeta \in I, \ 1 - \ell(I) \le r < 1}.$$
A positive Borel measure $\mu$ on $\mathbb{D}$ is a *Carleson measure* if there is a constant $C$ such that
$$\mu(S(I)) \le C \, \ell(I) \quad \text{for every arc } I \subseteq \mathbb{T}.$$

## Remarks

Carleson's embedding theorem: for $0 < p < \infty$, $\mu$ is a Carleson measure if and only if there is $C_p$ with $\int_{\mathbb{D}} \abs{f}^p \, d\mu \le C_p \norm{f}_{H^p}^p$ for all $f$ in the [[Hardy space|PNNNFJVF6W]] $H^p$.

Example: area measure $A$ on $\mathbb{D}$.
In polar coordinates, $A(S(I)) \le \ell(I) \int_{\max(0, 1 - \ell(I))}^1 r \, dr \le \ell(I) \min(\ell(I), 1) \le \ell(I)$.
So $A$ is a Carleson measure with $C = 1$.

Non-example: let $z_n = 1 - 2^{-n}$ and $\mu = \sum_{n \ge 1} n^{-2} \delta_{z_n}$, a finite measure.
Let $I_k$ be the arc of length $2^{-k}$ centred at $1$.
Then $S(I_k)$ contains $z_n$ for all $n \ge k$, so $\mu(S(I_k)) \ge \sum_{n \ge k} n^{-2} > 1/k$.
The ratio $\mu(S(I_k)) / \ell(I_k) > 2^k / k$ is unbounded, so $\mu$ is not a Carleson measure.
