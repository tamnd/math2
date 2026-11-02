---
tag: H6KS0E9MF5
kind: statement
role: theorem
name: Convergence of approximations for second-kind equations
msc: [45L05, 65R20, 47A58]
uses: [06GZ956657, M2NEP1K5AE, 2AFNVJ54G7, 8KJCN49V64, KHJ2G2R5G7]
about: [2AFNVJ54G7, 8KJCN49V64]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_integral_equation
---

## Statement

Let $X$ be a [[Banach space|06GZ956657]], let $K \colon X \to X$ be a [[compact operator|M2NEP1K5AE]] such that $I - K$ is injective, and let $f \in X$.
Let $\varphi \in X$ be the solution of $\varphi - K\varphi = f$.
Let $P_n \colon X \to X$ be bounded linear projections onto finite-dimensional subspaces $X_n$ such that $P_n \psi \to \psi$ for every $\psi \in X$.
Then there is $n_0$ such that for every $n \ge n_0$ the [[projection method|2AFNVJ54G7]] equation $\varphi_n - P_n K \varphi_n = P_n f$ has a unique solution $\varphi_n \in X$, which lies in $X_n$.
Moreover there is a constant $M$, independent of $n$ and $f$, such that
$$\norm{\varphi_n - \varphi} \le M \norm{P_n \varphi - \varphi} \quad \text{for all } n \ge n_0,$$
and in particular $\varphi_n \to \varphi$.

## Remarks

The solution $\varphi$ exists because, for compact $K$, injectivity of $I - K$ implies that $I - K$ is invertible with bounded inverse (Riesz theory, the [[Fredholm alternative|4HH8C9V8JQ]]).
Since $P_n \psi \to \psi$ for each $\psi$, the norms $\norm{P_n}$ are bounded by the [[uniform boundedness principle|YG0042V8CJ]], so the convergence is uniform on compact sets.
The set $\set{K\psi : \norm{\psi} \le 1}$ is relatively compact, hence $\norm{P_n K - K} \to 0$.
A perturbation argument then shows that $I - P_n K$ is invertible for large $n$, with $\norm{(I - P_n K)^{-1}} \le M$.
Finally $(I - P_n K)(\varphi_n - \varphi) = P_n \varphi - \varphi$, which gives the error bound; and if $\varphi_n - P_nK\varphi_n = P_n f$ then $\varphi_n = P_n(f + K\varphi_n) \in X_n$.

Example: for a continuous kernel on $[a, b]$, collocation with piecewise linear interpolation on grids with mesh tending to $0$ satisfies the hypothesis in $C[a, b]$, since $P_n \psi \to \psi$ uniformly for continuous $\psi$.
The error is then of the order of the interpolation error of the exact solution, for instance $O(h^2)$ for a twice continuously differentiable $\varphi$ and mesh size $h$.

The hypothesis of pointwise convergence $P_n \psi \to \psi$ is needed.
For collocation with polynomial interpolation at equidistant points in $C[a, b]$ it fails, since the norms of the interpolation operators grow without bound, and the theorem gives nothing.

## Explanations

### L1 human

The theorem says that for equations of the form "unknown minus a smoothing integral equals data", projection methods work as soon as the projections themselves approximate every function well.
The error of the computed solution is then at most a fixed multiple of the best error that the projections can achieve on the exact solution.
So the quality of the method is reduced to a question of approximation theory.

### L2 human

The key step is that a compact operator turns pointwise convergence of $P_n$ into norm convergence of $P_n K$.
This is why second-kind equations with compact $K$ are so well suited to numerical methods, in contrast to first-kind equations, which are ill-posed.
In a Hilbert space with orthogonal projections, this gives the convergence of the Galerkin method for second-kind equations.
For the Nyström method, $K$ is replaced by quadrature operators $K_n$ that do not converge in norm, and the same conclusion needs [[collectively compact operator approximation|AEZE6B2XXY]].
