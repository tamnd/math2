---
tag: 0HYPR64JM2
kind: statement
role: theorem
name: Mean value property
aliases: [mean-value-property-of-harmonic-functions, gauss-mean-value-theorem]
msc: [31A05]
uses: [031BG625Y3, 0DG10TVYPN]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_function
    locator: The mean value property
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula
    locator: Consequences
---

## Statement

Let $U \subseteq \mathbb{C}$ be an open set, and identify $\mathbb{C}$ with $\mathbb{R}^2$ by $x + iy \leftrightarrow (x, y)$.
Let $u : U \to \mathbb{R}$ be harmonic: $u$ is twice continuously differentiable and $u_{xx} + u_{yy} = 0$ on $U$.
Let $c \in \mathbb{C}$ and $r > 0$ be such that the closed disc $\{z : |z - c| \le r\}$ is contained in $U$.
Then
$$u(c) = \frac{1}{2\pi} \int_0^{2\pi} u(c + r e^{i\theta}) \, d\theta.$$

## Remarks

The value of $u$ at the center of the circle is the average of $u$ on the circle.
For holomorphic functions, the same formula holds, and it follows from [[Cauchy's integral formula|0DG10TVYPN]] with $a = c$. On a disc, $u$ is the [[real part of a holomorphic function|031BG625Y3]], which gives the harmonic case.
The property also holds for averages over the solid disc. A continuous function with the mean value property on all small circles is harmonic.

## Explanations

### L1 human

If $u$ is harmonic, its value at a point is the average of its values on each circle around that point, as long as the closed disc stays in the domain.
For example, $u = x^2 - y^2$ at $0$ is $0$, and on the unit circle it is $\cos 2\theta$, whose average is $0$.
