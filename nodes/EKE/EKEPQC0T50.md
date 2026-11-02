---
tag: EKEPQC0T50
kind: definition
name: Radical axis
msc: [51M04]
defines: BFD7T0YY42
uses: [060W5CBZP6, 02E9VT1RVQ, 0MP9BCF6DP]
sources:
  - url: https://en.wikipedia.org/wiki/Radical_axis
---

## Definition

Let $\Gamma_1$ and $\Gamma_2$ be [[circles|060W5CBZP6]] in the Euclidean plane with distinct centres $c_1 \ne c_2$ and radii $r_1, r_2$.
For a point $P$, its [[power|02E9VT1RVQ]] with respect to $\Gamma_i$ is $\pi_i(P) = \norm{P - c_i}^2 - r_i^2$.
The *radical axis* of $\Gamma_1$ and $\Gamma_2$ is the set
$$\set{P : \pi_1(P) = \pi_2(P)}.$$

## Remarks

Expanding the two powers, the condition becomes
$$2 \ip{P}{c_2 - c_1} = \norm{c_2}^2 - \norm{c_1}^2 - r_2^2 + r_1^2.$$
Since $c_2 - c_1 \ne 0$, this is a [[line|0MP9BCF6DP]] perpendicular to $c_1 c_2$.
For three circles with non-collinear centres, the three radical axes meet in one point, the radical centre.

Example: let $\Gamma_1$ be $x^2 + y^2 = 1$ and $\Gamma_2$ be $(x - 2)^2 + y^2 = 1$.
Then $\pi_1 = x^2 + y^2 - 1$ and $\pi_2 = x^2 - 4x + 4 + y^2 - 1$, and they are equal exactly when $x = 1$.

Non-example: concentric circles fail the condition $c_1 \ne c_2$.
For $c_1 = c_2$ and $r_1 \ne r_2$, the powers differ by the constant $r_1^2 - r_2^2 \ne 0$, so no point has equal powers.
