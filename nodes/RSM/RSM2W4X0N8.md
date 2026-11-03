---
tag: RSM2W4X0N8
kind: statement
role: theorem
name: Appell's equation of motion
msc: [70F25, 70H03, 70G10]
uses: [BCF1EX9W2M, 9WQT2RMGTZ, PTRV0QFSB9, Q8D2JWY8G6, GD776GVZSR, FZWAHMFZM3]
about: [PTRV0QFSB9, 9WQT2RMGTZ]
sources:
  - url: https://en.wikipedia.org/wiki/Appell%27s_equation_of_motion
same_as:
  wikidata: Q1002309
  wikipedia: Appell's equation of motion
---

## Statement

Consider $N$ point particles with masses $m_1, \dots, m_N > 0$, positions $x_k \in \R^3$ and applied forces $F_k$.
Let $q = (q_1, \dots, q_n)$ be [[generalized coordinates|BCF1EX9W2M]] with $x_k = x_k(q, t)$.
Suppose the motion obeys ideal constraints, possibly nonholonomic.
Suppose that, under these constraints, the velocities are exactly those of the form
$$\dot x_k = \sum_{r=1}^m e_{kr}(q, t)\, u_r + e_{k0}(q, t), \qquad k = 1, \dots, N.$$
Here $e_{kr}$ are smooth vector functions, and $u_1, \dots, u_m$ are independent quasi-velocities that take arbitrary real values.
Define the Gibbs–Appell function, or energy of [[acceleration|Q8D2JWY8G6]],
$$S = \frac12 \sum_{k=1}^N m_k \abs{\ddot x_k}^2,$$
written as a function of $q$, $u$, $\dot u$ and $t$, and the [[generalized forces|9WQT2RMGTZ]] $Q_r = \sum_{k} F_k \cdot e_{kr}$.
Then the motion satisfies
$$\frac{\partial S}{\partial \dot u_r} = Q_r, \qquad r = 1, \dots, m.$$

## Remarks

Differentiating the velocity formula gives $\ddot x_k = \sum_r e_{kr}\, \dot u_r + (\text{terms without } \dot u)$, so $\partial \ddot x_k / \partial \dot u_r = e_{kr}$ and $\partial S / \partial \dot u_r = \sum_k m_k \ddot x_k \cdot e_{kr}$.
The equations therefore say $\sum_k (m_k \ddot x_k - F_k) \cdot e_{kr} = 0$, which is [[d'Alembert's principle|GD776GVZSR]], because the vectors $(e_{1r}, \dots, e_{Nr})$ span the virtual displacements and ideal constraint forces do no virtual work.
For a holonomic system one may take $u_r = \dot q_r$, and then Appell's equations are equivalent to Lagrange's equations.
Their advantage is for [[nonholonomic systems|PTRV0QFSB9]]: they give exactly $m$ equations in the independent quasi-velocities, with no Lagrange multipliers.
Example: a particle of mass $m$ in the plane under a force $F$, with polar coordinates and $u = (\dot r, \dot\theta)$ has $S = \frac m2\big((\ddot r - r\dot\theta^2)^2 + (r\ddot\theta + 2\dot r\dot\theta)^2\big)$, and $\partial S / \partial \ddot\theta = m r (r\ddot\theta + 2\dot r \dot\theta) = Q_\theta$ is the angular momentum balance.

## Explanations

### L1 human

Appell's equations are a recipe for writing the equations of motion of a constrained system.
One builds a single quantity, half the mass-weighted sum of squared accelerations, and differentiates it with respect to the rates of change of the free speeds.
The recipe works even for rolling and skating systems, where the usual Lagrange recipe needs extra unknowns.

### L2 human

Appell's equations are the analytic form of [[Gauss's principle of least constraint|FZWAHMFZM3]]: minimizing $S - \sum_r Q_r \dot u_r$ over $\dot u$ gives exactly these equations.
They extend Lagrange's equations to nonholonomic systems written in quasi-velocities, and they are used for rolling bodies and in multibody dynamics.
The price is that one must compute accelerations, which is longer than computing the kinetic energy.
