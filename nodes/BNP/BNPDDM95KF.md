---
tag: BNPDDM95KF
kind: concept
name: Semilinear and antilinear maps
msc: ["15A04", "51A10"]
topics: [9080WQTZ3M]
audience: grad
uses: [0NRYHJPQG2, EZVN87C88J, DSQ17TNW1C, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Semilinear_map
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Semilinear_map
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Semilinear_map
    locator: General semilinear group
  - url: https://en.wikipedia.org/wiki/Semilinear_map
    locator: Applications
  - url: https://en.wikipedia.org/wiki/Antilinear_map
    locator: Definitions and characterizations
---

## Summary

A semilinear map respects sums, and it respects scalars only up to a fixed twist of the field, such as complex conjugation.
Precisely, let $V$ and $W$ be vector spaces over a field $K$, and let $\sigma$ be an [[automorphism|DSQ17TNW1C]] of $K$.
A map $T \colon V \to W$ is $\sigma$-semilinear if $T(u + v) = T(u) + T(v)$ and $T(\lambda v) = \sigma(\lambda)\, T(v)$ for all $u, v \in V$ and $\lambda \in K$.
For $\sigma = \id_K$, these are the [[linear maps|0NRYHJPQG2]].
For $K = \C$ and $\sigma$ the [[complex conjugation|0FTH2E9TAS]], they are the antilinear maps, with $T(\lambda v) = \bar\lambda\, T(v)$.

## Motivation

Some natural maps respect sums but twist scalars.
Complex conjugation $z \mapsto \bar z$ on $\C^n$ is the basic case, since it sends $iz$ to $-i\bar z$.
In an inner product space over $\C$, the map $v \mapsto \langle \cdot, v \rangle$ to the dual space is antilinear, so antilinear maps appear in Hilbert space theory and in quantum mechanics.
In projective geometry, semilinear maps describe all collineations of a projective space of dimension at least $2$.

## Notation

A $\sigma$-semilinear map is also called a semilinear map with companion automorphism $\sigma$.
An antilinear map is also called conjugate-linear.
The invertible semilinear maps $V \to V$, for all automorphisms $\sigma$ together, form the general semilinear group $\Gamma L(V)$.
More generally, $\sigma$ may be a [[field homomorphism|EZVN87C88J]] $K \to L$ between two fields, with $V$ over $K$ and $W$ over $L$.

## Remarks

### Examples

[[Complex conjugation on $\C^n$|MMSPCWKJQY]], $(z_1, \dots, z_n) \mapsto (\bar z_1, \dots, \bar z_n)$, is antilinear.
[[Squaring on the field with four elements|MJNB0GQVVY]] is semilinear for the Frobenius automorphism $a \mapsto a^2$, and it is not linear.
Each linear map is semilinear with $\sigma = \id_K$.

### What it is not

[[The real part $\C \to \C$|6J7N1XZB1M]] is additive, but it is semilinear for no automorphism of $\C$.
The map $z \mapsto z^2$ on $\C$ is not additive, so it is not semilinear.

### Properties

If $T \ne 0$ is $\sigma$-semilinear, then $\sigma$ is unique, as one sees by picking $v$ with $T(v) \ne 0$ and comparing $T(\lambda v) = \sigma(\lambda) T(v)$.
The composite of a $\sigma$-semilinear map after a $\tau$-semilinear map is $(\sigma\tau)$-semilinear, so the composite of two antilinear maps is linear.
The kernel and the image of a semilinear map are subspaces, and a semilinear bijection sends bases to bases.
Fix a basis $B$ of $V$.
Each semilinear bijection of $V$ is a linear bijection composed with the map that applies $\sigma$ to the coordinates in $B$, and so $\Gamma L(V) = GL(V) \rtimes \Aut(K)$ for $V \ne \{0\}$.
The field $\R$ has no automorphism other than the identity, so every semilinear map of real spaces is linear.

### Projective geometry

The [[fundamental theorem of projective geometry|GKV4RVXBRE]] states that the collineations of a projective space of dimension at least $2$ come from semilinear bijections.
So semilinear maps are the natural symmetries of projective spaces, and linear maps alone do not give all of them when $K$ has nontrivial automorphisms.

### Watch out

An antilinear map is not linear over $\C$: it is linear over $\R$, but $T(iv) = -i\,T(v)$.
Semilinearity requires additivity as well as the twisted rule for scalars.
For [[sesquilinear forms|054YEQ0Y8M]] and inner products, conventions differ.
Mathematicians often make $\langle u, v \rangle$ antilinear in the second slot, while physicists make it antilinear in the first.

### Try it

First, is $T(z, w) = (\bar z + \bar w, \; \bar w)$ on $\C^2$ antilinear?
Yes: it is additive, and $T(\lambda z, \lambda w) = (\bar\lambda \bar z + \bar\lambda \bar w, \; \bar\lambda \bar w) = \bar\lambda\, T(z, w)$.

Second, if $S$ and $T$ are antilinear maps $\C^n \to \C^n$, what is $S \circ T$?
It is linear, since $S(T(\lambda v)) = S(\bar\lambda\, T(v)) = \bar{\bar\lambda}\, S(T(v)) = \lambda\, S(T(v))$.

## Explanations

### L1 human

A semilinear map respects sums, and it respects scalars up to a fixed twist of the field.
Over the complex numbers, the twist is usually complex conjugation, and the map is called antilinear.

### L2 human

To test whether $T$ is antilinear, check additivity and $T(\lambda v) = \bar\lambda\, T(v)$.
For $T(z, w) = (\bar w, \bar z)$ on $\C^2$, we get $T(i(z, w)) = (-i\bar w, -i\bar z) = -i\,T(z, w)$, so $T$ is antilinear.
Watch out: checking only real scalars is not enough, since every continuous additive map passes that test.

### L3 human

A $\sigma$-semilinear map $V \to W$ is the same as a linear map $V \to \sigma^* W$, where $\sigma^* W$ is $W$ with $\lambda$ acting as $\sigma(\lambda)$.
Through this, semilinear maps reduce to linear maps, and much of the theory transfers.
By the fundamental theorem of projective geometry, $P\Gamma L(V)$ is the full collineation group of $\mathbb P(V)$ when $\dim V \ge 3$.
The group $P\Gamma L(3, 4)$ is a maximal subgroup of the Mathieu group $M_{24}$.
The [[Riesz map|04GYPXDXNH]] $V \to V^*$ of a complex inner product space and the [[adjoint|0R9NMSM1ZP]] $T \mapsto T^*$ are the standard antilinear maps of functional analysis.
