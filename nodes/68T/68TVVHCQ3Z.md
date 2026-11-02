---
tag: 68TVVHCQ3Z
kind: statement
role: theorem
name: Gauss–Codazzi equations
msc: [53A05, 53B25]
uses: [6080X3FAD4, DQCD11X1VM, 9KHQR16P1B, SQVQ5DQT6W, CAZYGE1T4E, JA29ETCM02]
about: [DQCD11X1VM, 9KHQR16P1B]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%E2%80%93Codazzi_equations
same_as:
  wikidata: Q3589432
  wikipedia: Gauss–Codazzi equations
---

## Statement

Let $M \subseteq \R^3$ be a [[regular surface|6080X3FAD4]] with a smooth unit normal field $N$ and [[shape operator|DQCD11X1VM]] $S$.
Let $I\!I(X, Y) = \ip{S X}{Y}$ be its [[second fundamental form|9KHQR16P1B]].
Let $\nabla$ be the [[Levi-Civita connection|CAZYGE1T4E]] of the induced metric on $M$, with [[Riemann curvature tensor|JA29ETCM02]] $R(X, Y) Z = \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$.
Then for all tangent vector fields $X, Y, Z, W$ on $M$:

1. (Gauss equation) $\ip{R(X, Y) Z}{W} = I\!I(Y, Z) \, I\!I(X, W) - I\!I(X, Z) \, I\!I(Y, W)$.
2. (Codazzi–Mainardi equation) $(\nabla_X S) Y = (\nabla_Y S) X$, where $(\nabla_X S) Y = \nabla_X (S Y) - S(\nabla_X Y)$.

## Remarks

Let $D$ be the flat connection of $\R^3$, given by directional derivatives.
The Gauss formula $D_X Y = \nabla_X Y + I\!I(X, Y) N$ and the Weingarten formula $D_X N = -S X$ split $D$ into tangent and normal parts.
Since $D$ has zero curvature, the tangent part of $D_X D_Y Z - D_Y D_X Z - D_{[X, Y]} Z = 0$ gives the Gauss equation, and the normal part gives the Codazzi–Mainardi equation.
Taking $X, Y$ orthonormal and $Z = Y$, $W = X$ in the Gauss equation gives $\ip{R(X, Y) Y}{X} = \det S = K$, the [[Gaussian curvature|SQVQ5DQT6W]].
Example: for the sphere of radius $r$ with the inner normal, $S = \frac{1}{r} \id$, so $(\nabla_X S) Y = \frac{1}{r} (\nabla_X Y - \nabla_X Y) = 0$ and both sides of the Codazzi equation vanish, while the Gauss equation gives sectional curvature $1/r^2$.

## Explanations

### L1 human

A surface in space has two kinds of data: how lengths are measured on it, and how it bends in space.
These cannot be chosen freely.
The Gauss–Codazzi equations are the compatibility conditions between them.

### L2 human

The Gauss equation contains the Theorema Egregium: the left side depends only on the metric, so $K = \det S$ does too.
Conversely, Bonnet's theorem says that on a simply connected domain, a metric and a symmetric form satisfying these equations come from a surface in $\R^3$, unique up to rigid motion.
This is the surface analogue of the fundamental theorem of space curves.
The same equations hold for hypersurfaces of $\R^{n+1}$, and with extra terms for submanifolds of a general Riemannian manifold.
