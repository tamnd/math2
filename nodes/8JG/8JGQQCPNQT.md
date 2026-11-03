---
tag: 8JGQQCPNQT
kind: concept
name: Zero-knowledge proof
msc: [68Q10, 94A60, 68Q15]
specializes: [7PFQZJF1DX]
sources:
  - url: https://en.wikipedia.org/wiki/Zero-knowledge_proof
same_as:
  wikidata: Q191943
  wikipedia: Zero-knowledge proof
---

## Summary

A zero-knowledge proof is an [[interactive proof|7PFQZJF1DX]] in which the verifier becomes convinced that a statement is true but learns nothing else.
"Nothing else" is made precise by a simulator.
Whatever the verifier sees could have been produced by an efficient algorithm that never talked to the prover.
The notion was introduced by Goldwasser, Micali and Rackoff in the 1980s.
It is a basic tool of cryptography, used for identification schemes and for protocols that must stay secure against cheating parties.

## Explanations

### L1 human

Imagine you want to convince a friend that you know the solution of a puzzle without showing the solution.
You answer a series of random challenges that you could only pass reliably if you really know it.
Each answer, taken alone, looks like something your friend could have made up without you.
So at the end your friend is sure that you know a solution, but cannot use what was seen to solve the puzzle.
A classical example is graph isomorphism: the prover shows that two graphs are isomorphic by answering random challenges about a freshly scrambled copy, never revealing the isomorphism itself.
