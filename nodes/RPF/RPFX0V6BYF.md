---
tag: RPFX0V6BYF
kind: definition
name: Littlewood polynomial
msc: [42A05, 30C10, 26D05]
defines: 5A16A9W335
uses: [J3NJQ5FZJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Littlewood_polynomial
---

## Definition

Let $n \ge 0$ be an integer.
A *Littlewood polynomial* of degree $n$ is a polynomial
$$p(z) = \sum_{k=0}^{n} a_k z^k$$
in one complex variable $z$ whose coefficients satisfy $a_k \in \set{-1, 1}$ for $k = 0, \ldots, n$.

## Remarks

On the unit circle, $\theta \mapsto p(e^{i\theta})$ is a [[trigonometric polynomial|J3NJQ5FZJ5]] with coefficients $a_k$.
By orthogonality of the functions $e^{ik\theta}$,
$$\frac{1}{2\pi} \int_{-\pi}^{\pi} \abs{p(e^{i\theta})}^2 \, d\theta = \sum_{k=0}^{n} a_k^2 = n + 1.$$
So $\max_{\abs{z} = 1} \abs{p(z)} \ge \sqrt{n+1}$ and $\min_{\abs{z} = 1} \abs{p(z)} \le \sqrt{n+1}$.
Littlewood asked whether there are constants $0 < A \le B$ and Littlewood polynomials of every degree with $A \sqrt{n+1} \le \abs{p(z)} \le B \sqrt{n+1}$ on $\abs{z} = 1$.
Balister, Booth, Bollobás, Morris and Tiba answered this positively in 2019.

Example: $p(z) = 1 + z - z^2$ has degree $2$ and coefficients $1, 1, -1$, all in $\set{-1, 1}$.
At $z = 1$ its value is $1$, and at $z = -1$ it is $-1$.

Non-example: $q(z) = 1 + z^2 = 1 + 0 \cdot z + z^2$ is not a Littlewood polynomial, since its coefficient of $z$ is $0$.
Polynomials with coefficients in $\set{-1, 0, 1}$ form a different, larger class.
