---
tag: XS0Q09SV2T
kind: definition
name: Method of fundamental solutions
msc: [65N80, 65N35]
defines: 6W72QW363B
uses: [K2NK9A8M5F, 0E0B6RA8K0, 8D56GQ4AG8]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_fundamental_solutions
---

## Definition

Let $\Omega \subset \R^d$ be a bounded domain and $L$ a linear elliptic differential operator with constant coefficients.
Let $G$ be a [[fundamental solution|K2NK9A8M5F]] of $L$, so that $L G = \delta$; it is smooth on $\R^d \setminus \set{0}$.
Consider $L u = 0$ in $\Omega$ with the condition $u = g$ on $\partial \Omega$.
The *method of fundamental solutions* has three ingredients:

1. source points $y_1, \ldots, y_n$ in $\R^d \setminus \overline{\Omega}$;
2. the trial function $u_n(x) = \sum_{j=1}^{n} c_j \, G(x - y_j)$, which satisfies $L u_n = 0$ in $\Omega$;
3. boundary points $x_1, \ldots, x_m \in \partial \Omega$, with $m \ge n$.

The coefficients $c_j$ solve $u_n(x_i) = g(x_i)$ for all $i$, exactly if $m = n$ and in the least squares sense if $m > n$.

## Remarks

The sources lie outside $\overline{\Omega}$, so each $G(\cdot - y_j)$ is smooth on $\overline{\Omega}$ and solves the equation there.
The error comes only from the boundary condition.
The sources are often placed on a curve or surface surrounding $\Omega$ at some distance.
The linear system becomes very ill-conditioned as $n$ grows, which limits the accuracy reached in floating point arithmetic.

Example: the [[Dirichlet problem|8D56GQ4AG8]] for the Laplace equation $\Delta u = 0$, with $\Delta$ the [[Laplacian|0E0B6RA8K0]], in the unit disk of $\R^2$.
Take $L = -\Delta$, with fundamental solution $G(x) = -\frac{1}{2\pi} \ln \abs{x}$.
Take sources $y_j = R (\cos \theta_j, \sin \theta_j)$ with $\theta_j = 2\pi j / n$ and $R > 1$.
Take as many boundary points $x_k = (\cos \alpha_k, \sin \alpha_k)$, with $\alpha_k = 2\pi (k - \tfrac12) / n$.
Every $u_n$ is harmonic in the disk, and the $c_j$ are fixed by matching $g$ at the $x_k$.

Non-example: with a source point inside $\Omega$, clause 1 fails.
Then $u_n$ has a logarithmic singularity in $\Omega$ and does not solve the equation there.
