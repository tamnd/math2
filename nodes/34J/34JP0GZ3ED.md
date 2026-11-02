---
tag: 34JP0GZ3ED
kind: definition
name: Fermi–Dirac integral
msc: ["33E20", "33B30"]
defines: HHKKPD81J2
uses: [0H5SYBSED9, 96CHDZKGQ0]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_Fermi%E2%80%93Dirac_integral
---

## Definition

Let $j > -1$ be a real number and let $\Gamma$ be the [[gamma function|0H5SYBSED9]].
The *complete Fermi–Dirac integral* of index $j$ is the function $F_j \colon \R \to \R$ given by
$$F_j(x) = \frac{1}{\Gamma(j+1)} \int_0^{\infty} \frac{t^j}{e^{t - x} + 1} \, dt.$$

## Remarks

The integral converges for $j > -1$: near $t = 0$ the integrand is bounded by $t^j$, and for large $t$ it decays like $t^j e^{x - t}$.

For $x < 0$, expanding $\frac{1}{e^{t-x} + 1} = \sum_{k \ge 1} (-1)^{k-1} e^{-k(t - x)}$ and integrating term by term gives
$$F_j(x) = \sum_{k=1}^{\infty} (-1)^{k-1} \frac{e^{kx}}{k^{j+1}} = -\operatorname{Li}_{j+1}(-e^x),$$
where $\operatorname{Li}_{j+1}$ is the [[polylogarithm|96CHDZKGQ0]], and the identity holds for all real $x$ by analytic continuation.
It also gives $F_j'(x) = F_{j-1}(x)$ for $j > 0$.

Example: for $j = 0$, $\int_0^\infty \frac{dt}{e^{t-x} + 1} = \log(1 + e^x)$, which matches $-\operatorname{Li}_1(-e^x) = \log(1 + e^x)$.

Non-example: for $j = -1$ the integrand behaves like $\frac{1}{t (e^{-x} + 1)}$ near $t = 0$, so the integral diverges; this is why $j > -1$ is required, and $F_{-1}$ is defined instead through the polylogarithm form.

Some authors omit the factor $1/\Gamma(j+1)$; the normalized version above is the one with $F_j(x) \sim e^x$ as $x \to -\infty$.
