---
tag: MS8PK4ZQNC
kind: definition
name: GNSS positioning
msc: [86A30, 65H10]
defines: TZ37HTS1AT
uses: [7WSH8Z6F7T, 0BYTQ4X1HC, 07EXVNF9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Satellite_navigation_solution
---

## Definition

Let $c$ be the speed of light.
Let $s_1, \dots, s_n \in \R^3$ be the positions of $n \ge 4$ satellites at the times they sent their signals, and let $\rho_1, \dots, \rho_n$ be the measured pseudoranges.
*GNSS positioning* is the determination of the receiver position $x \in \R^3$ and the receiver clock bias $\delta \in \R$ from the equations
$$\rho_i = \norm{x - s_i} + c\,\delta, \qquad i = 1, \dots, n.$$
When $n > 4$, or when the data contain errors, $(x, \delta)$ is defined as the [[least squares|0BYTQ4X1HC]] solution, minimising $\sum_i \big(\rho_i - \norm{x - s_i} - c\delta\big)^2$.

## Remarks

Example: if $\delta = 0$ were known, the equations would reduce to [[trilateration|7WSH8Z6F7T]] with distances $r_i = \rho_i$.
Non-example: three satellites do not suffice in general, since three equations cannot fix four unknowns $x_1, x_2, x_3, \delta$.
The solution is usually computed by [[Newton's method|07EXVNF9VP]] in its Gauss–Newton form, starting from a rough guess such as the centre of the Earth.
Closed-form solutions also exist, such as Bancroft's method.
In practice the model adds corrections for satellite clocks, the atmosphere and the rotation of the Earth during signal travel.
