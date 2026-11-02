---
tag: 9P8VK3H4YZ
kind: statement
role: theorem
name: Cartan's classification of symmetric spaces
msc: [53C35, 17B20]
uses: [PAA93R4WYD, 7CBT4SM83Y, WHDZ3MK56B]
about: [PAA93R4WYD]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_space
---

## Statement

1. Every simply connected Riemannian [[symmetric space|PAA93R4WYD]] is isometric to a Riemannian product $\R^k \times M_1 \times \cdots \times M_r$ of a Euclidean space and irreducible simply connected symmetric spaces $M_i$.
2. Every irreducible simply connected symmetric space other than $\R$ is of one of two types.
   Those of *compact type* are compact and have nonnegative sectional curvature.
   Those of *noncompact type* have nonpositive sectional curvature and are diffeomorphic to a Euclidean space.
3. There is a duality between irreducible simply connected symmetric spaces of compact type and of noncompact type.
   On Lie algebras it replaces $\mathfrak{g} = \mathfrak{k} \oplus \mathfrak{p}$ by $\mathfrak{k} \oplus i\mathfrak{p}$.
4. Up to scaling, the irreducible symmetric spaces of noncompact type are the quotients $G/K$.
   Here $G$ is a connected noncompact simple Lie group with trivial center and $K$ is a maximal compact subgroup.
   These spaces correspond bijectively to the isomorphism classes of noncompact real simple Lie algebras.

## Remarks

Statement 1 is the de Rham decomposition applied to symmetric spaces.
The rest reduces geometry to algebra: the symmetric space is determined by its symmetric Lie algebra $(\mathfrak{g}, \sigma)$, where $\sigma$ is the involution coming from the geodesic symmetry.
Using Cartan's classification of real simple Lie algebras, the list of irreducible noncompact type spaces consists of two kinds.
The first kind is $G_{\C}/G_u$ for a complex simple Lie group $G_{\C}$ with compact real form $G_u$.
The second kind comes from the noncompact real forms of the complex simple Lie algebras: seven infinite families labelled AI, AII, AIII, BDI, DIII, CI, CII and twelve exceptional spaces.

Examples: the hyperbolic space $H^n = SO_0(n, 1)/SO(n)$ is of noncompact type, and its dual is the sphere $S^n = SO(n+1)/SO(n)$.
The space $SL(n, \R)/SO(n)$ of positive definite symmetric matrices of determinant $1$ is of type AI.

## Explanations

### L1 human

Symmetric spaces look the same from every point, and there are surprisingly few of them.
Apart from flat space, every one is built from pieces that are either curved like a sphere or curved like hyperbolic space.
These pieces come in pairs and are listed completely by a finite table plus a few infinite families.

### L2 human

The classification turns a question in Riemannian geometry into the classification of simple Lie algebras and their involutions.
Symmetric spaces of noncompact type are the spaces on which arithmetic groups act, as in locally symmetric spaces $\Gamma \backslash G/K$.
The compact type includes the Grassmannians and the compact simple Lie groups with a bi-invariant metric.
For a simply connected symmetric space $G/K$ without Euclidean factor, the [[holonomy|WHDZ3MK56B]] group is $K$ acting on the tangent space.
This is why symmetric spaces appear as a separate case in Berger's list.
