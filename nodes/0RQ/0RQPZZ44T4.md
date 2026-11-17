---
tag: 0RQPZZ44T4
kind: definition
name: Identity element
msc: [08A02]
topics: [BAZT8JJ70S]
audience: school
defines: 07WYQPB8E3
uses: [0580ZJSA3Q]
formal:
  - system: lean4
    library: mathlib
    decl: Std.LawfulIdentity
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Identity_element
    locator: Definitions
  - book: isbn:9780471433347
    locator: Section 1.1
inventory: [75FBJRN7YR]
---

## Definition

Let $S$ be a set and let $\ast$ be a [[binary operation|0M418FE7BB]] on $S$.
An element $e \in S$ is a left identity when $e \ast a = a$ for all $a \in S$.
An element $e \in S$ is a right identity when $a \ast e = a$ for all $a \in S$.
An element $e \in S$ is an identity element (or two-sided identity) when it is both a left identity and a right identity.

## Notation

The identity element is written $e$, $1$ in multiplicative notation, or $0$ in additive notation.
In Mathlib, the class `Std.LawfulIdentity op o` states that `o` is a two-sided identity for the function `op`: `op o a = a` and `op a o = a` for all `a`.

## Remarks

The number $0$ is the identity element for addition on $\mathbb{Z}$, and $1$ is the identity element for multiplication.
If $e$ is a left identity and $f$ is a right identity, then $e = e \ast f = f$.
Thus an operation has at most one two-sided identity element.
The concept page [[identity element|07WYQPB8E3]] gives more examples, the non-examples and the first properties.

## Explanations

### L1 human

An identity element is an element that does nothing when you combine it with another element.
Adding $0$ to a number gives the same number, and multiplying a number by $1$ gives the same number.
Some operations have no identity element, for example addition on the positive integers.

### L2 human

To check that $e$ is an identity element, check both equations $e \ast a = a$ and $a \ast e = a$ for an arbitrary element $a$.
The equation $e \ast f = f$ in the Remarks uses that $e$ is a left identity, and the equation $e \ast f = e$ uses that $f$ is a right identity.
A trap is to check only one side: for subtraction on $\mathbb{Z}$, $a - 0 = a$, but $0 - a = -a$.
