---
tag: DSKV65NHZZ
kind: statement
role: theorem
name: Margulis superrigidity theorem
msc: ["22E40", 20G20]
uses: [0JYTG5K9Y4, 0V9PMN0RBH, 0KTW26C80J]
sources:
  - url: https://en.wikipedia.org/wiki/Superrigidity
---

## Statement

Let $G$ be a connected semisimple algebraic group defined over $\R$ whose real rank is at least $2$.
Assume that the identity component of $G(\R)$ has no compact factors.
Let $\Gamma$ be an irreducible lattice in $G(\R)$.
Let $H$ be a connected simple algebraic group over $\R$ with trivial center.
Let $\rho \colon \Gamma \to H(\R)$ be a [[group homomorphism|0JYTG5K9Y4]] such that $\rho(\Gamma)$ is Zariski dense in $H$ and its closure in $H(\R)$ is not compact.
Then there is a continuous homomorphism $\varphi \colon G(\R)^\circ \to H(\R)$, where $G(\R)^\circ$ is the identity component.
The map $\varphi$ agrees with $\rho$ on a subgroup of finite index in $\Gamma$.
In other words, $\rho$ virtually extends to $G(\R)^\circ$.

## Remarks

The proof builds a $\Gamma$-equivariant measurable map from the boundary $G(\R)/P$, with $P$ a minimal parabolic subgroup, to a projective variety of $H$.
This uses the amenability of $P$ and the ergodicity of the action of $\Gamma$ on $G(\R)/P$.
The higher rank is then used to show that this map is rational, and a rational boundary map gives the virtual extension.

Example: take $\Gamma = \mathrm{SL}_3(\Z)$ in $G = \mathrm{SL}_3$.
Every homomorphism of $\Gamma$ to such an $H(\R)$ with Zariski dense and unbounded image agrees, on a subgroup of finite index, with a continuous homomorphism of $\mathrm{SL}_3(\R)$.

The rank condition is necessary.
The group $\mathrm{SL}_2(\R)$ has real rank $1$, and $\mathrm{SL}_2(\Z)$ contains a [[free group|0KTW26C80J]] $F_2$ of finite index, which is a lattice in $\mathrm{SL}_2(\R)$.
A subgroup of index $2$ in $F_2$ is a free lattice $F_3$, and it maps onto $F_2$ by killing one free generator $x$.
Composing with the inclusion of $F_2$ into $\mathrm{SL}_2(\R)$ and then the projection to $\mathrm{PSL}_2(\R)$ gives a homomorphism $\rho$ with Zariski dense, unbounded image.
Suppose a continuous $\varphi \colon \mathrm{SL}_2(\R) \to \mathrm{PSL}_2(\R)$ agreed with $\rho$ on a subgroup $\Lambda$ of finite index in $F_3$.
Then $\varphi$ would be nontrivial, so its kernel, a proper normal subgroup of $\mathrm{SL}_2(\R)$, would lie in $\set{\pm I}$.
But some power $x^k$ with $k \ge 1$ lies in $\Lambda$ and in the kernel of $\rho$, and $x^k \ne \pm I$ because a free group has no torsion, so no such $\varphi$ exists.

## Explanations

### L1 human

Superrigidity says that certain discrete groups of matrices can only be represented in the ways the surrounding continuous group allows.
Any reasonable homomorphism of such a discrete group into another matrix group agrees, after passing to a subgroup of finite index, with a continuous homomorphism of the big group.
This holds for lattices in groups like $\mathrm{SL}_n(\R)$ with $n \ge 3$, but not for $\mathrm{SL}_2(\R)$.

### L2 human

Superrigidity is the main step in the proof of the Margulis arithmeticity theorem: every irreducible lattice in a group of real rank at least $2$ is an [[arithmetic group|4XWG6S7R4Z]].
It strengthens Mostow rigidity, which concerns isomorphisms between lattices, to arbitrary homomorphisms.
The rank one groups $\mathrm{Sp}(n, 1)$ and $F_{4(-20)}$ also satisfy superrigidity, by work of Corlette and of Gromov and Schoen.
