---
tag: JCX8X7VSQB
kind: concept
name: Calculus of inductive constructions
msc: [03B38, 68V15, 03B40]
uses: [TKMY3F6KSA, Q80JWCWNKX]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_constructions
---

## Summary

The calculus of inductive constructions is the [[calculus of constructions|TKMY3F6KSA]] extended with [[inductive types|Q80JWCWNKX]] and a hierarchy of universes.
Thierry Coquand and Christine Paulin-Mohring added the inductive definitions.
They give natural numbers, lists, equality and logical connectives as primitive types with their own induction principles.
It is the logic of the proof assistant Coq, now called Rocq, and a variant of it underlies Lean.
It keeps the impredicative sort of propositions of the calculus of constructions and adds predicative universes for data.

## Explanations

### L1 human

The calculus of constructions can encode numbers and lists, but the encodings are awkward and some natural properties cannot be proved about them.
The inductive version lets the user declare a new type by its constructors, for example natural numbers by zero and successor, and get induction on it for free.
Universes $\mathsf{Type}_0, \mathsf{Type}_1, \dots$ give each level of types a type one level up, which avoids a type of all types.
Most formal proofs in Coq and Lean are written in this system or close variants of it.
