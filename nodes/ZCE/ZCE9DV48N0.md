---
tag: ZCE9DV48N0
kind: definition
name: Mathieu function
msc: ["33E10", 34B30]
defines: 2DDZXF5EBY
uses: [0QQRP17Z7S, 0ATF6Q0633, 7WV6B2502K, BJVZXPB297]
sources:
  - url: https://en.wikipedia.org/wiki/Mathieu_function
---

## Definition

Let $a$ and $q$ be real numbers.
*Mathieu's equation* is the [[linear differential equation|0QQRP17Z7S]]
$$\frac{d^2 y}{dx^2} + (a - 2q \cos 2x)\, y = 0.$$
Fix $q$.
The values of $a$ for which the equation has a nonzero even solution of [[period|0ATF6Q0633]] $\pi$ or $2\pi$ form an increasing sequence $a_0(q) < a_1(q) < \cdots$.
For each $a_r(q)$, such a solution is unique up to a constant factor.
The *even Mathieu function* $\operatorname{ce}_r(x, q)$ is that solution for $a = a_r(q)$, normalised by $\int_0^{2\pi} \operatorname{ce}_r(x, q)^2\, dx = \pi$.
Its sign is fixed by continuity in $q$ from $\operatorname{ce}_0(x, 0) = \frac{1}{\sqrt 2}$ and $\operatorname{ce}_r(x, 0) = \cos rx$ for $r \ge 1$.
In the same way, odd solutions of period $\pi$ or $2\pi$ exist for an increasing sequence $b_1(q) < b_2(q) < \cdots$ of values of $a$.
The *odd Mathieu function* $\operatorname{se}_r(x, q)$ is the odd solution for $a = b_r(q)$, with the same normalisation and with $\operatorname{se}_r(x, 0) = \sin rx$.

## Remarks

The numbers $a_r(q)$ and $b_r(q)$ are the *characteristic values*; they are eigenvalues of [[Sturm–Liouville|7WV6B2502K]] problems on $[0, \pi]$ or $[0, \frac{\pi}{2}]$ with suitable boundary conditions.
The function $\operatorname{ce}_r$ or $\operatorname{se}_r$ has period $\pi$ when $r$ is even and period $2\pi$ when $r$ is odd.
Example: for $q = 0$ one has $a_r(0) = r^2$ and $\operatorname{ce}_r(x, 0) = \cos rx$ for $r \ge 1$; indeed $y = \cos rx$ satisfies $y'' + r^2 y = 0$ and $\int_0^{2\pi} \cos^2 rx\, dx = \pi$.
For $r = 0$ the constant must be $\frac{1}{\sqrt 2}$, since $\int_0^{2\pi} \frac12\, dx = \pi$.
Non-example: for $q = 0$ and $a = \frac14$, the solution $\cos \frac{x}{2}$ has period $4\pi$, not $\pi$ or $2\pi$, so it is not a Mathieu function in this sense.
For most other values of $a$, [[Floquet theory|BJVZXPB297]] gives a basis of solutions of the form $e^{i\mu x} p(x)$ and $e^{-i\mu x} p(-x)$, with $p$ of period $\pi$ and $\mu$ the characteristic exponent.
