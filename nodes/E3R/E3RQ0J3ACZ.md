---
tag: E3RQ0J3ACZ
kind: statement
role: theorem
name: Wigner's classification
msc: ["22E43", "22E70", 22D30]
uses: [8ZQ9TA4Q2Q, 74BPYJNZTM, FX3NEFYFFN, 12CEWPMSG4, 6Q7AHAZ6Q4, J58ED1GV6N, E5P8AG6CK7, 0H3WZXCZNF, 0YQPZB5Q1G]
about: [8ZQ9TA4Q2Q, 74BPYJNZTM]
sources:
  - url: https://en.wikipedia.org/wiki/Wigner%27s_classification
same_as:
  wikidata: Q12609547
  wikipedia: Wigner's classification
---

## Statement

Let $\tilde P = \R^{1,3} \rtimes \mathrm{SL}_2(\C)$ be the universal cover of the identity component of the [[Poincaré group|8ZQ9TA4Q2Q]].
Here $\R^{1,3}$ is Minkowski space with the form $p \cdot p = p_0^2 - p_1^2 - p_2^2 - p_3^2$, and [[SL(2,C)|J58ED1GV6N]] acts on it through the covering map onto the restricted Lorentz group.
The group $\mathrm{SL}_2(\C)$ also acts on the momentum space $\widehat{\R^{1,3}} \cong \R^{1,3}$ of characters $x \mapsto e^{i p \cdot x}$ of the translations.
For a momentum $p$, let $H_p \subseteq \mathrm{SL}_2(\C)$ be its stabilizer, the little group.

1. The irreducible [[unitary representations|74BPYJNZTM]] of $\tilde P$, up to equivalence, are in bijection with certain pairs $(\mathcal{O}, \sigma)$. Here $\mathcal{O}$ is an [[orbit|0YQPZB5Q1G]] of $\mathrm{SL}_2(\C)$ in momentum space. And $\sigma$ is an [[irreducible|FX3NEFYFFN]] unitary representation of $H_p$ for a chosen $p \in \mathcal{O}$, up to equivalence.
2. The representation attached to $(\mathcal{O}, \sigma)$ is the [[induced representation|6Q7AHAZ6Q4]] $\mathrm{Ind}_{\R^{1,3} \rtimes H_p}^{\tilde P} (e^{i p \cdot x} \sigma)$.
3. For the orbit $p \cdot p = m^2$ with $m > 0$ and $p_0 > 0$, the little group is isomorphic to [[SU(2)|E5P8AG6CK7]], and $\sigma$ is labelled by a spin $s \in \set{0, \tfrac12, 1, \tfrac32, \dots}$.
4. For the orbit $p \cdot p = 0$ with $p_0 > 0$, the little group is isomorphic to a double cover of the Euclidean group of the plane. The representations $\sigma$ that are trivial on its translation part are characters labelled by a helicity $h \in \tfrac12 \Z$; the others form the continuous spin representations.

## Remarks

The translations form an abelian normal subgroup, so the [[Mackey machine|12CEWPMSG4]] applies.
The orbits of $\mathrm{SL}_2(\C)$ on momentum space are the hyperboloids $p \cdot p = m^2$, the two halves of the light cone, the hyperboloids $p \cdot p < 0$ of one sheet, and the point $0$.
These orbits are locally closed, which is the condition under which Mackey's theory gives a complete classification by orbits and little groups.
The remaining orbits ($p \cdot p < 0$, $p_0 < 0$, and $p = 0$) give representations that are not used for physical particles.
For example, an electron is described by the orbit with mass $m > 0$ and spin $s = \tfrac12$, and a photon by the light cone orbit with helicities $\pm 1$.
The [[semidirect product|0H3WZXCZNF]] structure is essential: without the normal abelian subgroup of translations there is no momentum space to start from.

## Explanations

### L1 human

Symmetry of spacetime under shifts, rotations and boosts forms the Poincaré group.
Wigner found all the elementary ways in which this group can act on the states of a quantum system.
Each such way is labelled by a mass and by a spin or a helicity.
This is why physicists say that a particle "is" an irreducible representation of the Poincaré group.

### L2 human

The method is the general one for semidirect products $A \rtimes H$ with $A$ abelian.
First choose a character of $A$, here a momentum $p$, then a representation of its stabilizer in $H$, and induce.
For massive particles the stabilizer of $(m, 0, 0, 0)$ is $\mathrm{SU}(2)$, which explains why spin takes half-integer values.
The same method classifies the representations of the Euclidean motion groups and of the Heisenberg-type semidirect products.
