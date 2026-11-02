---
tag: KF06HRCM4N
kind: statement
role: theorem
name: Differentiable dependence on parameters
msc: [34A12]
uses: [019VSXSFMQ, 04SW7WECS8, 047NDTEPCV, 06SKCHDQT5]
about: [0FXDW992DS, 01J7FZ65J0]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
---

## Statement

Let $D \subseteq \R \times \R^n \times \R^k$ be open and let $f : D \to \R^n$, $(t, x, \lambda) \mapsto f(t, x, \lambda)$, be continuous with continuous partial derivatives with respect to $x$ and $\lambda$.
For $(t_0, x_0, \lambda) \in D$, let $t \mapsto \varphi(t; t_0, x_0, \lambda)$ be the [[maximal solution|019VSXSFMQ]] of $x' = f(t, x, \lambda)$ with $x(t_0) = x_0$.
Let $\Omega$ be the set of $(t, t_0, x_0, \lambda)$ for which $\varphi(t; t_0, x_0, \lambda)$ is defined.
Then:

1. The set $\Omega$ is open and $\varphi$ is [[continuously differentiable|06SKCHDQT5]] on $\Omega$.
2. The matrix $J(t) = \partial \varphi / \partial x_0$ solves the variational equation $J' = A(t)\, J$ with $J(t_0) = I$, where $A(t) = \partial_x f(t, \varphi(t), \lambda)$ is the [[Jacobian matrix|047NDTEPCV]] along the solution.
3. The matrix $K(t) = \partial \varphi / \partial \lambda$ solves $K' = A(t)\, K + \partial_\lambda f(t, \varphi(t), \lambda)$ with $K(t_0) = 0$.
4. The derivative with respect to the initial time is $\partial \varphi / \partial t_0 = -J(t)\, f(t_0, x_0, \lambda)$.

## Remarks

Proof idea: the parameter $\lambda$ can be absorbed into the state by adding the equation $\lambda' = 0$, so it suffices to treat initial values.
One shows that the difference quotients $(\varphi(t; t_0, x_0 + h e_i) - \varphi(t; t_0, x_0))/h$ converge, using the mean value theorem and [[Grönwall's inequality|07EJHQYR9A]] to compare them with the solution of the variational equation.
Example: for $x' = \lambda x$, $\varphi(t; 0, x_0, \lambda) = x_0 e^{\lambda t}$, and $K = \partial \varphi / \partial \lambda = t x_0 e^{\lambda t}$ indeed solves $K' = \lambda K + x_0 e^{\lambda t}$ with $K(0) = 0$.
If $f$ is only Lipschitz in $x$, the solution depends [[continuously|0G3DBXRRQJ]] on the data but need not be differentiable.
For $x' = \abs{x}$, the map $x_0 \mapsto \varphi(1; 0, x_0)$ is $e x_0$ for $x_0 \ge 0$ and $e^{-1} x_0$ for $x_0 < 0$, not differentiable at $0$.
If $f$ is of class $C^r$, then $\varphi$ is of class $C^r$.

## Explanations

### L1 human

If the equation and its parameters change a little, the solution changes a little, and in a smooth way.
The theorem also tells how fast the solution reacts: the rates of change solve a linear equation along the solution.
This is how one measures the sensitivity of a model to its inputs.

### L2 human

The variational equation is the linearization of the system along a given solution.
It is the basic tool for stability of periodic orbits, for Lyapunov exponents and for perturbation methods.
The result also shows that the flow of a $C^1$ vector field is a $C^1$ map, with derivative a [[fundamental matrix|0MQ24RBG93]] of the variational equation.
