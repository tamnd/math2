---
tag: FQX56M03XD
kind: definition
name: Complex dynamics
msc: [37F10, 30D05]
defines: BQQZ0ZCGQF
uses: [0NAHXR1FRH, 0J78KBPFZB, 0XDK9CGYKJ, 0G4F0XB9X2, AYVTR2ES5B, 5AA9AJEARJ]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_dynamics
---

## Definition

Let $X$ be the [[Riemann sphere|0J78KBPFZB]] $\hat{\C}$ or the complex plane $\C$, and let $f \colon X \to X$ be a [[holomorphic map|0NAHXR1FRH]].
For $n \ge 0$, the [[iterate|AYVTR2ES5B]] $f^n$ is the $n$-fold composition $f \circ \cdots \circ f$, with $f^0 = \id$.
The pair $(X, f)$ is a *holomorphic* [[discrete-time dynamical system|5AA9AJEARJ]].
The *orbit* of a point $z \in X$ is the sequence $z, f(z), f^2(z), \ldots$.
*Complex dynamics* is the study of the orbits of such systems and of how they depend on the point $z$ and on the map $f$.

## Remarks

The standard cases are [[rational functions|0XDK9CGYKJ]] $f \colon \hat{\C} \to \hat{\C}$ of degree at least $2$, polynomials of degree at least $2$, and transcendental [[entire functions|0G4F0XB9X2]] $f \colon \C \to \C$.
Example: $f(z) = z^2 + c$ with $c \in \C$ is a polynomial, hence holomorphic on $\C$, so $(\C, f)$ is a holomorphic dynamical system.
Non-example: $f(z) = \bar z^2$ is not holomorphic, since $\partial f / \partial \bar z = 2 \bar z \ne 0$ for $z \ne 0$, so its iteration is not part of complex dynamics in this sense.
Rational maps of degree $1$ are Möbius maps, whose dynamics is elementary, which is why the degree is usually taken to be at least $2$.
