---
tag: BTX4G1FDF6
kind: definition
name: First fundamental form
msc: [53A05]
defines: MAJ3DH7MZS
uses: [6080X3FAD4, 0BJDQ2HBH1, 05HQYM0R4G, 0HZNE5QZDJ]
sources:
  - url: https://en.wikipedia.org/wiki/First_fundamental_form
---

## Definition

Let $S \subseteq \R^3$ be a [[regular surface|6080X3FAD4]] and let $p \in S$.
Let $T_p S \subseteq \R^3$ be the [[tangent plane|0BJDQ2HBH1]] of $S$ at $p$, viewed as a $2$-dimensional linear subspace.
The *first fundamental form* of $S$ at $p$ is the [[quadratic form|0HZNE5QZDJ]] $I_p \colon T_p S \to \R$, $I_p(w) = \ip{w}{w}$, where $\ip{\cdot}{\cdot}$ is the [[dot product|05HQYM0R4G]] of $\R^3$.
In a local parametrisation $x(u, v)$ of $S$, its coefficients are
$$E = \ip{x_u}{x_u}, \qquad F = \ip{x_u}{x_v}, \qquad G = \ip{x_v}{x_v}.$$
For $w = a x_u + b x_v$, this gives $I_p(w) = E a^2 + 2F ab + G b^2$.

## Remarks

One writes $I = E \, du^2 + 2F \, du \, dv + G \, dv^2$.
The length of a curve $t \mapsto x(u(t), v(t))$, $t \in [a, b]$, is $\int_a^b \sqrt{E u'^2 + 2F u' v' + G v'^2} \, dt$, and the area of $x(R)$ is $\iint_R \sqrt{EG - F^2} \, du \, dv$.
Example: for the unit sphere with $x(\theta, \varphi) = (\sin \theta \cos \varphi, \sin \theta \sin \varphi, \cos \theta)$, one gets $E = 1$, $F = 0$ and $G = \sin^2 \theta$.
For $0 < \theta < \pi$ the form is positive definite, as it must be, since $EG - F^2 = \sin^2 \theta > 0$.
Non-example: at $\theta = 0$ the same formulas give $G = 0$, a degenerate form; the map is not a local parametrisation there, because $x_\varphi = 0$.
