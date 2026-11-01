---
tag: SVTT5MWB2X
kind: definition
name: Large sieve
msc: [11N35, 11L07]
defines: N15YK7XG1H
uses: [97PBMQCPPM, 0FANE7P0DY]
sources:
  - url: https://en.wikipedia.org/wiki/Large_sieve
---

## Definition

For real $x$ write $e(x) = e^{2\pi i x}$ and let $\norm{x}$ be the distance from $x$ to the nearest integer.
Let $M$ be an integer, $N \ge 1$ an integer and $(a_n)_{M < n \le M+N}$ complex numbers, and let
$$S(\alpha) = \sum_{M < n \le M + N} a_n\, e(n\alpha),$$
an [[exponential sum|97PBMQCPPM]].
Let $\delta \in (0, 1]$, and let $\alpha_1, \ldots, \alpha_R$ be real numbers with $\norm{\alpha_r - \alpha_s} \ge \delta$ for all $r \ne s$.
The *large sieve inequality* is
$$\sum_{r=1}^{R} \abs{S(\alpha_r)}^2 \le \left(N - 1 + \delta^{-1}\right) \sum_{M < n \le M+N} \abs{a_n}^2.$$
The *large sieve* is the method that bounds sifted sets by this inequality.
Its arithmetic form reads as follows.
For each prime $p \le Q$, let $\omega(p)$ residue classes modulo $p$ be removed, with $0 \le \omega(p) < p$.
If $\mathcal{Z}$ is a set of integers in $(M, M+N]$ that meets none of the removed classes, then
$$\#\mathcal{Z} \le \frac{N + Q^2}{L}, \qquad L = \sum_{q \le Q} \mu(q)^2 \prod_{p \mid q} \frac{\omega(p)}{p - \omega(p)},$$
where $\mu$ is the [[Möbius function|0FANE7P0DY]].

## Remarks

Example: take $N = 1$, so $S(\alpha) = a_{M+1} e((M+1)\alpha)$ and $\abs{S(\alpha_r)}^2 = \abs{a_{M+1}}^2$ for each $r$.
The $\delta$-separated points in $[0, 1)$ number at most $\delta^{-1}$, so the left side is at most $\delta^{-1} \abs{a_{M+1}}^2$, which is the right side.
Non-example: if the separation fails, say $\alpha_1 = \cdots = \alpha_R$, the left side is $R \abs{S(\alpha_1)}^2$, which exceeds any fixed bound as $R$ grows.
The fractions $a/q$ with $q \le Q$ and $\gcd(a, q) = 1$ are $Q^{-2}$-separated modulo $1$, which gives the form
$$\sum_{q \le Q} \sum_{\substack{a = 1 \\ \gcd(a,q) = 1}}^{q} \abs{S(a/q)}^2 \le (N - 1 + Q^2) \sum_{n} \abs{a_n}^2.$$
The constant $N - 1 + \delta^{-1}$ is due to Montgomery–Vaughan and Selberg.
