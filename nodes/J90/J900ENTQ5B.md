---
tag: J900ENTQ5B
kind: definition
name: Dirichlet series as Mellin transforms
msc: [11M41, 44A15, 30B50]
defines: K5RXH32SE7
uses: [8MWTEF6462, N5PVGRJE1T, 0H5SYBSED9, 0YBDSJARWN]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_series
---

## Definition

Let $a \colon \set{1, 2, 3, \dots} \to \C$ and let $F(s) = \sum_{n \ge 1} a(n) n^{-s}$ be its [[Dirichlet series|8MWTEF6462]].
Let $\sigma_a$ be its abscissa of [[absolute convergence|0YBDSJARWN]], and assume $\sigma_a < \infty$.
The *Mellin representations* of $F$ are the two identities below, which hold for every $s \in \C$ with $\operatorname{Re} s > \max(\sigma_a, 0)$.

1. With $f_a(x) = \sum_{n \ge 1} a(n) e^{-nx}$ for $x > 0$,
$$\Gamma(s) F(s) = \int_0^\infty x^{s-1} f_a(x) \, dx = \mathcal{M}f_a(s).$$
2. With the summatory function $A(x) = \sum_{n \le x} a(n)$ for $x > 0$,
$$\frac{F(s)}{s} = \int_1^\infty A(x) \, x^{-s-1} \, dx = \mathcal{M}A(-s).$$

Here $\mathcal{M}$ is the [[Mellin transform|N5PVGRJE1T]] and $\Gamma$ is the [[gamma function|0H5SYBSED9]].

## Remarks

For identity 1, $\int_0^\infty x^{s-1} e^{-nx} \, dx = \Gamma(s) n^{-s}$ when $\operatorname{Re} s > 0$, and the sum of the absolute values $\Gamma(\operatorname{Re} s) \sum_n \abs{a(n)} n^{-\operatorname{Re} s}$ is finite when $\operatorname{Re} s > \sigma_a$, so sum and integral may be exchanged.
For identity 2, $A(x) = 0$ for $x < 1$, and $\int_n^\infty x^{-s-1} \, dx = n^{-s}/s$; exchanging sum and integral is justified the same way.
Example: $a(n) = 1$ gives $\sigma_a = 1$, $f_a(x) = 1/(e^{x} - 1)$ and $A(x) = \floor{x}$, so
$$\Gamma(s) \zeta(s) = \int_0^\infty \frac{x^{s-1}}{e^{x} - 1} \, dx, \qquad \frac{\zeta(s)}{s} = \int_1^\infty \floor{x} \, x^{-s-1} \, dx, \qquad \operatorname{Re} s > 1.$$
Non-example: at $s = 1$ with $a(n) = 1$, the condition $\operatorname{Re} s > \sigma_a$ fails, and indeed $\int_0^\infty dx/(e^x - 1)$ diverges at $0$.
