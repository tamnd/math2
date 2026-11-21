---
tag: 1MDT9BF81H
kind: concept
name: Cylindric algebra
aliases: [cylindric-algebra]
msc: ["03G15"]
topics: [QYA4H5Y7VR]
audience: research
specializes: [0XADJKM699]
uses: [RKCSWWVYTC, 0XADJKM699, 086QKPF0A6, QC9M3Q8B8Q, 3H85NSFWHK]
sources:
  - url: https://en.wikipedia.org/wiki/Cylindric_algebra
    locator: Definition; Generalizations
  - book: isbn:9780720420432
  - book: isbn:9780444876799
same_as:
  wikidata: Q5199278
  wikipedia: Cylindric algebra
---

## Summary

A cylindric algebra is a [[Boolean algebra|0XADJKM699]] with operations $c_\kappa$ that model existential quantifiers and constants $d_{\kappa\lambda}$ that model equality of variables; see [[the definition|RKCSWWVYTC]].
They do for [[first-order logic|086QKPF0A6]] with equality what Boolean algebras do for propositional logic.
The cylindrification $c_\kappa$ plays the role of "there exists $v_\kappa$", and the diagonal element $d_{\kappa\lambda}$ plays the role of the formula $v_\kappa = v_\lambda$.
The main models are the cylindric set algebras of subsets of $U^\alpha$, and the algebras that are isomorphic to subdirect products of these are called representable.
The formulas of a first-order theory modulo provable equivalence form a locally finite cylindric algebra, and every such algebra is representable.

## Motivation

A first-order formula $\varphi(v_0, v_1, \dots)$ defines, in a structure with universe $U$, the set of assignments $s \in U^\alpha$ that satisfy it.
The connectives act on these sets as the Boolean operations.
The quantifier $\exists v_\kappa$ acts by projecting along coordinate $\kappa$ and then extending back to a cylinder.
Cylindric algebras axiomatize the laws of these operations by finitely many equation schemas, without syntax.

## Notation

We write $\mathbf{CA}_\alpha$ for the class of cylindric algebras of dimension $\alpha$, and $(A, +, \cdot, -, 0, 1, c_\kappa, d_{\kappa\lambda})_{\kappa, \lambda < \alpha}$ for one of them.
The dimension set of $x$ is $\Delta x = \set{\kappa < \alpha : c_\kappa x \ne x}$.
An algebra is *locally finite* if $\Delta x$ is finite for each $x$; the class is $\mathbf{Lf}_\alpha$.
$\mathbf{Cs}_\alpha$ is the class of cylindric set algebras, and $\mathbf{RCA}_\alpha$ the class of algebras isomorphic to subdirect products of members of $\mathbf{Cs}_\alpha$.

## Remarks

### Examples

1. [[The full cylindric set algebra of dimension $2$ on $\set{0, 1}$|CSKAYE1PA7]], with $16$ elements.
2. [[The cylindric algebra of a first-order theory|5MH9ZKCEHV]], which is locally finite of dimension $\omega$.
3. The full cylindric set algebra $\mathcal{P}(U^\alpha)$ for a nonempty set $U$.
4. Every Boolean algebra, with $c_\kappa x = x$ and $d_{\kappa\lambda} = 1$. It is a subalgebra of a power of the set algebra on a one-element $U$.
5. For $\alpha = 1$, the cylindric algebras are the monadic algebras: Boolean algebras with one closure operator $c$ whose image is a Boolean subalgebra. They are the [[modal algebras|3H85NSFWHK]] of S5, with $c$ as $\Diamond$.

### Non-examples

1. [[The power set of the real line with topological closure|TCA8AZBXRC]] fails the axiom $c(x \cdot c y) = c x \cdot c y$.
2. On a Boolean algebra with $0 \ne 1$, the operation $c_\kappa x = 0$ fails $x \le c_\kappa x$ at $x = 1$.
3. On a Boolean algebra with $0 \ne 1$, the operation $c_\kappa x = 1$ fails $c_\kappa 0 = 0$.

### Basic properties

1. Each $c_\kappa$ is additive, monotone and idempotent, and $c_\kappa(-c_\kappa x) = -c_\kappa x$. So the fixed points of $c_\kappa$ form a Boolean subalgebra.
2. $\mathbf{CA}_\alpha$ is a variety of Boolean algebras with operators, defined by finitely many equation schemas.
3. Every algebra in $\mathbf{Lf}_\alpha$ with $\alpha \ge \omega$ is representable; this is the algebraic form of the completeness theorem. See [[this theorem|WZ1BZYVD5G]].
4. For $\alpha \ge 3$, $\mathbf{RCA}_\alpha$ is a variety and a proper subclass of $\mathbf{CA}_\alpha$. For finite $\alpha \ge 3$, it is not finitely axiomatizable.
5. The [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of a first-order theory, built on formulas with free variables, is a locally finite cylindric algebra.

### History

Tarski introduced cylindric algebras as the algebraic counterpart of first-order logic with equality.
Henkin, Monk and Tarski wrote the standard monograph, in two parts that appeared in 1971 and 1985.
Andréka, Németi and their school later developed the theory further, in particular the study of the representable algebras.

### Common errors

1. Assuming that every cylindric algebra is representable. This fails for every dimension $\alpha \ge 3$.
2. Treating $c_\kappa$ as an arbitrary closure operator. Its image must be a Boolean subalgebra, which fails for topological closure.
3. Forgetting the diagonal elements. Without them, the algebras model first-order logic without equality, and their theory changes.

## Explanations

### L1 human

Think of the set of points of the plane that satisfy a formula $\varphi(x, y)$.
The formula "there exists $x$ such that $\varphi(x, y)$" describes the set swept out when that region is moved along the $x$-direction: a cylinder over the shadow of the region.
That is why the operation is called cylindrification.
The diagonal line $\set{(x, y) : x = y}$ is the set of the formula $x = y$.
A cylindric algebra keeps only the rules that these operations obey, so it can be studied with algebra.

### L2 human

1. Take $U = \set{0, 1}$ and dimension $2$, so points are pairs $(s_0, s_1)$.
2. Let $X = \set{(0, 1)}$, the set of the formula "$v_0 = 0$ and $v_1 = 1$".
3. $c_0 X$ frees coordinate $0$: $c_0 X = \set{(0, 1), (1, 1)}$, the set of "$v_1 = 1$".
4. $d_{01} = \set{(0, 0), (1, 1)}$, the set of "$v_0 = v_1$".
5. $c_0 X \cdot d_{01} = \set{(1, 1)}$, the set of "$v_0 = v_1$ and $v_1 = 1$".

The typical use: a first-order theory becomes an algebra, and questions about models become questions about homomorphisms into set algebras.
The trap: the dimension $\alpha$ counts variables, not the size of the universe $U$.

### L3 human

A cylindric algebra is a Boolean algebra with operators whose operators are $\alpha$ commuting S5 diamonds, linked by the diagonals.
Its complex algebras come from frames with $\alpha$ equivalence relations; the representable algebras come from the cube frames $U^\alpha$ and their relativizations.
The gap between $\mathbf{CA}_n$ and $\mathbf{RCA}_n$ for finite $n$ is related to the fact that proofs of formulas with $n$ variables may need more than $n$ variables.
The same phenomena appear in many-dimensional modal logics, such as products of S5.
