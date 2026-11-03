---
tag: 3SHK1KPXZD
kind: definition
name: Augmented Lagrangian method
msc: [90C30, 49M29, 65K05]
defines: AX0NJ6NK81
uses: [0VKKP8X6Q6, AY9Q1VNDJB]
sources:
  - url: https://en.wikipedia.org/wiki/Augmented_Lagrangian_method
---

## Definition

Let $f, h_1, \dots, h_l \colon \R^n \to \R$ be continuously differentiable, and write $h = (h_1, \dots, h_l)$.
Consider the problem of minimizing $f(x)$ subject to $h(x) = 0$.
For $\lambda \in \R^l$ and $\mu > 0$, the *augmented Lagrangian* is
$$L_\mu(x, \lambda) = f(x) + \lambda^T h(x) + \frac{\mu}{2} \norm{h(x)}^2.$$
The *augmented Lagrangian method* starts from $\lambda_0 \in \R^l$ and $\mu_0 > 0$, and for $k \ge 0$:

1. computes an approximate minimizer $x_{k+1}$ of $L_{\mu_k}(\cdot, \lambda_k)$ over $\R^n$;
2. updates the multiplier estimate by $\lambda_{k+1} = \lambda_k + \mu_k h(x_{k+1})$;
3. chooses $\mu_{k+1} \ge \mu_k$.

## Remarks

The update in clause 2 comes from comparing the first-order conditions: $\nabla_x L_{\mu_k}(x_{k+1}, \lambda_k) = \nabla f(x_{k+1}) + \sum_j \left(\lambda_{k,j} + \mu_k h_j(x_{k+1})\right) \nabla h_j(x_{k+1})$.
So $\lambda_k + \mu_k h(x_{k+1})$ plays the role of the [[Lagrange multiplier|0VKKP8X6Q6]].
Inequality constraints $g_i(x) \le 0$ are handled with slack variables or with a shifted max term.

Example: minimize $f(x) = x$ subject to $h(x) = x - 1 = 0$, with $\mu_k = \mu$ fixed and $\lambda_0 = 0$.
Minimizing $x + \lambda(x - 1) + \frac{\mu}{2}(x - 1)^2$ gives $x = 1 - (1 + \lambda)/\mu$.
So $x_1 = 1 - 1/\mu$ and $\lambda_1 = 0 + \mu(x_1 - 1) = -1$.
Then $x_2 = 1$, which is the exact solution, and $\lambda = -1$ is its Lagrange multiplier.

Non-example: keeping $\lambda_k = 0$ for all $k$ fails clause 2, and the method becomes the quadratic [[penalty method|AY9Q1VNDJB]].
In the example it then gives $1 - 1/\mu_k$, which is never feasible.
