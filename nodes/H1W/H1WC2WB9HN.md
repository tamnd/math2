---
tag: H1WC2WB9HN
kind: definition
name: Lagrangian duality
msc: [90C46, 49N15]
defines: QRXXH28W3A
uses: [NS0Q42Y3FX, 0QF1MZ9FRG, 0GCM7B6PBK]
sources:
  - url: https://en.wikipedia.org/wiki/Duality_(optimization)
---

## Definition

Let $D \subseteq \R^n$ be a nonempty set and let $f_0, f_1, \dots, f_m, h_1, \dots, h_p \colon D \to \R$ be functions.
The *primal problem* is the [[optimization problem|NS0Q42Y3FX]]
$$\text{minimize } f_0(x) \quad \text{subject to } x \in D,\ f_i(x) \le 0 \ (1 \le i \le m),\ h_j(x) = 0 \ (1 \le j \le p).$$
Its optimal value $p^*$ is the [[infimum|0QF1MZ9FRG]] of $f_0$ over the feasible points, with $p^* = +\infty$ if there are none.
The *Lagrangian* is $L \colon D \times \R^m \times \R^p \to \R$,
$$L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x).$$
The *dual function* is $g(\lambda, \nu) = \inf_{x \in D} L(x, \lambda, \nu)$, with values in $[-\infty, \infty)$.
The *Lagrange dual problem* is
$$\text{maximize } g(\lambda, \nu) \quad \text{subject to } \lambda \in [0, \infty)^m,\ \nu \in \R^p,$$
and its optimal value is $d^* = \sup\set{g(\lambda, \nu) : \lambda \ge 0,\ \nu \in \R^p}$.

## Remarks

The dual function is [[concave|0GCM7B6PBK]], as an infimum of affine functions of $(\lambda, \nu)$, so the dual is always a convex problem.
Weak duality: if $x$ is feasible and $\lambda \ge 0$, then $g(\lambda, \nu) \le L(x, \lambda, \nu) \le f_0(x)$, so $d^* \le p^*$.
The difference $p^* - d^*$ is the [[duality gap|AXBPKPSENT]].
For linear programs the Lagrange dual is the [[dual linear program|14VMJNXMDC]].

Example: $D = \R$, $f_0(x) = x^2$, $f_1(x) = 1 - x$.
Then $L(x, \lambda) = x^2 + \lambda (1 - x)$ is minimized at $x = \lambda / 2$, so $g(\lambda) = \lambda - \lambda^2 / 4$.
The dual optimum is $g(2) = 1$, which equals $p^* = 1$.

Non-example: a pair with $\lambda_1 < 0$ is not dual feasible.
For it, $\lambda_1 f_1(x)$ can be positive at a feasible $x$, and the bound $g(\lambda, \nu) \le p^*$ fails in general.
In the example, $g(-1) = -5/4$ happens to be below $p^*$, but the bound $L(x, \lambda) \le f_0(x)$ fails at $x = 2$.
