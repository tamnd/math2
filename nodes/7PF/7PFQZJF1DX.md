---
tag: 7PFQZJF1DX
kind: concept
name: Interactive proof system
msc: [68Q10, 68Q15, 68Q87]
sources:
  - url: https://en.wikipedia.org/wiki/Interactive_proof_system
same_as:
  wikidata: Q1665886
  wikipedia: Interactive proof system
---

## Summary

An interactive proof system is a protocol between an all-powerful prover and a randomised polynomial-time verifier.
By exchanging messages, the prover tries to convince the verifier that an input belongs to a language.
The verifier must accept true claims with high probability and reject false claims with high probability, whatever the prover does.
The class IP of languages with such proofs equals [[PSPACE|T9NTRY93ZT]], which is much larger than [[NP|QQRA9GBW51]] is believed to be.
Interactive proofs led to zero-knowledge proofs and to the PCP theorem.

## Explanations

### L1 human

In an NP proof, the prover writes down a certificate and the verifier checks it alone.
In an interactive proof, the verifier may ask random questions and the prover answers them.
For example, to convince someone that two graphs are not isomorphic, the verifier secretly picks one of them, scrambles its vertices and asks which graph it came from.
A prover can always answer correctly only if the graphs really are different; otherwise it must guess and is caught half of the time.
