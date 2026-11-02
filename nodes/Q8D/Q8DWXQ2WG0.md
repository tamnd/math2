---
tag: Q8DWXQ2WG0
kind: definition
name: Bicubic interpolation
msc: [65D05, 65D07, 41A05]
defines: P1G0M3S8QV
uses: [SS1YMS2NPC, HCQWPAHYAT, 5QJYCNRYMQ]
sources:
  - url: https://en.wikipedia.org/wiki/Bicubic_interpolation
---

## Definition

Let $U = [0, 1]^2$, and for each corner $c \in \set{0, 1}^2$ let real numbers $f(c)$, $f_x(c)$, $f_y(c)$ and $f_{xy}(c)$ be given.
The *bicubic interpolant* on $U$ is the unique polynomial
$$p(x, y) = \sum_{i=0}^{3} \sum_{j=0}^{3} a_{ij} x^i y^j$$
such that, at each corner $c$, $p = f(c)$, $\partial_x p = f_x(c)$, $\partial_y p = f_y(c)$ and $\partial_x \partial_y p = f_{xy}(c)$.
On a rectangular grid, *bicubic interpolation* applies this on each cell after an affine change of variables to $U$.
The derivative data are scaled by the cell sides.

## Remarks

The sixteen conditions determine the sixteen coefficients.
Indeed, $p$ is the tensor product of one-dimensional [[cubic Hermite interpolation|HCQWPAHYAT]] in $x$ and in $y$, so it exists and is unique.
Example: for $f(x, y) = x^3 y^3$, the data are $f = f_x = f_y = 0$ at every corner except $(1, 1)$, where $f = 1$, $f_x = f_y = 3$ and $f_{xy} = 9$; the interpolant is $x^3 y^3$, since it has the required form.
Non-example: the function $\sin(\pi x) \sin(\pi y)$ has zero value at all corners, but it is not a polynomial of the required form, so it is not a bicubic interpolant of any data.
On a grid, along a shared edge the value and the normal derivative are cubics determined by data at the two common corners only.
So adjacent patches join with continuous value and first derivatives.
The variant used for images replaces the derivatives by differences of neighboring pixel values, or uses a cubic convolution kernel on a $4 \times 4$ neighborhood.

## Explanations

### L1 human

On each square of the grid, bicubic interpolation fits a polynomial that is cubic in $x$ and cubic in $y$.
It matches the value, the slopes and the twist at the four corners, sixteen numbers in all, and this makes the whole surface smooth across cell edges.
