---
tag: Z11GGXV5KD
kind: definition
name: Thin plate spline
msc: [41A15, 41A05, 41A63]
defines: P9ZPH7EC8K
uses: [XJ0JGPBC8R, ZBSXSTQM2J, AS8A9F5SKE]
sources:
  - url: https://en.wikipedia.org/wiki/Thin_plate_spline
---

## Definition

Let $\varphi(r) = r^2 \log r$ for $r > 0$ and $\varphi(0) = 0$.
Let $x_1, \dots, x_N \in \R^2$ be distinct points, not all on one line, and let $y_1, \dots, y_N$ be real numbers.
The *thin plate spline* interpolant of these data is the function
$$s(x) = a_0 + a^T x + \sum_{i=1}^{N} w_i\, \varphi(\norm{x - x_i}), \qquad x \in \R^2,$$
with $a_0 \in \R$, $a \in \R^2$ and $w \in \R^N$ determined by:

1. $s(x_i) = y_i$ for $i = 1, \dots, N$;
2. $\sum_{i=1}^{N} w_i = 0$;
3. $\sum_{i=1}^{N} w_i x_i = 0$ in $\R^2$.

## Remarks

The conditions form a square linear system, and it has exactly one solution when the points are not collinear.
This is the [[polyharmonic spline|XJ0JGPBC8R]] with $d = 2$ and $m = 2$, built from the [[radial basis function|ZBSXSTQM2J]] $\varphi$.
Among all functions $f$ with square integrable second derivatives and $f(x_i) = y_i$, the spline $s$ minimizes the bending energy
$$\iint_{\R^2} \big( f_{x_1 x_1}^2 + 2 f_{x_1 x_2}^2 + f_{x_2 x_2}^2 \big)\, dx.$$
Away from the points, $s$ satisfies the [[biharmonic equation|AS8A9F5SKE]] $\Delta^2 s = 0$.
Example: if $y_i = c_0 + c^T x_i$ for an affine function, then $w = 0$, $a_0 = c_0$, $a = c$ satisfy all three clauses, so $s$ is that affine function.
Non-example: $f(x) = \varphi(\norm{x})$ with the single centre $0$ fails clause 2, since its only weight is $1$.
Thin plate splines are also used with one map per coordinate to define smooth deformations of the plane from matched landmark points.
