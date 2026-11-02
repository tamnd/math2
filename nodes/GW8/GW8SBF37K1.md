---
tag: GW8SBF37K1
kind: definition
name: Floquet theory
msc: [34C25, 34A30, 34D08]
defines: BJVZXPB297
uses: [0A6QZ367GX, 0MQ24RBG93, 0K665H5V1S, 089KWVYD69]
sources:
  - url: https://en.wikipedia.org/wiki/Floquet_theory
---

## Definition

Let $T > 0$ and let $A : \R \to \C^{n \times n}$ be continuous and [[periodic|089KWVYD69]] with period $T$.
*Floquet theory* is the theory of the [[linear system|0A6QZ367GX]] $x' = A(t)\, x$, based on the following objects.

1. For a [[fundamental matrix|0MQ24RBG93]] $\Phi$, the matrix $t \mapsto \Phi(t + T)$ is again a fundamental matrix, so $\Phi(t + T) = \Phi(t)\, M$ for a constant invertible matrix $M = \Phi(0)^{-1} \Phi(T)$, called the monodromy matrix.
2. A Floquet representation of $\Phi$ is a factorization $\Phi(t) = P(t)\, e^{tB}$ with a constant $B \in \C^{n \times n}$ and the [[matrix exponential|0K665H5V1S]] $e^{tB}$. Here $P : \R \to \C^{n \times n}$ is continuously differentiable, $T$-periodic and invertible at every $t$.

Floquet's theorem states that every fundamental matrix has a Floquet representation, with $B$ any matrix such that $e^{TB} = M$.

## Remarks

The eigenvalues of $M$ are the characteristic multipliers; they do not depend on the choice of $\Phi$, since another choice replaces $M$ by a similar matrix.
The change of variables $x = P(t)\, z$ turns the system into $z' = B z$ with constant coefficients.
All solutions tend to $0$ if and only if all multipliers have modulus less than $1$; there is a nonzero $T$-periodic solution if and only if $1$ is a multiplier.
Example: for $n = 1$ and $A(t) = 1 + \cos t$, $T = 2\pi$, the solution is $\Phi(t) = e^{t + \sin t}$, so $M = e^{2\pi}$, $B = 1$ and $P(t) = e^{\sin t}$, which is $2\pi$-periodic.
Non-example: if $A$ is not periodic, the solutions need not have this form.
For $A(t) = 2t$ the solution $e^{t^2}$ is not $P(t) e^{tB}$ with $P$ periodic, since then $\abs{\Phi(t)} \le C e^{t \operatorname{Re} B}$ would grow at most exponentially.
Over $\R$ one can take $B$ real if one allows $P$ to have period $2T$.
