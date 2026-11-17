---
tag: GD2JBXJV5Z
kind: concept
name: Axiomatic method
aliases: [axiomatic-system, axiomatics]
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: ug1
uses: [0B94TKFQJX, KK5F0F03ZW]
sources:
  - url: https://en.wikipedia.org/wiki/Axiomatic_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Euclid%27s_Elements
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_axioms
    locator: lead section
  - book: isbn:9781108439534
---

## Summary

The axiomatic method builds a part of mathematics from four kinds of items.
The primitive terms are words that the theory does not define, such as "point" and "line".
The axioms are statements about the primitive terms that the theory accepts without proof.
The definitions introduce new terms from the primitive terms and from terms that are already defined.
The [[theorems|KK5F0F03ZW]] are the statements that follow from the axioms by a [[mathematical proof|0B94TKFQJX]], with the definitions and the earlier theorems as tools.
An axiom system is a list of primitive terms and axioms.
The method matters because it makes each assumption explicit, so that each proof can be checked and each theorem holds in every structure that satisfies the axioms.

## Motivation

A chain of proofs must start somewhere.
If each statement needs a proof from earlier statements, and each term needs a definition from earlier terms, then the chain goes back forever.
The axiomatic method stops the chain on purpose: it names a short list of terms and statements and accepts them as the start.

A second reason is economy.
Many structures share the same few properties.
The integers under addition, the nonzero rationals under multiplication and the symmetries of a square all satisfy the axioms of a [[group|G5S1M9]].
A theorem proved once from the group axioms holds in all of these structures at the same time.

A third reason is control.
In [[Euclid's Elements|83WHDAV68J]] some proofs use facts that a figure suggests but that no postulate states.
When all assumptions are written down, such hidden steps become visible, and they can be removed or added as new axioms.

## Notation

The words "axiom" and "postulate" mean the same thing in modern usage.
Euclid used "postulate" for the geometric assumptions and "common notion" for general assumptions about magnitudes, such as "the whole is greater than the part".
Primitive terms are also called undefined terms or primitive notions.
In logic, an axiom system written in a formal language is a theory, and a structure in which all its axioms are true is a [[model|MVCH6N9SNW]] of it.

## Remarks

### Examples

- [[Euclid's Elements|83WHDAV68J]] starts Book I with definitions, five postulates and common notions, and derives each proposition from them. It is the first model of the method, although it has gaps.
- [[Hilbert's axioms|KM1FB8XZ2R]] for Euclidean geometry use the primitive terms point, line, plane, incidence, betweenness and congruence. They fill the gaps of Euclid's system.
- The [[Peano axioms|0QFT7Z76N5]] describe the natural numbers with the primitive terms zero and successor.
- The [[axioms of Zermelo-Fraenkel set theory with choice|BA761FKYGN]] use the single primitive relation "is an element of". Most of modern mathematics can be built from them.
- The [[group axioms as an axiomatic system|MRQW28BQ7D]]: a set, one operation and three axioms give a first theorem in a few lines.
- A [[four-point geometry|MJ5S28Y5WV]] is a small system in which consistency and independence can be checked by hand.

### Non-examples

- A list of facts collected from measurements, such as the angles of many drawn triangles, is not an axiom system. Its statements come from observation, and nothing is derived from them by proof.
- [[Euclid's construction of an equilateral triangle|BRAE42513N]] is not a derivation from Euclid's axioms alone. It uses the fact that two circles meet, and no postulate states this.
- A textbook chapter that proves results "from the picture" does not follow the method. The axiomatic method requires that each step uses an axiom, a definition or an earlier theorem.

### Basic properties

- A theorem of an axiom system is true in every [[model|MVCH6N9SNW]] of the system. The reason is that each axiom is true in the model, and each proof step keeps truth.
- If an axiom system has a model, then it is consistent, that is, it does not prove both a statement and its negation. This is the usual way to show [[consistency|VM8TQ70CVJ]].
- An axiom $A$ is independent of the other axioms when it cannot be proved from them. A model of the other axioms in which $A$ is false shows this, as in the [[four-point geometry|MJ5S28Y5WV]].
- The same axiom system can have models that are very different. The group axioms hold in finite groups and in infinite groups.
- A system with one model up to isomorphism is called categorical. The second-order Peano axioms and Hilbert's full system of geometry are categorical.

### History

Euclid wrote the *Elements* around 300 BC, and it served as the model of a deductive science for about two thousand years.
Attempts to prove the [[parallel postulate|2PC3XY0PYZ]] from the other postulates failed, and in the nineteenth century [[non-Euclidean geometry|SPCYMFN5V2]] showed that it is independent of them.
Giuseppe Peano gave his axioms for the natural numbers in 1889.
David Hilbert published *Grundlagen der Geometrie* in 1899, with a complete axiom system for Euclidean geometry and with proofs of consistency and independence by models.
Kurt Gödel's [[incompleteness theorems|X9WYNYE29C]] of 1931 showed limits of the method: a consistent system that contains enough arithmetic cannot prove all true statements of arithmetic, and it cannot prove its own consistency.

### Common errors

- An axiom is not a statement that is "true beyond doubt". It is a statement that the theory accepts as a starting point. The parallel postulate is true in Euclidean geometry and false in [[hyperbolic geometry|GN4N94GQ0Z]].
- A proof inside an axiom system may not use a property of the primitive terms that the axioms do not state. A figure can suggest such a property, but the figure is not a reason.
- Consistency and truth are different questions. A consistent system need not describe any intended structure, and the method itself does not decide which axioms to choose.

## Explanations

### L1 human

Think of a board game with a short rule book.
The rule book says what the pieces are and how they can move, but it does not say why.
Everything that happens in a game must follow from the rules.
In mathematics the pieces are the primitive terms, such as "point" and "line", and the rules are the axioms.
For example, one axiom of geometry says that through two different points there is exactly one line.
A theorem is a fact that follows from the axioms by careful steps, with no extra rules.

### L2 human

We use the axiomatic method on a small system.
The primitive terms are a set $G$ and an operation $*$ on $G$.
The axioms are the [[group axioms|G5S1M9]]: $*$ is associative, there is an identity element $e$, and each element has an inverse.

1. We want to prove the theorem: if $a * b = a * c$, then $b = c$.
2. Let $a'$ be an inverse of $a$, which exists by the inverse axiom.
3. From $a * b = a * c$ we get $a' * (a * b) = a' * (a * c)$, because $*$ gives one value for equal inputs.
4. By associativity, $(a' * a) * b = (a' * a) * c$.
5. By the choice of $a'$, $a' * a = e$, so $e * b = e * c$.
6. By the identity axiom, $e * b = b$ and $e * c = c$, so $b = c$.

Each step names an axiom, and no step uses a property of a particular group.
So the cancellation law holds in every group: in $(\mathbb{Z}, +)$, in the nonzero rationals under multiplication, and in each symmetry group.
The typical use of the method is exactly this: prove once, apply everywhere.
A trap is to use a property that holds in the familiar example but is not an axiom.
For example, $a * b = b * a$ holds in $(\mathbb{Z}, +)$, but it is not a group axiom, and it fails in the symmetric group $S_3$.

### L3 human

From the view of logic, an axiom system is a theory in a formal language, and its theorems are the sentences that a proof system derives from it.
[[Gödel's completeness theorem|WQ1ZE255SF]] says that, in first-order logic, a sentence is derivable exactly when it is true in every model.
So the two views of a theorem, "proved from the axioms" and "true in every model", agree, and models become the main tool for consistency and [[independence|QKCAEG2Y0E]].
The independence of the parallel postulate, of the [[axiom of choice|0HTGB13FE2]] and of the [[continuum hypothesis|0MN2MER9WN]] are all shown by models.

The method has two uses that pull in different directions.
A descriptive system, such as the Peano axioms or Hilbert's geometry, aims to capture one intended structure.
A structural system, such as the axioms of a group, a [[vector space|000AYPA9AJ]] or a [[topological space|0CQHFPGJ45]], aims to cover many structures at once, and its value is in the variety of its models.
[[Hilbert's program|P1RW6JWX73]] asked for finitary consistency proofs of the main systems, and Gödel's [[incompleteness theorems|X9WYNYE29C]] showed that this cannot be done inside the systems themselves.
These questions belong to [[mathematical logic|DYJ0KGTPMR]]; the practice of choosing and using axioms belongs to this topic.
