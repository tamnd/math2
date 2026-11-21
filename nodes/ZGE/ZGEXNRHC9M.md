---
tag: ZGEXNRHC9M
kind: concept
name: Recursively saturated model
aliases: [recursively-saturated-structure, resplendent-model]
msc: ["03C50", "03C57", "03C62"]
topics: [Z772KEC9BY]
audience: research
uses: [983GZBQYT4, 9V71Q3SD1G, PPGD5KW8JC, RMTZ5J64FX, HACXBCM7SS, 0EBACQFAZW]
history:
  notes: "Barwise and Schlipf studied recursively saturated and resplendent models in a 1976 paper and proved that countable recursively saturated structures are resplendent."
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
    locator: lead section
  - book: isbn:9780521587136
---

## Summary

Let $L$ be a finite or computable signature, with formulas coded by natural numbers.
An $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ is *recursively saturated* when for every finite tuple $\bar{a}$ of $\mathcal{M}$ and every [[computable|PPGD5KW8JC]] set $p(x, \bar{y})$ of $L$-formulas, if $p(x, \bar{a})$ is finitely satisfiable in $\mathcal{M}$, then some element of $\mathcal{M}$ realizes it.
It is *resplendent* when every expansion that is consistent with the theory of $(\mathcal{M}, \bar{a})$ and described by one sentence in finitely many new symbols can be carried out on $\mathcal{M}$ itself.
Recursive saturation is the part of saturation that can be stated with finitely many parameters and computable [[types|9V71Q3SD1G]].
Countable recursively saturated models exist for every theory, unlike countable saturated models, and they are resplendent.

## Motivation

A countable complete theory may have $2^{\aleph_0}$ types, and then it has no countable saturated model.
Most of these types are not computable, and the types that appear in practice, such as "larger than every numeral" or "a root of every polynomial of a computable list", are.
Recursive saturation keeps exactly these types, so it is available in every countable language and every theory, and it is still strong enough for many back-and-forth arguments.
Resplendence is the expansion property that recursive saturation gives in the countable case: second-order wishes that are consistent are met inside the model.

## Notation

The word "recursive" is the older name for "computable", and some authors write *computably saturated*.
The theory of $(\mathcal{M}, \bar{a})$ is the set of sentences with constants $\bar{c}$ for $\bar{a}$ that hold in $\mathcal{M}$ when $\bar{c}$ names $\bar{a}$.

## Remarks

### Examples

- Every $\aleph_0$-saturated structure in a computable language is recursively saturated, such as $(\Q, <)$; see [[the rational order is saturated|9H064SE6ZN]].
- An algebraically closed field of infinite transcendence degree is recursively saturated; see [[saturated algebraically closed fields|QX6K7CWWNV]].
- A countable recursively saturated model of [[Peano arithmetic|HACXBCM7SS]] exists, and it is not saturated; see [[a countable recursively saturated model of arithmetic|7S8PZZGBTM]].

### Non-examples

- The standard model of arithmetic omits the computable type of an infinite number; see [[the type of an infinite natural number|Q0H5CJGCAY]].
- The field $\overline{\Q}$ omits the computable type of a transcendental number; see [[the algebraic numbers are not saturated|9JGR3GXPMK]].
- The order $(\Z, <)$ omits the computable type of an element at infinite distance from $0$; see [[the integer order is homogeneous but not saturated|YNSR6VMS8A]].

### Basic properties

- Every structure $\mathcal{M}$ has a recursively saturated elementary extension of size $\abs{M} + \aleph_0$; the proof is in the [[definition|6PTR9NC149]].
- A resplendent structure is recursively saturated.
- A countable recursively saturated structure is resplendent.
- A countable recursively saturated structure need not be saturated, since only countably many types are computable.

### History

Barwise and Schlipf studied recursively saturated and resplendent models in 1976, and proved that countable recursively saturated structures are resplendent.

### Common errors

- Allowing infinitely many parameters: the definition allows a finite tuple $\bar{a}$ only, and a computable set of formulas in which $\bar{a}$ fills fixed variables.
- Confusing recursive saturation with saturation: a countable recursively saturated model of Peano arithmetic omits most complete types over $\emptyset$.

## Explanations

### L1 human

A recursively saturated structure realizes every list of properties that a computer program can produce, as long as the list is consistent and mentions finitely many elements of the structure.
So it has all the elements that a mechanical description can ask for.
It need not have elements for descriptions that no program can list.

### L2 human

We show that a recursively saturated model $\mathcal{M}$ of the theory of $(\N, 0, 1, +, \cdot, <)$ is nonstandard.

1. Let $p(x) = \set{\underline{n} < x : n \in \N}$, where $\underline{n}$ is the term $1 + \cdots + 1$ with $n$ terms.
2. A program can list the formulas of $p$, so $p$ is computable.
3. A finite part of $p$ is satisfied by a large numeral in $\mathcal{M}$, since $\mathcal{M}$ satisfies the same sentences as $\N$.
4. So some $b \in M$ realizes $p$, and $b$ lies above every standard number.

The typical use is to get nonstandard elements with prescribed computable properties.
The trap is to forget that the parameters must be finitely many.

### L3 human

In models of arithmetic, recursive saturation is a central tool: a countable nonstandard model of Peano arithmetic has a full satisfaction class exactly when it is recursively saturated.
See [[models of arithmetic|XFKQW3988J]] for the setting.
