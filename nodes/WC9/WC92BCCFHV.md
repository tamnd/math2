---
tag: WC92BCCFHV
kind: definition
name: Nonlinear difference equation
msc: [39A05, 39A20]
defines: 7C7FBZGERM
uses: [07TZV87Y0T]
sources:
  - url: https://en.wikipedia.org/wiki/Recurrence_relation
---

## Definition

Let $K$ be a field and let $k \ge 1$.
Let $f \colon \N \times K^k \to K$ be a function, and consider the [[recurrence relation|07TZV87Y0T]]
$$u_{n+k} = f(n, u_n, u_{n+1}, \dots, u_{n+k-1}) \qquad (n \in \N).$$
It is *linear* if there are functions $a_0, \dots, a_{k-1}, g \colon \N \to K$ with
$$f(n, y_0, \dots, y_{k-1}) = a_0(n) y_0 + \cdots + a_{k-1}(n) y_{k-1} + g(n)$$
for all $n \in \N$ and all $y_0, \dots, y_{k-1} \in K$.
It is a *nonlinear difference equation* if it is not linear.

## Remarks

Example: the [[logistic map|QN9X9BNKTX]] recurrence $u_{n+1} = r u_n (1 - u_n)$ over $\R$ with $r \ne 0$ is nonlinear.
Indeed, for fixed $n$ an affine function $y \mapsto a y + c$ has constant second difference zero, while $f(y) = r y - r y^2$ gives $f(2) - 2 f(1) + f(0) = -2r \ne 0$.
Non-example: the Fibonacci recurrence $u_{n+2} = u_{n+1} + u_n$ is linear, with $a_0 = a_1 = 1$ and $g = 0$.
The same definitions apply with $K$ replaced by $\R^m$ and $f$ by a map to $\R^m$, which gives nonlinear systems.
An autonomous first-order equation $u_{n+1} = f(u_n)$ is the iteration of the map $f$, so its study belongs to discrete dynamical systems.
