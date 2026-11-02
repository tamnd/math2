---
tag: 4XRVJE0KAN
kind: concept
name: Finite model theory
msc: [03C13, 68Q19]
specializes: [HFTBG5PMXC]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_model_theory
same_as:
  wikidata: Q5450405
  wikipedia: Finite model theory
---

## Summary

Finite model theory is the part of [[model theory|HFTBG5PMXC]] that studies logics on finite [[structures|983GZBQYT4]].
Many classical tools fail there; for example, the [[compactness theorem|1NR3HAWG9D]] does not hold when only finite structures are allowed.
Instead the field uses combinatorial tools such as [[Ehrenfeucht–Fraïssé games|2RE7YAZK8R]] and locality arguments.
It is closely tied to computer science, through databases and descriptive complexity, where [[Fagin's theorem|BG8Q0BYSQ3]] matches a logic with a complexity class.

## Explanations

### L1 human

A finite structure is, for example, a finite [[graph|00C0BR7D7H]] or a finite database table.
Finite model theory asks which properties of such objects can be written as sentences of a given logic.
A typical result: "the graph is connected" cannot be written as a single first-order sentence about finite graphs.
The proof uses a game between two players that compares two graphs move by move.
Questions of this kind relate the power of a logic to the computing time needed to check a property.
