---
tag: RDSY11X6N2
kind: definition
name: Relation algebra
msc: ["03G15"]
topics: [QYA4H5Y7VR]
audience: research
defines: GQK4DSA11K
uses: [0XADJKM699, 0N6R902FG1, 05AVARPXA2, 0PYSR20HGF, 054K3HNN5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Relation_algebra
  - book: isbn:9780821810415
---

## Definition

A *relation algebra* is a structure $(A, \vee, \wedge, -, 0, 1, ;, c, 1')$, where $;$ is a binary operation, $c$ is a unary operation and $1'$ is an element of $A$.
Write $\breve{x}$ for $c(x)$.
The following hold for all $x, y, z \in A$:

1. $(A, \vee, \wedge, -, 0, 1)$ is a [[Boolean algebra|0XADJKM699]], with order $\le$.
2. $(A, ;, 1')$ is a [[monoid|0N6R902FG1]].
3. $(x \vee y) ; z = (x ; z) \vee (y ; z)$.
4. $\breve{\breve{x}} = x$ and $\breve{(x \vee y)} = \breve{x} \vee \breve{y}$.
5. $\breve{(x ; y)} = \breve{y} ; \breve{x}$.
6. $\breve{x} ; -(x ; y) \le -y$.

## Notation

The operation $;$ is called relative product or composition, $\breve{x}$ is the converse of $x$, and $1'$ is the identity element.
Clause 6 is Tarski's axiom; with the others it is equivalent to the cycle law $(x ; y) \wedge z = 0 \iff (\breve{x} ; z) \wedge y = 0$.
Since every clause is an equation or an inequality, the relation algebras form a variety.

## Remarks

1. Let $U$ be a set and let $A$ be the set of all [[binary relations|05AVARPXA2]] on $U$, with the set operations.
Let $;$ be the [[composition|0PYSR20HGF]] $R ; S = \set{(a, c) : (a, b) \in R \text{ and } (b, c) \in S \text{ for some } b}$.
Let $\breve{R}$ be the [[converse|054K3HNN5Z]] relation and $1'$ the identity relation.
Check of clause 6: if $(a, c) \in \breve{R} ; -(R ; S)$, there is $b$ with $(b, a) \in R$ and $(b, c) \notin R ; S$.
If $(a, c)$ were in $S$, then $(b, c) \in R ; S$; so $(a, c) \notin S$.
See [[the full relation algebra on two points|~1daf4bfe]].
2. On the relations of a set $U$ with at least two elements, keep the Boolean operations, $;$ and $1'$, but take $\breve{R} = R$.
Clause 5 then says $R ; S = S ; R$ for all relations, which fails for $U = \set{a, b}$, $R = \set{(a, b)}$ and $S = \set{(b, b)}$, since $R ; S = \set{(a, b)}$ and $S ; R = \emptyset$.
3. Clause 5 holds with $\breve{x} = x$ when $;$ is commutative; [[Boolean algebras with $;$ equal to meet|~391395a2]] are relation algebras of this kind.
4. [[Formal languages|~36c0fb5a]] with concatenation satisfy clauses 1 to 3, but no unary operation on them satisfies clauses 4 and 6.
5. Right distributivity $z ; (x \vee y) = z ; x \vee z ; y$ is not listed; it follows from clauses 3, 4 and 5 by taking converses.

## Explanations

### L1 human

A relation algebra is a Boolean algebra with three extra pieces: a way to chain two elements, a way to reverse an element, and an element that does nothing when chained.
The six rules are the laws that relations obey under these operations.

### L2 human

1. On $U = \set{a, b}$, let $R = \set{(a, b)}$.
2. $\breve{R} = \set{(b, a)}$ and $R ; \breve{R} = \set{(a, a)}$, while $\breve{R} ; R = \set{(b, b)}$.
3. Clause 6 with $x = R$ and $y = 1'$: here $R ; 1' = R$ and $-R = \set{(a, a), (b, a), (b, b)}$.
4. $\breve{R} ; -R = \set{(b, a)}$, since the only pair of $-R$ that starts at $a$ is $(a, a)$.
5. $-1' = \set{(a, b), (b, a)}$ contains $(b, a)$, so clause 6 holds here.

The typical use: to check that a structure is a relation algebra, one checks clauses 5 and 6, which carry the content.
The trap: clause 6 is not symmetric; its mirror image $-(y ; x) ; \breve{x} \le -y$ is a consequence, not a separate axiom.
