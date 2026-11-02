---
tag: Y33AJ7GZ6R
kind: definition
name: Curvature form
msc: [53C05]
defines: ZAJFW1S078
uses: [NJ21PN5ZGJ, 0ZHSTAG8ZY, 0GRAATMGP1]
sources:
  - url: https://en.wikipedia.org/wiki/Curvature_form
---

## Definition

Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$, let $P \to M$ be a principal $G$-bundle, and let $\omega$ be a [[connection form|NJ21PN5ZGJ]] on $P$.
For $\mathfrak{g}$-valued $1$-forms $\alpha, \beta$ on $P$, let $[\alpha \wedge \beta]$ be the $\mathfrak{g}$-valued $2$-form $[\alpha \wedge \beta](X, Y) = [\alpha(X), \beta(Y)] - [\alpha(Y), \beta(X)]$.
The *curvature form* of $\omega$ is the $\mathfrak{g}$-valued $2$-form
$$\Omega = d\omega + \tfrac12 [\omega \wedge \omega],$$
where $d$ is the [[exterior derivative|0ZHSTAG8ZY]].
The connection is *flat* if $\Omega = 0$.

## Remarks

Unwinding the bracket, $\Omega(X, Y) = d\omega(X, Y) + [\omega(X), \omega(Y)]$.
This is the structure equation; an equivalent form is $\Omega(X, Y) = d\omega(hX, hY)$, where $h$ is the projection of $TP$ onto the horizontal bundle $\ker \omega$.
The form $\Omega$ vanishes on vertical vectors and satisfies $R_g^* \Omega = \mathrm{Ad}(g^{-1}) \Omega$.
For a matrix group, $\frac12 [\omega \wedge \omega] = \omega \wedge \omega$ with the matrix [[wedge product|0GRAATMGP1]], so $\Omega = d\omega + \omega \wedge \omega$.
Example: on $M \times G$ with $\omega$ the pullback of the [[Maurer–Cartan form|P1JVA39H5E]] $\theta$, the Maurer–Cartan equation $d\theta + \frac12 [\theta \wedge \theta] = 0$ gives $\Omega = 0$, so this connection is flat.
Non-example of flatness: for $G = \mathrm{U}(1)$ the bracket vanishes and $\Omega = d\omega$; for a connection on the Hopf bundle $S^3 \to S^2$, $\Omega$ descends to a $2$-form on $S^2$ with nonzero integral, so $\Omega \ne 0$.
