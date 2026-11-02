---
tag: MSDC626JK5
kind: definition
name: Random integral equation
msc: [45R05, 60H20, 45A05]
defines: VDQ32JT7ZS
uses: [R3SG1SN7JQ, 0NFPJVJJHX, YYNCJSR0PJ, 0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_differential_equation
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0NFPJVJJHX]] and let $[a, b]$ be a compact interval.
Let $k \colon [a, b] \times [a, b] \times \Omega \to \R$ and $h \colon [a, b] \times \Omega \to \R$ be [[measurable functions|YYNCJSR0PJ]].
Here the domains carry the product of the Borel $\sigma$-algebras and $\mathcal{F}$.
The *random (linear Fredholm) integral equation* with random kernel $k$ and random free term $h$ is
$$x(t, \omega) = h(t, \omega) + \int_a^b k(t, s, \omega) \, x(s, \omega) \, ds, \qquad t \in [a, b], \ \omega \in \Omega.$$
A *random solution* is a measurable function $x \colon [a, b] \times \Omega \to \R$ with the following property.
For $P$-almost every $\omega$, the integral converges absolutely and the equation holds, for every $t \in [a, b]$.

## Remarks

Random Volterra equations, with $\int_a^t$ in place of $\int_a^b$, and nonlinear random equations such as $x(t, \omega) = h(t, \omega) + \int_a^b k(t, s, \omega) f(s, x(s, \omega)) \, ds$ are defined in the same way.
A random solution is a [[stochastic process|0QH5ENKZM1]] indexed by $t \in [a, b]$.
The integral is an ordinary Lebesgue integral, computed separately for each $\omega$.

Example: $[a, b] = [0, 1]$, $Y$ a random variable with values in $[0, 1]$, $k(t, s, \omega) = Y(\omega)/2$ and $h = 1$.
A constant $x(t, \omega) = c(\omega)$ solves the equation when $c = 1 + Y c / 2$, that is, $c = 2/(2 - Y)$.
This $c$ is measurable, so $x(t, \omega) = 2/(2 - Y(\omega))$ is a random solution.

Non-example: the equation $x(t) = 1 + \int_0^t x(s) \, dW(s)$, with $W$ a [[Wiener process|22735FGJV6]], is not a random integral equation in this sense.
Almost every path of $W$ has unbounded variation, so the integral cannot be computed path by path as a Lebesgue–Stieltjes integral.
It is an Itô integral, and the equation is a [[stochastic Volterra equation|KA95J9V6AS]].

## Explanations

### L1 human

It is a family of integral equations, one for each outcome $\omega$ of a random experiment, solved outcome by outcome.
