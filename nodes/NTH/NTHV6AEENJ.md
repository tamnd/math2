---
tag: NTHV6AEENJ
kind: definition
name: Potential flow
msc: [76B99, 76A02]
defines: 84K7TEWZ2Z
uses: [470A1RJWBP, 0ABK9V9Y64, S8RG6N1PRT, 2JZ0C15A9C, 0NF6GQNXMY]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_flow
---

## Definition

Let $\Omega \subseteq \R^n$ be an open set, with $n = 2$ or $n = 3$.
Let $u$ be the velocity field of a flow in $\Omega$, depending on time $t$ in an interval $I$.
The flow is a *potential flow* if some function $\varphi \colon \Omega \times I \to \R$, differentiable in $x$, satisfies the following at every point and time.
$$u = \nabla \varphi$$
Here $\nabla$ is the [[gradient|0ABK9V9Y64]] in $x$.
The function $\varphi$ is the [[velocity potential|470A1RJWBP]].

## Remarks

A potential flow with $\varphi$ of class $C^2$ is irrotational, since the [[curl|0NF6GQNXMY]] of a gradient is $0$.
If it is also [[incompressible|2JZ0C15A9C]], then $\nabla \cdot u = \Delta \varphi = 0$, so $\varphi$ solves [[Laplace's equation|S8RG6N1PRT]] at each time.

Example: on $\Omega = \R^2$, $\varphi(x, y) = (x^2 - y^2)/2$ gives $u = (x, -y)$, the flow near a stagnation point.
It is incompressible, and indeed $\Delta \varphi = 1 - 1 = 0$.

Non-example: the rigid rotation $u = (-y, x)$ has curl $2 \ne 0$, so it is not the gradient of any function.

On a simply connected domain, a $C^1$ irrotational flow is a potential flow.
On other domains this can fail.
The point vortex $u = (-y, x)/(x^2 + y^2)$ on $\R^2 \setminus \set{0}$ is irrotational.
But its circulation around the unit circle is $2\pi \ne 0$, so it has no single-valued potential (see [[a curl-free field that is not conservative|0GRM3BS0DD]]).
