---
tag: P74SXXT7DX
kind: concept
name: Decidable language
msc: [03D25, 68Q45, 68Q04]
sources:
  - url: https://en.wikipedia.org/wiki/Recursive_language
same_as:
  wikidata: Q1455907
  wikipedia: Recursive language
---

## Summary

A decidable language, or recursive language, is a [[formal language|5MFZ4VNY6D]] with a [[Turing machine|758EYCN27B]] that halts on every input.
The machine answers correctly whether the input belongs to the language.
In other words, it is a [[decision problem|YAVW1XHNFH]] that an algorithm solves.
Under an encoding of strings by numbers, it corresponds to a [[computable set|PPGD5KW8JC]] of natural numbers.
Every decidable language is [[recursively enumerable|67R1A5Y54R]], but the converse fails.

## Explanations

### L1 human

A language is decidable when there is a program that, given any string, eventually stops and says yes or no correctly.
The program must never run forever.
For example, the set of strings of the form $a^n b^n$ is decidable: count the $a$s and the $b$s and compare.
The set of programs that halt on their own code is not decidable, by the halting problem.
