---
tag: VNS9QQATH1
kind: statement
role: theorem
name: Nyström method
msc: [65R20, 45B05]
uses: [526TCVMSHP, 8KJCN49V64, ADSVMCY77A, 0X3WGX95FE, 4HH8C9V8JQ, YG0042V8CJ]
about: [526TCVMSHP]
sources:
  - url: https://en.wikipedia.org/wiki/Nyström_method
same_as:
  wikidata: Q7071295
  wikipedia: Nyström method
---

## Statement

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \R$ and $f \colon [a, b] \to \R$ be [[continuous|0X3WGX95FE]], and consider the [[Fredholm integral equation of the second kind|526TCVMSHP]]
$$u(x) - \int_a^b K(x, y)\, u(y)\, dy = f(x), \qquad x \in [a, b].$$
Assume that its homogeneous version, with $f = 0$, has only the solution $u = 0$ in $C[a, b]$.
For each $n \ge 1$ let $Q_n(g) = \sum_{j=1}^{n} w_{j}^{(n)} g(x_{j}^{(n)})$ be a [[quadrature rule|ADSVMCY77A]] with nodes $x_j^{(n)} \in [a, b]$, such that $Q_n(g) \to \int_a^b g(y)\, dy$ for every $g \in C[a, b]$.
The *Nyström method* solves the linear system
$$u_i^{(n)} - \sum_{j=1}^{n} w_j^{(n)} K(x_i^{(n)}, x_j^{(n)})\, u_j^{(n)} = f(x_i^{(n)}), \qquad i = 1, \ldots, n,$$
and sets $u_n(x) = f(x) + \sum_{j=1}^{n} w_j^{(n)} K(x, x_j^{(n)})\, u_j^{(n)}$.
Then:

1. the integral equation has a unique solution $u \in C[a, b]$;
2. there is $n_0$ such that for $n \ge n_0$ the linear system has a unique solution;
3. there is a constant $C$ such that for $n \ge n_0$
$$\max_{x \in [a,b]} \abs{u_n(x) - u(x)} \le C \max_{x \in [a, b]} \Bigl| \int_a^b K(x, y) u(y)\, dy - \sum_{j=1}^{n} w_j^{(n)} K(x, x_j^{(n)}) u(x_j^{(n)}) \Bigr|,$$
and the right side tends to $0$ as $n \to \infty$.

## Remarks

Clause 1 is the [[Fredholm alternative|4HH8C9V8JQ]] for the compact integral operator $(\mathcal K u)(x) = \int_a^b K(x, y) u(y)\, dy$ on $C[a, b]$.
Write $(\mathcal K_n u)(x) = \sum_j w_j^{(n)} K(x, x_j^{(n)}) u(x_j^{(n)})$; the values $u_n(x_i^{(n)})$ equal $u_i^{(n)}$, and $u_n$ solves $u_n - \mathcal K_n u_n = f$.
By the [[uniform boundedness principle|YG0042V8CJ]] the sums $\sum_j \abs{w_j^{(n)}}$ are bounded, so $\mathcal K_n \to \mathcal K$ pointwise and the family $(\mathcal K_n)$ is collectively compact.
Anselone's theory of collectively compact operators then shows that $I - \mathcal K_n$ is invertible for large $n$ with uniformly bounded inverses, and $u_n - u = (I - \mathcal K_n)^{-1}(\mathcal K_n - \mathcal K) u$ gives clause 3.
So the error is of the order of the quadrature error on the smooth functions $y \mapsto K(x, y) u(y)$: with Gauss–Legendre nodes and smooth $K$ and $f$ it decays very fast.
The formula for $u_n$ is the Nyström interpolation; it extends the nodal values to all of $[a, b]$ with the accuracy of the nodal values.
Without unique solvability of the homogeneous equation the method has no limit to converge to: for $K = 1$ on $[0, 1]$ and $f = 0$ every constant solves the equation.

## Explanations

### L1 human

An integral equation asks for an unknown function that appears inside an integral.
The Nyström method replaces the integral by a quadrature rule, a weighted sum of values at a few nodes.
The equation, written at those same nodes, becomes an ordinary linear system for the values of the unknown there.
Suppose the original equation is uniquely solvable and the quadrature rule converges.
Then the theorem says that the discrete solutions converge to the true one, as fast as the quadrature rule does.

### L2 human

The Nyström method is the simplest and often the most accurate way to solve second-kind Fredholm equations with smooth kernels.
Its error analysis goes through the operator $\mathcal K_n$, which is not norm-convergent to $\mathcal K$ but is collectively compact, which is enough.
It contrasts with projection methods such as collocation and Galerkin methods, which approximate $u$ in a finite-dimensional subspace.
For weakly singular kernels one uses product integration rules, where the singular factor is integrated exactly.
Equations of the first kind are ill-posed and need regularization, so this theorem does not cover them.
