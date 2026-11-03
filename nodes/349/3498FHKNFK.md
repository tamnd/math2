---
tag: 3498FHKNFK
kind: definition
name: Spontaneous symmetry breaking
msc: [81R40, 81T13, 82B26]
defines: F5PJ0Q4RCF
uses: [7JBRGCVJRB, 96B4E2GPKJ, 0YQPZB5Q1G, 85TWR6E75P]
sources:
  - url: https://en.wikipedia.org/wiki/Spontaneous_symmetry_breaking
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]] that [[acts|96B4E2GPKJ]] smoothly on a finite-dimensional real vector space $V$ by linear maps.
Let $U \colon V \to \R$ be a smooth function, the potential, that is invariant: $U(g\phi) = U(\phi)$ for all $g \in G$ and $\phi \in V$.
Suppose that $U$ attains its minimum, and let $\phi_0$ be a minimum point, a classical ground state.
Let $H = \set{g \in G : g\phi_0 = \phi_0}$ be the stabilizer of $\phi_0$.
The symmetry $G$ is *spontaneously broken* to $H$ if $H \ne G$, that is, if some $g \in G$ moves $\phi_0$.

## Remarks

Since $U$ is invariant, every point of the [[orbit|0YQPZB5Q1G]] $G\phi_0$ is again a minimum point, so the ground states include a copy of the [[homogeneous space|85TWR6E75P]] $G/H$.
The same definition applies to a field theory with a constant field $\phi \colon \R^{1,3} \to V$ and Lagrangian density $\frac12 \abs{\partial\phi}^2 - U(\phi)$, where $G$ acts by orthogonal maps.

Example: $V = \C = \R^2$ with $G = U(1)$ acting by multiplication, and $U(\phi) = \lambda (\abs{\phi}^2 - v^2)^2$ with $\lambda, v > 0$.
The minimum points form the circle $\abs{\phi} = v$, and the stabilizer of $\phi_0 = v$ is trivial, so $U(1)$ is broken to $\set{1}$.

Non-example: the same $V$ and $G$ with $U(\phi) = m^2 \abs{\phi}^2 + \lambda \abs{\phi}^4$ and $m^2 > 0$.
The only minimum point is $\phi_0 = 0$, which is fixed by all of $U(1)$, so the symmetry is not broken.

In quantum theory the definition is stated for the vacuum state: the symmetry is spontaneously broken if the vacuum is not invariant under it.
This needs infinitely many degrees of freedom; in quantum mechanics with finitely many degrees of freedom, tunnelling usually makes the ground state unique and symmetric.
