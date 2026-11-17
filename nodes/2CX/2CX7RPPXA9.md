---
tag: 2CX7RPPXA9
kind: example
name: Category of groups
msc: ["20J15", "18A05"]
topics: [E1506A5A55]
audience: grad
instance_of: [A2DE66937D]
uses: [A2DE66937D, G5S1M9, 0JYTG5K9Y4, 08MG7H8JW5]
sources:
  - url: https://en.wikipedia.org/wiki/Category_of_groups
    locator: Relation to other categories
  - url: https://en.wikipedia.org/wiki/Category_of_groups
    locator: Categorical properties
  - url: https://en.wikipedia.org/wiki/Category_of_groups
    locator: Not additive and therefore not abelian
  - url: https://en.wikipedia.org/wiki/Free_product
    locator: Construction
same_as:
  wikidata: Q3912012
  wikipedia: Category of groups
---

## Example

The category of groups $\mathbf{Grp}$ has the [[groups|G5S1M9]] as objects and the [[group homomorphisms|0JYTG5K9Y4]] $f \colon G \to H$ as morphisms.
The composition is the composition of maps, and the identity morphism of $G$ is the identity map $\mathrm{id}_G$.
We check that this is a [[category|A2DE66937D]].

1. Let $f \colon G \to H$ and $g \colon H \to K$ be homomorphisms. For $x, y \in G$, we get $g(f(xy)) = g(f(x)f(y)) = g(f(x))\,g(f(y))$. So $g \circ f$ is a homomorphism, and the composition is defined.
2. The identity map $\mathrm{id}_G$ is a homomorphism, because $\mathrm{id}_G(xy) = xy = \mathrm{id}_G(x)\,\mathrm{id}_G(y)$.
3. For each homomorphism $f \colon G \to H$, we get $f \circ \mathrm{id}_G = f$ and $\mathrm{id}_H \circ f = f$, because this holds for all maps of sets.
4. The composition of maps is associative: $h \circ (g \circ f) = (h \circ g) \circ f$, because both maps send $x$ to $h(g(f(x)))$.

By steps 1 to 4, $\mathbf{Grp}$ satisfies the axioms of a category.

## Remarks

### Isomorphisms and special objects

- The isomorphisms of $\mathbf{Grp}$ are the bijective homomorphisms, because the inverse map of a bijective homomorphism is a homomorphism ([[group isomorphism|08MG7H8JW5]]).
- The [[trivial group|0BNPC9850Y]] $\{e\}$ is a [[zero object|AQET9YHH6F]]. From each group there is exactly one homomorphism to $\{e\}$, and from $\{e\}$ there is exactly one homomorphism to each group, because $e$ must go to the identity.
- For two groups $G$ and $H$, the zero morphism $G \to H$ is the trivial homomorphism $g \mapsto e_H$.

### Limits and colimits

- The [[product|S5744QZV4N]] of $G$ and $H$ is the [[direct product|00HF4RJ5QN]] $G \times H$ with the two projections. A pair of homomorphisms $K \to G$ and $K \to H$ gives exactly one homomorphism $K \to G \times H$.
- The [[coproduct|4FJ0S71P58]] of $G$ and $H$ is the [[free product|TM7QS7P7X9]] $G * H$ with the two inclusions. A pair of homomorphisms $G \to K$ and $H \to K$ gives exactly one homomorphism $G * H \to K$.
- The equaliser of two homomorphisms $u, v \colon G \to H$ is the subgroup $\{g \in G : u(g) = v(g)\}$ with its inclusion.
- The coequaliser of $u, v \colon G \to H$ is the projection $H \to H/R$, where $R$ is the [[normal closure|5WBSBAP4PD]] of the set $\{u(g)v(g)^{-1} : g \in G\}$. This follows from the [[universal property of the quotient group|0GJ83E78A5]].
- The pushout of two homomorphisms $K \to G$ and $K \to H$ is the [[amalgamated free product|M848AHBRCM]] $G *_K H$.
- $\mathbf{Grp}$ has all small limits and all small colimits.

### Kernels and cokernels

- The categorical kernel of $f \colon G \to H$ is the inclusion of the [[kernel|0W88CEGQP1]] $\ker f$ in $G$. It is the equaliser of $f$ and the zero morphism.
- The categorical cokernel of $f$ is the projection $H \to H/R$, where $R$ is the normal closure of the image $f(G)$.
- A subgroup inclusion $S \to G$ is a kernel of some morphism if and only if $S$ is a [[normal subgroup|0CB0DX5BVV]]. For example, the inclusion of $\{e, (1\,2)\}$ in $S_3$ is a monomorphism, but it is not a kernel.

### Monomorphisms and epimorphisms

A homomorphism $f \colon G \to H$ is a [[monomorphism|Y2NP1JFR86]] if and only if it is [[injective|09NWETVTNY]].

1. Assume that $f$ is injective, and let $u, v \colon K \to G$ be homomorphisms with $f \circ u = f \circ v$. For each $x \in K$, we get $f(u(x)) = f(v(x))$, so $u(x) = v(x)$. Thus $u = v$.
2. Assume that $f$ is a monomorphism. Let $i \colon \ker f \to G$ be the inclusion, and let $t \colon \ker f \to G$ be the trivial homomorphism.
3. For each $k \in \ker f$, we get $f(i(k)) = f(k) = e_H$ and $f(t(k)) = f(e_G) = e_H$. So $f \circ i = f \circ t$.
4. Because $f$ is a monomorphism, $i = t$. So each $k \in \ker f$ equals $e_G$, and $\ker f = \{e_G\}$.
5. A homomorphism with a trivial kernel is injective ([[this statement|0N2P0XRTDF]]). So $f$ is injective.

A homomorphism is an [[epimorphism|RVXDSY04KG]] if and only if it is [[surjective|01RVCMSN5N]] ([[this statement|E24V97RWEX]]).
This direction is harder, because the image of $f$ need not be normal.
So a homomorphism is an isomorphism if and only if it is both a monomorphism and an epimorphism.

### Functors to and from other categories

- The [[forgetful functor|WV3BPYCHVG]] $U \colon \mathbf{Grp} \to \mathbf{Set}$ sends a group to its underlying set, in the [[category of sets|WP0YB7VC59]].
- The [[free group|0KTW26C80J]] functor $F \colon \mathbf{Set} \to \mathbf{Grp}$ is [[left adjoint|TZHF6ZM92S]] to $U$. For a set $X$ and a group $G$, the homomorphisms $F(X) \to G$ correspond to the maps of sets $X \to U(G)$.
- The [[category of abelian groups|99ZVSM254K]] $\mathbf{Ab}$ is a full subcategory of $\mathbf{Grp}$. It is a [[reflective subcategory|FC7VB4WSG0]]: the reflector sends $G$ to its [[abelianisation|0AQZV0905N]] $G/[G, G]$.
- The [[universal property of the abelianisation|0EJ4PC8NJ6]] is the statement that this is a reflection: each homomorphism from $G$ to an abelian group factors in exactly one way through $G \to G/[G, G]$.

### Not additive

$\mathbf{Grp}$ is not an additive category, so it is not an [[abelian category|Y9CZ3MTNF1]].
In an additive category, the finite products and the finite coproducts are the same objects.
In $\mathbf{Grp}$, the coproduct $\mathbb{Z} * \mathbb{Z}$ is a free group on two generators, which is not abelian.
The product $\mathbb{Z} \times \mathbb{Z}$ is abelian, so the two groups are not isomorphic.

### History

Samuel Eilenberg and Saunders Mac Lane introduced categories in 1945.

## Explanations

### L1 human

The category of groups puts all groups and all homomorphisms between them into one structure.
Many constructions with groups are then special cases of general patterns of category theory.
For example, the direct product of two groups is a product in the sense of categories, and the free product is a coproduct.
The map $\mathbb{Z} \to \mathbb{Z}/2\mathbb{Z}$ that sends an integer to its parity is one morphism of this category.

### L2 human

We compare the product and the coproduct of two copies of $\mathbb{Z}/2\mathbb{Z}$.

1. The product is $\mathbb{Z}/2\mathbb{Z} \times \mathbb{Z}/2\mathbb{Z}$, which is the [[Klein four-group|0PMRQJVTME]], of order $4$.
2. The coproduct is the free product $\mathbb{Z}/2\mathbb{Z} * \mathbb{Z}/2\mathbb{Z}$. Let $a$ and $b$ be the generators of the two copies, so $a^2 = b^2 = e$.
3. The elements of the free product are the reduced words in $a$ and $b$, in which no letter follows itself. Examples are $e$, $a$, $b$, $ab$, $ba$, $aba$ and $abab$.
4. The powers $(ab)^n = abab \cdots ab$ are different reduced words for $n = 1, 2, 3, \dots$, so $ab$ has infinite order.
5. Thus the coproduct is an infinite group, but the product has order $4$.

A common error is to think that the coproduct of groups is the direct product.
This is true in $\mathbf{Ab}$, where the coproduct of two groups is their direct sum, but it is false in $\mathbf{Grp}$.
A second common error is to think that each monomorphism is a kernel, as in an abelian category.
In $\mathbf{Grp}$, only the inclusions of normal subgroups are kernels.

### L3 human

$\mathbf{Grp}$ is complete and cocomplete, and it is monadic over $\mathbf{Set}$ through the free group functor and the forgetful functor.
It is not abelian, but it keeps much of the structure of an abelian category.
The first isomorphism theorem says that each morphism factors as a regular epimorphism followed by a monomorphism, and the two factors are unique up to isomorphism.
In $\mathbf{Grp}$, the regular epimorphisms are exactly the surjective homomorphisms, and the regular monomorphisms are exactly the injective homomorphisms.
The normal monomorphisms, which are the kernels, are only the inclusions of normal subgroups.
These properties make $\mathbf{Grp}$ the main example of a semi-abelian category.
