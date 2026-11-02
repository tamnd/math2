---
tag: MPRCFT30Z7
kind: definition
name: Oscillatory solution of a difference equation
msc: [39A21]
defines: 3DRCZF6J9J
uses: [04CC6K5VDT]
sources:
  - url: https://en.wikipedia.org/wiki/Oscillation_theory
---

## Definition

Let $(x_n)_{n \ge n_0}$ be a [[real sequence|04CC6K5VDT]] that is a solution of a difference equation and is not identically zero.
The solution is *oscillatory* if for every integer $N \ge n_0$ there is an integer $n \ge N$ with
$$x_n \, x_{n+1} \le 0.$$
Otherwise it is *nonoscillatory*, that is, it is eventually positive or eventually negative.

## Remarks

Example: $x_n = (-1)^n$ solves $x_{n+1} = -x_n$.
For every $n$ one has $x_n x_{n+1} = -1 \le 0$, so the solution is oscillatory.

Non-example: $x_n = 2^{-n}$ solves $x_{n+1} = x_n / 2$.
Here $x_n x_{n+1} > 0$ for all $n$, so the condition fails already for $N = n_0$, and the solution is nonoscillatory.

One also speaks of oscillation about a value $x^*$, often an equilibrium, meaning that $(x_n - x^*)$ is oscillatory.
For the linear equation $x_{n+1} = a x_n$ with $a \ne 0$, every nonzero solution is oscillatory exactly when $a < 0$.
