---
tag: KNBQ68XG2M
kind: example
name: Whitney umbrella
msc: [57R45, 58K40, 14B05]
illustrates: [1JG3HFWX3T]
uses: [1JG3HFWX3T, 6P9PXQDSEN]
sources:
  - url: https://en.wikipedia.org/wiki/Whitney_umbrella
same_as:
  wikidata: Q2640354
  wikipedia: Whitney umbrella
---

## Example

The *Whitney umbrella* is the surface in $\R^3$ with equation
$$x^2 = y^2 z.$$
It contains the image of the smooth map $f \colon \R^2 \to \R^3$, $f(u, v) = (uv, u, v^2)$, since $(uv)^2 = u^2 \cdot v^2$.

Check of the singularity: the [[differential|6P9PXQDSEN]] of $f$ has matrix
$$\begin{pmatrix} v & u \\ 1 & 0 \\ 0 & 2v \end{pmatrix}.$$
Its first two rows show that it has rank $2$ unless $u = 0$.
For $u = 0$, its first and third rows show that it has rank $2$ unless $v = 0$.
So the origin is the only [[singular point|1JG3HFWX3T]] of $f$, and there the rank is $1$.

The points $(0, 0, z)$ with $z > 0$ have the two preimages $(0, \pm \sqrt{z})$, so the image crosses itself along the positive $z$-axis.
The origin has the single preimage $(0, 0)$ and is called the pinch point.
The points $(0, 0, z)$ with $z < 0$ satisfy the equation but are not in the image of $f$; they form the handle of the umbrella.

## Remarks

The map germ of $f$ at the origin is the cross-cap.
Whitney showed that, besides immersion germs, the cross-cap is the only singularity of a generic smooth map from a surface into $3$-space, and that it is stable.

## Explanations

### L1 human

Take a sheet, pinch one point and let the sheet pass through itself along a line starting at that point.
The result looks like an umbrella that has been folded and pushed through itself, with a stick, the handle, sticking out the other side.
The pinch point is where the map from the plane fails to be an immersion.
A generic smooth map of a surface into space has only isolated pinch points of this kind as singular points.
