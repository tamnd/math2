---
tag: DDH18HWKZ9
kind: statement
role: theorem
name: Earnshaw's theorem
msc: [31B05, 78A30]
uses: [0DEB0JMN0W, 0HYPR64JM2, 0N8NGKDZDZ]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Earnshaw%27s_theorem
same_as:
  wikidata: Q1064471
  wikipedia: Earnshaw's theorem
---

## Statement

Let $U \subseteq \R^n$ be an open set, $n \ge 2$, and let $\varphi \colon U \to \R$ be a [[harmonic function|0DEB0JMN0W]].
Then $\varphi$ has no strict local minimum and no strict local maximum in $U$.
Consequently, consider a charged particle with charge $q$ that moves under the force $F = -q \nabla \varphi$.
No [[equilibrium point|0N8NGKDZDZ]] in $U$ is a strict local minimum of its potential energy $q\varphi$.
In this sense the particle has no stable equilibrium in $U$.

## Remarks

Proof: suppose that $\varphi(x) > \varphi(a)$ for all $x \ne a$ in a ball $B(a, \rho) \subseteq U$.
Take $0 < r < \rho$.
By the [[mean value property|0HYPR64JM2]], $\varphi(a)$ is the average of $\varphi$ over the sphere of radius $r$ about $a$.
But every value on that sphere is larger than $\varphi(a)$, a contradiction.
A strict local maximum is excluded in the same way, or by applying the argument to $-\varphi$.
In physics, $\varphi$ is the potential of charges that lie outside $U$; it is harmonic in the charge-free region $U$.
Example: in $\R^3$, with $e_1 = (1, 0, 0)$ and $e_2 = (0, 1, 0)$, let $\varphi(x) = 1/\abs{x - e_1} + 1/\abs{x + e_1}$ be the potential of two unit charges at $\pm e_1$.
The origin is an equilibrium point by symmetry.
Along the $x_1$-axis, $\varphi(t e_1) = 2/(1 - t^2)$ has a minimum at $t = 0$, but along the $x_2$-axis, $\varphi(t e_2) = 2/\sqrt{1 + t^2}$ has a maximum, so the origin is a saddle point.
The theorem is about potentials that are harmonic; diamagnetic materials, feedback control and time-varying fields are classical ways around it in physics.

## Explanations

### L1 human

You cannot hold a charged particle at rest in a stable way using fixed charges alone.
At any point where the forces balance, there is a direction in which a small push makes the particle run away.
Mathematically, a harmonic function cannot have a bowl-shaped minimum, because its value at a point is the average of its values around the point.

### L2 human

The theorem is a direct consequence of the mean value property, and it is a weak form of the strong maximum and minimum principles.
It applies to every inverse-square force law, so it also rules out stable static configurations of point masses under Newtonian gravity.
At an equilibrium of a harmonic potential, the Hessian has trace $0$, so it cannot be positive definite.
This is another way to see that an equilibrium cannot be a nondegenerate minimum.
