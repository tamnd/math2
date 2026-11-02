---
tag: KEC5TGS9WM
kind: definition
name: Complete integral
msc: [35F20, 35A24]
defines: H90CS9B8YH
uses: [GC5BDZ6QBC, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_partial_differential_equation
---

## Definition

Let $U \subseteq \R^n$ and $A \subseteq \R^n$ be open sets, and let $F \colon \R^n \times \R \times U \to \R$ be a function.
Consider the first-order [[partial differential equation|GC5BDZ6QBC]] $F(\nabla u, u, x) = 0$ for $u \colon U \to \R$.
A *complete integral* of this equation is a function $u \colon U \times A \to \R$, written $u(x; a)$, such that:

1. $u$ is $C^2$ in $(x, a)$;
2. for each $a \in A$, the function $x \mapsto u(x; a)$ solves the equation on $U$;
3. for all $(x, a) \in U \times A$, the $n \times (n + 1)$ matrix
$$\big( D_a u \;\big|\; D^2_{xa} u \big) = \begin{pmatrix} u_{a_1} & u_{x_1 a_1} & \cdots & u_{x_n a_1} \\ \vdots & \vdots & & \vdots \\ u_{a_n} & u_{x_1 a_n} & \cdots & u_{x_n a_n} \end{pmatrix}$$
of [[partial derivatives|09EGC6F8PT]] has rank $n$.

## Remarks

Clause 3 says that $u$ depends on all $n$ parameters independently, so that no parameter can be removed by a change of the others.

Example: Clairaut's equation $x \cdot \nabla u + f(\nabla u) = u$, with $f \colon \R^n \to \R$ of class $C^2$, has the complete integral $u(x; a) = a \cdot x + f(a)$ for $a \in \R^n$.
Check: $\nabla u = a$, so $x \cdot a + f(a) = u$, and clause 2 holds.
For clause 3, $D^2_{xa} u$ is the identity matrix, so the matrix has rank $n$.

Non-example: for the equation $\partial_1 u = 0$ on $\R^2$, the family $u(x; a) = a_1 + a_2$ satisfies clauses 1 and 2 but not clause 3.
Indeed both rows of the matrix equal $(1, 0, 0)$, so its rank is $1$; the family really has only one parameter $a_1 + a_2$.
By contrast, $u(x; a) = a_1 + a_2 x_2$ is a complete integral of the same equation: the rows are $(1, 0, 0)$ and $(x_2, 0, 1)$.

Envelopes of subfamilies of a complete integral give further solutions, called general integrals, and the envelope of the whole family, when it exists, is a singular integral.
