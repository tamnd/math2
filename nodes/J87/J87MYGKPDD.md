---
tag: J87MYGKPDD
kind: definition
name: Heun function
msc: ["33E30", 34M03, 34M35]
defines: 87DAYKCZ5M
uses: [ZBVH2YE50B, H96HXG6CA0, 0QQRP17Z7S]
sources:
  - url: https://en.wikipedia.org/wiki/Heun_function
---

## Definition

Let $a \in \C \setminus \set{0, 1}$ and let $q, \alpha, \beta, \gamma, \delta, \epsilon$ be complex numbers with
$$\epsilon = \alpha + \beta + 1 - \gamma - \delta.$$
*Heun's equation* is the [[linear differential equation|0QQRP17Z7S]]
$$\frac{d^2 w}{dz^2} + \left( \frac{\gamma}{z} + \frac{\delta}{z - 1} + \frac{\epsilon}{z - a} \right) \frac{dw}{dz} + \frac{\alpha \beta z - q}{z (z - 1)(z - a)}\, w = 0.$$
Assume $\gamma \notin \set{0, -1, -2, \dots}$.
The *local Heun function* $Hl(a, q; \alpha, \beta, \gamma, \delta; z)$ is the unique solution of Heun's equation that is analytic at $z = 0$ and takes the value $1$ there.

## Remarks

Heun's equation is a [[Fuchsian equation|ZBVH2YE50B]] with [[regular singular points|H96HXG6CA0]] $0, 1, a, \infty$.
Every Fuchsian equation with four regular singular points takes this form after moving the singular points there and making one exponent $0$ at each finite point.
The exponents are $\set{0, 1 - \gamma}$ at $0$, $\set{0, 1 - \delta}$ at $1$, $\set{0, 1 - \epsilon}$ at $a$ and $\set{\alpha, \beta}$ at $\infty$.
The relation $\epsilon = \alpha + \beta + 1 - \gamma - \delta$ is Fuchs' relation: the sum of all exponents equals $2$.
The number $q$ is the accessory parameter; it is not determined by the exponents.
The power series of $Hl$ at $0$ converges in the disc $\abs{z} < \min(1, \abs{a})$.
Example: for $q = 0$ and $\alpha = 0$, the constant $w = 1$ is a solution, since $w' = w'' = 0$ and $\alpha\beta z - q = 0$; so $Hl(a, 0; 0, \beta, \gamma, \delta; z) = 1$.
Non-example: for $q = 1$ and $\alpha = 0$, the constant $1$ is not a solution, since the equation leaves the term $\frac{-1}{z (z - 1)(z - a)} \ne 0$.
A *Heun function* in the narrow sense is a local solution that is analytic at two singular points at once, for instance at $0$ and $1$.
This happens only for special values of $q$.
