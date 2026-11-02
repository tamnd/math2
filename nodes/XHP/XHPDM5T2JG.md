---
tag: XHPDM5T2JG
kind: statement
role: theorem
name: Noether's theorem
msc: [70H33, 49S05]
uses: [PS0VV149ET, 06738GGWWK, 0KZZ70ZHXP, 0262JP0NV9]
about: [0262JP0NV9, 8RA7AMWSAF]
sources:
  - url: https://en.wikipedia.org/wiki/Noether%27s_theorem
same_as:
  wikidata: Q578555
  wikipedia: Noether's theorem
---

## Statement

Let $L \colon \R^n \times \R^n \to \R$, written $L(q, v)$, be of class $C^2$.
Let $(h^s)_{s \in \R}$ be the [[flow|06738GGWWK]] of a complete $C^1$ vector field $X$ on $\R^n$, so that each $h^s$ is a [[diffeomorphism|0KZZ70ZHXP]] and $X(q) = \frac{d}{ds} h^s(q) \big|_{s = 0}$.
Assume that $L$ is invariant under the flow: $L\big(h^s(q), Dh^s(q) \, v\big) = L(q, v)$ for all $s \in \R$, $q \in \R^n$ and $v \in \R^n$.
Then the function
$$I(q, v) = \sum_{i=1}^n \frac{\partial L}{\partial v_i}(q, v) \, X_i(q)$$
is a [[first integral|0262JP0NV9]] of the [[Euler–Lagrange equations|PS0VV149ET]] $\frac{d}{dt} \frac{\partial L}{\partial v}(q, \dot q) = \frac{\partial L}{\partial q}(q, \dot q)$.
That is, $t \mapsto I(q(t), \dot q(t))$ is constant for every $C^2$ solution $q(t)$.

## Remarks

Along a solution, the Euler–Lagrange equations give $\frac{d}{dt} I = \frac{\partial L}{\partial q} \cdot X(q) + \frac{\partial L}{\partial v} \cdot DX(q) \, \dot q$.
The right side is the derivative in $s$ at $s = 0$ of $L(h^s(q), Dh^s(q) \, \dot q)$, which is $0$ by invariance.

Example: in the plane, let $L(q, v) = \frac{1}{2} \abs{v}^2 - U(\abs{q}^2)$ for a $C^2$ function $U \colon \R \to \R$.
It is invariant under the rotations $h^s$, with $X(q) = (-q_2, q_1)$.
The first integral is the angular momentum $I = q_1 v_2 - q_2 v_1$, which is conserved in every central force motion.

A related fact covers time: if $L$ does not depend on $t$, the energy $\dot q \cdot \frac{\partial L}{\partial v} - L$ is conserved.
The field-theory version says that each continuous symmetry of an action $\int L(x, u, \nabla u) \, dx$ gives a [[conservation law|8RA7AMWSAF]] in divergence form.

## Explanations

### L1 human

Noether's theorem links symmetries with conserved quantities.
If a mechanical system looks the same after you rotate it, then its angular momentum stays constant.
If it looks the same after you shift it in space, its momentum stays constant.
If its laws do not change in time, its energy stays constant.

### L2 human

The theorem turns a geometric fact, invariance of the Lagrangian under a one-parameter group, into a first integral that can be written down explicitly.
First integrals lower the order of the equations of motion, and in Hamiltonian terms the conserved quantity generates the symmetry through Poisson brackets.
Applied to a geodesic problem with a Killing field, it gives Clairaut's relation on surfaces of revolution.
In field theory, the same argument produces conserved currents, such as the energy–momentum tensor from translations.
