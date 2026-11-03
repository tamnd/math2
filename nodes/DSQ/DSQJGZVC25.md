---
tag: DSQJGZVC25
kind: definition
name: Paraxial wave equation
msc: [78A10, 35Q60, 78A60]
defines: 53DCTAEM5M
uses: [MNXKTXJ35G, N111BHFQ2H, EPZR6H2WJN]
sources:
  - url: https://en.wikipedia.org/wiki/Paraxial_approximation
---

## Definition

Let $k > 0$ be a wave number, and let $U(x, y, z)$ solve the [[Helmholtz equation|MNXKTXJ35G]] $\Delta U + k^2 U = 0$.
Write $U(x, y, z) = A(x, y, z) \, e^{ikz}$ with an envelope $A$ of class $C^2$.
Assume the slowly varying envelope condition $\abs{\partial_z^2 A} \ll \abs{k \, \partial_z A}$.
Dropping the term $\partial_z^2 A$ gives the *paraxial wave equation*
$$\partial_x^2 A + \partial_y^2 A + 2ik \, \partial_z A = 0.$$

## Remarks

Exactly, $\Delta U + k^2 U = e^{ikz} \bigl(\partial_x^2 A + \partial_y^2 A + \partial_z^2 A + 2ik \, \partial_z A\bigr)$, so the equation is the [[paraxial approximation|N111BHFQ2H]] of the Helmholtz equation.
Here the time dependence is $e^{-i\omega t}$; with the convention $e^{-ikz}$ the sign of the last term changes.
In the form $i \, \partial_z A = -\frac{1}{2k} (\partial_x^2 + \partial_y^2) A$ it is the free [[Schrödinger equation|EPZR6H2WJN]] in the plane, with $z$ in place of time.

Example: let $z_R > 0$, $q(z) = z - i z_R$ and $A = q^{-1} \exp\bigl(ik(x^2 + y^2)/(2q)\bigr)$.
With $r^2 = x^2 + y^2$, one computes $2ik \, \partial_z A = \bigl(-2ik/q^2 + k^2 r^2/q^3\bigr) q A$.
Also $(\partial_x^2 + \partial_y^2) A = \bigl(2ik/q^2 - k^2 r^2/q^3\bigr) q A$, so the sum vanishes.
This solution is the Gaussian beam.

Non-example: $A = e^{i k_x x}$ with $k_x \ne 0$ does not solve the equation, since $\partial_x^2 A = -k_x^2 A \ne 0$ while $\partial_z A = 0$.
The tilted beam $A = e^{i k_x x - i k_x^2 z/(2k)}$ does solve it.
