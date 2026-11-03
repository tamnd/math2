---
tag: SDJ23BAFF7
kind: concept
name: Finite-state transducer
msc: [68Q45]
sources:
  - url: https://en.wikipedia.org/wiki/Finite-state_transducer
same_as:
  wikidata: Q2166395
  wikipedia: Finite-state transducer
---

## Summary

A finite-state transducer is a finite automaton with two tapes: it reads an input word and writes an output word.
Its transitions are labelled by pairs of input and output pieces.
It defines a relation between input words and output words, called a rational relation.
Finite-state transducers generalize [[nondeterministic finite automata|SFMYM96C1B]], which have only an input tape, and the deterministic [[Mealy machines|BDWD5J39DJ]].
They are used in natural language processing, for example in morphology and speech recognition, and in text rewriting.

## Explanations

### L1 human

A transducer is a translator with finite memory.
Each arrow says "read this, write that", and either part may be empty.
For example, a one-state transducer can rewrite every lower-case letter of a word into upper case.
Because it may be nondeterministic and may read or write nothing on a step, one input can have several outputs, or none.
