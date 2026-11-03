---
tag: 2KZCM5V7YN
kind: statement
role: theorem
name: Wigner's theorem on symmetries
msc: [81R05, 81P16, 46N50]
uses: [HM2HHE3J51, RC1C7WXX1H, MM0EJ2GDE4]
about: [RC1C7WXX1H, MM0EJ2GDE4]
sources:
  - url: https://en.wikipedia.org/wiki/Wigner%27s_theorem
same_as:
  wikidata: Q1135224
  wikipedia: Wigner's theorem
---

## Statement

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]] and let $\mathbb{P}\mathcal{H}$ be its [[projective Hilbert space|RC1C7WXX1H]], the set of rays $[\psi] = \set{c\psi : c \in \C}$ of unit vectors $\psi$.
For rays $[\psi]$ and $[\varphi]$, the transition probability $\abs{\langle \psi, \varphi \rangle}^2$ depends only on the rays.
Let $T \colon \mathbb{P}\mathcal{H} \to \mathbb{P}\mathcal{H}$ be a surjective map with
$$\abs{\langle \psi', \varphi' \rangle}^2 = \abs{\langle \psi, \varphi \rangle}^2 \quad \text{whenever } T[\psi] = [\psi'] \text{ and } T[\varphi] = [\varphi'].$$
Then there is an operator $U \colon \mathcal{H} \to \mathcal{H}$ that is either [[unitary|MM0EJ2GDE4]] or antiunitary such that $T[\psi] = [U\psi]$ for every unit vector $\psi$.
Here $U$ is *antiunitary* if it is bijective, $U(a\psi + b\varphi) = \bar{a}U\psi + \bar{b}U\varphi$ and $\langle U\psi, U\varphi \rangle = \overline{\langle \psi, \varphi \rangle}$ for all $a, b \in \C$ and $\psi, \varphi \in \mathcal{H}$.
If $\dim \mathcal{H} \ge 2$, then $U$ is unique up to a factor $e^{i\theta}$ with $\theta \in \R$, and whether $U$ is unitary or antiunitary is determined by $T$.

## Remarks

A proof fixes an orthonormal basis $(e_k)$, chooses representatives of the image rays $T[e_k]$, and fixes their phases using the rays of the vectors $e_1 + e_k$.
The images of the remaining vectors are then forced, up to the choice between a linear and an antilinear extension, by the preserved transition probabilities.
Example: complex conjugation of coordinates, $K(z_1, \dots, z_n) = (\bar{z}_1, \dots, \bar{z}_n)$ on $\C^n$, preserves all transition probabilities and is antiunitary; it is not induced by any unitary operator when $n \ge 2$.
Time reversal in quantum mechanics is implemented by an antiunitary operator of this kind.
In dimension $1$ there is only one ray, so uniqueness fails: the identity map of $\mathbb{P}\C$ is induced both by $\id$ and by $K$.

## Explanations

### L1 human

In quantum mechanics a pure state is a ray, a vector up to a phase, and the physically meaningful numbers are the transition probabilities between rays.
A symmetry is a reshuffling of rays that keeps all these probabilities.
Wigner's theorem says that every such symmetry comes from a unitary or an antiunitary operator on the Hilbert space itself.
So symmetries can always be handled with linear algebra.

### L2 human

The theorem is the starting point of the representation theory of symmetry groups in quantum mechanics.
A symmetry group acting on rays gives operators $U(g)$ that multiply only up to phases, $U(g)U(h) = \omega(g, h)U(gh)$, that is, a projective representation.
For a connected Lie group, every element is a product of squares, and the square of a unitary or antiunitary operator is unitary, so all $U(g)$ are unitary.
Bargmann's theorem then says when the phases can be removed, and this leads to spin and to [[Wigner's classification|E3RQ0J3ACZ]] of particles.
