---
tag: QQFYC988SJ
kind: statement
role: theorem
name: Variation of parameters for difference equations
msc: [39A06]
uses: [9VA6P5KQQT, 0EB9N0S33C, 0VD9ZSWWJG]
about: [9VA6P5KQQT]
sources:
  - url: https://en.wikipedia.org/wiki/Variation_of_parameters
---

## Statement

Let $K$ be a field and let $m \ge 1$.
Let $A(0), A(1), \dots$ be [[invertible|0EB9N0S33C]] $m \times m$ matrices over $K$, and let $b(0), b(1), \dots$ be vectors in $K^m$.
Let $\Phi(0)$ be an invertible $m \times m$ matrix and let $\Phi(n+1) = A(n)\, \Phi(n)$ for $n \ge 0$.
Then each $\Phi(n)$ is invertible, and for each $x(0) \in K^m$ the solution of the [[matrix difference equation|9VA6P5KQQT]]
$$x(n+1) = A(n)\, x(n) + b(n) \qquad (n \ge 0)$$
is
$$x(n) = \Phi(n)\, \Phi(0)^{-1} x(0) + \sum_{k=0}^{n-1} \Phi(n)\, \Phi(k+1)^{-1} b(k) \qquad (n \ge 0).$$

## Remarks

The idea is to replace the constant vector $c$ in the homogeneous solution $\Phi(n) c$ by a varying vector $c(n)$.
Putting $x(n) = \Phi(n) c(n)$ into the equation gives $\Phi(n+1) c(n+1) = \Phi(n+1) c(n) + b(n)$, so $c(n+1) = c(n) + \Phi(n+1)^{-1} b(n)$.
Summing this telescoping relation from $0$ to $n - 1$ gives the formula.
Example: for $m = 1$ and a constant $A(n) = a \ne 0$, take $\Phi(n) = a^n$; the formula reads $x(n) = a^n x(0) + \sum_{k=0}^{n-1} a^{n-1-k} b(k)$.
Invertibility of the $A(n)$ is used to invert $\Phi(k+1)$.
Without it, the formula still holds if $\Phi(n)\, \Phi(0)^{-1}$ is replaced by the product $A(n-1) \cdots A(0)$.
Likewise $\Phi(n)\, \Phi(k+1)^{-1}$ is replaced by $A(n-1) \cdots A(k+1)$, which is the identity matrix when $k = n - 1$.
A scalar recurrence of order $m$ becomes such a system for the vector $(u_n, \dots, u_{n+m-1})$.
For $u_{n+2} + p_n u_{n+1} + q_n u_n = g_n$ with $q_n \ne 0$ and two independent homogeneous solutions $y_1, y_2$, this gives the particular solution with $u_0 = u_1 = 0$:
$$u_n = \sum_{k=0}^{n-1} g_k\, \frac{y_1(k+1)\, y_2(n) - y_1(n)\, y_2(k+1)}{C(k+1)},$$
where $C(j) = y_1(j) y_2(j+1) - y_2(j) y_1(j+1)$ is the Casoratian, which never vanishes.

## Explanations

### L1 human

The homogeneous equation is easy once you know a fundamental matrix: its solutions are $\Phi(n) c$ for constant vectors $c$.
To handle the extra input $b(n)$, let the constant $c$ change with $n$.
Each input $b(k)$ is then carried forward from time $k+1$ to time $n$ by the homogeneous dynamics, and the output is the sum of all these contributions.

### L2 human

This is the discrete form of the [[variation of parameters|0Y6TH5PQVS]] method for linear differential equations, where the sum becomes an integral.
It is also the discrete Duhamel principle: the response to the inputs is a sum of free responses started at each time.
With constant $A$, it reads $x(n) = A^n x(0) + \sum_{k=0}^{n-1} A^{n-1-k} b(k)$, which is the standard formula for linear time-invariant systems in discrete time.
Together with [[superposition|7W7VV861JW]], it describes all solutions of an inhomogeneous linear recurrence.
