---
tag: AHWXJ3GT02
kind: statement
role: theorem
name: Relation algebras and three-variable logic
aliases: [tarski-givant-translation, relation-algebra-three-variable-translation]
msc: ["03G15", "03B10"]
topics: [QYA4H5Y7VR]
audience: research
about: [GQK4DSA11K]
uses: [RDSY11X6N2, GQK4DSA11K, BQ9EEFPS10, 7R95RBEPP8, 086QKPF0A6, 0HE5WDQ9FJ, HACXBCM7SS]
proofs: [SRG5HRPJ69]
sources:
  - url: https://en.wikipedia.org/wiki/Relation_algebra
  - book: isbn:9780821810415
---

## Statement

Let $R_1, R_2, \ldots$ be binary relation symbols, and let $v_0, v_1, v_2$ be three individual variables.
A *relation algebra term* is built from variables $x_1, x_2, \ldots$ and $0, 1, 1'$ by $\vee$, $\wedge$, $-$, $;$ and $\breve{\ }$.

**Theorem.**

1. To each term $t$ one can assign a [[first-order|086QKPF0A6]] formula $\varphi_t(v_0, v_1)$ in the symbols $R_i$ and $=$, using only the variables $v_0, v_1, v_2$, such that for every set $U$ and every assignment of relations $\rho_i \subseteq U \times U$ to $x_i$ and to $R_i$, the value of $t$ in the [[full relation algebra|BQ9EEFPS10]] $\mathrm{Re}(U)$ is $\set{(a, b) : U \models \varphi_t[a, b]}$.
2. An equation $s = t$ holds in every representable [[relation algebra|GQK4DSA11K]] iff the sentence $\forall v_0 \forall v_1 (\varphi_s \leftrightarrow \varphi_t)$ is logically valid.
3. Conversely, every formula with at most the variables $v_0, v_1, v_2$ and free variables among $v_0, v_1$, in the symbols $R_i$ and $=$, is logically equivalent to $\varphi_t$ for some term $t$.
4. Let $\mathcal{L}^\times$ be the equational theory of relation algebras with two extra constants $p, q$ and the axioms $\breve{p} ; p \le 1'$, $\breve{q} ; q \le 1'$ and $\breve{p} ; q = 1$. Then [[ZF set theory|0HE5WDQ9FJ]] can be formalized in $\mathcal{L}^\times$ with one more constant for the membership relation, and [[Peano arithmetic|HACXBCM7SS]] can be formalized in the same way.

Parts 1 to 3 are due to Tarski; part 4 is the main result of the book of Tarski and Givant.

## Remarks

### Why each hypothesis is needed

1. Three variables are needed in part 1: composition $x ; y$ says "there is a $v_2$ between $v_0$ and $v_1$".
2. In part 3, the bound of three variables cannot be raised: the formula "there are at least four elements" uses four variables and is not equivalent to any $\varphi_t$.
3. In part 4, the elements $p$ and $q$ act as the two projections from ordered pairs; without them the theory only expresses three-variable statements.

### Consequences

1. The equational theory of representable relation algebras is recursively enumerable, by part 2 and the completeness theorem.
2. By part 4, the equational theory of relation algebras is undecidable, since it interprets an essentially undecidable theory.
3. Mathematics based on set theory can be developed as equational reasoning with no variables over individuals.

### Converse

Part 3 is the converse of part 1 for formulas with three variables.
For the axioms of $\mathsf{RA}$ in place of validity, part 2 has a weaker converse: the equations provable from the axioms correspond to the three-variable sentences that can be proved with four variables.

### Generalizations

1. Every relation algebra with elements $p, q$ as in part 4 is representable; [[this theorem|7R95RBEPP8]] shows that the hypothesis cannot be dropped.
2. The same translation works for cylindric algebras of dimension $n$ and formulas with $n$ variables.

## History

Tarski studied the calculus of relations as a formal system and proved its equivalence with three-variable logic.
Tarski and Givant developed the formalization of set theory in their book "A formalization of set theory without variables" (1987).
The connection between the axioms of $\mathsf{RA}$ and four-variable proofs was established by Maddux.

## Explanations

### L1 human

Statements about relations that use at most three names for objects can be written as equations between relations, with no names for objects at all.
With a way to pair objects, this is enough to write all of set theory.

### L2 human

1. "$R$ is transitive" is $\forall v_0 \forall v_1 (\exists v_2 (R(v_0, v_2) \land R(v_2, v_1)) \to R(v_0, v_1))$.
2. The formula $\exists v_2 (R(v_0, v_2) \land R(v_2, v_1))$ is equivalent to $\varphi_{x ; x}$.
3. So transitivity is the equation $(x ; x) \vee x = x$, that is, $x ; x \le x$.

The typical use: translate a three-variable property into an equation, and reason with the axioms of relation algebra.
The trap: two-variable formulas such as $R(v_1, v_0)$ still need the third variable for the translation of converse.

### L3 human

Part 2 identifies the equational theory of $\mathsf{RRA}$ with the three-variable fragment of first-order logic for binary relations.
Proofs of valid three-variable sentences may need more variables, and this is the logical side of the gap between $\mathsf{RA}$ and $\mathsf{RRA}$.
Part 4 shows that a variable-free equational calculus can be as strong as set theory, and it yields Tarski's theorem that $\mathsf{RA}$ has an undecidable equational theory.
