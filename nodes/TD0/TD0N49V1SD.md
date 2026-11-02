---
tag: TD0N49V1SD
kind: definition
name: Projection method for integral equations
msc: [45L05, 65R20, 47A58]
defines: 2AFNVJ54G7
uses: [06GZ956657, 033DA1WE8Y, 8KJCN49V64, M2NEP1K5AE]
sources:
  - url: https://en.wikipedia.org/wiki/Galerkin_method
---

## Definition

Let $X$ be a [[Banach space|06GZ956657]], let $K \colon X \to X$ be a bounded linear operator, typically a compact integral operator, and let $f \in X$.
Consider the [[equation of the second kind|8KJCN49V64]] $\varphi - K\varphi = f$.
Let $X_1, X_2, \ldots$ be finite-dimensional subspaces of $X$.
For each $n$ let $P_n \colon X \to X$ be a bounded linear [[projection|033DA1WE8Y]] with image $X_n$, that is $P_n^2 = P_n$ and $P_n(X) = X_n$.
The *projection method* defined by $(X_n, P_n)$ approximates $\varphi$ by the solution $\varphi_n \in X_n$ of
$$\varphi_n - P_n K \varphi_n = P_n f.$$
If $u_1, \ldots, u_N$ is a basis of $X_n$ and $\varphi_n = \sum_j c_j u_j$, this equation is a system of $N$ linear equations for $c_1, \ldots, c_N$.

## Remarks

Two choices of $P_n$ are standard.
In the *collocation method*, $X_n \subseteq C[a, b]$ and $P_n$ is interpolation at points $x_1, \ldots, x_N$, so the equation is required to hold at these points.
In the *Galerkin method*, $X$ is a Hilbert space and $P_n$ is the [[orthogonal projection|0B8KZRT28M]] onto $X_n$.
So the residual is required to be orthogonal to $X_n$; see the [[Galerkin method|Y5B0PEBKE8]].

Example: $X = L^2(0, 1)$, $(K\varphi)(x) = \int_0^1 x t \, \varphi(t) \, dt$, $f(x) = x$, and $X_1$ spanned by $u_1(x) = x$ with $P_1$ orthogonal.
With $\varphi_1 = c x$, one has $K\varphi_1 = \frac{c}{3} x$, so the equation is $c - \frac{c}{3} = 1$ and $c = \frac32$.
Since $K$ maps into $X_1$ and $f \in X_1$, this is the exact solution: $\frac32 x - \frac{x}{3} \cdot \frac32 = x$.

Non-example: the Nyström method replaces the integral in $K$ by a quadrature rule and solves for the values of the unknown at the nodes.
It approximates the operator $K$ instead of projecting the unknown onto a fixed subspace, so it is not a projection method in this sense.
Its analysis uses [[collectively compact operator approximation|AEZE6B2XXY]].

The convergence of projection methods for second-kind equations is described by the [[convergence theorem for second-kind equations|H6KS0E9MF5]].
