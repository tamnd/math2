---
tag: 0BRXFNQ5JV
kind: statement
role: theorem
name: Polar form
aliases: [polar-form-of-a-complex-number]
msc: [30A99]
uses: [0SQSQP748R, 0KW2X0TFBX, 04R3CY41VJ]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_coordinate_system
    locator: Complex numbers
  - url: https://en.wikipedia.org/wiki/Complex_number
    locator: Polar form
---

## Statement

Let $z$ be a complex number with $z \neq 0$, let $r = |z|$ be its [[modulus|0KW2X0TFBX]] and let $\theta = \operatorname{Arg} z$ be its [[principal argument|0SQSQP748R]].
Then
$$z = r (\cos \theta + i \sin \theta) = r e^{i \theta}.$$

## Remarks

The second equality is [[Euler's formula|04R3CY41VJ]].
The pair $(r, \theta)$ gives the polar coordinates of the point $z$ in the [[complex plane|0CTE7A31XQ]].
Polar form makes products easy: $r e^{i \theta} \cdot s e^{i \varphi} = r s \, e^{i (\theta + \varphi)}$.

## Explanations

### L1 human

You can describe a point of the plane by its distance from $0$ and its direction.
For example, $1 + i$ has distance $\sqrt{2}$ and direction $\pi/4$, so $1 + i = \sqrt{2} \, e^{i \pi/4}$.
