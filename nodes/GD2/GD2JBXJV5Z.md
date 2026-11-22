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

The axiomatic method writes down a short list of starting statements, accepts them without proof, and then proves everything else from them.
Its value is that every assumption is on the table, so each proof can be checked and each theorem holds wherever the starting statements hold.
An axiom system has four kinds of items.
The *primitive terms* are words that the system does not define, such as "point" and "line".
The *axioms* are statements about the primitive terms that the system accepts as its starting point.
The *definitions* build new terms from the primitive terms and from terms defined earlier.
The [[theorems|KK5F0F03ZW]] are the statements that follow from the axioms by a [[mathematical proof|0B94TKFQJX]], with the definitions and the earlier theorems as tools.

## Motivation

A chain of proofs has to start somewhere.
If every statement needs a proof from earlier statements, and every word needs a definition in earlier words, the chain goes back forever.
The axiomatic method stops the chain on purpose: it names a few terms and statements and agrees to begin there.

The method also saves work.
The integers under addition, the nonzero rationals under multiplication and the symmetries of a square all satisfy the three axioms of a [[group|G5S1M9]].
So a theorem proved once from those three axioms holds in all of these structures, and in every other group, at the same time.

Finally, the method exposes hidden steps.
Some proofs in [[Euclid's Elements|83WHDAV68J]] use a fact that the figure shows but that no postulate states.
Once every assumption must be written down, such a step becomes visible, and it is either proved or added as a new axiom.
The later pages on [[conjectures|WMEMMHZ3BH]] and on the [[functions of proof|ENY0GKRJS8]] return to this, since systematization is one of the jobs that a proof does.

## Notation

In modern usage "axiom" and "postulate" mean the same thing.
Euclid used "postulate" for his geometric assumptions and "common notion" for general assumptions about magnitudes, such as "the whole is greater than the part".
Primitive terms are also called undefined terms or primitive notions.
In logic, an axiom system in a formal language is called a *theory*, and a structure in which all its axioms are true is a [[model|MVCH6N9SNW]] of the theory.

## Remarks

### A system small enough to check by hand

Take the primitive terms "point", "line" and "lies on", and three axioms.
There are exactly four points.
Each two distinct points lie on exactly one common line.
Each line has exactly two points on it.
From these alone we can prove that there are exactly six lines, since lines match pairs of points and four points form
$$\binom{4}{2} = \frac{4 \cdot 3}{2} = 6$$
pairs.
The [[four-point geometry|MJ5S28Y5WV]] gives this proof in full.
It also shows the other half of the method: it builds small models in which some axioms hold and one fails, and so it proves that no axiom follows from the other two.

### One proof, many structures

The [[group axioms read as an axiom system|MRQW28BQ7D]] give a first theorem in a few lines: a group has only one identity element.
If $e$ and $f$ are both identities, then
$$e = e * f = f,$$
where the first equality holds because $f$ is an identity and the second because $e$ is one.
No step uses what the elements are.
So the result holds at once in $(\mathbb{Z}, +)$, where the identity is $0$, in the nonzero rationals under multiplication, where it is $1$, and in every symmetry group.
This is the main use of the method in modern algebra and topology: one proof, applied to every structure that satisfies the axioms.

### Euclid's gap and Hilbert's repair

The first proposition of the *Elements* builds an equilateral triangle on a segment $AB$ from two circles, one centered at $A$ and one at $B$, and takes a point where they cross.
None of Euclid's postulates or common notions says that the two circles cross.
The [[analysis of the construction|BRAE42513N]] shows that the gap is real.
In the plane $\mathbb{Q}^2$ of points with rational coordinates, the two circles of radius $1$ about $(0, 0)$ and $(1, 0)$ would meet only at
$$\left(\tfrac{1}{2}, \pm \tfrac{\sqrt{3}}{2}\right),$$
and these points are not in $\mathbb{Q}^2$.
[[Hilbert's axioms|KM1FB8XZ2R]] close this gap and others.
Their primitive terms are point, line and plane, with the relations of incidence, betweenness and congruence, and their axioms of continuity supply the crossing point.

### What models tell you

A model turns questions about an axiom system into questions about one structure.
A theorem of the system is true in every model, because each axiom is true there and each proof step keeps truth.
So if a system has a model, it cannot prove both a statement and its negation, since both would be true in that model; this is the usual proof of [[consistency|VM8TQ70CVJ]].
An axiom is [[independent|QKCAEG2Y0E]] of the others when some model makes the others true and that axiom false.
This is how the [[parallel postulate|2PC3XY0PYZ]] was shown to be independent of Euclid's other postulates: [[hyperbolic geometry|GN4N94GQ0Z]] is a model of the others in which it fails.
One system can have very different models, since the group axioms hold in finite and in infinite groups.
A system whose models are all isomorphic is called *categorical*, and the second-order [[Peano axioms|0QFT7Z76N5]] are the standard example.

### What it is not

A table of the angle sums of a hundred drawn triangles is not an axiom system.
Its entries come from measurement, and nothing in it is derived by proof.
A chapter that justifies steps by pointing at a picture does not follow the method either, because the method allows only axioms, definitions and earlier theorems as reasons.
Euclid's first proposition, read strictly, is the standard case of such a step.

### Watch out

An axiom is not a statement that is "true beyond doubt".
It is a statement that the system takes as a starting point.
The parallel postulate is true in Euclidean geometry and false in hyperbolic geometry, and both systems are consistent if either one is.

A second trap is to use a property of your favorite model inside a general proof.
Every example of a group that a beginner meets first, such as $(\mathbb{Z}, +)$, satisfies $a * b = b * a$.
But this is not a group axiom, and it fails in the symmetric group $S_3$.
A proof that uses it proves a theorem about commutative groups only.

### History

Euclid wrote the *Elements* around 300 BC, and for about two thousand years it was the model of a deductive science.
Attempts to prove the parallel postulate from the other postulates failed, and the [[non-Euclidean geometry|SPCYMFN5V2]] of the nineteenth century showed that it is independent of them.
Giuseppe Peano published his axioms for the natural numbers in 1889.
David Hilbert published *Grundlagen der Geometrie* in 1899, with a full axiom system for Euclidean geometry and with proofs of consistency and independence by models.
In 1931 Kurt Gödel's [[incompleteness theorems|X9WYNYE29C]] showed a limit of the method: a consistent system that contains enough arithmetic cannot prove every true statement of arithmetic, and it cannot prove its own consistency.

### Try it

First, in the four-point geometry, how many lines pass through each point?
Each point forms a pair with each of the other three points, and each pair gives exactly one line, so the answer is $3$.

Second, use the group axioms and the uniqueness of inverses to show that the inverse of $a'$ is $a$.
The equations $a' * a = e$ and $a * a' = e$ say that $a$ is an inverse of $a'$, and $a'$ has only one inverse, so it is $a$.

Third, does $a * b = b * a$ follow from the group axioms?
No: in $S_3$, composing the transpositions $(1\,2)$ and $(1\,3)$ in the two orders sends $1$ to $3$ in one order and to $2$ in the other.

## Explanations

### L1 human

Think of a board game with a short rule book.
The rule book says what the pieces are and how they move, and it does not explain why.
Everything that happens in a game must follow from those rules.
In mathematics the pieces are the primitive terms, such as "point" and "line", and the rules are the axioms.
One rule of geometry says that through two different points there is exactly one line.
A theorem is a fact that follows from the rules by careful steps, with no extra rules slipped in.

### L2 human

Here is a typical use: prove the cancellation law $a * b = a * c \Rightarrow b = c$ for every [[group|G5S1M9]], using only the axioms.
The axioms say that $*$ is associative, that there is an identity $e$, and that each element has an inverse.

1. Let $a'$ be an inverse of $a$, which exists by the inverse axiom.
2. Apply $a' *$ to both sides of $a * b = a * c$; the results are equal because $*$ gives one value for each pair of inputs.
   $$a' * (a * b) = a' * (a * c).$$
3. Regroup by associativity.
   $$(a' * a) * b = (a' * a) * c.$$
4. Replace $a' * a$ by $e$, by the choice of $a'$, and then use the identity axiom.
   $$b = e * b = e * c = c.$$

Each step names an axiom, and no step uses a property of a particular group.
So the law holds in $(\mathbb{Z}, +)$, where it says $a + b = a + c \Rightarrow b = c$, and equally in every symmetry group.
Watch out: we multiplied by $a'$ on the left of both sides.
Multiplying on the left of one side and on the right of the other would need commutativity, which the axioms do not give.

### L3 human

In logic an axiom system is a theory in a formal language, and its theorems are the sentences that a proof system derives from it.
[[Gödel's completeness theorem|WQ1ZE255SF]] says that in first-order logic a sentence is derivable exactly when it is true in every model.
So "proved from the axioms" and "true in every model" agree, and models become the standard tool for consistency and independence.
The independence of the parallel postulate, of the [[axiom of choice|0HTGB13FE2]] and of the [[continuum hypothesis|0MN2MER9WN]] are all proved with models.

The method is used in two ways that pull in different directions.
A descriptive system, such as the Peano axioms or Hilbert's geometry, aims to pin down one intended structure.
A structural system, such as the axioms of a group, a [[vector space|000AYPA9AJ]] or a [[topological space|0CQHFPGJ45]], aims to cover many structures, and its value lies in the variety of its models.
[[Hilbert's program|P1RW6JWX73]] asked for finitary proofs that the main systems are consistent, and Gödel's theorems showed that a system of this kind cannot prove its own consistency.
These questions belong to [[mathematical logic|DYJ0KGTPMR]], while the choice and use of axioms in daily practice is part of the [[methodology of mathematics|3FJ3XMV9KD]].
