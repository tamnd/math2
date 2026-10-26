---
tag: 0BEZX8F2XW
kind: statement
role: theorem
name: Solutions for complex conjugate roots
msc: [34A30]
uses: [0QDXMG46QW, 0A6PGTTP2A, 0HRVY67CNV, 04R3CY41VJ]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_equation_(calculus)
    locator: Complex roots
---

## Statement

Let $a_0, \dots, a_{n-1}$ be real numbers, and let $p$ be the [[characteristic polynomial|0QDXMG46QW]] of the equation $y^{(n)} + a_{n-1} y^{(n-1)} + \dots + a_0 y = 0$.
Let $\alpha + i \beta$ be a root of $p$ of multiplicity $m$, with $\alpha, \beta \in \mathbb{R}$ and $\beta \ne 0$.
Then $\alpha - i \beta$ is also a root of multiplicity $m$, and the $2m$ functions
$$x^k e^{\alpha x} \cos(\beta x), \quad x^k e^{\alpha x} \sin(\beta x), \qquad k = 0, \dots, m - 1,$$
are linearly independent real solutions of the equation on $\mathbb{R}$.

## Remarks

By [[Euler's formula|04R3CY41VJ]], $e^{(\alpha + i \beta) x} = e^{\alpha x} (\cos \beta x + i \sin \beta x)$. Its real and imaginary parts are solutions because the coefficients are real.
For order $2$ and roots $\alpha \pm i \beta$, the real solutions are $e^{\alpha x} (c_1 \cos \beta x + c_2 \sin \beta x)$.
Example: $y'' + 2 y' + 5 y = 0$ has the roots $-1 \pm 2 i$, so its solutions are $e^{-x} (c_1 \cos 2x + c_2 \sin 2x)$.
These families for all roots, together with those of [[real roots|0HRVY67CNV]], give a real fundamental system.

## Explanations

### L1 human

Complex roots come in conjugate pairs, because the polynomial has real coefficients.
Each pair gives an oscillation: a sine and a cosine with frequency $\beta$.
The real part $\alpha$ makes the oscillation grow if $\alpha > 0$ and decay if $\alpha < 0$.
