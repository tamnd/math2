---
tag: 0SSKBQN58M
kind: statement
role: theorem
name: Hurwitz's theorem
aliases: [hurwitz-theorem-complex-analysis]
msc: [30C15]
uses: [097KNJFJ7V, 0DG0Z72CQD, 0431RN0R1N, 064N002TX4]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_(complex_analysis)
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_(complex_analysis)
    locator: Applications
same_as:
  wikidata: Q1136043
  wikipedia: Hurwitz's theorem (complex analysis)
---

## Statement

Let $G$ be a [[domain|097KNJFJ7V]] in $\mathbb{C}$, that is, a connected open set.
Let $(f_k)$ be a sequence of [[holomorphic|0DG0Z72CQD]] functions on $G$ that converges uniformly on each compact subset of $G$ to a function $f$.
Suppose that $f$ is not identically zero on $G$, and that $f$ has a zero of [[order|064N002TX4]] $m$ at a point $z_0 \in G$.
Then for each sufficiently small $\rho > 0$ there is an integer $N$ with the following property.
For each $k \ge N$, the function $f_k$ has exactly $m$ zeros in the disc $|z - z_0| < \rho$, each counted as many times as its order.

## Remarks

The limit $f$ is holomorphic on $G$ by the [[theorem on uniform limits|0431RN0R1N]].
A consequence: if no $f_k$ has a zero in $G$, then $f$ either has no zero in $G$ or is identically zero.
A second consequence: if each $f_k$ is injective on $G$, then $f$ is injective or constant.
The radius $\rho$ must be small: $f_n(z) = z - 1 + \frac{1}{n}$ has one zero in the unit disc, but its limit $z - 1$ has none there.

## Explanations

### L1 human

Zeros of holomorphic functions do not suddenly appear or disappear under uniform limits.
Near a zero of the limit, each function far along in the sequence has the same number of zeros.
The proof compares $f_k$ with $f$ on a small circle, as in [[Rouché's theorem|0D430QR02W]].
