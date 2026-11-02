---
tag: Q28DM6ZCMF
kind: statement
role: theorem
name: Duhamel's principle
msc: [34A30, 34A12]
uses: [037ZNY7NAG, 0H1GN6P9R5, 0FXDW992DS, 020M04FN1H, 0Y6TH5PQVS]
about: [037ZNY7NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Duhamel%27s_principle
---

## Statement

Let $I$ be an open interval, and let $A \colon I \to \R^{n \times n}$ and $f \colon I \to \R^n$ be continuous.
Let $\Phi$ be a [[fundamental matrix|0H1GN6P9R5]] of the homogeneous [[linear system|037ZNY7NAG]] $x' = A(t) x$ on $I$, and put $\Phi(t, s) = \Phi(t) \Phi(s)^{-1}$ for $t, s \in I$.
Let $t_0 \in I$ and $x_0 \in \R^n$.
Then the [[initial value problem|0FXDW992DS]]
$$x' = A(t) x + f(t), \qquad x(t_0) = x_0$$
has exactly one solution on $I$, and it is
$$x(t) = \Phi(t, t_0)\, x_0 + \int_{t_0}^{t} \Phi(t, s)\, f(s)\, ds.$$
If $A$ is constant, then $\Phi(t, s) = e^{(t - s) A}$, the [[matrix exponential|020M04FN1H]].

## Remarks

Differentiating under the integral sign gives $x'(t) = A(t) \Phi(t, t_0) x_0 + \Phi(t, t) f(t) + \int_{t_0}^t A(t) \Phi(t, s) f(s)\, ds = A(t) x(t) + f(t)$, since $\Phi(t, t)$ is the identity.
Uniqueness holds because the difference of two solutions solves the homogeneous system with initial value $0$, so it is zero.
The formula is the matrix form of [[variation of parameters|0Y6TH5PQVS]].

Example: for $x' = -x + 1$ and $x(0) = 0$, one has $\Phi(t, s) = e^{-(t - s)}$.
The formula gives $x(t) = \int_0^t e^{-(t - s)}\, ds = 1 - e^{-t}$, and indeed $x' = e^{-t} = -x + 1$.

## Explanations

### L1 human

The principle says how to solve a linear equation with an outside force once one can solve it without the force.
At each instant $s$, the force gives the system a small kick $f(s)\, ds$.
That kick then evolves by the unforced equation from time $s$ to time $t$.
The solution is the free evolution of the initial state plus the sum of all these evolved kicks.

### L2 human

The function $\Phi(t, s)$ is often called the state transition matrix or propagator.
The same idea works for evolution equations such as the heat equation and the wave equation, where $\Phi(t, s)$ becomes a solution operator.
In the theory of $C_0$-semigroups, the formula defines the mild solution of an inhomogeneous abstract Cauchy problem.
For a boundary value problem, the analogous object is the [[Green's function|SH6JY9RN2E]].
