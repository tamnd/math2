---
tag: D8H0MJCS63
kind: definition
name: Boundary integral method for the Dirichlet problem
msc: [31B10, 31A10, 45B05]
defines: QQ62R5ZAXJ
uses: [8D56GQ4AG8, EG8Z3FWV9A, J58YA8QNNX, M2NEP1K5AE, 4HH8C9V8JQ, 05D5EGMFYV]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_element_method
---

## Definition

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded open set whose [[boundary|05D5EGMFYV]] $\partial\Omega$ is a $C^2$ hypersurface.
Let $f \colon \partial\Omega \to \R$ be continuous, and consider the interior [[Dirichlet problem|8D56GQ4AG8]] with data $f$.
For a continuous density $\varphi$ on $\partial\Omega$, let $D\varphi$ be its [[double layer potential|EG8Z3FWV9A]], and let $K\varphi(x) = \int_{\partial\Omega} \frac{\partial \Phi(x - y)}{\partial \nu(y)} \varphi(y)\, d\sigma(y)$ for $x \in \partial\Omega$, as in the [[jump relations|J58YA8QNNX]].
Here $\Phi$ is the fundamental solution of the Laplacian with $-\Delta\Phi = \delta_0$, $\sigma$ is surface measure on $\partial\Omega$ and $\nu$ is the outward unit normal.
The *boundary integral method* (double layer method) for this problem consists of the following steps.

1. Seek the solution in the form $u = D\varphi$ on $\Omega$, with $\varphi$ unknown.
2. Solve the boundary integral equation
$$-\tfrac12 \varphi(x) + K\varphi(x) = f(x), \qquad x \in \partial\Omega,$$
for a continuous $\varphi$.
3. Take $u = D\varphi$ on $\Omega$ and $u = f$ on $\partial\Omega$.

## Remarks

By the jump relations, the interior boundary values of $D\varphi$ are $K\varphi - \tfrac12\varphi$, so step 2 is exactly the condition that $u$ is continuous on $\overline{\Omega}$ with $u = f$ on $\partial\Omega$.
Since $\partial\Omega$ is $C^2$, the kernel of $K$ is weakly singular and $K$ is a [[compact operator|M2NEP1K5AE]] on $C(\partial\Omega)$.
So the equation is a Fredholm equation of the second kind.
By the [[Fredholm alternative|4HH8C9V8JQ]], it is solvable for every $f$ once the homogeneous equation has only the solution $\varphi = 0$.
This holds when $\R^n \setminus \overline{\Omega}$ is connected.

Example: let $\Omega$ be the unit ball in $\R^3$ and $f \equiv 1$.
Gauss's integral gives $K1 = -\tfrac12$ on the sphere, so $\varphi \equiv -1$ solves $-\tfrac12\varphi + K\varphi = \tfrac12 + \tfrac12 = 1$.
Then $u = D(-1) = 1$ in the ball, the correct solution.

Non-example: let $\Omega$ be the shell $\set{x \in \R^3 : 1 < \abs{x} < 2}$, whose complement has the bounded component $\set{\abs{x} \le 1}$.
Let $\varphi = 1$ on the inner sphere and $\varphi = 0$ on the outer sphere.
The outward normal of $\Omega$ on the inner sphere points toward the origin, so $D\varphi = 1$ in the inner ball and $D\varphi = 0$ outside it, in particular on $\Omega$.
Thus $\varphi \ne 0$ solves the homogeneous equation, and the equation of step 2 is not uniquely solvable.
