---
tag: VG89W21QAR
kind: definition
name: Legendre transformation of thermodynamic potentials
msc: [80A10, 26A51]
defines: 2B0YR3D0XA
uses: [ZQYMWVT1TT, MKZW03Q590, 3W28H76A82, F6JVQ12X43, 722RZK72P5, JXKY6C8JTA, RBG5ZBM35Y]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre_transformation
---

## Definition

Let $\Phi(x_1, \dots, x_n)$ be a [[thermodynamic potential|MKZW03Q590]] that is differentiable in its natural variables $x_1, \dots, x_n$.
Let $y_i = \partial \Phi / \partial x_i$ be the [[conjugate variable|3W28H76A82]] of $x_i$.
Fix $1 \le k \le n$ and suppose that the map $(x_1, \dots, x_k) \mapsto (y_1, \dots, y_k)$, at fixed $x_{k+1}, \dots, x_n$, is invertible.
The *Legendre transform* of $\Phi$ in $x_1, \dots, x_k$ is
$$\Psi = \Phi - \sum_{i=1}^{k} x_i \, y_i,$$
written as a function of $y_1, \dots, y_k, x_{k+1}, \dots, x_n$ by solving $y_i = \partial \Phi / \partial x_i$ for $x_1, \dots, x_k$.

## Remarks

Then $d\Psi = -\sum_{i \le k} x_i \, dy_i + \sum_{i > k} y_i \, dx_i$, so $x_i = -\partial \Psi / \partial y_i$ for $i \le k$.
The sign is opposite to the usual mathematical one: for one variable, $\Psi(y) = -\Phi^*(y)$, where $\Phi^*$ is the [[Legendre transform|ZQYMWVT1TT]] of analysis.
Example: from the [[internal energy|F6JVQ12X43]] $U(S, V)$ with $T = \partial U / \partial S$, the transform in $S$ is the [[Helmholtz free energy|JXKY6C8JTA]] $F = U - TS$.
The check: $dF = dU - T \, dS - S \, dT = -S \, dT - p \, dV$.
The transform in $V$, with $-p = \partial U / \partial V$, is the [[enthalpy|722RZK72P5]] $H = U + pV$, and the transform in both is the [[Gibbs free energy|RBG5ZBM35Y]].
Non-example: when $U$ is linear in $S$ on an interval at fixed $V$, $T$ does not determine $S$ and the invertibility clause fails.
Then one uses the convex conjugate instead: $F(T, V) = \inf_S \big(U(S, V) - TS\big)$.

## Explanations

### L1 human

The Legendre transformation swaps a variable for the slope of the potential in that variable.
Subtracting the product of the two keeps all the information, and the new function has the slope as its variable.
