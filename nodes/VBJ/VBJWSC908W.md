---
tag: VBJWSC908W
kind: statement
role: theorem
name: Swan's induction theorem
msc: [19A22, 20C10]
uses: [G5S1M9, 0KVGH0J5B3, 0CB0DX5BVV, 06QYRTX9KQ, 4NMTSX0XDS, 5FDMY7PDYY, KJKNJMGKZZ, F0HQXQ0HCD, PAP76H0ND9]
about: [5FDMY7PDYY, 4NMTSX0XDS]
sources:
  - url: https://en.wikipedia.org/wiki/Brauer%27s_theorem_on_induced_characters
  - url: https://arxiv.org/abs/1210.1044
---

## Statement

Let $G$ be a finite [[group|G5S1M9]].
A subgroup $H$ of $G$ is *hyperelementary* if $H$ has a [[cyclic|0KVGH0J5B3]] [[normal subgroup|0CB0DX5BVV]] $C$ such that $H/C$ is a [[$p$-group|06QYRTX9KQ]] for some prime $p$.
For a finite group $H$, let $\mathrm{Sw}(H)$ be the *Swan group* of $H$.
It is the [[Grothendieck group|5FDMY7PDYY]] of the finitely generated $\Z[H]$-modules that are free as abelian groups, over the [[group ring|4NMTSX0XDS]] $\Z[H]$.
Its defining relations are $[M] = [M'] + [M'']$ for every [[short exact sequence|KJKNJMGKZZ]] $0 \to M' \to M \to M'' \to 0$.
For $H \le G$, induction $M \mapsto \Z[G] \otimes_{\Z[H]} M$ defines a homomorphism $\operatorname{Ind}_H^G \colon \mathrm{Sw}(H) \to \mathrm{Sw}(G)$.

Then the sum of the induction maps
$$\bigoplus_{H} \mathrm{Sw}(H) \to \mathrm{Sw}(G),$$
where $H$ runs over the hyperelementary subgroups of $G$, is surjective.

## Remarks

The [[tensor product|F0HQXQ0HCD]] over $\Z$, with $G$ acting on both factors, makes $\mathrm{Sw}(G)$ a commutative ring with unit the class $[\Z]$ of the trivial module.
By the projection formula $\operatorname{Ind}_H^G(x) \cdot y = \operatorname{Ind}_H^G(x \cdot \operatorname{Res}^G_H y)$, a form of [[Frobenius reciprocity|PAP76H0ND9]], the image of the map is an ideal.
So it suffices to show that $[\Z]$ lies in the image, and this is the heart of Swan's proof.
If $G$ is itself hyperelementary, the statement is trivial.
The symmetric group $S_3$ is hyperelementary, with $C$ of order $3$ and $p = 2$.
The alternating group $A_4$ is not: its only normal subgroups are $1$, the Klein four-group and $A_4$, and none is cyclic with a $p$-group quotient.
Its hyperelementary subgroups are the cyclic subgroups and the Klein four-group.
So every class in $\mathrm{Sw}(A_4)$ is a $\Z$-combination of classes induced from these subgroups.
The theorem is an integral analogue of [[Brauer's theorem on induced characters|V8JVWE87TE]], which uses elementary subgroups.

## Explanations

### L1 human

Integral representations of a finite group are hard to classify.
Swan's theorem says that, up to the bookkeeping of a Grothendieck group, all of them can be built from representations of special small subgroups.
These subgroups, the hyperelementary ones, are a cyclic group extended by a group of prime power order.
So many questions about a general finite group reduce to questions about these simpler groups.

### L2 human

The Swan ring acts on many K-theoretic functors of $\Z[G]$, such as $K_0$, $K_1$ and the Whitehead group, through tensor products.
Each such functor is a module over $\mathrm{Sw}(G)$ compatible with induction and restriction, and then the theorem forces it to be computable from hyperelementary subgroups.
This is Dress's induction method, and it is how the theorem is used in algebraic K-theory and surgery theory.
It plays a key part in the Farrell–Hsiang method for proving the [[Farrell–Jones conjecture|B2X59B7J8V]].
