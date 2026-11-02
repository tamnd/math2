---
tag: 2JD72JT9FQ
kind: statement
role: theorem
name: Hopf–Lax formula
msc: [35F21, 35F25, 49L25]
uses: [5TRXQKP7DY, 07Q7CNM5WF, ZQYMWVT1TT, 0AW1E6YTJY]
about: [5TRXQKP7DY]
sources:
  - url: https://en.wikipedia.org/wiki/Hamilton–Jacobi_equation
---

## Statement

Let $H \colon \R^n \to \R$ be a smooth [[convex function|07Q7CNM5WF]] that is superlinear: $H(p)/\abs{p} \to \infty$ as $\abs{p} \to \infty$.
Let $L \colon \R^n \to \R$ be its [[Legendre transform|ZQYMWVT1TT]], $L(q) = \sup_{p \in \R^n} \big(p \cdot q - H(p)\big)$.
Let $g \colon \R^n \to \R$ be [[Lipschitz continuous|0AW1E6YTJY]].
For $x \in \R^n$ and $t > 0$ define
$$u(x, t) = \min_{y \in \R^n} \left( t\, L\!\left(\frac{x - y}{t}\right) + g(y) \right),$$
and set $u(x, 0) = g(x)$.
Then the minimum is attained, and $u$ is Lipschitz continuous on $\R^n \times [0, \infty)$.
Moreover, $u$ is differentiable at almost every point of $\R^n \times (0, \infty)$, and at each such point
$$\partial_t u + H(\nabla u) = 0.$$
So $u$ is a solution almost everywhere of the [[Hamilton–Jacobi equation|5TRXQKP7DY]] with initial value $g$.

## Remarks

The formula comes from the calculus of variations.
The value $u(x, t)$ is the least cost $\int_0^t L(\dot w(s))\, ds + g(w(0))$ over paths $w$ with $w(t) = x$.
By convexity of $L$, Jensen's inequality shows that straight paths are optimal, which gives the minimum over the starting point $y$.
The almost everywhere differentiability comes from the Lipschitz bound and Rademacher's theorem.
The equation itself follows from the semigroup property $u(x, t) = \min_y \big( (t - s) L((x - y)/(t - s)) + u(y, s) \big)$ for $0 \le s < t$.

Example: for $H(p) = \tfrac12 \abs{p}^2$ one has $L(q) = \tfrac12 \abs{q}^2$, and the formula reads $u(x, t) = \min_y \big( \abs{x - y}^2/(2t) + g(y) \big)$.
For $g(y) = \abs{y}$ in dimension $1$ this gives $u(x, t) = \abs{x} - t/2$ for $\abs{x} \ge t$ and $u(x, t) = x^2/(2t)$ for $\abs{x} \le t$.

Solutions almost everywhere are far from unique, so the formula alone does not settle the initial value problem.
Under the hypotheses above the Hopf–Lax function is also a [[viscosity solution|H1ERJ3T75T]], and this is the property that singles it out.

## Explanations

### L1 human

The Hopf–Lax formula writes down a solution of a nonlinear first-order equation with no differential equation solving at all: one only takes a minimum.
To get $u$ at a point $x$ and time $t$, one looks at all starting points $y$.
For each, one adds the start value $g(y)$ to the cost of travelling from $y$ to $x$ in time $t$, and keeps the cheapest.
The solution stays meaningful even after smooth solutions break down and corners appear.

### L2 human

The formula is the starting point of the theory of weak solutions of Hamilton–Jacobi equations in Evans' textbook.
Differentiating it in $x$ in dimension $1$ gives the Lax–Oleinik formula for the entropy solution of a scalar [[conservation law|8RA7AMWSAF]] with convex flux, since $v = \partial_x u$ solves $v_t + H(v)_x = 0$.
For $H(p) = \tfrac12 \abs{p}^2$ the formula is a Moreau envelope of $g$, and it is also the limit as $\nu \to 0$ of the solutions of the viscous equation obtained by the [[Cole–Hopf transformation|VBMQ9SJ3DH]].
