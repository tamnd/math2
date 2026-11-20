---
tag: 00BKRZKMSS
kind: concept
name: Composition of linear maps
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
uses: [0NRYHJPQG2, 0THBK9V825]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
  - book: isbn:9780134860244
    locator: Section 2.3
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Summary

The composition of two [[linear maps|0NRYHJPQG2]] $S \colon U \to V$ and $T \colon V \to W$ is the map $T \circ S \colon U \to W$ that applies $S$ first and then $T$.
It is again a linear map.
For matrix transformations, composition is the product of the matrices.

## Motivation

Many maps are built in stages: rotate, then reflect, then project.
To study the result, we need the composite of the stages as a single map.
Composition is also the reason for the definition of matrix multiplication.
Cayley chose the product of matrices so that it describes two linear substitutions done one after the other.

## Notation

The composite is written $T \circ S$, or $TS$ when the maps are linear.
The notation $TS$ means "first $S$, then $T$", which matches the order of the product of matrices.
For a map $T \colon V \to V$, the powers are $T^0 = \id_V$, $T^1 = T$ and $T^{k+1} = T \circ T^k$.

## Remarks

### Examples

- [[A rotation and a reflection of the plane|~a7ff7d55]]: the two orders give two different reflections.
- [[Differentiation and integration of polynomials|~71de384c]]: $D \circ J$ is the identity, but $J \circ D$ is not.
- The composite of the [[matrix transformations|W6KB0J3SZZ]] $x \mapsto Bx$ and $y \mapsto Ay$ is $x \mapsto (AB)x$.

### Non-examples

- [[The pointwise product of two linear maps|~8cc2e580]] is not their composite, and it is not linear.
- Composition is defined only when the target of $S$ is the source of $T$. For $S \colon \R^2 \to \R^3$ and $T \colon \R^2 \to \R^2$, the composite $T \circ S$ does not exist.

### Basic properties

- The composite of two linear maps is linear, by the [[theorem on composites|~ed2e194c]].
- Composition is associative: $(R \circ T) \circ S = R \circ (T \circ S)$. This holds for all [[functions|0THBK9V825]].
- The identity maps are neutral: $T \circ \id_V = T = \id_W \circ T$.
- Composition is bilinear: $T \circ (S_1 + S_2) = T \circ S_1 + T \circ S_2$, $(T_1 + T_2) \circ S = T_1 \circ S + T_2 \circ S$, and scalars move out of each factor.
- In finite dimension with chosen bases, the [[matrix of a composite is the product of the matrices|05Q1B7MH0M]].
- Composition is not commutative in general, even for maps $V \to V$.

### History

Cayley introduced matrices in 1858 and defined their product as the composite of two linear substitutions.
Peano gave the abstract definition of a linear map in 1888, and composition then became the product in the [[algebra of endomorphisms|~42300f41]].

### Common errors

- Reading $T \circ S$ from left to right. The map on the right acts first.
- Assuming $T \circ S = S \circ T$. Even for $2 \times 2$ matrices, $AB \ne BA$ in general.
- Confusing the composite with the pointwise product. Only the composite is defined for general vector spaces.

## Explanations

### L1 human

To compose two linear maps, apply one and then the other.
The result is again a linear map.
For example, rotating the plane by a right angle twice gives the rotation by a half turn, which is the map $v \mapsto -v$.

### L2 human

For $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$, apply $B$ first and then $A$ to $x = (1, 1)$.

1. $Bx = (2, 1)$.
2. $A(2, 1) = (3, 1)$.
3. The product is $AB = \begin{pmatrix} 2 & 1 \\ 0 & 1 \end{pmatrix}$, and $AB\,x = (3, 1)$, as in step 2.

The other order gives $BA = \begin{pmatrix} 2 & 2 \\ 0 & 1 \end{pmatrix}$ and $BA\,x = (4, 1)$.
The trap is to forget that the order of the factors matters.

### L3 human

Vector spaces over $F$ and linear maps form a category, with composition as the operation on arrows.
Bilinearity of composition makes this category enriched over vector spaces: each $\Hom(U, V)$ is a vector space.
For $V = W = U$, composition is the multiplication of the [[algebra of endomorphisms|~42300f41]].
In Mathlib the composite of `g` and `f` is written `g.comp f` or `g ∘ₗ f`.
