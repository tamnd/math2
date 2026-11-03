---
tag: BEM454AYTT
kind: statement
role: theorem
name: Lagrange's equations of motion
msc: [70H03, 70F20]
uses: [BCF1EX9W2M, AXA8HN8Y45, C9YCMAPKMT, DF7DKHTQ7A, 9WQT2RMGTZ, ZC3YKMKRGP, PS0VV149ET]
about: [47JMCBM3VJ]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrangian_mechanics
---

## Statement

Consider $N$ particles with masses $m_1, \ldots, m_N > 0$ and positions $r_1, \ldots, r_N \in \R^3$.
Assume they are subject to [[holonomic constraints|AXA8HN8Y45]] described by [[generalized coordinates|BCF1EX9W2M]] $q = (q_1, \ldots, q_n)$.
This means that $r_k = r_k(q, t)$ for $C^2$ maps $r_k$, and that every $q$ in an open set $U \subseteq \R^n$ gives an allowed configuration.
Assume the constraints are ideal: the constraint forces do no work in any virtual displacement $\delta r_k = \sum_j \frac{\partial r_k}{\partial q_j}\delta q_j$.
Let $F_k$ be the applied force on particle $k$, and let $Q_j = \sum_k F_k \cdot \frac{\partial r_k}{\partial q_j}$ be the [[generalized forces|9WQT2RMGTZ]].
Let $T = \sum_k \tfrac12 m_k \abs{\dot r_k}^2$ be the [[kinetic energy|C9YCMAPKMT]], written as a function of $(q, \dot q, t)$.
Then every motion $q(t)$ satisfies
$$\frac{d}{dt}\frac{\partial T}{\partial \dot q_j} - \frac{\partial T}{\partial q_j} = Q_j, \qquad j = 1, \ldots, n.$$
If moreover $Q_j = -\partial V / \partial q_j$ for a [[potential energy|DF7DKHTQ7A]] $V(q, t)$, then with $L = T - V$ the motions satisfy
$$\frac{d}{dt}\frac{\partial L}{\partial \dot q_j} - \frac{\partial L}{\partial q_j} = 0, \qquad j = 1, \ldots, n.$$

## Remarks

The proof starts from d'Alembert's form of the [[principle of virtual work|ZC3YKMKRGP]], $\sum_k (F_k - m_k \ddot r_k) \cdot \delta r_k = 0$, which is where the hypothesis on ideal constraints enters.
Two identities follow from $\dot r_k = \sum_j \frac{\partial r_k}{\partial q_j}\dot q_j + \frac{\partial r_k}{\partial t}$: first $\frac{\partial \dot r_k}{\partial \dot q_j} = \frac{\partial r_k}{\partial q_j}$, and second $\frac{d}{dt}\frac{\partial r_k}{\partial q_j} = \frac{\partial \dot r_k}{\partial q_j}$.
With them, $\sum_k m_k \ddot r_k \cdot \frac{\partial r_k}{\partial q_j} = \frac{d}{dt}\frac{\partial T}{\partial \dot q_j} - \frac{\partial T}{\partial q_j}$, and since the $\delta q_j$ are independent, the equations follow.
The second form is the system of [[Euler–Lagrange equations|PS0VV149ET]] of $L$.
Without the ideal-constraint hypothesis, for example with sliding friction at a contact, the constraint forces contribute to $Q_j$ and do not drop out.

Example: a simple pendulum of length $\ell$ and mass $m$, with angle $\theta$ from the downward vertical, has $T = \tfrac12 m\ell^2\dot\theta^2$ and $V = -mg\ell\cos\theta$.
The equation is $m\ell^2\ddot\theta + mg\ell\sin\theta = 0$, and the tension of the rod never appears.

## Explanations

### L1 human

Lagrange's equations are Newton's laws rewritten in any coordinates that fit the constraints, such as angles for a pendulum.
One needs only the kinetic energy and the applied forces expressed in these coordinates.
The forces that keep the system on its constraints, which are often unknown, disappear from the equations.

### L2 human

These are the equations of the second kind; the equations of the first kind keep Cartesian coordinates and add Lagrange multipliers for the constraint forces.
For conservative forces they are the Euler–Lagrange equations of $L = T - V$, which links them with [[Hamilton's principle|FAQ9CH2Z76]] and the [[stationary-action principle|Q104C67P26]].
Through the Legendre transform they become Hamilton's equations.
