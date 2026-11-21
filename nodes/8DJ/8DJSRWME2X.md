---
tag: 8DJSRWME2X
kind: statement
role: theorem
name: Lyndon's homomorphism preservation theorem
aliases: [lyndon-positivity-theorem, lyndons-theorem-positive-sentences]
msc: ["03C40", "03C13"]
topics: [JYJHB4YBAH]
audience: grad
about: [KBXSZC6BV1, MEC3ZMC4F1]
uses: [KBXSZC6BV1, 92SWXST1ZM, MVCH6N9SNW, DKFGQTRYZE, MCZRXR3SVB, 1NR3HAWG9D, 8WZF9SBP39]
history:
  first_stated: "1959"
  notes: Roger Lyndon, Properties preserved under homomorphism, Pacific Journal of Mathematics 9 (1959). Ajtai and Gurevich showed in 1987 that the theorem fails over finite structures, and Rossman proved the finite homomorphism preservation theorem in 2008.
sources:
  - url: https://doi.org/10.2140/pjm.1959.9.143
  - book: isbn:9780521587136
---

## Statement

Let $L$ be a signature.
A formula is *positive* if it is built from [[atomic formulas|MCZRXR3SVB]], including equations, and from $\top$ and $\bot$, with $\wedge$, $\vee$, $\forall$ and $\exists$ only.
A *surjective [[homomorphism|KBXSZC6BV1]]* $h \colon A \to B$ of $L$-structures is an onto map that preserves the constants, the functions and the relations: $R^A(\bar a)$ implies $R^B(h \bar a)$.
A [[sentence|DKFGQTRYZE]] $\varphi$ is *preserved by surjective homomorphisms* if $A \models \varphi$ implies $B \models \varphi$ for every surjective homomorphism $h \colon A \to B$.

1. A sentence $\varphi$ is preserved by surjective homomorphisms if and only if it is logically equivalent to a positive sentence.
2. For an $L$-[[theory|92SWXST1ZM]] $T$, the class of [[models|MVCH6N9SNW]] of $T$ is closed under surjective homomorphic images if and only if $T$ has the same models as the set of its positive consequences.

A proof is in [[the proof of Lyndon's theorem|59KCR1HFP9]].

## Remarks

### Why each hypothesis is needed

- Surjectivity. The positive sentence $\forall x \, R(x)$ holds in a one-point structure with $R$ true, and it fails after the inclusion into a two-point structure with $R$ true only at the first point. For all homomorphisms one needs existential-positive sentences.
- Positivity. The sentence $\exists x \exists y \, \neg(x = y)$ holds in every structure with two elements and fails in its image under a map onto one point.
- The constant $\bot$. The sentence $\exists x \, \neg(x = x)$ has no models, so it is preserved. Every positive sentence without $\bot$ holds in the one-point structure in which every relation is true, so $\bot$ is needed.
- All structures. Ajtai and Gurevich found a sentence that is preserved by surjective homomorphisms between finite structures but is not equivalent on finite structures to a positive sentence.

### Consequences

- An elementary class of algebras closed under homomorphic images has positive axioms. This is one half of the logic behind [[Birkhoff's HSP theorem|5083DHSK82]], where closure under subalgebras and products reduces positive axioms to equations.
- The theory of groups in $\set{\cdot, {}^{-1}, e}$ consists of equations, so the image of a group under a surjective homomorphism of structures is a group.
- The theory of fields has the non-positive axiom $0 \ne 1$; its image under the map onto one point is not a field.

### Converse

The easy direction is an induction on positive formulas: if $A \models \psi(\bar a)$ then $B \models \psi(h \bar a)$, where surjectivity handles $\forall$.

### Generalizations

- Homomorphism preservation theorem: a sentence is preserved by all homomorphisms if and only if it is equivalent to an existential-positive sentence.
- Rossman's equirank theorem: the existential-positive sentence can be taken with the same quantifier rank.
- Rossman's finite theorem: over finite structures in a finite relational signature, a sentence of quantifier rank $n$ preserved by homomorphisms is equivalent on finite structures to an existential-positive sentence of quantifier rank at most $\rho(n)$, for an explicit function $\rho$.

## History

Roger Lyndon published the theorem in 1959 in "Properties preserved under homomorphism", and his proof used his interpolation theorem.
Miklós Ajtai and Yuri Gurevich showed in 1987 that it fails over finite structures, and Alexei Stolboushkin gave a simpler counterexample in 1995.
Benjamin Rossman proved in 2008 that the homomorphism preservation theorem holds over finite structures.

## Explanations

### L1 human

A homomorphism copies a structure onto another, and it is allowed to glue elements together.
Gluing can destroy facts such as "these two points are different", but never facts such as "these two points are linked".
A positive rule only speaks of links and equalities, combined with "and", "or", "for all" and "there exists".
Lyndon's theorem says that the first-order rules that survive every gluing onto a structure are exactly the positive rules.

### L2 human

We check that the positive sentence $\forall x \, \exists y \, E(x, y)$ survives a surjective homomorphism.

1. Let $A$ be the directed cycle on $\set{0, 1, 2, 3}$ with edges $i \to i + 1 \bmod 4$, and let $B$ be the directed cycle on $\set{0, 1}$.
2. Let $h(i) = i \bmod 2$. An edge $i \to i + 1$ goes to $h(i) \to h(i) + 1 \bmod 2$, an edge of $B$, so $h$ is a homomorphism. It is onto.
3. Take $u \in B$. Choose $x \in A$ with $h(x) = u$, which exists since $h$ is onto.
4. In $A$ there is $y$ with $E(x, y)$, and then $E(u, h(y))$ holds in $B$.
5. So $B \models \forall x \, \exists y \, E(x, y)$.

The typical use is negative: if one surjective homomorphism destroys a property, the property has no positive axioms.
A trap is to forget equality: $x = y$ is atomic, so it is positive, while $x \ne y$ is not.

### L3 human

The proof of Lyndon's theorem builds two elementary chains and a surjective homomorphism between their unions, by a back-and-forth construction; it is the same sandwich pattern as for the [[Chang-Łoś-Suszko theorem|RK7NK2P75J]].
Lyndon's own route was through the [[Lyndon interpolation theorem|BRDT1BT7WW]], which keeps track of positive and negative occurrences of relation symbols.
In finite model theory, the homomorphism preservation theorem matters for database theory, where existential-positive sentences are the unions of conjunctive queries.
Rossman's proof of the finite case is combinatorial and avoids compactness, unlike the failures of [[Łoś-Tarski|9RN0KYXNT1]] and of Lyndon's theorem in the finite; see [[preservation theorems|T69D2NS1HP]].
