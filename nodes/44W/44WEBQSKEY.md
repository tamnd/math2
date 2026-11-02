---
tag: 44WEBQSKEY
kind: example
name: Pseudosphere
msc: [53A05, 53A35]
illustrates: [SQVQ5DQT6W]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudosphere
---

## Example

For $t > 0$ and $\theta \in \R$, let
$$x(t, \theta) = \left(\operatorname{sech} t \cos\theta, \; \operatorname{sech} t \sin\theta, \; t - \tanh t\right).$$
This is the [[surface of revolution|NE09EDK19V]] of the tractrix $t \mapsto (\operatorname{sech} t, \, t - \tanh t)$ about the $z$-axis, and its image is called the pseudosphere.
Its [[Gaussian curvature|SQVQ5DQT6W]] is $-1$ at every point.

Check.
Write $r(t) = \operatorname{sech} t$ and $z(t) = t - \tanh t$.
Then $r'(t) = -\operatorname{sech} t \tanh t$ and $z'(t) = \tanh^2 t$, so $r'^2 + z'^2 = \tanh^2 t \,(\operatorname{sech}^2 t + \tanh^2 t) = \tanh^2 t$.
For $t > 0$ the speed is $\tanh t > 0$, and the arc length from $t = 0$ is $s = \ln\cosh t$.
So in terms of arc length, $r = 1/\cosh t = e^{-s}$.
For a surface of revolution with profile parametrized by arc length, $K = -r''(s)/r(s)$, and here $K = -e^{-s}/e^{-s} = -1$.

## Remarks

The surface is not complete: as $t \to 0$ it ends in a sharp circular edge of radius $1$, where the parametrization stops being regular.
This agrees with [[Hilbert's theorem|XM772FD0BS]], which says that no complete surface of constant curvature $-1$ sits smoothly and isometrically in $\R^3$.
Pieces of the pseudosphere are locally isometric to pieces of the hyperbolic plane, so they were used as early models of [[hyperbolic geometry|GN4N94GQ0Z]].

## Explanations

### L1 human

The pseudosphere looks like a trumpet: a long thin horn that widens to a sharp rim.
A sphere has the same positive curvature everywhere; the pseudosphere has the same negative curvature everywhere.
At each point it bends like a saddle, curving up in one direction and down in the other.
