---
tag: DBVE636BXN
kind: definition
name: Mixed finite element method
msc: [65N30, 65N12]
defines: 87VMQ892VW
uses: [HM2HHE3J51, 0SQZMXB6GP, 98GZ9DVHTA, Y5B0PEBKE8, M4CEZ5K9HP, 0MWV6ZTK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Mixed_finite_element_method
---

## Definition

Let $V$ and $Q$ be real [[Hilbert spaces|HM2HHE3J51]] of functions on a bounded polygonal domain $\Omega \subset \R^d$.
Let $a \colon V \times V \to \R$ and $b \colon V \times Q \to \R$ be bounded [[bilinear forms|0SQZMXB6GP]], and let $f \in V'$ and $g \in Q'$.
The *mixed formulation* is the problem: find $(u, p) \in V \times Q$ with
$$a(u, v) + b(v, p) = f(v) \ \text{ for all } v \in V, \qquad b(u, q) = g(q) \ \text{ for all } q \in Q.$$
A *mixed finite element method* for it consists of:

1. a mesh $\mathcal{T}_h$ of $\Omega$;
2. two [[finite element|98GZ9DVHTA]] spaces $V_h \subseteq V$ and $Q_h \subseteq Q$ of piecewise polynomial functions on $\mathcal{T}_h$, chosen separately;
3. the [[Galerkin|Y5B0PEBKE8]] problem: find $(u_h, p_h) \in V_h \times Q_h$ with the two equations above for all $v \in V_h$ and $q \in Q_h$.

## Remarks

Example: the mixed Poisson problem.
For $-\Delta u = s$ with $s \in L^2(\Omega)$ in $\Omega$ with $u = 0$ on $\partial \Omega$, set $\sigma = \nabla u$.
Take $V = H(\operatorname{div}, \Omega)$, the vector fields in $L^2$ whose [[divergence|0MWV6ZTK6S]] is in $L^2$, and $Q = L^2(\Omega)$.
Multiplying $\sigma = \nabla u$ by $\tau \in V$ and integrating by parts with $u = 0$ on the boundary gives $\int_\Omega \sigma \cdot \tau + \int_\Omega u \, \nabla \cdot \tau = 0$, and the equation gives $\int_\Omega (\nabla \cdot \sigma) q = -\int_\Omega s q$.
This has the form above with $a(\sigma, \tau) = \int_\Omega \sigma \cdot \tau$, $b(\tau, q) = \int_\Omega q \, \nabla \cdot \tau$, $f = 0$ and $g(q) = -\int_\Omega s q$.
A stable choice is the lowest-order Raviart–Thomas space for $V_h$ with piecewise constants for $Q_h$.

Non-example: the standard method seeks $u_h$ alone, in continuous piecewise linear functions in the [[Sobolev space|M4CEZ5K9HP]] $H^1_0(\Omega)$.
It has one unknown field and no form $b$, so it is not a mixed method.

The matrix of the discrete problem has the block form $\begin{pmatrix} A & B^T \\ B & 0 \end{pmatrix}$, which is symmetric when $a$ is but never positive definite.
