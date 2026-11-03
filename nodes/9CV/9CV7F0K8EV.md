---
tag: 9CV7F0K8EV
kind: definition
name: Frank–Wolfe algorithm
msc: [90C25, 90C30, 65K05]
defines: 8EE3C9Y1NS
uses: [02AS45T3H9, 0R6EWFKRCF, 07GR3TNW4H, 0ABK9V9Y64, YX1DJK2QAG]
sources:
  - url: https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm
---

## Definition

Let $C \subseteq \R^n$ be a nonempty [[compact|0R6EWFKRCF]] [[convex set|02AS45T3H9]], and let $f \colon \R^n \to \R$ be a differentiable [[convex function|07GR3TNW4H]] with [[gradient|0ABK9V9Y64]] $\nabla f$.
Let $x_0 \in C$.
The *Frank–Wolfe algorithm* produces a sequence $(x_k)$ in $C$ by repeating, for $k = 0, 1, 2, \dots$:

1. choose $s_k \in \operatorname*{arg\,min}_{s \in C} \nabla f(x_k)^T s$;
2. set $\gamma_k = 2/(k + 2)$;
3. set $x_{k+1} = x_k + \gamma_k (s_k - x_k)$.

## Remarks

The minimum in step 1 exists because $C$ is compact and $s \mapsto \nabla f(x_k)^T s$ is continuous.
Since $\gamma_k \in (0, 1]$, the point $x_{k+1}$ is a convex combination of $x_k$ and $s_k$, so it lies in $C$.
The step size can also be found by a line search over $[0, 1]$.
If $\nabla f$ is Lipschitz with constant $L$ and $d$ is the diameter of $C$, then $f(x_k) - \min_C f \le 2 L d^2 / (k + 2)$ for $k \ge 1$.
The number $\nabla f(x_k)^T (x_k - s_k)$ is an upper bound for $f(x_k) - \min_C f$, by convexity, and serves as a stopping test.

Example: $C$ the probability [[simplex|YX1DJK2QAG]] $\set{x \in \R^n : x \ge 0, \sum_i x_i = 1}$.
A linear function $c^T s$ is minimised over $C$ at a vertex $e_j$ with $c_j = \min_i c_i$.
So step 1 picks the coordinate with the smallest partial derivative.
If $x_0$ is a vertex, then $x_k$ has at most $k + 1$ nonzero entries.

Non-example: take the unbounded set $C = [0, \infty) \subseteq \R$, $f(x) = (x - 1)^2$ and $x_0 = 2$.
Step 1 minimises $2 s$ over $s \ge 0$, so $s_0 = 0$, and $x_1 = 0$ since $\gamma_0 = 1$.
Now $f'(0) = -2$, and $-2 s$ has no minimum over $s \ge 0$, so step 1 fails; compactness of $C$ is needed for the method to be defined.
