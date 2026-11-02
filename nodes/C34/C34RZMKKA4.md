---
tag: C34RZMKKA4
kind: statement
role: theorem
name: Kazhdan–Margulis theorem
msc: ["22E40", 22D05]
uses: [XJS07AJ50Y, 5M7D1BSHVZ, 0ZCY0Z80B6, BTYF5Y5PFY]
about: [5M7D1BSHVZ, XJS07AJ50Y]
sources:
  - url: https://en.wikipedia.org/wiki/Kazhdan–Margulis_theorem
same_as:
  wikidata: Q28401823
  wikipedia: Kazhdan–Margulis theorem
---

## Statement

Let $G$ be a connected [[semisimple Lie group|XJS07AJ50Y]] without compact factors.
Then there is an open [[neighbourhood|0ZCY0Z80B6]] $U$ of the identity $e$ in $G$ with the following property.
For every [[discrete subgroup|5M7D1BSHVZ]] $\Gamma$ of $G$ there is $g \in G$ such that $g \Gamma g^{-1} \cap U = \set{e}$.

## Remarks

The proof starts from a [[Zassenhaus neighbourhood|FZ798EZ6M0]]: the elements of $\Gamma$ close to $e$ generate a nilpotent group.
One then conjugates by suitable elements of $G$ that expand this nilpotent part, which is possible because $G$ has no compact factors.

Example: $G = \mathrm{SL}_2(\R)$ and $\Gamma = \mathrm{SL}_2(\Z)$.
Conjugating the element $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ by $\operatorname{diag}(t, t^{-1})$ gives $\begin{pmatrix} 1 & t^2 \\ 0 & 1 \end{pmatrix}$, which is close to $e$ for small $t$.
So some conjugates of $\Gamma$ come close to $e$, and the theorem only asserts that some conjugate stays away.

The hypothesis on compact factors is necessary.
In the compact semisimple group $\mathrm{SO}(3)$, let $\Gamma_n$ be the finite cyclic group of rotations about one axis by multiples of $2\pi/n$.
Every conjugate of $\Gamma_n$ contains a rotation by the angle $2\pi/n$.
So for a given $U$, every conjugate of $\Gamma_n$ meets $U \setminus \set{e}$ once $n$ is large.

## Explanations

### L1 human

A discrete subgroup has no elements arbitrarily close to the identity, but it might still have some fairly close ones.
The theorem says that, after moving the subgroup by a conjugation, one can keep all its elements outside a fixed neighbourhood of the identity.
The size of this neighbourhood depends only on the big group, not on the subgroup.

### L2 human

The main consequence concerns [[lattices|BTYF5Y5PFY]].
The volume of $G/\Gamma$ is at least a constant $c(G) > 0$ that does not depend on the lattice $\Gamma$.
Indeed a small ball around $e$ injects into $G/(g\Gamma g^{-1})$, and $G/\Gamma$ and $G/(g\Gamma g^{-1})$ have the same volume.
For quotients of symmetric spaces, this gives a uniform lower bound for the volume of locally symmetric orbifolds of a given type.
