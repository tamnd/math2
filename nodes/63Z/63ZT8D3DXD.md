---
tag: 63ZT8D3DXD
kind: problem
name: Yamabe problem
msc: [53C21, 58J05, 35J61]
uses: [7CBT4SM83Y, ZHX2VYQDZ3, 0E0B6RA8K0]
about: [ZHX2VYQDZ3]
sources:
  - url: https://en.wikipedia.org/wiki/Yamabe_problem
same_as:
  wikidata: Q3406245
  wikipedia: Yamabe problem
history:
  posed_by: "Hidehiko Yamabe"
  first_stated: "1960"
---

## Problem

Let $(M, g)$ be a compact [[Riemannian manifold|7CBT4SM83Y]] without boundary, of dimension $n \ge 3$.
Is there a smooth positive function $u$ on $M$ such that the metric $\tilde g = u^{4/(n-2)} g$ has constant [[scalar curvature|ZHX2VYQDZ3]]?

## Remarks

The scalar curvature $\tilde R$ of $\tilde g$ is related to the scalar curvature $R$ of $g$ by
$$-\frac{4(n-1)}{n-2} \Delta_g u + R u = \tilde R \, u^{(n+2)/(n-2)},$$
where $\Delta_g$ is the Laplace–Beltrami operator of $g$, the analogue of the [[Laplacian|0E0B6RA8K0]].
So the problem asks for a positive solution of this semilinear elliptic equation with $\tilde R$ constant.
The exponent $(n+2)/(n-2)$ is the critical Sobolev exponent, and this is why the direct variational method does not apply at once.
The answer is yes.
Yamabe proposed a proof that Neil Trudinger found to contain a gap.
Trudinger, Thierry Aubin and Richard Schoen completed the proof, with Schoen settling the remaining cases with the positive mass theorem.
In dimension $2$ the analogous statement is a consequence of the uniformization theorem.

## Explanations

### L1 human

On a curved space one can stretch lengths by a factor that varies from point to point, without changing angles.
The Yamabe problem asks whether such a stretching can always make the scalar curvature, an average of the curvature at each point, the same everywhere.
It is a higher-dimensional version of the fact that every surface can be given a metric of constant curvature, and the answer is again yes.
