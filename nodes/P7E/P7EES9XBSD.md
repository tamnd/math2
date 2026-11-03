---
tag: P7EES9XBSD
kind: definition
name: Wilson loop
msc: [81T13, 53C29, 81T25]
defines: 61YB1GGZ7B
uses: [8E37E74XVP, NJ21PN5ZGJ, WHDZ3MK56B, 7JA7WH92K0, 07PTPSZPME, 707DEWCCFX]
sources:
  - url: https://en.wikipedia.org/wiki/Wilson_loop
---

## Definition

Let $G$ be a Lie group, let $P \to M$ be a [[principal $G$-bundle|8E37E74XVP]] over a smooth manifold $M$, and let $A$ be a [[connection|NJ21PN5ZGJ]] on $P$.
Let $\gamma \colon [0, 1] \to M$ be a piecewise smooth closed curve based at $x = \gamma(0)$.
Choose a point $p$ in the fibre $P_x$.
The [[holonomy|WHDZ3MK56B]] of $A$ along $\gamma$ is the element $\mathrm{Hol}_A(\gamma, p) \in G$ such that the horizontal lift of $\gamma$ from $p$ ends at $p \cdot \mathrm{Hol}_A(\gamma, p)$.
Let $\rho \colon G \to GL(V)$ be a finite-dimensional [[representation|7JA7WH92K0]].
The *Wilson loop* of $A$ along $\gamma$ in the representation $\rho$ is
$$W_\rho(\gamma, A) = \operatorname{tr} \rho\big(\mathrm{Hol}_A(\gamma, p)\big),$$
where $\operatorname{tr}$ is the [[trace|07PTPSZPME]].

## Remarks

The value does not depend on $p$: another point $p g$ of the fibre gives the holonomy $g^{-1} \mathrm{Hol}_A(\gamma, p) \, g$, and the trace is invariant under conjugation.
For the same reason $W_\rho(\gamma, A)$ is unchanged when $A$ is moved by an element of the [[gauge group|707DEWCCFX]].
On a trivial bundle with a matrix group, physicists write $W_\rho(\gamma, A) = \operatorname{tr} \mathcal{P} \exp\left( \oint_\gamma A \right)$, a path-ordered exponential, with signs and factors of $i$ that depend on conventions.

Example: $G = U(1)$, $\rho$ the identity representation, $M = \R^2$, and $A = i\alpha$ for a real $1$-form $\alpha$.
Then the holonomy commutes with everything, $W(\gamma, A) = \exp\left(\pm i \oint_\gamma \alpha\right)$ with the sign fixed by the convention, and by Stokes' theorem $\oint_\gamma \alpha = \int_D d\alpha$ when $\gamma$ bounds a disc $D$.
For $\alpha = \frac{B}{2}(x \, dy - y \, dx)$ and $\gamma$ the circle of radius $r$, this gives $W = e^{\pm i B \pi r^2}$, the exponential of the flux.

Non-example: for a non-abelian group, the holonomy $\mathrm{Hol}_A(\gamma, p)$ itself is not a Wilson loop and is not gauge invariant.
It changes by conjugation, and only class functions of it, such as traces, are invariant.

In a quantum gauge theory, or in [[lattice gauge theory|ZBJY59W3Z5]], one studies the expectation value $\langle W_\rho(\gamma, A) \rangle$.
For a rectangle of sides $R$ and $T$ in the time direction, decay like $e^{-\sigma R T}$ with $\sigma > 0$, the area law, is Wilson's criterion for confinement.
