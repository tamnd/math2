---
tag: YKZ1FP1PAG
kind: definition
name: Circle average
msc: [31A05, 28A25]
defines: Y7A1TP40MB
uses: [060W5CBZP6, DWJF7ABPR1, 0HYPR64JM2]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_value_theorem
---

## Definition

Let $E$ be $\R$ or $\C$, let $c \in \C$ and let $r \ge 0$.
Let $f$ be a function with values in $E$, defined at least on the [[circle|060W5CBZP6]] $\set{z \in \C : \abs{z - c} = r}$.
Assume that $\theta \mapsto f(c + r e^{i\theta})$ is [[Lebesgue integrable|DWJF7ABPR1]] on $[0, 2\pi]$.
The *circle average* of $f$ on the circle of centre $c$ and radius $r$ is
$$M(f; c, r) = \frac{1}{2\pi} \int_0^{2\pi} f(c + r e^{i\theta}) \, d\theta.$$

## Remarks

Example: let $f(z) = z$, with $c \in \C$ and $r > 0$.
Then $M(f; c, r) = c + \frac{r}{2\pi} \int_0^{2\pi} e^{i\theta} \, d\theta = c$, since the integral of $e^{i\theta}$ over a full period is $0$.
Non-example: let $f(z) = 1/\abs{z - 1}$ on $\C \setminus \set{1}$, with $c = 0$ and $r = 1$.
Then $f(e^{i\theta}) = 1/(2\abs{\sin(\theta/2)})$ for $0 < \theta < 2\pi$, which is not integrable near $\theta = 0$, so the circle average is not defined.
For $r = 0$ the circle average is $f(c)$.
The [[mean value property|0HYPR64JM2]] says that $M(u; c, r) = u(c)$ when $u$ is harmonic on a neighbourhood of the closed disc of centre $c$ and radius $r$.
For $r > 0$, $M(f; c, r)$ is the integral of $f$ against arc length on the circle, divided by the length $2\pi r$.
