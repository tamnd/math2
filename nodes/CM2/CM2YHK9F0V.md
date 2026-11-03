---
tag: CM2YHK9F0V
kind: object
name: Hofstadter's butterfly
msc: [82D20, 81Q10, 47B36]
uses: [QP0TK2M29V, D08SKTH2T2, BMKATJ802A, 0BXNDZFQME]
sources:
  - url: https://en.wikipedia.org/wiki/Hofstadter%27s_butterfly
same_as:
  wikidata: Q2913166
  wikipedia: Hofstadter's butterfly
---

## Description

For $\alpha, \theta \in \R$ let $H_{\alpha,\theta}$ be the Harper operator on $\ell^2(\Z)$,
$$(H_{\alpha,\theta} u)(n) = u(n+1) + u(n-1) + 2\cos\big(2\pi(n\alpha + \theta)\big) u(n),$$
the [[almost Mathieu operator|D08SKTH2T2]] with coupling $\lambda = 1$.
Let $\sigma(\alpha)$ be the union over $\theta$ of the [[spectra|BMKATJ802A]] of $H_{\alpha,\theta}$, a subset of $[-4, 4]$.
*Hofstadter's butterfly* is the set $\set{(\alpha, E) : 0 \le \alpha \le 1, \ E \in \sigma(\alpha)}$, drawn in the plane.
It describes an electron hopping on the square lattice in a perpendicular magnetic field with $\alpha$ flux quanta per plaquette.
Douglas Hofstadter computed and drew it in 1976.
It is a picture of how the [[band structure|QP0TK2M29V]] of a lattice electron depends on the magnetic flux.

## Remarks

Check at $\alpha = 0$: the potential is the constant $c = 2\cos(2\pi\theta)$, the spectrum is $[c - 2, c + 2]$, and the union over $\theta$ is $[-4, 4]$, one band.

Check at $\alpha = 1/2$: the potential is $(-1)^n c$ with $c = 2\cos(2\pi\theta)$, of period $2$.
Its two bands are given by $E^2 = c^2 + 4\cos^2 k$, $k \in [-\pi, \pi]$, so they are $[-\sqrt{c^2 + 4}, -\abs{c}]$ and $[\abs{c}, \sqrt{c^2 + 4}]$.
Taking the union over $c \in [-2, 2]$ gives $[-2\sqrt2, 0] \cup [0, 2\sqrt2]$: two bands that touch at $E = 0$.

For $\alpha = p/q$ in lowest terms, $\sigma(\alpha)$ is a union of $q$ closed intervals, the two central ones touching when $q$ is even.
For irrational $\alpha$, $\sigma(\alpha)$ does not depend on $\theta$; it is a [[Cantor set|0BXNDZFQME]] (the [[ten martini problem|3X4ZQ41PXG]]) of Lebesgue measure zero.
The picture is symmetric under $\alpha \mapsto 1 - \alpha$ and $E \mapsto -E$, and its parts repeat on smaller scales, which makes it look like a fractal.

## Explanations

### L1 human

Put an electron on a square grid and switch on a magnetic field.
Plot the allowed energies vertically against the strength of the field horizontally.
The result is a picture with wings inside wings, which looks like a butterfly.
When the field gives a simple fraction $p/q$ of a flux quantum per square, the energies form $q$ bands.
For irrational values they form a dust of points, a Cantor set.
Each gap in the picture carries an integer, the Hall conductance.
This connects the butterfly with the [[quantum Hall effect|11AZ4RGXVN]].
