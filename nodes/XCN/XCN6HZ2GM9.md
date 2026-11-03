---
tag: XCN6HZ2GM9
kind: statement
role: theorem
name: Classification of simple Lie algebras
msc: ["17B20", "17B22", "17B25"]
uses: [XDAXWHBNSZ, AR0D7V1J8T, CS73JZQS66, 9YTSFBHZKG, 1ZAT1Z967A, TQC9E2PE0T, ZGSAEYV8FX, 9QT1JR4KNY, 9YFX87K2VY, 250J3R9W97, G127K65CSX, B75K1ZJ1RE]
about: [XDAXWHBNSZ, CS73JZQS66]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_Lie_algebra
---

## Statement

Let $F$ be an algebraically closed field of characteristic $0$, such as $\C$.
Every finite-dimensional [[simple Lie algebra|XDAXWHBNSZ]] over $F$ is isomorphic to exactly one algebra in the following list:

1. $A_l = \mathfrak{sl}_{l+1}(F)$ for $l \ge 1$, of dimension $l(l+2)$;
2. $B_l = \mathfrak{so}_{2l+1}(F)$ for $l \ge 2$, of dimension $l(2l+1)$;
3. $C_l = \mathfrak{sp}_{2l}(F)$ for $l \ge 3$, of dimension $l(2l+1)$;
4. $D_l = \mathfrak{so}_{2l}(F)$ for $l \ge 4$, of dimension $l(2l-1)$;
5. one of the five exceptional algebras $E_6, E_7, E_8, F_4, G_2$, of dimensions $78, 133, 248, 52, 14$.

The index $l$ is the rank, and the algebra of each type has the connected [[Dynkin diagram|CS73JZQS66]] of the same name.

## Remarks

The proof has three steps.
First, a simple Lie algebra is determined up to isomorphism by its root system, which is irreducible, by the theorem on the [[root system of a semisimple Lie algebra|AR0D7V1J8T]].
Second, the connected Dynkin diagrams of root systems are exactly $A_l, B_l, C_l, D_l, E_6, E_7, E_8, F_4, G_2$; this is a combinatorial argument on positive definite quadratic forms.
Third, each of these root systems comes from a simple Lie algebra.
For the classical types one checks the matrix algebras [[special linear|1ZAT1Z967A]], [[orthogonal|TQC9E2PE0T]] and [[symplectic|ZGSAEYV8FX]], and in general [[Serre's theorem|9YTSFBHZKG]] builds the algebra from its Cartan matrix.
The bounds on $l$ remove repetitions: $B_1 \cong A_1$, $C_2 \cong B_2$, $D_3 \cong A_3$, while $D_1$ is abelian and $D_2 \cong A_1 \times A_1$ is not simple.
The exceptional algebras are [[E8|9QT1JR4KNY]], [[E7|9YFX87K2VY]], [[E6|250J3R9W97]], [[F4|G127K65CSX]] and [[G2|B75K1ZJ1RE]].
Over $\R$ or in positive characteristic the list is different.

## Explanations

### L1 human

The simple Lie algebras over the complex numbers fall into four infinite families of matrix algebras and five exceptional cases.
Nothing else exists.
This is one of the great classification results of mathematics, and it rests on drawing each algebra as a small diagram of dots and lines.

### L2 human

Through the Lie correspondence, the theorem also classifies the simply connected complex simple Lie groups and the simply connected compact simple Lie groups.
The simply laced diagrams of types $A$, $D$ and $E$ also classify the simple surface singularities and the quivers of finite representation type.
In a course it is the endpoint of the structure theory: Cartan subalgebra, roots, root system, base, Cartan matrix, Dynkin diagram.
