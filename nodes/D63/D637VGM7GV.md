---
tag: D637VGM7GV
kind: definition
name: Quasi-algebraically closed field
msc: ["12E30", 11D72]
defines: G7RM16N4PF
uses: [0QA8CHH8MG, SD3M01318E, 02SJG1HC32, 08RTDHX1SK, 08895Q5W96]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-algebraically_closed_field
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]].
The field $K$ is *quasi-algebraically closed*, or a *$C_1$ field*, if the following holds.
For all integers $n > d \ge 1$, every [[homogeneous polynomial|SD3M01318E]] $f \in K[x_1, \ldots, x_n]$ of degree $d$ has a zero $(a_1, \ldots, a_n) \in K^n$ with $(a_1, \ldots, a_n) \ne (0, \ldots, 0)$.

## Remarks

Every [[algebraically closed field|02SJG1HC32]] is $C_1$.
Indeed, let $g(t) = f(t, 1, 0, \ldots, 0)$.
If $g$ is not constant, it has a root $t_0$, and $(t_0, 1, 0, \ldots, 0)$ is a nontrivial zero of $f$.
If $g$ is constant, the coefficient of $x_1^d$ in $f$ is $0$, so $(1, 0, \ldots, 0)$ is a nontrivial zero of $f$.

Example: a [[finite field|08RTDHX1SK]] $\F_q$ is $C_1$.
Check: by the [[Chevalley–Warning theorem|08895Q5W96]], the number of zeros in $\F_q^n$ of a polynomial of degree $d < n$ is divisible by the characteristic.
The zero vector is one zero, so there is another.

Non-example: $\R$ is not $C_1$.
The form $x^2 + y^2 + z^2$ has degree $2$ in $3$ variables, but its only real zero is $(0, 0, 0)$.

More generally, $K$ is a $C_i$ field if every homogeneous polynomial of degree $d \ge 1$ in $n > d^i$ variables has a nontrivial zero; $C_1$ is the case $i = 1$.
