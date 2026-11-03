---
tag: A9KY8Q08DN
kind: statement
role: theorem
name: Hertz's principle of least curvature
msc: [70H30, 70F25, 70G45]
uses: [AXA8HN8Y45, PTRV0QFSB9, C9YCMAPKMT, Q8D2JWY8G6, MGYKGP7PW3, 7JQS6VKFEZ, NSYMQMHPDN, Q61VFHCH2J, FZWAHMFZM3, GD776GVZSR]
about: [AXA8HN8Y45, PTRV0QFSB9]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%27s_principle_of_least_constraint
---

## Statement

Consider $N$ point particles with masses $m_1, \dots, m_N > 0$ and positions $x_1, \dots, x_N \in \R^3$, and write $x = (x_1, \dots, x_N) \in \R^{3N}$.
Give $\R^{3N}$ the mass-weighted inner product $\langle u, w \rangle = \sum_{k=1}^N m_k\, u_k \cdot w_k$ and its norm $\norm{u}$.
Assume the system obeys ideal time-independent constraints and that no applied forces act.
Each constraint is either a smooth [[holonomic constraint|AXA8HN8Y45]] $f(x) = 0$ or a smooth linear velocity constraint $a(x) \cdot \dot x = 0$, as in a [[nonholonomic system|PTRV0QFSB9]].
Then along every motion:

1. The [[kinetic energy|C9YCMAPKMT]] $\frac12 \norm{\dot x}^2$ is constant.
2. At each instant, the actual [[acceleration|Q8D2JWY8G6]] $\ddot x$ has the least norm $\norm{\ddot x}$ among all accelerations compatible with the constraints at the same position and velocity.
3. Hence, at each point, the path has the least mass-weighted [[curvature|7JQS6VKFEZ]] among compatible paths through that point in the same direction.

## Remarks

Part 2 is the special case without applied forces of [[Gauss's principle of least constraint|FZWAHMFZM3]], which states that $\ddot x$ minimizes $\sum_k m_k \abs{\ddot x_k - F_k / m_k}^2$ when forces $F_k$ act.
For the proof, note that the compatible accelerations form an affine subspace whose direction is the space of virtual displacements.
Ideal constraint forces are orthogonal to that space in the mass-weighted inner product.
So the actual acceleration is the point of the affine subspace closest to $0$.
Part 1 follows since $\frac{d}{dt}\frac12\norm{\dot x}^2 = \langle \ddot x, \dot x\rangle$ and $\dot x$ is itself a virtual displacement for time-independent constraints.
Part 3 follows from Parts 1 and 2 by comparing compatible paths run at the same constant speed $s > 0$.
For such a path $\ddot x$ is orthogonal to $\dot x$, and the curvature equals $\norm{\ddot x}/s^2$.
For holonomic constraints the result says that free motions are [[geodesics|NSYMQMHPDN]] of the [[configuration space|MGYKGP7PW3]] with the [[Riemannian metric|Q61VFHCH2J]] given by the kinetic energy, run at constant speed.
Example: a particle confined to a sphere with no applied force moves at constant speed along a great circle.

## Explanations

### L1 human

When nothing pushes a constrained system, it moves along the straightest path that the constraints allow.
A bead on a smooth wire, or a particle sliding on a smooth sphere, keeps its speed and turns only as much as the constraint forces it to.
Hertz proposed to build all of mechanics on this idea, treating forces as the effect of hidden constraints.

### L2 human

The principle is a geometric form of [[d'Alembert's principle|GD776GVZSR]] in the absence of applied forces.
For holonomic systems it identifies free motion with geodesic motion on the configuration space, which links mechanics with Riemannian geometry.
With a potential $V$, the Jacobi metric turns motion at fixed energy into geodesic motion again, by rescaling the kinetic energy metric by $E - V$.
For nonholonomic constraints the paths are still the straightest compatible paths.
In general they are not the shortest compatible paths, so they do not come from a variational principle of the usual kind.
