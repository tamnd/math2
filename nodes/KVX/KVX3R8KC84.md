---
tag: KVX3R8KC84
kind: definition
name: Adjoint functors
msc: [18A40]
defines: TZHF6ZM92S
uses: [A2DE66937D, 28NQ0KRHD3, VJXS8AK67E, KYCPCC57FT]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_functors
---

## Definition

Let $\mathcal{C}$ and $\mathcal{D}$ be [[categories|A2DE66937D]], and let $F \colon \mathcal{C} \to \mathcal{D}$ and $G \colon \mathcal{D} \to \mathcal{C}$ be [[functors|28NQ0KRHD3]].
An *adjunction* between $F$ and $G$ is a family of bijections
$$\varphi_{c, d} \colon \Hom_{\mathcal{D}}(F c, d) \to \Hom_{\mathcal{C}}(c, G d),$$
one for each object $c$ of $\mathcal{C}$ and each object $d$ of $\mathcal{D}$.
The family must be natural in $c$ and in $d$.
Naturality means $\varphi(k \circ g \circ F h) = G k \circ \varphi(g) \circ h$.
This must hold for all $h \colon c' \to c$, $g \colon F c \to d$ and $k \colon d \to d'$.
If an adjunction exists, $F$ is *left adjoint* to $G$ and $G$ is *right adjoint* to $F$, written $F \dashv G$.

## Remarks

Equivalently, $\varphi$ is a [[natural isomorphism|KYCPCC57FT]] between the two [[hom functors|VJXS8AK67E]] $\Hom_{\mathcal{D}}(F -, -)$ and $\Hom_{\mathcal{C}}(-, G -)$ from $\mathcal{C}^{\mathrm{op}} \times \mathcal{D}$ to sets.

Example: let $F$ send a set $X$ to the free group $F(X)$, and let $G$ send a group to its underlying set.
A homomorphism $g \colon F(X) \to H$ is determined by its values on the generators, and these values can be any elements of $H$.
So $\varphi(g) = g|_X$ is a bijection, and it is natural in $X$ and $H$.

Non-example: the forgetful functor $G$ from groups to sets has no right adjoint.
Indeed, a left adjoint preserves colimits, hence the initial object.
But $G$ sends the trivial group, which is initial, to a one-point set, which is not initial in sets.

Another standard example is $- \times Y \dashv (-)^Y$ in sets, where $Z^Y$ is the set of maps $Y \to Z$.
