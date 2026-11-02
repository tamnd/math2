---
tag: GRZAY7GWC5
kind: definition
name: Weyl–Titchmarsh theory
msc: [34B20, 34L05]
defines: XT8PA31VAX
uses: [89AA6XJY5K, 6J9FXT6HAV, X6XGGH5FPW]
sources:
  - url: https://en.wikipedia.org/wiki/Sturm–Liouville_theory
---

## Definition

Let $q \colon [0, \infty) \to \R$ be integrable on each interval $[0, R]$ with $R > 0$.
Assume that the [[Schrödinger operator|89AA6XJY5K]] $-y'' + q y$ is in the [[limit-point case|6J9FXT6HAV]] at $\infty$.
For $z \in \C \setminus \R$, let $\psi(z, \cdot)$ be a nonzero solution of $-y'' + q y = z y$ with $\int_0^\infty \abs{\psi(z, x)}^2 \, dx < \infty$; by the limit-point assumption it is unique up to a constant factor.
The Weyl–Titchmarsh function, or $m$-function, of $q$ is
$$m(z) = \frac{\psi'(z, 0)}{\psi(z, 0)}, \qquad z \in \C \setminus \R.$$
Weyl–Titchmarsh theory is the study of the spectral theory of such operators through the function $m$.

## Remarks

The quotient does not depend on the choice of $\psi$.
Also $\psi(z, 0) \ne 0$, since otherwise the non-real number $z$ would be an eigenvalue of the self-adjoint operator with the Dirichlet condition $y(0) = 0$.
The function $m$ is analytic on $\C \setminus \R$, satisfies $m(\overline{z}) = \overline{m(z)}$, and maps the [[upper half-plane|X6XGGH5FPW]] into itself.
So $m$ is a Herglotz function, and the measure in its [[Herglotz representation|9ZBAX4ZPX0]] is the spectral measure of the operator with the condition $y(0) = 0$.
Example: for $q = 0$, the solution $\psi(z, x) = e^{i\sqrt{z}\, x}$, with the branch of $\sqrt{z}$ that has positive imaginary part, is square integrable on $[0, \infty)$.
So $m(z) = i \sqrt{z}$; for $z = i$ this is $e^{3\pi i/4}$, which lies in the upper half-plane.
Non-example: for $z \in \C \setminus \R$ the solution $e^{-i\sqrt{z}\, x}$ grows exponentially, so it cannot be used for $\psi$.
Some books use the other sign convention, or the boundary condition $y'(0) = h y(0)$ at $0$, which changes $m$ by a Möbius transformation.

## Explanations

### L1 human

The $m$-function compares the slope and the value at $0$ of the one solution that stays square integrable at infinity.
It is a single analytic function, and its boundary behaviour on the real line encodes the spectrum of the operator.
