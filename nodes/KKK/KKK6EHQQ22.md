---
tag: KKK6EHQQ22
kind: definition
name: Laguerre series expansion of the Laplace transform
msc: [44A10, 33C45, 65R10]
defines: HYRFMXAJVW
uses: [0V49JEZW06, WAMRHWW82R, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Laguerre_polynomials
---

## Definition

Let $L_n$ be the [[Laguerre polynomial|WAMRHWW82R]] of degree $n$, and let $\ell_n(t) = e^{-t/2} L_n(t)$ for $t \ge 0$.
The functions $\ell_0, \ell_1, \dots$ form an orthonormal basis of the [[space|SASP14MA1Z]] $L^2(0, \infty)$.
Let $f \in L^2(0, \infty)$, with coefficients $a_n = \int_0^\infty f(t)\, \ell_n(t)\, dt$, and let $F$ be its [[Laplace transform|0V49JEZW06]].
The *Laguerre series expansion* of $F$ is
$$F(s) = \sum_{n=0}^{\infty} a_n \frac{(s - 1/2)^n}{(s + 1/2)^{n+1}}, \qquad \operatorname{Re} s > 0.$$

## Remarks

The expansion holds because the Laplace transform of $\ell_n$ is $(s - 1/2)^n / (s + 1/2)^{n+1}$, and because $F(s)$ is the $L^2$ inner product of $f$ with $e^{-\bar{s} t}$, which lies in $L^2(0, \infty)$ when $\operatorname{Re} s > 0$.
With $w = (s - 1/2)/(s + 1/2)$, which maps the half-plane $\operatorname{Re} s > 0$ onto the unit disk, it reads $(s + 1/2) F(s) = \sum_{n} a_n w^n$.
The coefficients satisfy $\sum_n \abs{a_n}^2 = \norm{f}_2^2 < \infty$.

Example: $f = \ell_1$, that is $f(t) = e^{-t/2}(1 - t)$.
Then $a_1 = 1$ and all other $a_n = 0$.
The check: $\int_0^\infty e^{-st} e^{-t/2}(1 - t)\, dt = \frac{1}{s + 1/2} - \frac{1}{(s + 1/2)^2} = \frac{s - 1/2}{(s + 1/2)^2}$.

Non-example: $f(t) = 1$ has the Laplace transform $1/s$, but $f \notin L^2(0, \infty)$, so the coefficients $a_n$ are not defined by the formula above.

Applying the same expansion to $e^{-\sigma t} f(bt)$ for parameters $\sigma$ and $b > 0$ gives the scaled variants used in practice.
