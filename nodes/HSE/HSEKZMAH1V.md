---
tag: HSEKZMAH1V
kind: statement
role: theorem
name: Schauder estimates
msc: [35J15, 35B45, 35B65]
uses: [XY8GEQSWPR, P101AX1ZSC, 012PBA0FMD]
about: [XY8GEQSWPR, P101AX1ZSC]
sources:
  - url: https://en.wikipedia.org/wiki/Schauder_estimates
same_as:
  wikidata: Q7430990
  wikipedia: Schauder estimates
---

## Statement

Let $n \ge 1$, let $0 < \alpha < 1$, and let $U \subseteq \R^n$ be a bounded open set.
Let
$$L u = \sum_{i,j=1}^{n} a_{ij}(x) \, \partial_i \partial_j u + \sum_{i=1}^{n} b_i(x) \, \partial_i u + c(x) \, u,$$
where $a_{ij} = a_{ji}$, $b_i$ and $c$ are functions on $U$.
Let $\lambda > 0$ and $\Lambda$ be constants with $\sum_{i,j} a_{ij}(x) \xi_i \xi_j \ge \lambda \abs{\xi}^2$ for all $x \in U$ and $\xi \in \R^n$.
Assume that every coefficient has $C^{0,\alpha}(\overline{U})$ norm at most $\Lambda$.
Here $C^{k,\alpha}$ denotes the [[Hölder space|P101AX1ZSC]] of functions whose derivatives up to order $k$ are bounded and [[Hölder continuous|012PBA0FMD]] with exponent $\alpha$.
Its norm is written $\norm{\cdot}_{C^{k,\alpha}}$.

1. (Interior estimate.) Let $u \in C^{2,\alpha}(U)$ be bounded with $f = L u \in C^{0,\alpha}(\overline{U})$, and let $V$ be an open set whose closure is a compact subset of $U$. Then
$$\norm{u}_{C^{2,\alpha}(\overline{V})} \le C \big( \sup_U \abs{u} + \norm{f}_{C^{0,\alpha}(\overline{U})} \big),$$
where $C$ depends only on $n$, $\alpha$, $\lambda$, $\Lambda$, $U$ and $V$.
2. (Global estimate.) Assume moreover that $U$ has $C^{2,\alpha}$ boundary. Let $u \in C^{2,\alpha}(\overline{U})$, let $f = L u$, and let $\varphi \in C^{2,\alpha}(\overline{U})$ with $u = \varphi$ on $\partial U$. Then
$$\norm{u}_{C^{2,\alpha}(\overline{U})} \le C \big( \sup_U \abs{u} + \norm{\varphi}_{C^{2,\alpha}(\overline{U})} + \norm{f}_{C^{0,\alpha}(\overline{U})} \big),$$
where $C$ depends only on $n$, $\alpha$, $\lambda$, $\Lambda$ and $U$.

## Remarks

Proof idea: first treat the Laplacian, where $u$ is given by convolution of $f$ with the fundamental solution.
Potential estimates show that the second derivatives of the Newtonian potential of a $C^{0,\alpha}$ function are $C^{0,\alpha}$.
A linear change of variables gives the same bound for operators with constant coefficients.
For variable coefficients one freezes them at a point.
On a small ball, $L$ is close to a constant-coefficient operator, and the error is absorbed using the smallness of the Hölder seminorm of the coefficients on small balls.
The global estimate follows by flattening the boundary locally and treating half-balls in the same way.

Example: for $L = \Delta$, the estimate says that a harmonic function is controlled in $C^{2,\alpha}$ on interior sets by its supremum.
It also says that a solution of Poisson's equation $\Delta u = f$ with $f \in C^{0,\alpha}$ has second derivatives in $C^{0,\alpha}$.

The restriction $0 < \alpha < 1$ is needed.
For $\alpha = 0$ the estimate fails: there are continuous $f$ for which $\Delta u = f$ has no solution with continuous second derivatives.
For $\alpha = 1$ it also fails: a Lipschitz $f$ need not give $u$ with Lipschitz second derivatives.

Together with the method of continuity, the global estimate gives existence of $C^{2,\alpha}(\overline{U})$ solutions of the Dirichlet problem for $L$ with $c \le 0$, starting from the case of the Laplacian.

## Explanations

### L1 human

The Schauder estimates say that solutions of elliptic equations are two derivatives smoother than the right-hand side, when smoothness is measured with Hölder norms.
If the data are slightly better than continuous, the second derivatives of the solution are slightly better than continuous too, with a bound on how much.
This is a quantitative form of the idea that elliptic equations smooth things out.

### L2 human

The Schauder estimates are a priori estimates: they bound the $C^{2,\alpha}$ norm of a solution that is already known to exist.
Combined with the maximum principle, which gives uniqueness and bounds $\sup \abs{u}$ when $c \le 0$, they give existence of classical solutions through the method of continuity or the Leray–Schauder theory.
Applied to derivatives of $u$, they give higher regularity: if the coefficients and $f$ are in $C^{k,\alpha}$, then $u$ is in $C^{k+2,\alpha}$ inside $U$.
They are the Hölder counterpart of the $L^p$ theory of Calderón and Zygmund.
They are also a key step in nonlinear problems such as Hilbert's nineteenth problem, once the De Giorgi–Nash–Moser theorem has given Hölder continuity of the coefficients.
