---
tag: 3GKR8PKRH3
kind: definition
name: Network synthesis
msc: [94C05, 30C10]
defines: 6AX5E50CZY
uses: [0XDK9CGYKJ, 0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Network_synthesis
---

## Definition

Let $s$ denote the complex frequency of the [[Laplace transform|0V49JEZW06]].
A [[rational function|0XDK9CGYKJ]] $Z(s)$ with real coefficients is *positive real* if $\operatorname{Re} Z(s) \ge 0$ for every $s \in \C$ with $\operatorname{Re} s > 0$ that is not a pole of $Z$.
A *realization* of $Z$ is a finite one-port network whose driving-point impedance is $Z$.
It is built from resistors, inductors and capacitors with positive values and from ideal transformers.
*Network synthesis* is the problem of deciding, for a given $Z$, whether it has a realization, and of constructing one.
The same name is used for prescribed admittances, transfer functions and matrices of multi-port networks.

## Remarks

By Brune's theorem, a rational function with real coefficients has a realization if and only if it is positive real.
Example: $Z(s) = R + Ls$ with $R, L > 0$ is positive real, since $\operatorname{Re} Z(s) = R + L \operatorname{Re} s > 0$ when $\operatorname{Re} s > 0$.
It is realized by a resistor $R$ in series with an inductor $L$.
Non-example: $Z(s) = s - 1$ is not positive real, since $\operatorname{Re} Z(1/2) = -1/2 < 0$, so no passive network realizes it.
Realizations are never unique: the impedances of different networks can coincide.
For lossless networks, [[Foster's reactance theorem|CPXHX475CW]] describes the realizable impedances completely.
