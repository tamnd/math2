---
tag: Z4F0TEHBP1
kind: example
name: The second derivative test for x³ − 3x + y²
msc: [15A63, 26B12]
topics: [6TSCEW8QMK]
audience: ug1
instance_of: [01RBSSGMY5]
uses: [01RBSSGMY5, 0693Y2METT, 0GYDV9FE98, 0YTCMFB4HC]
sources:
  - url: https://en.wikipedia.org/wiki/Second_partial_derivative_test
  - url: https://en.wikipedia.org/wiki/Definite_quadratic_form
    locator: lead section
---

## Example

Let $f(x, y) = x^3 - 3x + y^2$ on $\mathbb{R}^2$.
We find its critical points and classify them by the type of a quadratic form.

1. The gradient is $\nabla f = (3x^2 - 3, \, 2y)$. It is zero exactly when $x = \pm 1$ and $y = 0$, so the [[critical points|0YTCMFB4HC]] are $(1, 0)$ and $(-1, 0)$.
2. The second partial derivatives are $f_{xx} = 6x$, $f_{xy} = 0$ and $f_{yy} = 2$. So the [[Hessian matrix|0693Y2METT]] is $H(x, y) = \begin{pmatrix} 6x & 0 \\ 0 & 2 \end{pmatrix}$.
3. At $(1, 0)$ the Hessian is $\operatorname{diag}(6, 2)$, and its form $6u^2 + 2v^2$ is positive definite. By [[the second derivative test|0GYDV9FE98]], $(1, 0)$ is a strict local minimum, with $f(1, 0) = 1 - 3 = -2$.
4. At $(-1, 0)$ the Hessian is $\operatorname{diag}(-6, 2)$, and its form $-6u^2 + 2v^2$ is indefinite. So $(-1, 0)$ is a saddle point, with $f(-1, 0) = -1 + 3 = 2$.
5. Check of step 4 by hand: along the $x$-direction, $f(-1 + t, 0) = 2 - 3t^2 + t^3$, which is less than $2$ for small $t \ne 0$. Along the $y$-direction, $f(-1, s) = 2 + s^2$, which is more than $2$ for $s \ne 0$.

## Remarks

The test works because, near a critical point $c$, Taylor's formula gives
$$f(c + h) = f(c) + \tfrac{1}{2} h^{\mathsf{T}} H(c) h + o(\lVert h \rVert^2).$$
So the [[type of the quadratic form|01RBSSGMY5]] $h \mapsto h^{\mathsf{T}} H(c) h$ decides the local behavior whenever it is definite or indefinite.
When the form is only semidefinite, the test gives no answer.

Change one sign and the picture changes.
For $g(x, y) = x^3 - 3x - y^2$ the Hessian at $(1, 0)$ is $\operatorname{diag}(6, -2)$, which is indefinite, and the Hessian at $(-1, 0)$ is $\operatorname{diag}(-6, -2)$, which is negative definite.
So $g$ has a saddle at $(1, 0)$ and a local maximum at $(-1, 0)$.

## Explanations

### L1 human

At a critical point the surface is flat to first order, like the top of a hill or the bottom of a valley.
The second derivatives say how it bends.
At $(1, 0)$ the surface bends up in every direction, so the point is the bottom of a valley.
At $(-1, 0)$ it bends down along the $x$-direction and up along the $y$-direction, so the point is a saddle, like a mountain pass.

### L2 human

The typical use is in optimization in several variables: find the zeros of the gradient, then classify each one by its Hessian form.
Watch out: a local minimum need not be a global minimum.
Here $f(x, 0) = x^3 - 3x$ tends to $-\infty$ as $x \to -\infty$, so $f$ has no smallest value, although $(1, 0)$ is a strict local minimum.
