---
tag: JHE88QBRFK
kind: statement
role: theorem
name: Borde–Guth–Vilenkin theorem
msc: ["83F05", "83C75"]
uses: [63ZKC7AFX2, BY4QYYS788, RNRTS8WWNM, ECJMS4VDTF, J70F32P86W]
about: [81HPA9X0Y1, 202254GTP0]
sources:
  - url: https://en.wikipedia.org/wiki/Borde%E2%80%93Guth%E2%80%93Vilenkin_theorem
same_as:
  wikidata: Q85850287
  wikipedia: Borde–Guth–Vilenkin theorem
---

## Statement

Let $(M, g)$ be a [[spacetime|63ZKC7AFX2]] with a congruence of comoving timelike geodesics, the observers that define the expansion.
Let $\gamma$ be a timelike or null [[geodesic|RNRTS8WWNM]] with affine parameter $\lambda$.
Let $H$ be the local expansion rate along $\gamma$, measured from the change of the velocity of $\gamma$ relative to the comoving observers.
Suppose that along the past part of $\gamma$ the average expansion rate
$$H_{\text{av}} = \frac{1}{\lambda_f - \lambda_i} \int_{\lambda_i}^{\lambda_f} H \, d\lambda$$
is bounded below by a constant $H_{\min} > 0$ for every $\lambda_i < \lambda_f$.
Then $\gamma$ has a finite affine length to the past.
In particular, a spacetime that is expanding on average in this sense along all past geodesics is past geodesically incomplete.

## Remarks

The key estimate shows that $\int_{\lambda_i}^{\lambda_f} H\, d\lambda$ is bounded above by a quantity that depends only on the endpoint $\lambda_f$, so $(\lambda_f - \lambda_i) H_{\min}$ is bounded and the past affine length is finite.
In a flat [[Friedmann–Lemaître–Robertson–Walker|ECJMS4VDTF]] model with [[scale factor|J70F32P86W]] $a$, a null geodesic has affine parameter with $d\lambda = a(t)\, dt / a(t_f)$, so $\int H\, d\lambda = \int \dot a\, dt / a(t_f) = (a(t_f) - a(t_i))/a(t_f) \le 1$, and the past affine length is at most $1/H_{\min}$.
The theorem uses no energy condition and does not use the Einstein equations, only the averaged expansion condition.
Example: the flat slicing of de Sitter space, $a = e^{Ht}$, satisfies the hypothesis, and indeed it is past incomplete.
The full de Sitter space extends it, and in the extension the averaged expansion condition fails.
Arvind Borde, Alan Guth and Alexander Vilenkin published it in 2003.

## Explanations

### L1 human

The theorem says that a universe that has, on average, always been expanding cannot be infinitely old in the past.
If you follow a light ray or a free particle back in time through such a universe, you reach the edge of the spacetime after a finite time.
It applies in particular to models of eternal inflation, which must therefore have had some kind of beginning.

### L2 human

Classical singularity theorems of Penrose and Hawking derive geodesic incompleteness from energy conditions, which inflationary matter can violate.
The Borde–Guth–Vilenkin theorem avoids energy conditions entirely and replaces them by a purely kinematic hypothesis on the average expansion.
Its conclusion is incompleteness, not a curvature singularity: it says the classical description must break down or be extended into a region where the hypothesis fails.
It is often discussed together with the [[Big Bang|202254GTP0]] and with [[cosmic inflation|81HPA9X0Y1]].
