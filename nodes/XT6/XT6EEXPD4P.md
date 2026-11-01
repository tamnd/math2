---
tag: XT6EEXPD4P
kind: statement
role: theorem
name: Jordan–Schur theorem
msc: [20H20, 20C15]
uses: [0FCHE902D7, 082GHNPJ53, 0CB0DX5BVV, 0DTXBQPA2S, 0R9R0Y1HDK, JZNQTTMG58, 0KTW26C80J]
about: [0FCHE902D7]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan–Schur_theorem
same_as:
  wikidata: Q2360531
  wikipedia: Jordan–Schur theorem
---

## Statement

For each positive integer $n$ there is an integer $J(n)$ with the following property.
Every finite subgroup $G$ of the [[general linear group|0FCHE902D7]] $\mathrm{GL}_n(\C)$ has an [[abelian|082GHNPJ53]] [[normal subgroup|0CB0DX5BVV]] $A$ of [[index|0DTXBQPA2S]] $[G : A] \le J(n)$.

## Remarks

Jordan proved the theorem for finite groups.
Schur extended it to [[torsion groups|JZNQTTMG58]] of matrices: every torsion subgroup of $\mathrm{GL}_n(\C)$ has an abelian normal subgroup of finite index.

Idea of the proof: a finite group $G$ preserves a Hermitian inner product, so after a change of basis $G$ lies in the [[unitary group|0R9R0Y1HDK]] $U(n)$.
If two unitary matrices are close enough to the identity, their commutator is even closer to the identity.
In a finite group this forces the elements in a small ball around the identity to generate an abelian subgroup $A$.
This $A$ is normal, since conjugation by unitary matrices preserves distances to the identity.
Its index is at most the number of small balls needed to cover $U(n)$, which depends only on $n$.

Example: for $n = 2$, the dihedral group of order $2m$ acts on $\C^2$ by rotations and reflections of the plane.
It is not abelian for $m \ge 3$, but its rotations form a cyclic normal subgroup of index $2$.

The finiteness or torsion hypothesis is necessary.
The group $\mathrm{SL}_2(\Z) \subseteq \mathrm{GL}_2(\C)$ contains a nonabelian [[free group|0KTW26C80J]] of finite index, and a nonabelian free group has no abelian subgroup of finite index.

## Explanations

### L1 human

Finite groups of invertible matrices of a fixed size are almost abelian.
Each one contains an abelian piece whose number of cosets is bounded by a number that depends only on the size of the matrices.
So a finite group of $3 \times 3$ matrices can be huge, but most of its complexity is commutative.

### L2 human

The bound $J(n)$ does not depend on the order of $G$, and this is the whole point.
The same commutator argument in the Euclidean group is behind the first of the [[Bieberbach theorems|YE87R5CDJY]] on [[crystallographic groups|7KTJKFQT2N]].
The theorem also shows that a finite group with no abelian normal subgroup of small index, such as a large alternating group, has no faithful complex representation of small degree.
