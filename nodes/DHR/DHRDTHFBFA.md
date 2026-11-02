---
tag: DHRDTHFBFA
kind: definition
name: Five-point stencil
msc: [65N06, 65D25]
defines: 73WPYFAEWS
uses: [752Z7DRT7P, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Five-point_stencil
---

## Definition

Let $h > 0$ be a grid spacing.

1. In one dimension, the *five-point stencil* at $x \in \R$ is the set of points $x - 2h, x - h, x, x + h, x + 2h$.
The associated formulas for a function $f$ are
$$f'(x) \approx \frac{-f(x + 2h) + 8 f(x + h) - 8 f(x - h) + f(x - 2h)}{12 h},$$
$$f''(x) \approx \frac{-f(x + 2h) + 16 f(x + h) - 30 f(x) + 16 f(x - h) - f(x - 2h)}{12 h^2}.$$
2. In two dimensions, the *five-point stencil* at $(x, y) \in \R^2$ is the set of points $(x, y)$, $(x \pm h, y)$, $(x, y \pm h)$.
The associated *five-point Laplacian* of a function $u$ is
$$\Delta_h u(x, y) = \frac{u(x + h, y) + u(x - h, y) + u(x, y + h) + u(x, y - h) - 4 u(x, y)}{h^2}.$$

## Remarks

The one-dimensional weights are the [[finite difference coefficients|752Z7DRT7P]] for the stencil $-2, -1, 0, 1, 2$.
For $f \in C^5$, the first formula has error $-\frac{h^4}{30} f^{(5)}(\xi)$ for some $\xi$ in $(x - 2h, x + 2h)$, so it has order $4$; the second has order $4$ for $f \in C^6$.
Check of the second formula on $f(s) = s^2$ at $x = 0$: $\frac{-4h^2 + 16h^2 + 16h^2 - 4h^2}{12h^2} = 2 = f''(0)$.
For $u \in C^4$, each one-dimensional second difference has error $\frac{h^2}{12} \partial^4 u$ at an intermediate point, so $\abs{\Delta_h u - \Delta u} \le \frac{h^2}{12} \big( \max \abs{u_{xxxx}} + \max \abs{u_{yyyy}} \big)$ and the five-point Laplacian approximates the [[Laplacian|0E0B6RA8K0]] to second order.
Non-example: the nine-point and the diagonal five-point stencil $(x \pm h, y \pm h)$ also approximate $\Delta u$, the latter as $\frac{1}{2h^2}\big(\sum u(x \pm h, y \pm h) - 4u(x,y)\big)$, but it uses different points and is not the five-point stencil defined here.

## Explanations

### L1 human

In one dimension, the five-point stencil uses two points on each side of $x$ and gives very accurate derivative estimates.
In two dimensions, it uses the four neighbours of a grid point and estimates the Laplacian, which measures how a value differs from the average of its surroundings.
