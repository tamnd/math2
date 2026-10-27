---
tag: 004FRCXH6M
kind: definition
name: Exterior derivative
msc: [58A10]
defines: 0ZHSTAG8ZY
uses: [0QHTX7WQEY, 0S166D363M, 0MTENFBW3Q, 05AXG3QRKR, 0NS2QYVC4Y, 0GDNHS9J2X, 02NSMQVQWK, 0X308R2DBE]
sources:
  - url: https://en.wikipedia.org/wiki/Exterior_derivative
    locator: In terms of local coordinates
  - url: https://en.wikipedia.org/wiki/Exterior_derivative
    locator: In terms of axioms
  - url: https://en.wikipedia.org/wiki/Exterior_derivative
    locator: Exterior derivative in vector calculus
inventory: [70KHYD4XYE]
---

## Definition

Let $U \subseteq \mathbb{R}^n$ be open, and let $\omega = \sum_I f_I \, dx_I$ be a [[differential k-form|0QHTX7WQEY]] on $U$ whose coefficients $f_I$ are of class $C^1$.
The exterior derivative of $\omega$ is the $(k + 1)$-form
$$d\omega = \sum_I \sum_{j=1}^n \frac{\partial f_I}{\partial x_j} \, dx_j \wedge dx_I,$$
where $\wedge$ is the [[wedge product|0S166D363M]].

## Remarks

For a function $f$, $df = \sum_j \partial_j f \, dx_j$ is its differential, the [[one-form|0MTENFBW3Q]] that corresponds to the [[gradient|0NS2QYVC4Y]].
The operator $d$ is linear and satisfies $d(\alpha \wedge \beta) = d\alpha \wedge \beta + (-1)^k \alpha \wedge d\beta$ for a $k$-form $\alpha$. For $C^2$ forms, [[d d = 0|0X308R2DBE]].
In the plane, $d(L \, dx + M \, dy) = (\partial_x M - \partial_y L) \, dx \wedge dy$.
In $\mathbb{R}^3$, $d(F_1 \, dx + F_2 \, dy + F_3 \, dz)$ has the components of the [[curl|0GDNHS9J2X]] of $F$ as coefficients of $dy \wedge dz$, $dz \wedge dx$ and $dx \wedge dy$. Also $d(F_1 \, dy \wedge dz + F_2 \, dz \wedge dx + F_3 \, dx \wedge dy) = (\nabla \cdot F) \, dx \wedge dy \wedge dz$, which is the [[divergence|02NSMQVQWK]].

## Explanations

### L1 human

The exterior derivative is one operation that does the work of gradient, curl and divergence together.
You differentiate each coefficient in each direction and attach the new direction with a wedge product.
