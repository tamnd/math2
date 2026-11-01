---
tag: PQV6DNE0CW
kind: definition
name: Binary quadratic form
msc: ["11E16"]
defines: SBDSYA037Q
uses: [2FQVQCTV88, 0C4JS9RF5M, 0C8WYW4KYQ, 0V9PMN0RBH]
sources:
  - url: https://en.wikipedia.org/wiki/Binary_quadratic_form
---

## Definition

A *binary quadratic form* (with integer coefficients) is a polynomial
$$f(x, y) = ax^2 + bxy + cy^2$$
in two variables $x, y$, with coefficients $a, b, c$ in the [[integers|0C4JS9RF5M]].
Its *discriminant* is $D = b^2 - 4ac$.
The form is *primitive* if the [[greatest common divisor|0C8WYW4KYQ]] of $a$, $b$, $c$ is $1$.
Two forms $f$ and $g$ are *properly equivalent* if $g(x, y) = f(\alpha x + \beta y, \gamma x + \delta y)$ for some matrix $\begin{pmatrix} \alpha & \beta \\ \gamma & \delta \end{pmatrix}$ in the [[special linear group|0V9PMN0RBH]] $\mathrm{SL}_2(\Z)$.

## Remarks

Properly equivalent forms have the same discriminant and represent the same integers.
The discriminant always satisfies $D \equiv 0$ or $1 \pmod 4$.
The form is positive definite if and only if $D < 0$ and $a > 0$.
Some authors write the form as $ax^2 + 2bxy + cy^2$ and require $a, b, c$ to be integers; this is Gauss's convention.

Example: $x^2 + y^2$ has $a = 1$, $b = 0$, $c = 1$, so it is a primitive binary quadratic form of discriminant $-4$.

Non-example: $x^2 + y^2 + z^2$ is a quadratic form with integer coefficients, but it has three variables, so it is not binary.
