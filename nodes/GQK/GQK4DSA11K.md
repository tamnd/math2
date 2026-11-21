---
tag: GQK4DSA11K
kind: concept
name: Relation algebra
msc: ["03G15"]
topics: [QYA4H5Y7VR]
audience: research
specializes: [0XADJKM699]
uses: [RDSY11X6N2, 0XADJKM699, 05AVARPXA2, 0PYSR20HGF, 054K3HNN5Z, 086QKPF0A6]
sources:
  - url: https://en.wikipedia.org/wiki/Relation_algebra
  - book: isbn:9780821810415
same_as:
  wikidata: Q5965969
  wikipedia: Relation algebra
---

## Summary

A relation algebra is a [[Boolean algebra|0XADJKM699]] with a binary operation $;$, a unary operation $\breve{\ }$ and a constant $1'$, subject to the axioms of [[the definition|RDSY11X6N2]].
The operations behave like [[composition|0PYSR20HGF]] and [[converse|054K3HNN5Z]] of [[binary relations|05AVARPXA2]] and like the identity relation.
The main example is the algebra of all binary relations on a set.
Relation algebras are the algebraic form of a fragment of [[first-order logic|086QKPF0A6]] with three variables.
Tarski and Givant showed that set theory and arithmetic can be formalized in an equational theory of this kind.

## Motivation

Many statements about relations are equations between relations built by Boolean operations, composition and converse.
For example, "$R$ is transitive" is $R ; R \le R$, and "$R$ is a function" is $\breve{R} ; R \le 1'$.
A relation algebra keeps the laws that these operations obey in every algebra of relations, and studies them abstractly.
The question of which laws suffice leads to the representation problem.

## Notation

We write $(A, \vee, \wedge, -, 0, 1, ;, \breve{\ }, 1')$, with $x \le y$ for $x \vee y = y$, and $0' = -1'$ for the diversity element.
A relation algebra is *representable* if it is isomorphic to a subalgebra of a direct product of full relation algebras $\mathcal{P}(U \times U)$.
$\mathsf{RA}$ is the class of relation algebras and $\mathsf{RRA}$ the class of representable ones.

## Remarks

### Examples

1. [[The full relation algebra on a set|BQ9EEFPS10]]; on two points it has $16$ elements.
2. [[A Boolean algebra with $;$ equal to meet and trivial converse|KACAJCSSCR]].
3. For a group $G$, the power set $\mathcal{P}(G)$ with $X ; Y = \set{gh : g \in X, h \in Y}$, $\breve{X} = \set{g^{-1} : g \in X}$ and $1' = \set{e}$.
4. The algebra of relations contained in an equivalence relation $E$ on $U$, with top element $E$.

### Non-examples

1. [[The algebra of formal languages|FCA4HXDAHQ]] is a residuated Boolean algebra, but no unary operation on it satisfies the axioms of converse.
2. The relations on a set with at least two elements, with converse replaced by the identity map, fail $\breve{(x ; y)} = \breve{y} ; \breve{x}$.

### Basic properties

1. Composition is monotone and distributes over arbitrary existing joins in each argument.
2. Converse is a Boolean automorphism of order two, and $\breve{1'} = 1'$.
3. The cycle law: $(x ; y) \wedge z = 0$ iff $(\breve{x} ; z) \wedge y = 0$ iff $(z ; \breve{y}) \wedge x = 0$.
4. Every relation algebra is a [[residuated Boolean algebra|KCG48CWY69]], with $x \backslash y = -(\breve{x} ; -y)$.
5. $\mathsf{RRA}$ is a variety, $\mathsf{RRA} \ne \mathsf{RA}$, and $\mathsf{RRA}$ has no finite equational basis.

### History

De Morgan, Peirce and Schröder developed a calculus of relations in the nineteenth century.
Tarski proposed the axioms of relation algebra in his 1941 paper "On the calculus of relations".
Lyndon found the first non-representable relation algebra, and Monk proved that the representable ones have no finite basis.
Tarski and Givant presented the formalization of set theory in their book "A formalization of set theory without variables".

### Common errors

1. Reading $x ; y$ as $y \circ x$. In the relational notation, $R ; S$ applies $R$ first and then $S$.
2. Assuming every relation algebra is representable. The axioms are sound for relations but not complete.
3. Treating $1'$ as the top element. The top is $1$, the universal relation; $1'$ is the identity.

## Explanations

### L1 human

Relations such as "is a parent of" can be combined in several ways.
Composing "parent of" with itself gives "grandparent of", and taking its converse gives "child of".
They also form a Boolean algebra: one can take "parent or sibling", "not a parent", and so on.
A relation algebra keeps the laws that these operations obey and studies them abstractly, without a set of people in the background.

### L2 human

1. On $U = \set{a, b, c}$, let $R = \set{(a, b), (b, c)}$.
2. $R ; R = \set{(a, c)}$, the pairs joined by a path of length two.
3. $\breve{R} = \set{(b, a), (c, b)}$.
4. $R ; R \le R$ fails, so $R$ is not transitive; $R + R ; R$ is the transitive closure.

The typical use: properties of relations, such as transitivity or functionality, become inequalities in a relation algebra.
The trap: an inequality true in every algebra of relations need not follow from the relation algebra axioms.

### L3 human

Relation algebras are Boolean algebras with operators, and the cycle law says that $y \mapsto x ; y$ and $z \mapsto \breve{x} ; z$ are conjugate operators.
They are the algebras of the three-variable fragment of first-order logic with only binary relations; by a result of Maddux, the equations of $\mathsf{RA}$ correspond to the three-variable sentences that can be proved with four variables.
Hirsch and Hodkinson proved that representability of finite relation algebras is undecidable, with games played on atom structures.
Composition and converse also make sense between different sets, and this leads to the categorical notion of an allegory.
