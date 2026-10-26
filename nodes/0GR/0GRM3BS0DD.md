---
tag: 0GRM3BS0DD
kind: counterexample
name: Curl-free field that is not conservative
aliases: [vortex-field]
msc: [26B12]
uses: [0GDNHS9J2X, 05R9NF2J49, 0B22P010D6, 075C629XTH, 0BFN21TF5F, 0YS8RX87F4]
sources:
  - url: https://en.wikipedia.org/wiki/Conservative_vector_field
    locator: Irrotational vector fields
  - url: https://en.wikipedia.org/wiki/Closed_and_exact_differential_forms
    locator: Examples
---

## Counterexample

One could guess that each $C^1$ vector field with zero [[curl|0GDNHS9J2X]] on an open set is [[conservative|05R9NF2J49]].
This is false.
Let $U = \{(x, y, z) \in \mathbb{R}^3 : (x, y) \ne (0, 0)\}$, which is $\mathbb{R}^3$ minus the $z$-axis, and let
$$F(x, y, z) = \left( \frac{-y}{x^2 + y^2}, \ \frac{x}{x^2 + y^2}, \ 0 \right).$$
Then $\nabla \times F = 0$ on $U$, but $F$ is not conservative on $U$.

## Remarks

The third component of $\nabla \times F$ is $\partial_x \big( x / (x^2 + y^2) \big) - \partial_y \big( -y / (x^2 + y^2) \big) = \frac{y^2 - x^2}{(x^2 + y^2)^2} - \frac{y^2 - x^2}{(x^2 + y^2)^2} = 0$, and the other two components are zero.
On the unit circle $\gamma(t) = (\cos t, \sin t, 0)$, $t \in [0, 2\pi]$, we have $F(\gamma(t)) \cdot \gamma'(t) = 1$. So the circulation is $2\pi \ne 0$, and [[path independence|0BFN21TF5F]] fails.
The domain $U$ is not [[simply connected|075C629XTH]], so this does not contradict the theorem for [[convex|0B22P010D6]] or simply connected sets.
Locally, $F = \nabla \theta$, where $\theta$ is the polar angle of $(x, y)$. But no continuous choice of $\theta$ exists on all of $U$.

## Explanations

### L1 human

The field circles around the $z$-axis, and its strength falls off with distance in just the right way to have no local swirl.
But a loop around the axis picks up work $2\pi$, so no potential can exist. The hole in the domain causes this.
