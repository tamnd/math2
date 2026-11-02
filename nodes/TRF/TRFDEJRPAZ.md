---
tag: TRFDEJRPAZ
kind: definition
name: Pitchfork bifurcation
msc: [34C23, 37G10]
defines: P88X34MSVV
uses: [0G4X36AE0X, 0V33BNKZ9S, 0FP31SX5EA]
sources:
  - url: https://en.wikipedia.org/wiki/Pitchfork_bifurcation
---

## Definition

Let $f \colon \R \times \R \to \R$ be [[smooth|0V33BNKZ9S]], and consider the family of scalar equations $x' = f(x, \mu)$ with parameter $\mu$.
Assume that $f$ is [[odd|0FP31SX5EA]] in $x$: $f(-x, \mu) = -f(x, \mu)$ for all $x$ and $\mu$.
Then $f(0, \mu) = 0$, so $0$ is an [[equilibrium point|0G4X36AE0X]] for every $\mu$.
The family has a *pitchfork bifurcation* at $(x, \mu) = (0, 0)$ if:

1. $f_x(0, 0) = 0$;
2. $f_{x\mu}(0, 0) \ne 0$;
3. $f_{xxx}(0, 0) \ne 0$.

## Remarks

Under these conditions, besides $x = 0$, the equilibria near $(0, 0)$ form a curve $\mu = m(x)$ with $m$ even, $m(0) = 0$ and $m''(0) = -f_{xxx}(0, 0) / (3 f_{x\mu}(0, 0))$.
So on one side of $\mu = 0$ there is a symmetric pair of new equilibria, and the stability of $0$ changes at $\mu = 0$.
The bifurcation is supercritical when the new equilibria are stable and subcritical when they are unstable.

Example: $f(x, \mu) = \mu x - x^3$.
It is odd in $x$, $f_x(0, 0) = 0$, $f_{x\mu} = 1$ and $f_{xxx} = -6$.
The new equilibria are $\pm\sqrt{\mu}$ for $\mu > 0$, and they are stable since $f_x(\pm\sqrt{\mu}, \mu) = -2\mu < 0$.
The equation $x' = \mu x + x^3$ gives the subcritical case.

Non-example: $f(x, \mu) = \mu x - x^2$ is not odd in $x$, so the symmetry hypothesis fails; it gives a transcritical bifurcation.
Without the symmetry, a small perturbation such as $\mu x - x^3 + \varepsilon$ breaks the pitchfork into a saddle-node and a separate branch.
