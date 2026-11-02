---
tag: QGPHXKCNNX
kind: definition
name: Ehrhart polynomial
msc: [52B20, 11P21, 05A15]
defines: 9DEG0WRDHR
uses: [F39N9NBFPZ, 1G0B73WPX8]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrhart_polynomial
---

## Definition

Let $P \subseteq \R^n$ be a [[lattice polytope|F39N9NBFPZ]] of dimension $d$.
For each integer $t \ge 1$, let
$$L_P(t) = \#\left(tP \cap \Z^n\right), \qquad tP = \set{tx : x \in P},$$
be the number of integer points in the dilate $tP$.
By Ehrhart's theorem, there is a unique [[polynomial|1G0B73WPX8]] $E_P(t)$ with rational coefficients such that $E_P(t) = L_P(t)$ for all integers $t \ge 1$.
This polynomial $E_P$ is the *Ehrhart polynomial* of $P$.

## Remarks

The polynomial $E_P$ has degree $d$, and $E_P(0) = 1$.
If $d = n$, the leading coefficient of $E_P$ is the volume of $P$.
In general the leading coefficient is the volume of $P$ measured inside its affine hull, normalised by the lattice of integer points of that affine hull.

Example: for the unit square $P = [0,1]^2$, the dilate $tP = [0,t]^2$ contains $(t+1)^2$ integer points, so $E_P(t) = t^2 + 2t + 1$.
For the triangle with vertices $(0,0)$, $(1,0)$, $(0,1)$, the dilate contains the points $(a,b) \in \Z^2$ with $a, b \ge 0$ and $a + b \le t$, so $E_P(t) = (t+1)(t+2)/2$.
In both cases the leading coefficient is the area, $1$ and $1/2$.

Non-example: the segment $P = [0, 1/2]$ is a rational polytope but not a lattice polytope.
Here $L_P(t) = \floor{t/2} + 1$, which is not a polynomial in $t$; it is only a quasi-polynomial of period $2$.
So the hypothesis that the vertices are integer points is needed.

The generating function $\sum_{t \ge 0} E_P(t) z^t$ is a rational function of the form $h^*(z)/(1-z)^{d+1}$, where $h^*$ is a polynomial with nonnegative integer coefficients.
