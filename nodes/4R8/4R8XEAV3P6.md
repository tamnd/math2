---
tag: 4R8XEAV3P6
kind: definition
name: Laguerre polynomials
msc: [33C45, 42C05]
defines: WAMRHWW82R
uses: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Laguerre_polynomials
---

## Definition

Let $\alpha > -1$ be a real number and let $n \ge 0$ be an integer.
The *generalized Laguerre polynomial* of degree $n$ and parameter $\alpha$ is
$$L_n^{(\alpha)}(x) = \sum_{k=0}^{n} (-1)^k \frac{\Gamma(n + \alpha + 1)}{(n - k)! \, \Gamma(k + \alpha + 1)} \frac{x^k}{k!},$$
where $\Gamma$ is the [[gamma function|0H5SYBSED9]].
The *Laguerre polynomial* of degree $n$ is $L_n = L_n^{(0)}$.

## Remarks

For $\alpha = 0$ the coefficient is a binomial coefficient: $L_n(x) = \sum_{k=0}^{n} \binom{n}{k} \frac{(-x)^k}{k!}$.
Example: $L_1^{(\alpha)}(x) = 1 + \alpha - x$ and $L_2(x) = 1 - 2x + \frac{x^2}{2}$.
Rodrigues' formula: $L_n^{(\alpha)}(x) = \frac{x^{-\alpha} e^x}{n!} \frac{d^n}{dx^n} \left( e^{-x} x^{n + \alpha} \right)$.
Orthogonality: $\int_0^\infty L_m^{(\alpha)}(x) L_n^{(\alpha)}(x) \, x^\alpha e^{-x} \, dx = \frac{\Gamma(n + \alpha + 1)}{n!} \delta_{mn}$.
The polynomial $L_n^{(\alpha)}$ solves the [[Laguerre equation|FTGTM3JB1F]] $x y'' + (\alpha + 1 - x) y' + n y = 0$.
Check for $n = 1$: $y = 1 + \alpha - x$ gives $0 - (\alpha + 1 - x) + (1 + \alpha - x) = 0$.
Non-example: the clause $\alpha > -1$ is needed for orthogonality, because for $\alpha \le -1$ the weight $x^\alpha e^{-x}$ is not integrable near $0$.
