---
tag: 6DHQTFAJ03
kind: statement
role: theorem
name: Five-term relation for the dilogarithm
msc: ["33B30", "11G55"]
uses: [G0X0NWSDB7, Q8K5MWEXB9, 04DXAFN2ES]
about: [G0X0NWSDB7, Q8K5MWEXB9]
sources:
  - url: https://en.wikipedia.org/wiki/Dilogarithm
---

## Statement

Let $\operatorname{Li}_2$ be the [[dilogarithm|G0X0NWSDB7]], and for $0 < x < 1$ let
$$L(x) = \operatorname{Li}_2(x) + \tfrac12 \log x \, \log(1 - x)$$
be the Rogers dilogarithm, where $\log$ is the [[natural logarithm|04DXAFN2ES]].
Let $D$ be the [[Bloch–Wigner function|Q8K5MWEXB9]].

1. For all real $x, y$ with $0 < x < 1$ and $0 < y < 1$,
$$L(x) + L(y) = L(xy) + L\left(\frac{x(1-y)}{1-xy}\right) + L\left(\frac{y(1-x)}{1-xy}\right).$$
2. For all complex $x, y$ such that $x$, $y$, $1 - xy$, $\frac{1-x}{1-xy}$ and $\frac{1-y}{1-xy}$ all lie in $\C \setminus \set{0, 1}$,
$$D(x) + D(1 - xy) + D(y) + D\left(\frac{1-x}{1-xy}\right) + D\left(\frac{1-y}{1-xy}\right) = 0.$$

## Remarks

For the real form, fix $y$ and differentiate both sides in $x$.
Using $\frac{d}{dx}\operatorname{Li}_2(x) = -\frac{\log(1-x)}{x}$, the derivatives of the two sides agree, and both sides tend to $L(y)$ as $x \to 0^+$, since $L(x) \to 0$.
The complex form follows in the same way from the differential of $D$, which is an explicit real-analytic $1$-form on $\C \setminus \set{0, 1}$.

Example: with $y = x$, the third argument is $\frac{x(1-x)}{1-x^2} = \frac{x}{1+x}$, so the relation gives
$$2L(x) = L(x^2) + 2L\left(\frac{x}{1+x}\right), \qquad 0 < x < 1.$$

The five arguments in the complex form are cross-ratios of five points on the Riemann sphere taken four at a time.
Geometrically, $D(z)$ is the hyperbolic volume of the ideal tetrahedron with vertices $0, 1, \infty, z$.
The relation says that two ways of cutting an ideal polyhedron with five vertices into ideal tetrahedra give the same volume.

The correction term $\frac12 \log x \log(1-x)$ is needed: the plain dilogarithm $\operatorname{Li}_2$ satisfies a five-term relation only with extra products of logarithms.

## Explanations

### L1 human

The dilogarithm is a function defined by a power series, much like the logarithm.
The logarithm turns products into sums; the dilogarithm has a more complicated rule that ties together its values at five related points.
This five-term rule is the basic functional equation of the dilogarithm, and many other identities for it can be derived from it.

### L2 human

The relation is usually stated for the Rogers dilogarithm on $(0, 1)$ or for the Bloch–Wigner function on $\C \setminus \set{0, 1}$, because these versions have no elementary correction terms.
It is the defining relation of the Bloch group in algebraic K-theory, and it explains why sums of values $D(z_i)$ compute volumes of hyperbolic $3$-manifolds.
Its quantum analogue is the pentagon identity of the [[quantum dilogarithm|6HMT17DVX7]].
