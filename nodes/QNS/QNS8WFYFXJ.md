---
tag: QNS8WFYFXJ
kind: definition
name: Cauchy–Riemann equations in several variables
msc: [32W05, 32A10]
defines: 9PT772R94A
uses: [507C34W0ZT, 09EGC6F8PT, WMXDVF36ZT, 0T71SSYZ39]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations
---

## Definition

Let $D \subseteq \C^n$ be an open set, write $z_j = x_j + i y_j$ with $x_j, y_j$ real, and let $f = u + iv \colon D \to \C$ with $u, v$ real-valued.
Suppose that all first [[partial derivatives|09EGC6F8PT]] of $u$ and $v$ exist on $D$.
The function $f$ satisfies the *Cauchy–Riemann equations* on $D$ if for every $j = 1, \dots, n$, at every point of $D$,
$$\frac{\partial u}{\partial x_j} = \frac{\partial v}{\partial y_j}, \qquad \frac{\partial u}{\partial y_j} = -\frac{\partial v}{\partial x_j}.$$

## Remarks

With the [[Wirtinger derivatives|WMXDVF36ZT]] $\frac{\partial}{\partial \bar z_j} = \frac12 \left( \frac{\partial}{\partial x_j} + i \frac{\partial}{\partial y_j} \right)$, the $2n$ real equations are the $n$ complex equations $\partial f / \partial \bar z_j = 0$, $j = 1, \dots, n$.
For $n = 1$ they are the classical [[Cauchy–Riemann equations|0T71SSYZ39]].
A function $f$ of class $C^1$ on $D$ is [[holomorphic|507C34W0ZT]] if and only if it satisfies the Cauchy–Riemann equations on $D$.
Example: $f(z_1, z_2) = z_1 z_2$ satisfies them, since $\partial f / \partial \bar z_1 = 0$ and $\partial f / \partial \bar z_2 = 0$.
Non-example: $f(z_1, z_2) = z_1 \bar z_2$ satisfies the pair for $j = 1$ but not the pair for $j = 2$, since $\partial f / \partial \bar z_2 = z_1$, which is not zero when $z_1 \ne 0$.
