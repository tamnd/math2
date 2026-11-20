---
tag: 07JBSZE0V4
kind: concept
name: Dual space
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug1
specializes: [000AYPA9AJ]
uses: [07YQ1C78G0, 0X9MBPP2Z3, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Algebraic dual space
  - book: isbn:9783031410253
    locator: Section 3F
  - book: isbn:9780134860244
    locator: Section 2.6
  - book: isbn:9780387728285
    locator: Chapter 3
same_as:
  wikidata: Q752487
  wikipedia: Dual space
inventory: [X25E8AQW7R]
---

## Summary

Let $F$ be a field and let $V$ be a [[vector space|000AYPA9AJ]] over $F$.
The dual space of $V$ is the set $V^* = \Hom_F(V, F)$ of all [[linear forms|07YQ1C78G0]] on $V$, with the pointwise operations $(f + g)(v) = f(v) + g(v)$ and $(af)(v) = a f(v)$.
It is a vector space over $F$, as a case of the [[space of linear maps|0X9MBPP2Z3]].
The dual space turns questions about linear equations and coordinates into questions about vectors in a second space, and it is the base of all duality theory.

## Motivation

A vector is often known only through measurements: its coordinates, its components along given directions, or the values of linear equations at it.
Each such measurement is a linear form.
Measurements can be added and scaled, so they form a vector space of their own.
This space is the dual space.
Many facts about $V$ have a mirror image in $V^*$: subspaces of $V$ match subspaces of $V^*$, and linear maps $V \to W$ match linear maps $W^* \to V^*$.

## Notation

The dual space is written $V^*$, $V'$, $V^\vee$, $\Hom(V, F)$ or $\mathcal{L}(V, F)$.
In functional analysis, $V'$ or $V^*$ often means the continuous dual, which is a different space.
Elements of $V^*$ are called linear forms, linear functionals, dual vectors or covectors.
The value of $f \in V^*$ at $v \in V$ is written $f(v)$ or $\langle f, v \rangle$.
Mathlib writes `Module.Dual F V` for $V^*$.

## Remarks

### Examples

- [[Row vectors as linear forms|EGJXHX96R9]]: $(F^n)^*$ is isomorphic to the space of rows of length $n$, by $c \mapsto (x \mapsto cx)$.
- [[The dual of F^(N)|GZ627X1S7Y]]: the dual of the space of finitely supported sequences is the space $F^{\N}$ of all sequences.
- [[The trace pairing on matrices|4F7GWKTQ1H]]: $A \mapsto (X \mapsto \tr(AX))$ is an isomorphism from $M_n(F)$ onto $M_n(F)^*$.
- The dual of the zero space is the zero space, since the only map $\set{0} \to F$ sends $0$ to $0$.
- The dual of $F$, as a vector space over itself, is $F$: each linear form on $F$ is $x \mapsto cx$ with $c = f(1)$.

### Non-examples

- [[The affine functions on R^2|FWNY6EYBC3]] form a vector space of dimension $3$, but they are not the dual space: the constant function $1$ is not linear.
- The space of all functions $\R^2 \to \R$ is not $(\R^2)^*$: it contains $(x, y) \mapsto xy$, which is not additive.
- The space $V$ itself is not $V^*$, even when the two have the same dimension. An isomorphism $V \to V^*$ needs a choice, as the [[basis-dependent isomorphism of R^2 and its dual|A3CP855PNV]] shows.

### Basic properties

- If $\dim V = n$ is finite, then $\dim V^* = n$, by the theorem on the [[dimension of the dual space|00889YD15K]]. A basis of $V$ gives the [[dual basis|0ZD2CF6ZS0]] of $V^*$.
- If $V$ is infinite-dimensional, then $\dim V^* > \dim V$, by the [[Erdős-Kaplansky theorem|S5ET1HG2ZX]].
- The evaluation map $V \to V^{**}$ is injective, and it is an isomorphism exactly when $V$ is finite-dimensional, by the theorem on the [[double dual|0ZJM9D7NPS]].
- Each subspace $U$ of $V$ has an [[annihilator|0ASHNYF7AG]] $U^0 \subseteq V^*$, and in finite dimension $\dim U + \dim U^0 = \dim V$.
- Each linear map $f \colon V \to W$ has a [[dual map|0AZ5ARP287]] $f^* \colon W^* \to V^*$, and $(g \circ f)^* = f^* \circ g^*$.
- If $V$ has a basis $B$, then $f \mapsto (f(b))_{b \in B}$ is an isomorphism $V^* \to F^B$, by the [[theorem on bases|0R8X9XA83A]].

### History

In the tensor calculus of Ricci and Levi-Civita (1900), quantities with lower indices, the covariant components, play the role of elements of the dual space.
Riesz and Fréchet showed in 1907 that the continuous linear forms on the space of square-integrable functions come from inner products.
The algebraic dual space of an arbitrary vector space, with no topology, became standard in the linear algebra books of the twentieth century.

### Common errors

- Thinking that $V^*$ is "the same as" $V$. In finite dimension they are isomorphic, but no isomorphism is preferred, and in infinite dimension they are not isomorphic.
- Thinking that the coordinate forms of an infinite basis are a basis of $V^*$. They are linearly independent, but they [[do not span V*|JCMJDY59CH]].
- Confusing the algebraic dual of this page with the continuous dual of a normed space.

## Explanations

### L1 human

The dual space of a space of vectors is the space of all linear "measuring rules" on those vectors.
On the plane, the rule "$3$ times the first coordinate plus the second" is one element of the dual space.
Two rules can be added: the sum of the rules $x$ and $y$ is the rule $x + y$.
A rule can be scaled: $5$ times the rule $x$ is the rule $5x$.
So the measuring rules form a space, and on the plane this space is again two-dimensional.

### L2 human

We find a basis of the dual space of $P_1(\R)$, the polynomials $a + bx$, and write a given form in it.

1. A form $f$ on $P_1(\R)$ is fixed by $f(1)$ and $f(x)$, because $1, x$ is a basis.
2. Let $\varphi_0(a + bx) = a$ and $\varphi_1(a + bx) = b$. These are linear forms, and $f = f(1)\varphi_0 + f(x)\varphi_1$.
3. So $\varphi_0, \varphi_1$ span $P_1(\R)^*$. They are independent, since $\varphi_i$ is $1$ at one basis vector and $0$ at the other.
4. Take $f(p) = \int_0^2 p(t)\,dt$. Then $f(1) = 2$ and $f(x) = 2$, so $f = 2\varphi_0 + 2\varphi_1$.
5. Check on $p = 3 + x$: directly $\int_0^2 (3 + t)\,dt = 6 + 2 = 8$, and $2 \cdot 3 + 2 \cdot 1 = 8$.

The typical use of the dual space is to describe a subspace by equations, that is, by the forms that vanish on it.
A trap: in infinite dimension, a form need not be a finite combination of coordinate forms.

### L3 human

The dual space is the contravariant functor $\Hom(-, F)$ on vector spaces, applied to $V$.
It turns direct sums into products: $(\bigoplus_i V_i)^* \cong \prod_i V_i^*$, which explains why duals of infinite-dimensional spaces are large.
In finite dimension, $V^* \otimes W \cong \Hom(V, W)$, and the [[tensor product|0BF2DE2SYK]] and the dual space together give all of multilinear algebra.
A [[nondegenerate bilinear form|01NHFZF2SK]] $V \times V \to F$ is the same as an isomorphism $V \to V^*$, and an inner product is such a form; this is the [[Riesz representation|04GYPXDXNH]] in finite dimension.
In functional analysis, one replaces $V^*$ by the [[continuous dual space|4A82S5FVRT]], which keeps the good duality properties for Banach and Hilbert spaces.
