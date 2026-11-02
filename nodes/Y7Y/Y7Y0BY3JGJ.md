---
tag: Y7Y0BY3JGJ
kind: definition
name: Hypergeometric differential equation
msc: ["33C05", "34M03"]
defines: W8VE25R5A7
uses: [0NT64JV96A, H96HXG6CA0, 463X5V31D9]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function
---

## Definition

Let $a, b, c \in \C$.
The *hypergeometric differential equation* is the second-order linear [[ordinary differential equation|0NT64JV96A]] for a function $w$ of a complex variable $z$:
$$z(1 - z) \, \frac{d^2 w}{dz^2} + \big[c - (a + b + 1) z\big] \frac{dw}{dz} - ab \, w = 0.$$

## Remarks

Its singular points on the Riemann sphere are $0$, $1$ and $\infty$, and all three are [[regular singular points|H96HXG6CA0]].
The exponents are $\set{0, 1 - c}$ at $0$, $\set{0, c - a - b}$ at $1$ and $\set{a, b}$ at $\infty$.

Example: if $c \notin \set{0, -1, -2, \ldots}$, the [[hypergeometric function|463X5V31D9]] $w = {}_2F_1(a, b; c; z)$ is a solution.
To check it, put $w = \sum_n t_n z^n$; the equation gives $(n+1)(n+c)\, t_{n+1} = (n+a)(n+b)\, t_n$, which is exactly the recursion of the coefficients $t_n = \frac{(a)_n (b)_n}{(c)_n n!}$.
If moreover $c \notin \Z$, a second, independent solution near $0$ is $z^{1-c} \, {}_2F_1(a - c + 1, b - c + 1; 2 - c; z)$.

Non-example: [[Kummer's equation|NT917KFR57]] $z w'' + (c - z) w' - a w = 0$ is not of this form; it has a regular singular point at $0$, but its singular point at $\infty$ is irregular.

In the notation of the Riemann P-symbol, the solutions form
$$P\begin{Bmatrix} 0 & 1 & \infty & \\ 0 & 0 & a & z \\ 1 - c & c - a - b & b & \end{Bmatrix}.$$
