---
about:
- G12KXDHPPS
- V6Q24CHJG8
kind: statement
msc:
- 42A20
name: Convergence of the Fourier series of a piecewise smooth function
role: theorem
sources:
- url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-fourier-and-pde.tex#L1701
  locator: ch-fourier-and-pde.tex:1701
tag: JD1AKBE02G
uses:
- G12KXDHPPS
- 0ATF6Q0633
---

## Statement

Let $L > 0$.
Let $f \colon \R \to \R$ be a [[periodic function|0ATF6Q0633]] of period $2L$ that is piecewise smooth.
This means that on each period, $f$ has finitely many break points.
Between them $f$ is continuously differentiable, and $f$ and $f'$ have one-sided limits at the break points.

Let $F(t)$ be the [[Fourier series|G12KXDHPPS]] of $f$, with coefficients $a_n$ and $b_n$:

$$F(t) = \frac{a_0}{2} + \sum_{n=1}^\infty \left[ a_n \cos\left(\frac{n\pi t}{L}\right) + b_n \sin\left(\frac{n\pi t}{L}\right) \right].$$

Then:

1. The series $F(t)$ converges at every real $t$.
2. If $f$ is continuous at $t$, then $F(t) = f(t)$.
3. If $f$ is not continuous at $t$, then $F(t) = \frac{f(t^-) + f(t^+)}{2}$, the average of the one-sided limits.

## Remarks

The value of the sum at a jump is the midpoint of the jump.

A piecewise smooth function has bounded variation on a period, so this is a special case of the [[Dirichlet conditions|75ZQW12WY0]] test.
