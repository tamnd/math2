---
tag: 8AX4XREEPX
kind: statement
role: theorem
name: Schlömilch's generalization of the condensation test
msc: [40A05]
uses: [0KN22AAW5R, 0CVVKY7GY2, 0B96KMDDD1]
about: [FJKV01J9F1]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_condensation_test
---

## Statement

Let $(a_n)_{n \ge 1}$ be a [[decreasing|0KN22AAW5R]] real sequence with $a_n \ge 0$ for all $n$.
Let $u_0 < u_1 < u_2 < \cdots$ be positive integers, and put $\Delta u_k = u_{k+1} - u_k$.
Assume that there is a constant $M$ with $\Delta u_{k} \le M \, \Delta u_{k-1}$ for all $k \ge 1$.
Then $\sum_{n=1}^{\infty} a_n$ [[converges|0CVVKY7GY2]] if and only if $\sum_{k=0}^{\infty} \Delta u_k \, a_{u_k}$ converges.

## Remarks

The proof cuts the series into blocks $u_k \le n < u_{k+1}$ of $\Delta u_k$ terms each.
Since $(a_n)$ decreases, the block sum lies between $\Delta u_k \, a_{u_{k+1}}$ and $\Delta u_k \, a_{u_k}$.
The upper bound shows that convergence of the condensed series gives convergence of $\sum a_n$.
The lower bound and $\Delta u_{k+1} \le M \Delta u_k$ show that $\Delta u_{k+1} a_{u_{k+1}}$ is at most $M$ times the block sum, which gives the converse.
With $u_k = 2^k$ this is the [[Cauchy condensation test|0B96KMDDD1]].
With $u_k = k^2$ for $k \ge 1$ the condensed series is $\sum (2k+1) a_{k^2}$, and the condition holds since $(2k+3)/(2k+1) \le 3$.
For $a_n = 1/n^p$ with $p > 0$ this gives $\sum (2k+1)/k^{2p}$, which converges exactly when $2p - 1 > 1$, that is $p > 1$.

## Explanations

### L1 human

For a decreasing series, you may keep only a sparse set of terms, provided you weight each kept term by the length of the gap after it.
The gaps may grow, but not too fast from one gap to the next.
The sparse weighted series and the original series then converge or diverge together.

### L2 human

The Cauchy condensation test uses the gaps $2^k$.
Schlömilch's version lets you choose gaps adapted to the series, such as the squares, which helps when $a_{k^2}$ has a simpler form than $a_{2^k}$.
The hypothesis that consecutive gaps have bounded ratio is what makes the lower bound work.
The proof is the same comparison of block sums as in the Cauchy case.
