---
tag: M4TXKR87H8
kind: definition
name: Schur stable polynomial
msc: [39A30, 93D20, 26C10]
defines: X11Q0G8PNA
uses: [019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_polynomial
---

## Definition

Let $P(z) = a_n z^n + a_{n-1} z^{n-1} + \cdots + a_0$ be a polynomial of degree $n \ge 1$ with complex coefficients.
The polynomial $P$ is *Schur stable* if every complex [[root|019MA1VTR2]] $\lambda$ of $P$ satisfies $\abs{\lambda} < 1$.

## Remarks

Example: $P(z) = z^2 - z + \tfrac{1}{2}$ has roots $\tfrac{1}{2} \pm \tfrac{1}{2} i$.
Each has modulus $\sqrt{1/4 + 1/4} = 1/\sqrt{2} < 1$, so $P$ is Schur stable.

Non-example: $P(z) = z^2 - 1$ has roots $1$ and $-1$.
They have modulus exactly $1$, so the strict inequality fails and $P$ is not Schur stable.

Some authors call such polynomials simply *stable* in a discrete-time context, or say that $P$ has all its zeros in the open unit disc.
The polynomial $P$ is Schur stable if and only if its reversed polynomial $z^n P(1/z)$ has all its roots outside the closed unit disc, provided $a_0 \ne 0$.
