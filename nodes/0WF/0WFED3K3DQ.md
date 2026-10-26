---
tag: 0WFED3K3DQ
kind: statement
role: theorem
name: Sylvester's law of inertia
msc: [15A63, "11E04"]
uses: [0N28QN4CYA, 0SPYAGE7T0]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester's_law_of_inertia
    locator: Statement
same_as:
  wikidata: Q1752621
  wikipedia: Sylvester's law of inertia
---

## Statement

Let $A$ be a real symmetric $n \times n$ matrix.
Let $P$ and $P'$ be invertible real $n \times n$ matrices such that $D = P^T A P$ and $D' = P'^T A P'$ are diagonal.
Then $D$ and $D'$ have the same number of positive diagonal entries and the same number of negative diagonal entries.
They also have the same number of zero diagonal entries.

## Remarks

So these three numbers are invariants of the quadratic form $x \mapsto x^T A x$; they give its [[signature|07EZA80NEH]].
They are also the numbers of positive, negative and zero eigenvalues of $A$, counted with multiplicity.
Equivalently, two real symmetric matrices are congruent if and only if they have the same numbers of positive, negative and zero eigenvalues.

## History

James Joseph Sylvester published the theorem in 1852.

## Explanations

### L1 human

A real quadratic form can be written as a sum of squares in many ways.
The numbers of plus signs and minus signs are always the same.
For example, $x^2 + 2xy$ always has one plus sign and one minus sign.
