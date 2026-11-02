---
tag: KQWJ8SGJEZ
kind: definition
name: Tangential Cauchy–Riemann equations
msc: [32V05, 32V10, 35N10]
defines: X7GP9BECD8
uses: [VKFW27WXEZ, WY6K3P4YCG, 9PT772R94A]
sources:
  - url: https://en.wikipedia.org/wiki/CR_manifold
---

## Definition

Let $M$ be a smooth real [[submanifold|VKFW27WXEZ]] of $\C^n$.
For $p \in M$, let $T^{0,1}_p M = (T_p M \otimes \C) \cap T^{0,1}_p \C^n$, where $T_p M$ is the [[tangent space|WY6K3P4YCG]] and $T^{0,1}_p \C^n$ is spanned by $\partial / \partial \bar z_1, \dots, \partial / \partial \bar z_n$.
A function $f \colon M \to \C$ of class $C^1$ satisfies the *tangential Cauchy–Riemann equations* if $X f = 0$ for every $p \in M$ and every $X \in T^{0,1}_p M$.

## Remarks

These are the [[Cauchy–Riemann equations|9PT772R94A]] restricted to the directions in which a function on $M$ can be differentiated.
When $T^{0,1} M$ has constant rank, it is the conjugate of a CR structure on $M$, and the solutions are the [[CR functions|JFKYYK2CEB]]; one writes the equations as $\bar\partial_b f = 0$.

For a hypersurface $M = \set{\rho = 0}$, with $\rho$ real and $d\rho \ne 0$ on $M$, the space $T^{0,1}_p M$ is spanned by the operators
$$L_{jk} = \frac{\partial \rho}{\partial \bar z_j} \frac{\partial}{\partial \bar z_k} - \frac{\partial \rho}{\partial \bar z_k} \frac{\partial}{\partial \bar z_j}, \quad 1 \le j < k \le n,$$
so the equations are $L_{jk} f = 0$.
Each $L_{jk}$ is tangent to $M$ because $L_{jk} \rho = 0$.

Example: on $S^3 \subset \C^2$, with $\rho = \abs{z_1}^2 + \abs{z_2}^2 - 1$, there is one equation $L_{12} f = 0$ with $L_{12} = z_1 \, \partial / \partial \bar z_2 - z_2 \, \partial / \partial \bar z_1$.
The function $f = z_1 z_2$ is a solution, since it does not depend on $\bar z_1, \bar z_2$.

Non-example: $f = \abs{z_1}^2$ on $S^3$.
Then $L_{12} f = -z_2 z_1$, which is nonzero at points where $z_1 z_2 \ne 0$, so $f$ does not satisfy the equations.

For a real curve $M$ in $\C$, $T^{0,1} M = 0$, so every function satisfies the tangential equations.
