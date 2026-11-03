---
tag: AKRJ7MDNMW
kind: statement
role: theorem
name: Cardy's formula
msc: [82B43, 60K35, 81T40]
uses: [BH7YPXCYDK, MP8VSZK19A, 09ASMRMD67, 0H5SYBSED9, 0YYT36R4YD]
about: [BH7YPXCYDK]
sources:
  - url: https://en.wikipedia.org/wiki/Cardy_formula
same_as:
  wikidata: Q15302927
  wikipedia: Cardy formula
---

## Statement

Let $\Omega \subset \C$ be a bounded simply connected domain whose boundary is a Jordan curve.
Let $a, b, c, d$ be four distinct points on $\partial \Omega$, in counterclockwise order.
Write $ab$ for the arc of $\partial \Omega$ from $a$ to $b$ that contains no other marked point, and $cd$ likewise.
For $\delta > 0$, consider site [[percolation|BH7YPXCYDK]] at its [[critical value|MP8VSZK19A]] $p = 1/2$ on the triangular lattice with mesh $\delta$.
Let $P_\delta$ be the probability that some path of open sites inside $\Omega$ joins the boundary arc $ab$ with the boundary arc $cd$.
Let $\varphi$ be a [[conformal map|0YYT36R4YD]] from $\Omega$ onto the upper half-plane with $\varphi(a) < \varphi(b) < \varphi(c) < \varphi(d)$ real, and let
$$\eta = \frac{(\varphi(a) - \varphi(b))(\varphi(c) - \varphi(d))}{(\varphi(a) - \varphi(c))(\varphi(b) - \varphi(d))} \in (0, 1)$$
be their [[cross-ratio|09ASMRMD67]].
Then
$$\lim_{\delta \to 0} P_\delta = \frac{3 \, \Gamma(2/3)}{\Gamma(1/3)^2} \, \eta^{1/3} \, {}_2F_1\Big(\frac13, \frac23; \frac43; \eta\Big),$$
where $\Gamma$ is the [[gamma function|0H5SYBSED9]] and ${}_2F_1$ is the Gauss hypergeometric function.

## Remarks

John Cardy derived the formula in 1992 from conformal field theory, with arguments that are not rigorous.
Stanislav Smirnov proved it in 2001 for site percolation on the triangular lattice, by his [[theorem on conformal invariance of percolation|ZEBG1G27TV]]; for other lattices it is still open.

Check of the boundary values: as $b \to a$ the arc from $a$ to $b$ shrinks, $\eta \to 0$, and the right side tends to $0$.
As $b \to c$ the two arcs touch, $\eta \to 1$, and Gauss's formula ${}_2F_1(\alpha, \beta; \gamma; 1) = \frac{\Gamma(\gamma) \Gamma(\gamma - \alpha - \beta)}{\Gamma(\gamma - \alpha) \Gamma(\gamma - \beta)}$ gives ${}_2F_1(\frac13, \frac23; \frac43; 1) = \frac{\Gamma(4/3) \Gamma(1/3)}{\Gamma(2/3)}$.
So the limit is $3 \Gamma(4/3) / \Gamma(1/3) = 1$, as it should be.

Lennart Carleson observed that the formula becomes linear when $\Omega$ is an equilateral triangle with vertices $a, b, c$.

## Explanations

### L1 human

Colour each small hexagon of a honeycomb black or white with a fair coin, inside some region drawn on the plane.
Mark four points on the boundary, and ask whether black hexagons connect one boundary arc to the opposite one.
When the hexagons are tiny, the answer has a definite probability, and Cardy's formula computes it.
It depends on the shape only through one number, the cross-ratio, so stretching the region by a conformal map does not change it.

### L2 human

Crossing probabilities are the basic observables of critical percolation, and they control the behaviour of the clusters at all scales.
Cardy's formula is the first exact scaling limit in percolation, and it identifies the limit of the crossing probabilities as conformally invariant.
Its proof is a main step toward the description of the boundaries of critical clusters by the [[Schramm–Loewner evolution|AQ75M2JTB2]] with parameter $6$.
