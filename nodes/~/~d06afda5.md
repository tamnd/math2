---
tag: ~d06afda5
kind: concept
name: Primitive notion
aliases: [undefined-term, primitive-term, primitive-notions]
msc: ["00A35", "03A05"]
topics: [BP0WAF23HB]
audience: ug1
uses: [~d1d36166, KM1FB8XZ2R, 0QFT7Z76N5, 0HE5WDQ9FJ]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_notion
    locator: Details
  - url: https://en.wikipedia.org/wiki/Primitive_notion
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_axioms
    locator: lead section
---

## Summary

A primitive notion is a term of a theory that the theory does not define.
Examples are "point", "line" and "lies on" in [[Hilbert's axioms|KM1FB8XZ2R]] for geometry, and "set" and "is an element of" in [[Zermelo-Fraenkel set theory|0HE5WDQ9FJ]].
The axioms of the theory fix how primitive notions may be used, and proofs use only these axioms.
Each other term of the theory gets a [[definition|~d1d36166]] in terms of the primitive notions.
Primitive notions matter because definitions cannot go on forever: each chain of definitions must stop at undefined terms.

## Motivation

Try to define each word of a definition with other words.
A "line segment" is a part of a line between two points.
A "line" is a straight curve, and a "curve" is a set of points.
A "point" is ... something with no size.
At some step, the chain either repeats a word, which makes it circular, or it stops at a word with no definition.
A theory chooses where to stop.
It names a few primitive notions, and it states axioms about them instead of definitions.

## Notation

1. Books often list primitive notions at the start of a chapter, as "undefined terms".
2. A primitive relation is often written as a symbol, such as $\in$ for membership or $I(P, \ell)$ for "the point $P$ lies on the line $\ell$".
3. In logic, the primitive notions of a theory form its signature: its symbols for constants, functions and relations.

## Remarks

### Meaning through axioms

A primitive notion has no definition, but it is not without meaning.
Its meaning is the role it plays in the axioms.
Hilbert wrote that points, lines and planes could be replaced by "tables, chairs and beer mugs", as long as the axioms hold.
So a proof in the theory must not use a picture of a point or a line.
Each step must follow from the axioms and from earlier theorems.

### Models

A model of a theory is an interpretation of its primitive notions that makes all axioms true.
One theory can have very different models.
The [[three-point model|~008697e6]] interprets "point" as one of three letters and "line" as a set of two letters, and it satisfies three axioms of incidence geometry.
Each theorem of the theory holds in each model, because its proof uses only the axioms.

### Choice of primitive notions

The same theory can use different primitive notions.
[[Tarski's axioms|14DWEDXWCC]] for plane geometry use points as the only objects, with "between" and "equidistant" as primitive relations.
Lines are then defined from points.
In the coordinate plane, built from real numbers, points and lines are both [[defined notions|~45607300]].
So "primitive" is a property of a term in a theory, not of the term alone.

### Examples

1. [[Point, line and incidence in incidence geometry|~008697e6]], with a model of three points.
2. [[Set and membership in Zermelo-Fraenkel set theory|~e47f9981]].
3. In the [[Peano axioms|0QFT7Z76N5]], the primitive notions are "natural number", "zero" and "successor".
4. In Hilbert's axioms of 1899, the primitive notions are point, line, plane, and the relations "lies on", "between" and "congruent".

### Non-examples

1. [[A line in the coordinate plane|~45607300]] is not a primitive notion: it is defined as the solution set of a linear equation.
2. In ZF, the empty set is not primitive: it is defined as the set with no elements, after a proof that exactly one such set exists.
3. In the Peano axioms, "addition" is not primitive in most presentations: it is defined by recursion from the successor.

### Basic properties

1. Each theory with definitions has at least one primitive notion, or each definition would be circular.
2. A primitive notion is used only through the axioms. So a statement that holds in one model but not in another cannot be proved in the theory.
3. Replacing the primitive notions by others with the same axioms gives the same theorems. This is the principle behind Hilbert's beer mugs.
4. A term that is primitive in one theory can be defined in another. Natural numbers are primitive for Peano and defined in set theory.

### History

[[Euclid's Elements|83WHDAV68J]] begin with descriptions of a point and a line, such as "a point is that which has no part", but no proof uses them.
Pasch in 1882 used undefined terms for geometry, and stated that proofs must not depend on their intuitive meaning.
Peano in 1889 and Hilbert in 1899 gave axioms with explicit primitive notions for arithmetic and geometry.

### Common errors

1. A student uses a picture in a proof, for example "two lines meet in at most one point, because lines are straight". In incidence geometry this fact needs a proof from the axioms.
2. A student thinks that a primitive notion is vague or meaningless. Its use is exactly as precise as the axioms make it.
3. A student tries to define each term and builds a circular chain of definitions.

## Explanations

### L1 human

A dictionary explains each word with other words.
If we keep looking up each word, we eventually come back to words we already looked up.
Mathematics avoids this circle by starting with a few words that it does not define, such as "point" and "line".
Instead of saying what these words mean, it lists rules about them, such as "through two points there is exactly one line".
Every fact about points and lines must then follow from these rules.

### L2 human

We prove a theorem from incidence axioms, with "point", "line" and "lies on" as primitive notions.
Axiom 1 says that for two distinct points there is exactly one line on which both lie.

Theorem: two distinct lines have at most one common point.

1. Let $\ell$ and $m$ be distinct lines, and assume that distinct points $P$ and $Q$ lie on both.
2. By axiom 1, exactly one line contains both $P$ and $Q$.
3. Both $\ell$ and $m$ contain $P$ and $Q$, so $\ell = m$.
4. This contradicts $\ell \neq m$. So $\ell$ and $m$ have at most one common point.

The proof never says what a point or a line is.
So the theorem holds in each model of axiom 1, including models with finitely many points.
A trap is to add facts from a drawing, such as "lines are infinite", which axiom 1 does not give.

### L3 human

In first-order logic, the primitive notions of a theory are its signature, and the theory is a set of sentences in that signature.
Padoa's method shows that a primitive notion cannot be defined from the others: find two models that agree on the other notions and differ on this one.
Beth's definability theorem gives the converse for first-order logic: if no such pair of models exists, an explicit definition exists.
In [[model theory|HFTBG5PMXC]], a model is a structure for the signature that satisfies the axioms.
Set theory takes $\in$ as its only primitive relation, and it defines numbers, functions and spaces from it, which makes $\in$ the primitive notion of most of mathematics.
