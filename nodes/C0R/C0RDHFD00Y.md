---
tag: C0RDHFD00Y
kind: definition
name: Moment map
msc: [53D20]
defines: ZARM34FZ6Z
uses: [CAN490EPRT, 0WCY42EV9V, C5EH3B4BEP]
sources:
  - url: https://en.wikipedia.org/wiki/Momentum_map
---

## Definition

Let $(M, \omega)$ be a [[symplectic manifold|CAN490EPRT]] and let $G$ be a [[Lie group|7JBRGCVJRB]] with [[Lie algebra|5JJYBJ6A8K]] $\mathfrak{g}$ and dual space $\mathfrak{g}^*$.
Let $G$ [[act|0WCY42EV9V]] smoothly on $M$ by symplectomorphisms.
For $\xi \in \mathfrak{g}$, let $\xi_M$ be the vector field $\xi_M(x) = \frac{d}{dt}\big|_{t=0} \exp(t\xi) \cdot x$.
A *moment map* for the action is a smooth map $\mu \colon M \to \mathfrak{g}^*$ such that:

1. For every $\xi \in \mathfrak{g}$, the function $\mu^\xi(x) = \langle \mu(x), \xi \rangle$ satisfies $\iota_{\xi_M} \omega = d\mu^\xi$, so $\xi_M$ is the [[Hamiltonian vector field|C5EH3B4BEP]] of $\mu^\xi$.
2. $\mu$ is equivariant: $\mu(g \cdot x) = \mathrm{Ad}^*_g \mu(x)$ for all $g \in G$ and $x \in M$, where $\mathrm{Ad}^*$ is the coadjoint action.

An action with a moment map is called a *Hamiltonian action*.

## Remarks

Example: let the circle $S^1 = \R / 2\pi\Z$ act on $\R^2$ by rotations, with $\omega = dx \wedge dy$.
Identify $\mathfrak{g}$ and $\mathfrak{g}^*$ with $\R$; the generator is $\xi_M = -y\,\partial_x + x\,\partial_y$.
Let $\mu(x, y) = -\frac{1}{2}(x^2 + y^2)$.
Then $\iota_{\xi_M} \omega = -y\,dy - x\,dx = d\mu$, and clause 2 holds because $G$ is abelian and $\mu$ is rotation invariant.

Non-example: the translations of the torus $T^2 = \R^2 / \Z^2$ in the $x$ direction preserve $\omega = dx \wedge dy$, but there is no moment map.
Clause 1 would need $\iota_{\partial_x} \omega = dy$ to be the differential of a function on $T^2$, and $dy$ is closed but not exact there.

For a connected group, clause 2 can be replaced by an infinitesimal condition.
It says that $\xi \mapsto \mu^\xi$ is a Lie algebra homomorphism into functions with the [[Poisson bracket|2S0MXDT4YH]], up to the sign convention.
When $G$ is abelian, a moment map can be changed by adding any constant in $\mathfrak{g}^*$.
Many authors use the opposite sign convention in clause 1.
