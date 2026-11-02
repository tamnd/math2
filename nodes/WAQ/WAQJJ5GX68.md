---
tag: WAQJJ5GX68
kind: concept
name: Many-sorted algebra
msc: [08A68, 68Q65]
specializes: [QJGPT2W0FT]
sources:
  - url: https://en.wikipedia.org/wiki/Many-sorted_logic
---

## Summary

A many-sorted algebra has several carrier sets, one for each sort, and operations whose arguments and values may lie in different carriers.
It is also called a heterogeneous algebra.
Many-sorted algebras describe structures with several kinds of objects.
Examples are a module with its ring of scalars, and an automaton with its states and its input letters.
They are the standard setting for the algebraic specification of [[abstract data types|86144NHH59]] in computer science.

## Explanations

### L1 human

An ordinary algebra has one set of elements, and every operation takes elements of this set to an element of the same set.
Many real structures mix several kinds of things.
A vector space has vectors and scalars, and scalar multiplication takes one scalar and one vector to a vector.
A many-sorted algebra keeps one set for each kind, or sort, and records for each operation which sorts it takes and which sort it returns.
This avoids nonsense such as multiplying two vectors when only scalar times vector is meant.
