---
tag: EY18HD35RG
kind: definition
name: Charlier polynomials
msc: [33C45, 42C05]
defines: 6KH8KVYS3R
uses: [0GBZM0MT0F, 0XB9GQTN9G]
sources:
  - url: https://en.wikipedia.org/wiki/Charlier_polynomials
---

## Definition

Let $a > 0$ be a real number and let $n \ge 0$ be an integer.
Write $x^{\underline{k}} = x (x - 1) \cdots (x - k + 1)$ for the falling factorial, with $x^{\underline{0}} = 1$.
The *Charlier polynomial* of degree $n$ with parameter $a$ is
$$C_n(x; a) = \sum_{k=0}^{n} \binom{n}{k} \left( -\frac{1}{a} \right)^k x^{\underline{k}},$$
where $\binom{n}{k}$ is the [[binomial coefficient|0GBZM0MT0F]].

## Remarks

In hypergeometric notation, $C_n(x; a) = {}_2F_0\left( -n, -x; ; -\frac{1}{a} \right)$.
They are orthogonal for the [[Poisson distribution|0XB9GQTN9G]]: $\sum_{x=0}^{\infty} \frac{a^x}{x!} C_m(x; a) C_n(x; a) = a^{-n} e^a n! \, \delta_{mn}$.
Example: $C_1(x; a) = 1 - \frac{x}{a}$.
Check: $\sum_{x \ge 0} \frac{a^x}{x!} \left( 1 - \frac{x}{a} \right) = e^a - \frac{1}{a} \cdot a e^a = 0$, and $\sum_{x \ge 0} \frac{a^x}{x!} \left( 1 - \frac{x}{a} \right)^2 = e^a \left( 1 - 2 + \frac{a + a^2}{a^2} \right) = \frac{e^a}{a}$.
They are symmetric in degree and variable: $C_n(x; a) = C_x(n; a)$ for nonnegative integers $n$ and $x$.
Non-example: the monomials $1$ and $x$ are not orthogonal for this weight, since $\sum_{x \ge 0} \frac{a^x}{x!} x = a e^a \ne 0$.
