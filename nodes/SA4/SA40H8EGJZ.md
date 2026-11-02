---
tag: SA40H8EGJZ
kind: definition
name: Weak solution
msc: [35D30]
defines: SJZX81A783
uses: [GC5BDZ6QBC, C3EC148VZD]
sources:
  - url: https://en.wikipedia.org/wiki/Weak_solution
---

## Definition

Let $U \subseteq \R^n$ be open, let $m \ge 1$, and let
$$P = \sum_{\abs{\alpha} \le m} a_\alpha(x) \, \partial^\alpha$$
be a linear differential operator on $U$ with coefficients $a_\alpha \in C^\infty(U)$, where $\alpha$ runs over multi-indices.
Its formal transpose is the operator $P^t \varphi = \sum_{\abs{\alpha} \le m} (-1)^{\abs{\alpha}} \partial^\alpha (a_\alpha \varphi)$.
Let $f$ be a locally integrable function on $U$.
A locally integrable function $u$ on $U$ is a *weak solution* of $P u = f$ if
$$\int_U u \, P^t \varphi \, dx = \int_U f \, \varphi \, dx \quad \text{for all } \varphi \in C_c^\infty(U),$$
where $C_c^\infty(U)$ is the space of test functions on $U$.

## Remarks

The identity is what integration by parts gives when $u$ is of class $C^m$ and $P u = f$ holds pointwise.
So every classical solution is a weak solution.
Conversely, a weak solution of class $C^m$ satisfies $P u = f$ almost everywhere, and everywhere if $f$ is continuous.
If $u$ has [[weak derivatives|C3EC148VZD]] up to order $m$, the condition says that $\sum a_\alpha D^\alpha u = f$ almost everywhere.

Example: on $\R^2$ with variables $(x, t)$, let $u(x, t) = 1$ for $x > t$ and $u(x, t) = 0$ for $x \le t$, and let $P = \partial_t + \partial_x$, so $P^t \varphi = -(\varphi_t + \varphi_x)$.
Put $\psi(y, t) = \varphi(y + t, t)$; then $\partial_t \psi = \varphi_x + \varphi_t$ at the point $(y + t, t)$.
Hence $\int\!\!\int u \, (\varphi_t + \varphi_x) \, dx \, dt = \int_0^\infty \int_{\R} \partial_t \psi(y, t) \, dt \, dy = 0$, because $\psi(y, \cdot)$ has compact support.
So $u$ is a weak solution of $u_t + u_x = 0$, though it is discontinuous.

Non-example: the step $w(x, t) = 1$ for $x > 0$ and $0$ for $x \le 0$ is not a weak solution of the same equation.
Here $\int\!\!\int w \, (\varphi_t + \varphi_x) \, dx \, dt = -\int_{\R} \varphi(0, t) \, dt$, which is not zero for a test function with $\varphi(0, t) > 0$ near some $t$.

For second-order equations in divergence form, such as $-\sum_{i,j} \partial_j (a_{ij} \partial_i u) = f$ with bounded coefficients, one often asks instead that $u$ lie in a Sobolev space $H^1_0(U)$ and that $\int_U \sum_{i,j} a_{ij} \, \partial_i u \, \partial_j v \, dx = \int_U f v \, dx$ for all $v \in H^1_0(U)$.
This is the variational form of the definition.
