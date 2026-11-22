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

A linear map is a function between [[vector spaces|000AYPA9AJ]] that respects the two operations, addition and scaling.
It is the kind of function that linear algebra studies, in the same way that continuous functions are the subject of topology.
Let $F$ be a [[field|04C5ZBG1WT]] and let $V$ and $W$ be vector spaces over $F$.
A *linear map* from $V$ to $W$ is a function $T \colon V \to W$ such that, for all $u, v \in V$ and all $a \in F$,
$$T(u + v) = T(u) + T(v) \quad \text{(additivity)}, \qquad T(av) = a\, T(v) \quad \text{(homogeneity)}.$$
The [[formal definition|0RJF668P1T]] states these two conditions.
An equivalent single condition is $T(au + v) = a\,T(u) + T(v)$ for all $u, v \in V$ and $a \in F$.

## Motivation

Many problems in mathematics have the form "given $w$, find $v$ with $T(v) = w$".
For a linear system $Ax = b$ the function is $x \mapsto Ax$, and for the differential equation $y'' + y = f$ it is $y \mapsto y'' + y$.
In both cases the function respects sums and scalar multiples.
That one property explains the shape of the solutions: one particular solution plus all solutions of $T(v) = 0$.
So it pays to study the property once, in general, and the concept of a linear map does exactly that.

Linear maps appear well outside algebra.
In physics, a linear medium is one where the response to two causes is the sum of the two responses, which is the principle of superposition.
In computing, every rotation, scaling and projection of a picture on the screen is a linear map of the coordinates.
In the rest of the area, linear maps return as [[matrices|0YQSGNYE3K]] once bases are fixed, as the maps to the field that make up the [[dual space|07JBSZE0V4]], and as the maps whose eigenvalues the spectral theory studies.

## Notation

We write $T \colon V \to W$, and often $Tv$ for $T(v)$.
The names "linear map", "linear mapping", "linear transformation", "linear operator" and "vector space homomorphism" mean the same object in most books.
Some books, such as Axler, keep the word "operator" for a linear map from a space to itself, an [[endomorphism|0J7H0YBFDJ]], and in functional analysis an "operator" is often a [[continuous linear map|03TM135G0N]].
The set of all linear maps $V \to W$ is written $\Hom_F(V, W)$, $\mathcal{L}(V, W)$ or $L(V, W)$, and it is itself a vector space, the [[space of linear maps|0X9MBPP2Z3]].
In Mathlib a linear map is a term of type `V →ₗ[F] W`, a structure `LinearMap` that packs the function with the two conditions.

## Remarks

### A first check

Take $T \colon \R^2 \to \R^2$ with $T(x, y) = (2x + y, \; x - 3y)$, and test both conditions on concrete vectors first.
For $u = (1, 2)$ and $v = (3, -1)$ we get $T(u) = (4, -5)$ and $T(v) = (5, 6)$.
The sum is $u + v = (4, 1)$, and
$$T(4, 1) = (8 + 1, \; 4 - 3) = (9, 1) = (4, -5) + (5, 6).$$
For the scalar $a = 3$ we get $T(3u) = T(3, 6) = (12, -15) = 3\,T(u)$.
A test on particular vectors can only disprove linearity.
For a proof we repeat the computation with letters: each entry of $T(x, y)$ is a sum of constant multiples of $x$ and $y$, and such expressions split over sums and pull out scalars.

### Where linear maps come from

The main source is matrices: for an $m \times n$ matrix $A$, the map $x \mapsto Ax$ from $F^n$ to $F^m$ is linear.
The [[theorem on matrix transformations|W6KB0J3SZZ]] shows that every linear map $F^n \to F^m$ has this form.
Geometry gives the [[rotations, reflections, projections and shears of the plane|5BXHREC8C8]].
Calculus gives differentiation and integration of polynomials, and sequences give the shift maps; the [[examples of linear maps|0SS770NS8B]] work these out, together with evaluation at a point, the trace and the transpose.
On every space there are also the zero map $v \mapsto 0$, the identity $v \mapsto v$ and, for a fixed scalar $c$, the scaling $v \mapsto cv$.
The scaling is linear because $c(u + v) = cu + cv$ and $c(av) = a(cv)$ are axioms of a vector space.

### What fails to be linear

A [[translation|DTCM6N02A9]] $v \mapsto v + w_0$ with $w_0 \ne 0$ moves the origin, so it fails both conditions.
The [[squaring map|RMC0D67M01]] on $\R$ fixes the origin but fails additivity, since $(1 + 1)^2 = 4$ and $1^2 + 1^2 = 2$.
The map $x \mapsto x^3$ is a bijection of $\R$, but [[it is not linear either|T4286X5GA4]].

Neither condition implies the other, and two maps show it.
Complex conjugation $z \mapsto \bar z$ on $\C$ is additive, but $\overline{i \cdot 1} = -i$ while $i \cdot \bar 1 = i$, so it fails homogeneity over $\C$; it is a [[semilinear map|BNPDDM95KF]].
The map $(x, y) \mapsto \sqrt[3]{x^3 + y^3}$ from $\R^2$ to $\R$ is homogeneous, because a real cube root pulls out a real factor $a$.
It fails additivity: $(1, 0)$ and $(0, 1)$ both go to $1$, while their sum $(1, 1)$ goes to $\sqrt[3]{2} \ne 2$.

### The rules you get for free

The two conditions have many consequences, and the [[lemma on zero and linear combinations|STYEWH8R4E]] collects the first ones.
A linear map sends $0$ to $0$ and $-v$ to $-T(v)$, and it sends each linear combination $\sum a_i v_i$ to $\sum a_i T(v_i)$.
The [[composite of two linear maps is linear|FSXBBV9C76]], and the [[inverse of a bijective linear map is linear|E08G7CVKPK]].
The vectors that go to $0$ form a subspace, the [[kernel|0S23E6YE83]], and the values form a subspace, the [[image|0WSFKKT6FF]].
Finally, a linear map is [[determined by its values on a basis|0R8X9XA83A]], and these values can be chosen freely.

### Watch out

In school, $x \mapsto 2x + 1$ is a "linear function" because its graph is a line.
In linear algebra it is not linear, since it sends $0$ to $1$; it is an [[affine map|0JF0TVYGWT]].
The second trap is to check only one condition: complex conjugation and the cube-root map above each pass one condition and fail the other.
The third trap is to check a few chosen vectors and stop: the map $(x, y) \mapsto \sqrt[3]{x^3 + y^3}$ passes the test for $u = v = (1, 1)$, but it is not linear.

### History

Linear substitutions of variables were in use long before the abstract concept, for example in the theory of quadratic forms.
Cayley's memoir of 1858 on matrices introduced a matrix as a short notation for a linear transformation of variables.
Peano gave the first modern axiomatic definition of a vector space and of a linear map in 1888.

### Try it

First, is $T(x, y) = (y, \; 0)$ on $\R^2$ linear?
Yes: both entries are sums of constant multiples of $x$ and $y$, and $T$ is multiplication by $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

Second, is $S(x, y) = (xy, \; x)$ linear?
No: $S(1, 1) = (1, 1)$ but $S(2, 2) = (4, 2) \ne 2\,S(1, 1) = (2, 2)$, so homogeneity fails.

## Explanations

### L1 human

A linear map is a rule that turns vectors into vectors and treats sums and scalings fairly.
When the input is doubled, the output is doubled.
When two inputs are added, their outputs are added.
For example, "multiply by 3" on numbers is linear: $3 \cdot (2 + 5) = 21$ and $3 \cdot 2 + 3 \cdot 5 = 21$.
The rule "add 1" is not linear, because it sends $0$ to $1$, and a linear rule must send $0$ to $0$.

### L2 human

Here is a typical check: is $T \colon \R^3 \to \R^2$, $T(x, y, z) = (x + 2y, \; 3z - x)$, linear?
Take $u = (x_1, y_1, z_1)$ and $v = (x_2, y_2, z_2)$, add them first and then apply $T$:
$$T(u + v) = \bigl(x_1 + x_2 + 2(y_1 + y_2), \; 3(z_1 + z_2) - (x_1 + x_2)\bigr).$$
Regroup the terms by vector:
$$T(u + v) = (x_1 + 2y_1, \; 3z_1 - x_1) + (x_2 + 2y_2, \; 3z_2 - x_2) = T(u) + T(v).$$
For a real $a$, the factor $a$ comes out of every term, so $T(au) = a\,T(u)$.
So $T$ is linear, and in fact it is multiplication by the matrix $\begin{pmatrix} 1 & 2 & 0 \\ -1 & 0 & 3 \end{pmatrix}$.
Check: $T(1, 1, 1) = (3, 2)$, and the rows of the matrix give $1 + 2 + 0 = 3$ and $-1 + 0 + 3 = 2$.
Once linearity is known, the tools of the area apply: kernel, image, matrix and rank.
To show that a map is not linear, one failing instance is enough, and the quickest test is often $T(0) \ne 0$.
Watch out: $T(0) = 0$ does not prove linearity, since the squaring map fixes $0$.

### L3 human

Linear maps are the morphisms of the [[category|A2DE66937D]] of vector spaces over $F$.
Kernels, images, direct sums and quotients are the usual constructions in this category, and every short exact sequence in it splits.
The same definition over a ring gives the homomorphisms of [[modules|0NZ8JA25WK]], and additivity alone gives a [[group homomorphism|0JYTG5K9Y4]] of the additive groups.
A [[semilinear map|BNPDDM95KF]] twists homogeneity by an automorphism of the field, and Mathlib takes this twisted form as its basic notion.
In analysis one adds continuity, which gives the [[continuous linear maps|03TM135G0N]] of normed spaces.
With bases, a linear map between finite-dimensional spaces becomes a [[matrix|0YQSGNYE3K]], and the sub-area on matrices of linear maps builds this dictionary.
