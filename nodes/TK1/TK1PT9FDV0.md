---
tag: TK1PT9FDV0
kind: statement
role: theorem
name: Lichnerowicz–Obata eigenvalue theorem
msc: [58J50, 53C21, 53C24]
uses: [7CBT4SM83Y, 4GTNM0WHDH, F4NWZNTRMD, B8TYKV7AA1, P9CM4GQ2T0]
about: [B8TYKV7AA1, 4GTNM0WHDH]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace–Beltrami_operator
---

## Statement

Let $(M, g)$ be a compact connected [[Riemannian manifold|7CBT4SM83Y]] without boundary, of dimension $n \ge 2$.
Let $k > 0$, and assume that the [[Ricci curvature|4GTNM0WHDH]] satisfies $\operatorname{Ric} \ge (n - 1) k \, g$.
Let $\lambda_1$ be the smallest nonzero eigenvalue of the [[Laplace–Beltrami operator|F4NWZNTRMD]] $\Delta = -\operatorname{div} \operatorname{grad}$ on $M$.

1. (Lichnerowicz) $\lambda_1 \ge n k$.
2. (Obata) $\lambda_1 = n k$ if and only if $(M, g)$ is isometric to the round [[sphere|P9CM4GQ2T0]] $S^n$ of radius $1/\sqrt{k}$.

## Remarks

The proof of the inequality applies the Bochner formula to an eigenfunction $f$ with $\Delta f = \lambda_1 f$.
With $\nabla^2 f$ the Hessian, the formula reads $-\frac12 \Delta \abs{\nabla f}^2 = \abs{\nabla^2 f}^2 - \ip{\nabla f}{\nabla \Delta f} + \operatorname{Ric}(\nabla f, \nabla f)$.
Integrating over $M$ and using $\abs{\nabla^2 f}^2 \ge (\Delta f)^2 / n$ gives $\lambda_1 \ge nk$.
In the equality case the Hessian of $f$ equals $-k f g$, and Obata showed that a complete manifold carrying a nonconstant solution of this equation is a round sphere.
On the unit sphere $S^n$ one has $\operatorname{Ric} = (n-1) g$ and $\lambda_1 = n$, attained by the restrictions of the coordinate functions, so the bound is sharp.
The hypothesis $k > 0$ is needed: flat tori have $\operatorname{Ric} = 0$, and the flat torus $\R^n / L\Z^n$ has $\lambda_1 = 4\pi^2 / L^2$, which tends to $0$ as $L$ grows.

## Explanations

### L1 human

The first nonzero eigenvalue of the Laplacian measures the lowest pitch at which a closed manifold can vibrate.
A positive lower bound on the Ricci curvature makes the manifold small and round, and this forces the pitch up.
Lichnerowicz's bound says how far up.
Obata's part says that the round sphere is the only shape that sits exactly at the bound.

### L2 human

This is the model comparison theorem of spectral geometry: a curvature bound gives an eigenvalue bound, with rigidity in the extreme case.
It sits beside the Bonnet–Myers theorem, which under the same hypothesis bounds the diameter by $\pi/\sqrt{k}$.
The Bochner technique used in the proof is the same one used for vanishing theorems for harmonic forms.
For a lower bound on $\lambda_1$ without curvature assumptions, see [[Cheeger's inequality|JRGADFNBV2]].
