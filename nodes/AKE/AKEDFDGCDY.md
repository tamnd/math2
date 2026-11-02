---
tag: AKEDFDGCDY
kind: definition
name: Riemann P-symbol
msc: ["33C05", "34M03"]
defines: WWW053WXP2
uses: [RS8Z48E784, 0SG74WBFA2]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%27s_differential_equation
---

## Definition

Let $a, b, c$ be distinct points of the Riemann sphere, and let $\alpha, \alpha', \beta, \beta', \gamma, \gamma' \in \C$ with $\alpha + \alpha' + \beta + \beta' + \gamma + \gamma' = 1$.
The *Riemann P-symbol* is the table
$$P\begin{Bmatrix} a & b & c & \\ \alpha & \beta & \gamma & z \\ \alpha' & \beta' & \gamma' & \end{Bmatrix}.$$
It denotes the set of solutions $w(z)$ of [[Riemann's differential equation|RS8Z48E784]] with singular points $a, b, c$.
The exponents are $\alpha, \alpha'$ at $a$, $\beta, \beta'$ at $b$ and $\gamma, \gamma'$ at $c$.
When one of the points is $\infty$, the equation is the limiting form in which the factors involving that point are dropped.

## Remarks

The order of the columns, and the order of the two exponents within a column, do not matter.
Two basic rules hold.

1. If $T$ is a [[Möbius transformation|0SG74WBFA2]], then the P-symbol with points $a, b, c$ and variable $z$ equals the P-symbol with points $T(a), T(b), T(c)$, the same exponents, and variable $T(z)$.
2. If $a, b, c$ are finite, then for all $k, l \in \C$,
$$\left(\frac{z - a}{z - b}\right)^{k} \left(\frac{z - c}{z - b}\right)^{l} P\begin{Bmatrix} a & b & c & \\ \alpha & \beta & \gamma & z \\ \alpha' & \beta' & \gamma' & \end{Bmatrix} = P\begin{Bmatrix} a & b & c & \\ \alpha + k & \beta - k - l & \gamma + l & z \\ \alpha' + k & \beta' - k - l & \gamma' + l & \end{Bmatrix}.$$

Example: the [[hypergeometric function|463X5V31D9]] satisfies
$${}_2F_1(a, b; c; z) \in P\begin{Bmatrix} 0 & \infty & 1 & \\ 0 & a & 0 & z \\ 1 - c & b & c - a - b & \end{Bmatrix},$$
and the exponents add up to $0 + (1 - c) + a + b + 0 + (c - a - b) = 1$, as required.

Non-example: a table whose six exponents do not add up to $1$ is not a valid P-symbol.
No second-order Fuchsian equation has exactly those three singular points with those exponents.

Rule 2 is consistent with the sum condition: the shifts $k$, $-k-l$, $l$ appear twice each and add up to $0$.
