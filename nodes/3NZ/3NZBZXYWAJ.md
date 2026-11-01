---
tag: 3NZBZXYWAJ
kind: definition
name: Eisenstein series
msc: [11F11]
defines: EYREVY31BN
uses: [X6XGGH5FPW, GWKN5VG78A, 1XWBY4N0VT, 04J4Z73J5B, 0KC00K7KY4]
sources:
  - url: https://en.wikipedia.org/wiki/Eisenstein_series
---

## Definition

Let $k \ge 4$ be an even integer and let $\mathbb{H}$ be the [[upper half-plane|X6XGGH5FPW]].
The *Eisenstein series of weight $k$* is the function $G_k \colon \mathbb{H} \to \C$ given by
$$G_k(\tau) = \sum_{(m, n) \in \Z^2 \setminus \set{(0, 0)}} \frac{1}{(m\tau + n)^k}.$$
The *normalized Eisenstein series* is $E_k = G_k / (2\zeta(k))$, where $\zeta$ is the [[Riemann zeta function|1XWBY4N0VT]].

## Remarks

For $k \ge 3$ the series converges absolutely and locally uniformly on $\mathbb{H}$.
So $G_k$ is holomorphic, and it is a [[modular form|GWKN5VG78A]] of weight $k$ for $\mathrm{SL}_2(\Z)$.
With $q = e^{2 \pi i \tau}$, $\sigma_{k-1}(n) = \sum_{d \mid n} d^{k-1}$ (a [[divisor function|04J4Z73J5B]]) and $B_k$ the $k$-th [[Bernoulli number|0KC00K7KY4]]:
$$E_k(\tau) = 1 - \frac{2k}{B_k} \sum_{n \ge 1} \sigma_{k-1}(n) q^n.$$
Example: $B_4 = -1/30$ gives $E_4 = 1 + 240 \sum_{n \ge 1} \sigma_3(n) q^n$, and $B_6 = 1/42$ gives $E_6 = 1 - 504 \sum_{n \ge 1} \sigma_5(n) q^n$.
Non-example: for odd $k$, the terms for $(m, n)$ and $(-m, -n)$ cancel, so the sum is $0$; this is why $k$ is even.
For $k = 2$ the double series does not converge absolutely, and the function $E_2$ obtained by summing in a fixed order is not a modular form.
