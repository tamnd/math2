---
tag: DKVBV788GT
kind: definition
name: Meijer G-function
msc: [33C60]
defines: 19JNNN5KV7
uses: [1PDGBGEHM2, 0H5SYBSED9, 06ZGPYTWK8]
sources:
  - url: https://en.wikipedia.org/wiki/Meijer_G-function
---

## Definition

Let $m, n, p, q$ be integers with $0 \le m \le q$ and $0 \le n \le p$.
Let $a_1, \dots, a_p$ and $b_1, \dots, b_q$ be complex numbers such that $a_k - b_j$ is not a positive integer for $1 \le k \le n$ and $1 \le j \le m$.
Let $\Gamma$ be the [[gamma function|0H5SYBSED9]], and let $z \ne 0$ be complex with a fixed branch of $\log z$.
The *Meijer G-function* is the [[Barnes integral|1PDGBGEHM2]]
$$G^{m, n}_{p, q}\left( \begin{matrix} a_1, \dots, a_p \\ b_1, \dots, b_q \end{matrix} \,\middle|\, z \right) = \frac{1}{2\pi i} \int_L \frac{\prod_{j = 1}^{m} \Gamma(b_j - s) \prod_{k = 1}^{n} \Gamma(1 - a_k + s)}{\prod_{j = m + 1}^{q} \Gamma(1 - b_j + s) \prod_{k = n + 1}^{p} \Gamma(a_k - s)}\, z^{s}\, ds.$$
The path $L$ separates the poles $s = b_j + \ell$ of the factors $\Gamma(b_j - s)$ from the poles $s = a_k - 1 - \ell$ of the factors $\Gamma(1 - a_k + s)$, where $\ell \in \N$.
Call these the $b$-poles and the $a$-poles.
The path $L$ is one of the following:

1. a path from $-i\infty$ to $+i\infty$, where the integral converges;
2. a loop from $+\infty$ to $+\infty$ around all $b$-poles once in the negative direction, when $q \ge 1$ and either $p < q$, or $p = q$ and $\abs{z} < 1$;
3. a loop from $-\infty$ to $-\infty$ around all $a$-poles once in the positive direction, when $p \ge 1$ and either $p > q$, or $p = q$ and $\abs{z} > 1$.

## Remarks

The condition on $a_k - b_j$ makes the two families of poles disjoint, so a separating path exists.
When more than one choice of $L$ is possible, they give the same value.
Example: $G^{1, 0}_{0, 1}(- ; 0 \mid z) = e^{-z}$, where $-$ marks the empty list of parameters $a_k$.
Check: the integrand is $\Gamma(-s) z^s$, and with the loop of type 2 the residues at $s = \ell$ give $\sum_{\ell \ge 0} \frac{(-1)^\ell}{\ell!} z^\ell$.
Non-example: $m = 2$ with $q = 1$ is not allowed, since $m \le q$ fails; there are not enough parameters $b_j$ for two factors $\Gamma(b_j - s)$.
Every [[generalized hypergeometric function|VDBAW9PN88]] is a G-function: if no $a_k$ is a nonpositive integer, no $b_j$ is a nonpositive integer, $p \le q + 1$, and $\abs{z} < 1$ when $p = q + 1$, then
$${}_pF_q(a_1, \dots, a_p; b_1, \dots, b_q; z) = \frac{\prod_{j} \Gamma(b_j)}{\prod_{k} \Gamma(a_k)}\, G^{1, p}_{p, q + 1}\left( \begin{matrix} 1 - a_1, \dots, 1 - a_p \\ 0, 1 - b_1, \dots, 1 - b_q \end{matrix} \,\middle|\, -z \right).$$
