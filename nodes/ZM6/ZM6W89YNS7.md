---
tag: ZM6W89YNS7
kind: statement
role: theorem
name: Frenet–Serret formulas
msc: [53A04]
uses: [7JQS6VKFEZ, S4BZ697DSH, 00R1JDDV5X, 0SEDGXG9S3, 0FWJ0VW561]
about: [7JQS6VKFEZ, S4BZ697DSH]
sources:
  - url: https://en.wikipedia.org/wiki/Frenet%E2%80%93Serret_formulas
same_as:
  wikidata: Q947922
  wikipedia: Frenet–Serret formulas
---

## Statement

Let $I \subseteq \R$ be an interval and let $\gamma \colon I \to \R^3$ be a curve of class $C^3$ parametrised by [[arc length|00R1JDDV5X]] $s$.
Assume that its [[curvature|7JQS6VKFEZ]] $\kappa(s)$ is positive for all $s \in I$.
Let $T = \gamma'$, $N = T' / \kappa$ and $B = T \times N$, and let $\tau$ be the [[torsion|S4BZ697DSH]] of $\gamma$.
Then $(T(s), N(s), B(s))$ is a positively oriented [[orthonormal basis|0FWJ0VW561]] of $\R^3$ for each $s$, and
$$T' = \kappa N, \qquad N' = -\kappa T + \tau B, \qquad B' = -\tau N.$$

## Remarks

The first formula is the definition of $N$, and the third is the definition of $\tau$.
For the second, differentiate the identities $\ip{N}{N} = 1$, $\ip{N}{T} = 0$ and $\ip{N}{B} = 0$.
They give $\ip{N'}{N} = 0$, $\ip{N'}{T} = -\ip{N}{T'} = -\kappa$ and $\ip{N'}{B} = -\ip{N}{B'} = \tau$.
In matrix form the formulas say that $(T, N, B)' = (T, N, B) A$ with a skew-symmetric matrix $A$ built from $\kappa$ and $\tau$.
For the helix $(a \cos t, a \sin t, bt)$ with $a > 0$, both $\kappa = a / (a^2 + b^2)$ and $\tau = b / (a^2 + b^2)$ are constant.
The hypothesis $\kappa > 0$ is needed, since the normal $N$ is not defined where $\kappa = 0$.
For example, two plane arcs in different planes, smoothly joined through a straight segment, form a curve with $\tau = 0$ wherever $\kappa > 0$ that lies in no plane.

## Explanations

### L1 human

At each point of a space curve there are three natural directions: forward, the way the curve bends, and the direction perpendicular to both.
The Frenet–Serret formulas tell how these three arrows turn as one moves along the curve.
Only two numbers control this turning: the curvature and the torsion.

### L2 human

The formulas form a linear system of ordinary differential equations for the frame $(T, N, B)$ with coefficients $\kappa$ and $\tau$.
This is why curvature and torsion determine the curve up to a rigid motion, by the [[fundamental theorem of space curves|TNYQ5R0NVM]].
They give quick proofs of basic facts.
A curve with $\kappa > 0$ and $\tau = 0$ lies in a plane.
A curve with constant $\kappa > 0$ and $\tau = 0$ is an arc of a circle.
In $\R^n$ there is an analogous frame with $n - 1$ generalised curvatures, under a nondegeneracy hypothesis on the derivatives.
