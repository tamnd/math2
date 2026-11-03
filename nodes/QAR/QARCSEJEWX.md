---
tag: QARCSEJEWX
kind: definition
name: Generalized Lotka–Volterra equation
msc: [92D25, 34C60, 92D40]
defines: 4SFBZ8FJF1
uses: [1YEMFQ1H32, 0673D85QKZ, 00Y5QZ82AA, 0N8NGKDZDZ]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_Lotka%E2%80%93Volterra_equation
---

## Definition

Let $n \ge 1$, let $r \in \R^n$, and let $A = (a_{ij})$ be a real $n \times n$ matrix, called the interaction matrix.
The *generalized Lotka–Volterra equation* is the [[autonomous system|0673D85QKZ]]
$$x_i' = x_i \left( r_i + \sum_{j=1}^{n} a_{ij} x_j \right), \qquad i = 1, \ldots, n,$$
for $x = (x_1, \ldots, x_n) \in \R_{\ge 0}^n$, where $x_i$ is the size of population $i$.
In vector form it reads $x' = \operatorname{diag}(x) \, (r + A x)$.

## Remarks

It is a [[population model|1YEMFQ1H32]]: if $x_i = 0$ then $x_i' = 0$, so each face of the orthant is invariant.
Example: with $n = 2$, $r = (\alpha, -\gamma)$ and $A = \begin{pmatrix} 0 & -\beta \\ \delta & 0 \end{pmatrix}$ for positive $\alpha, \beta, \gamma, \delta$, the system is the [[Lotka–Volterra predator–prey equations|00Y5QZ82AA]].
Non-example: $x' = x(1 - x^2)$ is not of this form, because its per capita rate $1 - x^2$ is not affine in $x$.
If $A$ is invertible, the only possible [[equilibrium point|0N8NGKDZDZ]] with all entries positive is $x^* = -A^{-1} r$, and it exists when all entries of $-A^{-1} r$ are positive.
The sign pattern of $a_{ij}$ and $a_{ji}$ describes the interaction: $(-, -)$ competition, $(+, -)$ predation or parasitism, $(+, +)$ mutualism.
