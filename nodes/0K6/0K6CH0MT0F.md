---
tag: 0K6CH0MT0F
kind: concept
name: Alternating multilinear map
aliases: [alternating-form, alternating-n-linear-form]
msc: ["15A69", "15A75"]
topics: [DTBK11SR77]
audience: ug2
specializes: [0443XNARDV]
uses: [0443XNARDV, 0NZ8JA25WK, 0310REJJY8, 0CRMGPAH83]
sources:
  - url: https://en.wikipedia.org/wiki/Alternating_multilinear_map
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
same_as:
  wikidata: Q4736615
  wikipedia: Alternating multilinear map
---

## Summary

Let $K$ be a [[commutative ring|0310REJJY8]], let $M$ and $N$ be [[modules|0NZ8JA25WK]] over $K$, and let $n \ge 1$.
A map $f \colon M^n \to N$ is an *alternating multilinear map* when two conditions hold.
First, $f$ is [[multilinear|0443XNARDV]]: it is $K$-linear in each argument when the other arguments are fixed.
Second, $f(v_1, \dots, v_n) = 0$ whenever $v_i = v_j$ for some $i \neq j$.
When $N = K$ the map is an *alternating $n$-linear form*.
The idea matters because the [[determinant|00KDZRW4C0]] is the alternating $n$-linear form on $K^n$ with value $1$ on the standard basis, and alternating forms measure signed volume.

## Motivation

The signed area of a parallelogram in the plane has three simple properties.
It is linear in each side, it is zero when the two sides are equal, and it is $1$ for the unit square.
These properties already fix the area formula $u_1 v_2 - u_2 v_1$.
Alternating multilinear maps are the maps with the first two properties, in any number of arguments.
They give a definition of the determinant that does not depend on a formula.

## Notation

The alternating $n$-linear maps $M^n \to N$ form a $K$-module, often written $\operatorname{Alt}^n(M; N)$ or $L^n_a(M; N)$.
For $N = K$ one writes $\operatorname{Alt}^n(M)$; it is the dual of the top exterior power $\Lambda^n M$ when $M$ is free of rank $n$.
Some books write "skew-symmetric" or "antisymmetric" for the sign rule of the [[antisymmetry theorem|VJZVSTWYYW]].
That rule is weaker than "alternating" in characteristic $2$.

## Remarks

### Examples

- The signed area $\omega(u, v) = u_1 v_2 - u_2 v_1$ on $\mathbb{R}^2$. It is bilinear, and $\omega(u, u) = 0$; see the [[worked example|VFFVMRTVRZ]].
- The [[scalar triple product|059Q2XWJDC]] $(u, v, w) \mapsto u \cdot (v \times w)$ on $\mathbb{R}^3$. It is trilinear and vanishes when two vectors are equal; see the [[second example|DT0H0YQ4H7]].
- The [[determinant|00KDZRW4C0]] of the rows of an $n \times n$ matrix, as a map $(K^n)^n \to K$.
- The [[cross product|0N5N15HWZ7]] $(u, v) \mapsto u \times v$ from $(\mathbb{R}^3)^2$ to $\mathbb{R}^3$. It is bilinear and $u \times u = 0$.
- For $k \le n$ and fixed columns $j_1 < \dots < j_k$, the map that sends $k$ vectors of $K^n$ to the determinant of their entries in these columns. This is an alternating $k$-linear form on $K^n$.
- The zero map $M^n \to N$.

### Non-examples

- The [[dot product|0S52TNNTH9]] on $\mathbb{R}^2$ is bilinear but not alternating, because $e_1 \cdot e_1 = 1 \neq 0$.
- The form $f(x, y) = xy$ on the field $\mathbb{F}_2$ is antisymmetric but not alternating, because $f(1, 1) = 1$; see the [[non-example|QFAWSF1A04]].
- The permanent $\operatorname{perm}\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad + bc$ is multilinear in the rows, but it is $2$ on the matrix with two rows $(1, 1)$.
- The map $(u, v) \mapsto u_1 v_2 - u_2 v_1 + 1$ is not multilinear, because it is not $0$ when $u = 0$.

### Basic properties

- An alternating map changes sign when two arguments are exchanged, and $f(v_{\sigma(1)}, \dots, v_{\sigma(n)}) = \sgn(\sigma) f(v_1, \dots, v_n)$. The converse holds when $2$ is not a zero divisor on $N$, so outside characteristic $2$ for vector spaces. See the [[antisymmetry theorem|VJZVSTWYYW]].
- An alternating map is zero on each family in which one vector is a linear combination of the others. Over a field it is zero on each [[linearly dependent|0CRMGPAH83]] family, by the same theorem.
- So on a vector space of dimension $n$, each alternating $k$-linear map with $k > n$ is zero.
- The alternating $n$-linear forms on $K^n$ form a free $K$-module of rank $1$, with the Leibniz form as a basis. This is the [[existence and uniqueness theorem|1C8RRWHD45]].

### Common errors

- Reading "alternating" as "antisymmetric". In characteristic $2$ the two notions differ, as the form $xy$ on $\mathbb{F}_2$ shows.
- Treating a multilinear map as a linear map on $M^n$. For example $f(2u, 2v) = 4 f(u, v)$ for a bilinear map, not $2 f(u, v)$.
- Thinking that the values must alternate in sign. The word refers only to the sign change under an exchange of two arguments.

## Explanations

### L1 human

An alternating map takes several vectors and gives a number, or a vector.
It grows in proportion when one input grows, and it adds up when one input is a sum.
It gives zero when two inputs are equal.
The signed area of a parallelogram is the standard example.
For the sides $(2, 0)$ and $(0, 3)$ the area is $6$, and for two equal sides the area is $0$.

### L2 human

We check that $\omega(u, v) = u_1 v_2 - u_2 v_1$ is alternating and bilinear on $\mathbb{R}^2$.

1. For fixed $v$, the map $u \mapsto u_1 v_2 - u_2 v_1$ is a linear combination of the coordinates of $u$, so it is linear.
2. For fixed $u$, the map $v \mapsto u_1 v_2 - u_2 v_1$ is linear for the same reason.
3. $\omega(u, u) = u_1 u_2 - u_2 u_1 = 0$, so $\omega$ is alternating.
4. Then $\omega(v, u) = -\omega(u, v)$, by the [[antisymmetry theorem|VJZVSTWYYW]]; directly, $v_1 u_2 - v_2 u_1 = -(u_1 v_2 - u_2 v_1)$.

The typical use is to prove that a formula equals a determinant: check that it is multilinear, alternating and $1$ on the standard basis.
A trap: a symmetric form such as the dot product is never alternating unless it is zero, because $f(u, u) = 0$ for all $u$ forces $f(u, v) = -f(v, u) = -f(u, v)$, so $2 f(u, v) = 0$.

### L3 human

The alternating $k$-linear maps $M^k \to N$ correspond to the linear maps $\Lambda^k M \to N$, where $\Lambda^k M$ is the $k$-th exterior power of $M$.
This universal property defines the exterior algebra, which belongs to [[exterior algebra|3BHDPE74HF]] and is only named here.
For $M$ free of rank $n$, the module $\Lambda^n M$ is free of rank $1$, and the determinant of an endomorphism is the scalar by which it acts on this line.
On manifolds, alternating forms on the tangent spaces are the differential forms, and integration of top forms extends the volume of parallelotopes.
