---
tag: QMQEJKFEYZ
kind: concept
name: Primitive notion
aliases: [undefined-term, primitive-term, primitive-notions]
msc: ["00A35", "03A05"]
topics: [BP0WAF23HB]
audience: ug1
uses: [8ZCZ3HW91Z, KM1FB8XZ2R, 0QFT7Z76N5, 0HE5WDQ9FJ]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_notion
    locator: Details
  - url: https://en.wikipedia.org/wiki/Primitive_notion
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_axioms
    locator: lead section
---

## Summary

Every definition explains a word with older words, so the chain of definitions must stop somewhere, at words that the theory does not define.
Those words are the primitive notions of the theory, and the axioms, not definitions, fix how they behave.

Take the definition of a subset: $A \subseteq B$ means that every $x$ with $x \in A$ also has $x \in B$.
It explains "subset" with "is an element of", and in [[Zermelo-Fraenkel set theory|0HE5WDQ9FJ]] the chain stops there, because "set" and $\in$ have no definition.
In general, a *primitive notion* of a theory is a term, an object, a relation or an operation that the theory uses without a [[definition|8ZCZ3HW91Z]].
The theory states axioms about its primitive notions, every other term is defined from them, and every proof uses only the axioms and the definitions.

## Motivation

Try to define every word of a definition.
A line segment is the part of a line between two points.
A line is a straight curve, a curve is a set of points, and a point is something with no size.
At some step the chain either repeats a word, and the definitions become circular, or it reaches a word with no definition.
So a theory must choose where to stop.

The choice has a benefit as well as a cost.
Since a primitive notion has no definition, a proof cannot use a mental picture of it, and every step must come from the axioms.
Then each theorem holds for every interpretation of the primitive notions that satisfies the axioms.
This is the start of axiomatic geometry, of set theory as a foundation, and of [[model theory|HFTBG5PMXC]].

## Notation

Books often list the primitive notions at the start of a chapter, under the heading "undefined terms".
A primitive relation usually gets a symbol, such as $\in$ for membership, or $I(P, \ell)$ for "the point $P$ lies on the line $\ell$".
In logic, the primitive notions of a theory form its *signature*, the list of its symbols for constants, functions and relations.

## Remarks

### Meaning through axioms

A primitive notion has no definition, but it still has meaning: its meaning is the role it plays in the axioms.
For example, an incidence axiom says that through two distinct points there is exactly one line.
That axiom tells us how "point", "line" and "lies on" behave together, and nothing else about them.
Hilbert is reported to have said that one must always be able to say "tables, chairs and beer mugs" in place of "points, lines and planes".
So a proof in the theory may not use a picture.
"Two lines meet in at most one point, because lines are straight" is not a proof, but the argument in the L2 explanation below is.

### One theory, many models

A *model* of a theory is an interpretation of its primitive notions that makes all its axioms true.
One theory can have models that look very different.
The [[three-point model|RF12XC7AY0]] interprets "point" as one of the letters $A$, $B$, $C$ and "line" as a set of two letters, and it satisfies three axioms of incidence geometry.
The Euclidean plane satisfies the same three axioms.
A theorem proved from the axioms holds in both models, because its proof uses only the axioms.
And a statement that holds in one model and fails in another cannot be proved from the axioms.

### Primitive in which theory?

Whether a term is primitive depends on the theory, not on the term.
[[Hilbert's axioms|KM1FB8XZ2R]] of 1899 take point, line and plane as primitive objects, with the relations "lies on", "between" and "congruent".
[[Tarski's axioms|14DWEDXWCC]] for plane geometry take points as the only objects, with "between" and "equidistant" as primitive relations, and then define lines from points.
In the coordinate plane, built from the real numbers, points and lines are both [[defined notions|P9WVMHJZWZ]].
In the same way, natural numbers are primitive in the [[Peano axioms|0QFT7Z76N5]], where "natural number", "zero" and "successor" are undefined, and they are defined sets in set theory.

### Examples and non-examples

[[Set and membership|Y2BSHY2D6M]] are the primitive notions of ZF, and everything else in that theory, from the empty set to the real numbers, is defined from them.
Point, line and incidence are primitive in incidence geometry, as the [[three-point model|RF12XC7AY0]] shows.

The empty set is not primitive in ZF.
It is defined as "the set with no elements", after a proof that such a set exists and that the axiom of extensionality makes it unique.
In most presentations of Peano arithmetic, addition is not primitive either.
It is defined by recursion from the successor, with $m + 0 = m$ and $m + S(n) = S(m + n)$.

### Watch out

The first error is to treat a primitive notion as vague.
A primitive notion is exactly as precise as its axioms make it, and no more.

The second error is the opposite one: to use facts about a primitive notion that the axioms do not give.
A student who writes "lines are infinite, so ..." in incidence geometry has used a drawing, and the three-point model shows that the axioms allow lines with two points.

The third error is to try to define every term, which ends in a circle such as "a set is a collection, and a collection is a set".

### History

[[Euclid's Elements|83WHDAV68J]] open with descriptions such as [[a point is that which has no part|FYC7X2HYBH]], but no proof in the *Elements* uses them.
Moritz Pasch, in 1882, built geometry on undefined terms and required that proofs must not depend on their intuitive meaning or on figures.
Peano in 1889 and Hilbert in 1899 gave axiom systems for arithmetic and for geometry with explicit primitive notions.

### Try it

First, in ZF, is "$x \subseteq y$" primitive?
No: it is defined as $\forall z \, (z \in x \Rightarrow z \in y)$, which uses only $\in$ and logic.

Second, can the axiom "every line has at least three points" be proved from the three incidence axioms of the three-point model?
No: the three-point model satisfies those axioms, and its lines have only two points.

## Explanations

### L1 human

A dictionary explains each word with other words.
If you keep looking up each word, you come back to words that you have already looked up.
Mathematics avoids this circle by starting with a few words that it does not define, such as "point" and "line".
Instead of saying what these words mean, it lists rules about them, such as "through two points there is exactly one line".
Every fact about points and lines must then follow from these rules.

### L2 human

Here is a proof that uses primitive notions and nothing else.
Take "point", "line" and "lies on" as primitive, with one axiom: for two distinct points, exactly one line contains both.
We prove that two distinct lines $\ell$ and $m$ have at most one common point.
Suppose that two distinct points $P$ and $Q$ lie on both $\ell$ and $m$.
By the axiom, exactly one line contains both $P$ and $Q$, so $\ell = m$, which contradicts $\ell \ne m$.
So $\ell$ and $m$ share at most one point.

The proof never says what a point or a line is.
So the theorem holds in every model of the axiom, including models with finitely many points.
Watch out: the proof does not show that two lines meet at all, and in the Euclidean plane parallel lines do not.

### L3 human

In first-order logic, the primitive notions of a theory are its signature, and the theory is a set of sentences in that signature.
Padoa's method shows that one primitive notion cannot be defined from the others: find two models with the same domain that agree on the other notions and differ on this one.
Beth's definability theorem gives the converse for first-order logic: if no such pair of models exists, an explicit definition exists.

Set theory takes $\in$ as its only primitive relation, and it defines numbers, functions and spaces from it.
This is why $\in$ is the primitive notion behind most of mathematics.
Type theories, such as the one in Lean, make a different choice: types, functions and inductive definitions are primitive, and sets are defined from them.
