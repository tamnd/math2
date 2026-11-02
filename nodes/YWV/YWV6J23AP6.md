---
tag: YWV6J23AP6
kind: statement
role: theorem
name: Weierstrass–Enneper parameterization
msc: [53A10, 30F45]
uses: [41X0YW2R9N, 0NAHXR1FRH, 0ZZ7ZYDR8W, 0QW64ARSHB, 0YYT36R4YD]
about: [41X0YW2R9N]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass–Enneper_parameterization
same_as:
  wikidata: Q7979830
  wikipedia: Weierstrass–Enneper parameterization
---

## Statement

Let $U \subset \C$ be a [[simply connected domain|0QW64ARSHB]] and let $z_0 \in U$.
Let $f$ be a [[holomorphic function|0NAHXR1FRH]] on $U$ and $g$ a [[meromorphic function|0ZZ7ZYDR8W]] on $U$.
Assume that the zeros of $f$ are exactly the poles of $g$.
Assume also that at a pole of $g$ of order $m$, the function $f$ has a zero of order exactly $2m$.
For $z \in U$, let
$$x_1(z) = \operatorname{Re} \int_{z_0}^{z} \frac{f(w)\,(1 - g(w)^2)}{2} \, dw, \quad x_2(z) = \operatorname{Re} \int_{z_0}^{z} \frac{i f(w)\,(1 + g(w)^2)}{2} \, dw, \quad x_3(z) = \operatorname{Re} \int_{z_0}^{z} f(w) g(w) \, dw.$$
Then $x = (x_1, x_2, x_3) \colon U \to \R^3$ is a [[conformal|0YYT36R4YD]] immersion whose image is a [[minimal surface|41X0YW2R9N]].
Conversely, after a rotation of $\R^3$ if needed, every conformal minimal immersion of $U$ into $\R^3$ arises in this way.

## Remarks

The idea of the proof: for a conformal immersion $x$, write $\varphi_k = 2\,\partial x_k / \partial z$.
The surface is minimal exactly when each $x_k$ is harmonic, that is, when each $\varphi_k$ is holomorphic.
Conformality is the equation $\varphi_1^2 + \varphi_2^2 + \varphi_3^2 = 0$.
The substitution $f = \varphi_1 - i\varphi_2$ and $g = \varphi_3 / (\varphi_1 - i\varphi_2)$ solves this equation, and it gives back the integrands above.
The condition on zeros and poles makes the integrands holomorphic and keeps $(\varphi_1, \varphi_2, \varphi_3)$ nonzero, so $x$ is an immersion.

The data $f = 2$ and $g(z) = z$ on $\C$ give the [[Enneper surface|73XN6AS0WX]].
The function $g$ is the Gauss map of the surface followed by stereographic projection.
Simple connectivity of $U$ makes the integrals independent of the path; on other domains one must check that the real parts of the periods vanish.

## Explanations

### L1 human

This formula produces minimal surfaces from two functions of a complex variable.
Choose the functions, compute three integrals, and take real parts: the result is always a minimal surface.
So the study of minimal surfaces in space turns into a study of complex functions.

### L2 human

The representation is the main tool for constructing complete minimal surfaces, such as [[Costa's minimal surface|EF0QMQB2J1]].
On a Riemann surface that is not simply connected, the same formulas work once the real periods of the three forms vanish; this period problem is usually the hardest step.
Because $g$ is the Gauss map, curvature questions become questions about meromorphic functions.
For example, the total curvature of a complete minimal surface of finite total curvature is $-4\pi$ times the degree of $g$.
