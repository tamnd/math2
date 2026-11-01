---
tag: 6HVAGKSQWB
kind: definition
name: Bump function
msc: ["26E10", 46F05]
defines: HS65DW0HXH
uses: [0BE3QDH73A, 00R0X1WGPX, 09RTYYHXKA, 0JD5ZNW0F4]
sources:
  - url: https://en.wikipedia.org/wiki/Bump_function
---

## Definition

Let $n \ge 1$.
A *bump function* on $\R^n$ is a function $\varphi \colon \R^n \to \R$ such that:

1. $\varphi$ is [[smooth|0BE3QDH73A]], that is, of class $C^\infty$;
2. the support $\overline{\set{x \in \R^n : \varphi(x) \ne 0}}$ of $\varphi$ is [[compact|00R0X1WGPX]].

The set of bump functions on $\R^n$ is often written $C_c^\infty(\R^n)$.

## Remarks

Example: let $\psi(x) = e^{-1/(1 - x^2)}$ for $\abs{x} < 1$ and $\psi(x) = 0$ for $\abs{x} \ge 1$.
Let $g(t) = e^{-1/t}$ for $t > 0$ and $g(t) = 0$ for $t \le 0$, which is [[smooth|09RTYYHXKA]].
Then $\psi(x) = g(1 - x^2)$ is a composition of smooth functions, so it is smooth.
Its support is $[-1, 1]$, which is compact.

Non-example: the Gaussian $e^{-x^2}$ is smooth, but it is nonzero at every point, so its support $\R$ is not compact.
The tent function $\max(0, 1 - \abs{x})$ has compact support $[-1, 1]$, but it is not differentiable at $0$ and $\pm 1$.

A bump function that is not identically zero is not [[analytic|0JD5ZNW0F4]] on $\R^n$, since an analytic function that vanishes on a nonempty open set of $\R^n$ is zero.
For each compact set $K$ and open set $U \supseteq K$ in $\R^n$, some bump function equals $1$ on $K$, takes values in $[0, 1]$, and has support in $U$.
