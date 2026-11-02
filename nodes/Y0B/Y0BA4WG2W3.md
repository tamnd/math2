---
tag: Y0BA4WG2W3
kind: definition
name: Confluent hypergeometric function
msc: [33C15]
defines: 6AZ4ZBN1M8
uses: [YZHM3HSM0F, NT917KFR57, 0MZB06ST2B]
sources:
  - url: https://en.wikipedia.org/wiki/Confluent_hypergeometric_function
---

## Definition

Let $a$ and $b$ be complex numbers with $b \notin \set{0, -1, -2, \dots}$.
Write $(x)_n = x (x + 1) \cdots (x + n - 1)$ for the [[Pochhammer symbol|YZHM3HSM0F]], with $(x)_0 = 1$.
*Kummer's confluent hypergeometric function* is the [[power series|0MZB06ST2B]]
$$M(a, b, z) = {}_1F_1(a; b; z) = \sum_{n = 0}^{\infty} \frac{(a)_n}{(b)_n} \frac{z^n}{n!}, \qquad z \in \C.$$
More generally, a *confluent hypergeometric function* is any solution of [[Kummer's equation|NT917KFR57]] $z w'' + (b - z) w' - a w = 0$.

## Remarks

The ratio of consecutive terms is $\frac{(a + n) z}{(b + n)(n + 1)}$, which tends to $0$, so the series converges for every $z$ and $M(a, b, \cdot)$ is entire.
Inserting the series into Kummer's equation shows that $M(a, b, z)$ is its solution that is analytic at $0$ with $M(a, b, 0) = 1$.
Example: $M(a, a, z) = e^z$, since $(a)_n / (a)_n = 1$.
Example: $M(1, 2, z) = \frac{e^z - 1}{z}$, since $\frac{(1)_n}{(2)_n\, n!} = \frac{1}{(n + 1)!}$.
Non-example: for $b = -1$ the series is not defined, since $(b)_2 = 0$ appears in a denominator.
If $a = -m$ with $m$ a nonnegative integer, the series stops and $M(-m, b, z)$ is a polynomial of degree $m$; for $b = \alpha + 1$ it is a multiple of the generalized Laguerre polynomial $L_m^{(\alpha)}(z)$.
Another notation is $\Phi(a; b; z)$.
