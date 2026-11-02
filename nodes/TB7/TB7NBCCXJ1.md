---
tag: TB7NBCCXJ1
kind: definition
name: Saddle-node bifurcation
msc: [34C23, 37G10]
defines: MAP5J6HK0T
uses: [0G4X36AE0X, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Saddle-node_bifurcation
---

## Definition

Let $f \colon \R \times \R \to \R$ be [[smooth|0V33BNKZ9S]], and consider the family of scalar equations $x' = f(x, \mu)$ with parameter $\mu$.
Write $f_x$, $f_\mu$, $f_{xx}$ for the partial derivatives of $f$.
The family has a *saddle-node bifurcation* at $(x, \mu) = (0, 0)$ if:

1. $f(0, 0) = 0$, so $0$ is an [[equilibrium point|0G4X36AE0X]] for $\mu = 0$;
2. $f_x(0, 0) = 0$;
3. $f_{xx}(0, 0) \ne 0$;
4. $f_\mu(0, 0) \ne 0$.

## Remarks

Under these conditions, the equilibria near $(0, 0)$ form a curve $\mu = m(x)$ with $m(0) = m'(0) = 0$ and $m''(0) = -f_{xx}(0, 0) / f_\mu(0, 0) \ne 0$.
So for $\mu$ on one side of $0$ there are two equilibria near $0$, one stable and one unstable, and on the other side there are none.

Example: $f(x, \mu) = \mu - x^2$.
Then $f(0, 0) = 0$, $f_x = -2x$ vanishes at $0$, $f_{xx} = -2 \ne 0$ and $f_\mu = 1 \ne 0$.
The equilibria are $\pm\sqrt{\mu}$ for $\mu > 0$, and there are none for $\mu < 0$.

Non-example: $f(x, \mu) = \mu x - x^2$.
Here $f_\mu(0, 0) = 0$, so clause 4 fails; the two equilibria $0$ and $\mu$ exist for all $\mu$ and only cross, which is a transcritical bifurcation.

For a system in $\R^n$, clause 2 is replaced by a condition on the Jacobian matrix at the equilibrium.
It must have a simple eigenvalue $0$ and no other eigenvalue on the imaginary axis.
The conditions 3 and 4 are then imposed on the equation reduced to a centre manifold.
