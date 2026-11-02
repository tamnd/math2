---
tag: XDQ8CF0EZD
kind: definition
name: Square root of a positive operator
msc: [47A60, 47B65]
defines: 3JY5HNFRMF
uses: [HM2HHE3J51, 77020CY5ZW]
sources:
  - url: https://en.wikipedia.org/wiki/Square_root_of_a_matrix
---

## Definition

Let $H$ be a [[Hilbert space|HM2HHE3J51]] and let $A \colon H \to H$ be a [[positive operator|77020CY5ZW]].
A *positive square root* of $A$ is a positive operator $B \colon H \to H$ with $B^2 = A$.
Every positive $A$ has exactly one positive square root; it is called *the square root* of $A$ and written $A^{1/2}$ or $\sqrt{A}$.

## Remarks

Example: on $L^2[0, 1]$ let $A$ be multiplication by $x$, so $(Af)(x) = x f(x)$.
Multiplication by $\sqrt{x}$ is a positive operator $B$, since $\ip{Bf}{f} = \int_0^1 \sqrt{x} \abs{f(x)}^2 \, dx \ge 0$, and $B^2 f = x f$; so $A^{1/2} = B$.

Non-example: $-I$ satisfies $(-I)^2 = I$, but $\ip{-x}{x} = -\norm{x}^2 < 0$ for $x \ne 0$, so $-I$ is a square root of $I$ but not the positive square root.

The square root is given by the continuous functional calculus, $A^{1/2} = f(A)$ with $f(t) = \sqrt{t}$ on the spectrum of $A$.
It is also the norm limit of polynomials in $A$, so it commutes with every bounded operator that commutes with $A$.
