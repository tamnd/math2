---
tag: S84R3CH6YD
kind: definition
name: BRST quantization
msc: [81T70, 81T13, 17B56]
defines: DCHKJBKCMR
uses: [5JJYBJ6A8K, 0MDMZ965VE, 362T9VND0H, 69NARSMQCM, 5WKBCMW1BC]
sources:
  - url: https://en.wikipedia.org/wiki/BRST_quantization
---

## Definition

Let $\mathfrak{g}$ be a finite-dimensional real [[Lie algebra|5JJYBJ6A8K]] with basis $T_1, \dots, T_r$ and structure constants $[T_a, T_b] = \sum_c f^c_{ab} T_c$.
Let $\rho$ be a representation of $\mathfrak{g}$ on a complex vector space $V$ of states.
Let $\Lambda \mathfrak{g}^*$ be the [[exterior algebra|0MDMZ965VE]] of the dual space, graded by degree, with dual basis $c^1, \dots, c^r$ of $\mathfrak{g}^*$, the *ghosts*.
Let $b_a$ be the contraction of $\Lambda\mathfrak{g}^*$ with $T_a$, the *antighosts*, so that $b_a c^b + c^b b_a = \delta^b_a$.
The *BRST operator* on the BRST complex $C = \Lambda \mathfrak{g}^* \otimes_\R V$ is
$$Q = \sum_{a} c^a\, \rho(T_a) - \frac12 \sum_{a, b, c} f^c_{ab}\, c^a c^b\, b_c,$$
where $c^a$ acts by left multiplication on the first factor.
Then $Q^2 = 0$, $Q$ raises the ghost degree by $1$, and the space of *BRST-physical states* is the cohomology $H^0(Q) = \ker(Q|_{C^0})$, and more generally $H^k(Q) = \ker(Q|_{C^k}) / Q(C^{k-1})$.

## Remarks

Here $Q$ is the differential of the [[Chevalley–Eilenberg complex|362T9VND0H]] of $\mathfrak{g}$ with coefficients in $V$, so $H^\bullet(Q)$ is the [[Lie algebra cohomology|69NARSMQCM]] $H^\bullet(\mathfrak{g}, V)$.
On $v \in V = C^0$ one has $(Qv)(T_a) = \rho(T_a)v$, so $H^0(Q)$ is the space $V^{\mathfrak{g}}$ of invariant vectors, the gauge-invariant states.
On a $1$-form $\theta \in \mathfrak{g}^*$ with $V$ trivial, the second term gives $(Q\theta)(x, y) = -\theta([x, y])$.

Example: let $\mathfrak{g} = \mathfrak{so}(3)$ act on $V = \C^3$ by the standard representation.
Then $H^0(Q) = 0$, since no nonzero vector of $\C^3$ is fixed by all rotations.

Non-example: the operator $\sum_a c^a \rho(T_a)$ alone does not square to zero when $\mathfrak{g}$ is non-abelian; its square is $\frac12 \sum f^c_{ab}\, c^a c^b \rho(T_c)$, and the ghost term is what cancels it.

In gauge field theory the same construction is applied to the Lie algebra of infinitesimal gauge transformations.
It is combined with extra antighost and auxiliary fields from gauge fixing, and the ghosts are then the [[Faddeev–Popov ghosts|5WKBCMW1BC]].
