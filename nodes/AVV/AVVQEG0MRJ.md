---
tag: AVVQEG0MRJ
kind: concept
name: Type system
msc: [68N15, 03B38, 68Q55]
sources:
  - url: https://en.wikipedia.org/wiki/Type_system
same_as:
  wikidata: Q865760
  wikipedia: Type system
---

## Summary

A type system is a set of rules that assigns a type to each part of a program.
Examples of types are "integer" and "function from integers to booleans".
Its purpose is to reject programs that would misbehave, for example by adding a number to a function, before they run.
A type system is sound when well-typed programs cannot reach such errors, a property called [[type safety|CY0V19041Y]].
Type systems for programming languages are formal systems in the sense of [[type theory|Q48KGV33AH]].

## Explanations

### L1 human

In everyday language, "the number seven is green" is grammatical but makes no sense.
A type system catches the same kind of nonsense in programs.
It labels each expression with a kind of value and checks that operations get the right kinds.
For example, `length("hello") + 1` passes, while `length(5) + "a"` is rejected.
Some languages check types before the program runs (static typing), others while it runs (dynamic typing).
