---
tag: A0F09CMEJM
kind: definition
name: Poisson's equation
msc: [35J05, 31B35]
defines: DWK5N5SKTK
uses: [0E0B6RA8K0, S8RG6N1PRT, 02BH3MCBQB, 0DEB0JMN0W, BSJ8X2XRN9]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson%27s_equation
---

## Definition

Let $U \subseteq \R^n$ be an [[open set|02BH3MCBQB]] and let $f \colon U \to \R$ be a given function.
*Poisson's equation* on $U$ with right-hand side $f$ is the equation
$$\Delta u = f$$
for an unknown function $u \colon U \to \R$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
A *classical solution* is a twice continuously differentiable function $u$ on $U$ with $\Delta u(x) = f(x)$ for every $x \in U$.

## Remarks

Example: on $U = \R^n$ with $f = 1$, the function $u(x) = \abs{x}^2 / (2n)$ is a classical solution, since each term $\partial_i^2 (x_i^2 / (2n))$ equals $1/n$.
Non-example: $u(x) = \abs{x}^2 / 2$ on $\R^2$ is not a solution for $f = 1$, since $\Delta u = 2$.
With $f = 0$ the equation is [[Laplace's equation|S8RG6N1PRT]].
If $u_1$ and $u_2$ solve the same Poisson equation, then $u_1 - u_2$ is [[harmonic|0DEB0JMN0W]].
Many texts write the equation as $-\Delta u = f$, the sign that makes the operator positive.
If $f$ is twice continuously differentiable with compact support in $\R^n$, $n \ge 2$, then $u = \Phi * f$ solves $-\Delta u = f$ on $\R^n$, where $\Phi$ is the [[fundamental solution of the Laplacian|BSJ8X2XRN9]].
Weak and distributional solutions are defined for less regular $f$.
