---
tag: 0NRYHJPQG2
kind: concept
name: Linear map
aliases: [linear-transformation]
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
uses: [000AYPA9AJ, 04C5ZBG1WT]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
  - book: isbn:9783031410253
    locator: Chapter 3
  - book: isbn:9780134860244
    locator: Section 2.1
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter Three, Section II
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: History
same_as:
  wikidata: Q207643
  wikipedia: Linear map
---

## Summary

Let $F$ be a [[field|04C5ZBG1WT]] and let $V$ and $W$ be [[vector spaces|000AYPA9AJ]] over $F$.
A *linear map* from $V$ to $W$ is a function $T \colon V \to W$ with two properties, for all $u, v \in V$ and all $a \in F$:
$$T(u + v) = T(u) + T(v) \quad \text{(additivity)}, \qquad T(av) = a\, T(v) \quad \text{(homogeneity)}.$$
The [[formal definition|0RJF668P1T]] states these two conditions.
Linear maps are the functions that respect the operations of a vector space, so they are the maps that linear algebra studies.
Matrices, derivatives, integrals and coordinate maps are all linear maps.

## Motivation

Many problems have the form "given $w$, find $v$ with $T(v) = w$".
For a linear system $Ax = b$ the function is $x \mapsto Ax$.
For the differential equation $y'' + y = f$ the function is $y \mapsto y'' + y$.
In both cases the function respects sums and scalar multiples.
This one property explains the shape of the solution set: one particular solution plus all solutions of $T(v) = 0$.
The concept of a linear map isolates this property and makes it the object of study.

## Notation

- We write $T \colon V \to W$, and often $Tv$ for $T(v)$.
- The terms "linear map", "linear mapping", "linear transformation", "linear operator" and "vector space homomorphism" name the same object in most books.
- Some books, for example Axler, reserve "operator" for a linear map from a space to itself, an [[endomorphism|0J7H0YBFDJ]].
- In functional analysis, "operator" often means a [[continuous linear map|03TM135G0N]], or a linear map defined only on a subspace.
- The set of all linear maps $V \to W$ is written $\Hom_F(V, W)$, $\mathcal{L}(V, W)$ or $L(V, W)$; see the [[space of linear maps|0X9MBPP2Z3]].
- In Mathlib, a linear map is a term of type `V →ₗ[F] W`, a structure `LinearMap` whose fields are the function and the two conditions.

## Remarks

### Examples

- For an $m \times n$ matrix $A$, the map $x \mapsto Ax$ from $F^n$ to $F^m$ is linear, and every linear map $F^n \to F^m$ has this form, by the [[theorem on matrix transformations|W6KB0J3SZZ]].
- Rotations, reflections, projections, shears and scalings of the plane are linear; the [[plane transformations example|~0b7363a3]] gives their matrices.
- Differentiation and integration of polynomials, shifts of sequences, evaluation at a point, the trace and the transpose are linear; see the [[examples of linear maps|0SS770NS8B]].
- The zero map $v \mapsto 0$ and the identity map $v \mapsto v$ are linear on every vector space.
- For a fixed scalar $c$, the map $v \mapsto cv$ is linear, because $c(u + v) = cu + cv$ and $c(av) = a(cv)$ by the axioms of a vector space.

### Non-examples

- A [[translation|~866bb5bd]] $v \mapsto v + w_0$ with $w_0 \ne 0$ fails both conditions, and it sends $0$ to $w_0 \ne 0$.
- The [[squaring map|~1498930f]] $x \mapsto x^2$ on $\R$ fails additivity, because $(1 + 1)^2 = 4$ but $1^2 + 1^2 = 2$.
- Complex conjugation $z \mapsto \bar z$ on $\C$ is additive, but it fails homogeneity over $\C$: it sends $i \cdot 1$ to $-i$, while $i \cdot \bar 1 = i$. It is a [[semilinear map|~8c967182]].
- The map $(x, y) \mapsto \sqrt[3]{x^3 + y^3}$ from $\R^2$ to $\R$ is homogeneous, but it fails additivity: $(1, 0)$ and $(0, 1)$ go to $1$ and $1$, while $(1, 1)$ goes to $\sqrt[3]{2} \ne 2$.
- The map $x \mapsto x^3$ on $\R$ is a bijection, but it [[is not linear|~cf936aba]].

### Basic properties

- A linear map sends $0$ to $0$, $-v$ to $-T(v)$, and each linear combination $\sum a_i v_i$ to $\sum a_i T(v_i)$, by the [[lemma on zero and linear combinations|~c10ad39e]].
- The two conditions together are equivalent to the single condition $T(au + v) = a T(u) + T(v)$ for all $u, v \in V$ and $a \in F$, by the same lemma.
- The [[composite of two linear maps is linear|~ed2e194c]], and the [[inverse of a bijective linear map is linear|~12368ba0]].
- The [[kernel|0S23E6YE83]] of a linear map is a subspace of $V$, and its [[image|0WSFKKT6FF]] is a subspace of $W$.
- A linear map is [[determined by its values on a basis|0R8X9XA83A]], and these values can be chosen freely.

### History

Linear substitutions of variables were used long before the abstract concept, for example in the theory of quadratic forms.
Cayley's memoir of 1858 on matrices treated a matrix as a linear transformation of variables.
Peano gave the first modern definition of a vector space and of a linear map in 1888.

### Common errors

- Calling $x \mapsto 2x + 1$ linear. Its graph is a line, but as a map $\R \to \R$ it is an [[affine map|0JF0TVYGWT]], because it sends $0$ to $1$.
- Checking only one of the two conditions. The non-examples above show that neither condition implies the other in general.
- Checking the conditions for a few chosen vectors only. A test on particular vectors can disprove linearity, but a proof needs arbitrary vectors and scalars.

## Explanations

### L1 human

A linear map is a rule that turns vectors into vectors and treats sums and scalings fairly.
When the input is doubled, the output is doubled.
When two inputs are added, their outputs are added.
For example, the rule "multiply by 3" on numbers is linear: $3 \cdot (2 + 5) = 21$ and $3 \cdot 2 + 3 \cdot 5 = 21$.
The rule "add 1" is not linear, because it sends $0$ to $1$, and a linear rule must send $0$ to $0$.

### L2 human

We show that $T \colon \R^3 \to \R^2$, $T(x, y, z) = (x + 2y,\ 3z - x)$, is linear.

1. Let $u = (x_1, y_1, z_1)$ and $v = (x_2, y_2, z_2)$. Then $T(u + v) = \bigl(x_1 + x_2 + 2(y_1 + y_2),\ 3(z_1 + z_2) - (x_1 + x_2)\bigr)$.
2. We regroup the terms: this equals $(x_1 + 2y_1,\ 3z_1 - x_1) + (x_2 + 2y_2,\ 3z_2 - x_2) = T(u) + T(v)$.
3. For $a \in \R$, $T(au) = (a x_1 + 2 a y_1,\ 3 a z_1 - a x_1) = a\,(x_1 + 2y_1,\ 3z_1 - x_1) = a\,T(u)$.
4. So $T$ is linear. For example, $T(1, 1, 1) = (3, 2)$, and $T$ is multiplication by the matrix $\begin{pmatrix} 1 & 2 & 0 \\ -1 & 0 & 3 \end{pmatrix}$.

The typical use is a check of this kind with general vectors, followed by the tools of linear algebra: kernel, image, matrix and rank.
To show that a map is not linear, one failing instance is enough, and the quickest test is often $T(0) \ne 0$.
The trap: $T(0) = 0$ does not prove linearity, because the squaring map sends $0$ to $0$ and is not linear.

### L3 human

Linear maps are the morphisms of the [[category|A2DE66937D]] of vector spaces over $F$.
Kernels, images, isomorphisms, direct sums and quotients are the categorical constructions in this category, and every short exact sequence in it splits.
The same definition over a ring gives the homomorphisms of [[modules|0NZ8JA25WK]], and the additivity condition alone gives a [[group homomorphism|0JYTG5K9Y4]] of the additive groups.
A [[semilinear map|~8c967182]] twists homogeneity by an automorphism of the field, and Mathlib takes this general form as its basic notion.
In analysis one adds continuity, which gives the [[continuous linear maps|03TM135G0N]] of normed spaces.
With bases, a linear map between finite-dimensional spaces becomes a [[matrix|0YQSGNYE3K]], and maps to the field itself form the [[dual space|07JBSZE0V4]].
