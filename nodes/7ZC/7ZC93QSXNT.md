---
tag: 7ZC93QSXNT
kind: definition
name: Ramanujan tau function
msc: [11F30, 11F11, 11A25]
defines: 6DNZAGCSQS
uses: [A50Y012RBP, X6XGGH5FPW, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Ramanujan_tau_function
---

## Definition

Let $\mathbb{H}$ be the [[upper half-plane|X6XGGH5FPW]], and for $z \in \mathbb{H}$ let $q = e^{2 \pi i z}$.
The *Ramanujan tau function* $\tau \colon \Z_{\ge 1} \to \Z$ is defined by the expansion
$$q \prod_{m = 1}^{\infty} (1 - q^m)^{24} = \sum_{n = 1}^{\infty} \tau(n) q^n.$$
The left side is the [[cusp form|A50Y012RBP]] $\Delta(z)$ of weight $12$.

## Remarks

Example: the coefficient of $q^2$ comes only from $q \cdot (1 - q)^{24}$, which gives $-24$; so $\tau(2) = -24$.
The function is multiplicative: $\tau(mn) = \tau(m)\tau(n)$ when $\gcd(m, n) = 1$.
For primes $p$ and $r \ge 1$, $\tau(p^{r+1}) = \tau(p)\tau(p^r) - p^{11} \tau(p^{r-1})$.
Non-example: $\tau$ is not completely multiplicative, since $\tau(4) = \tau(2)^2 - 2^{11} = -1472 \neq 576 = \tau(2)^2$.
Ramanujan's congruence: $\tau(n) \equiv \sigma_{11}(n) \pmod{691}$, where $\sigma_{11}(n) = \sum_{d \mid n} d^{11}$.
For $n = 2$: $\sigma_{11}(2) - \tau(2) = 2049 + 24 = 2073 = 3 \cdot 691$.
Whether $\tau(n) \neq 0$ for all $n$ is an open question, known as Lehmer's conjecture.
