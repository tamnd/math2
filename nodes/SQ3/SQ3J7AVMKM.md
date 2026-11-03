---
tag: SQ3J7AVMKM
kind: concept
name: Partial trace
msc: [81P16, 15A69, 47B10]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_trace
same_as:
  wikidata: Q7140394
  wikipedia: Partial trace
---

## Summary

The partial trace takes an operator on a [[tensor product|EY0X2NKA3S]] $\mathcal{H}_A \otimes \mathcal{H}_B$ and traces out the factor $\mathcal{H}_B$, giving an operator on $\mathcal{H}_A$.
It is the unique linear map that sends $X \otimes Y$ to $\tr(Y)\, X$; in infinite dimensions one also asks that it be continuous in the trace norm.
In quantum mechanics it produces the reduced state of a subsystem from the state of a composite system.
The reduced state gives exactly the statistics of all measurements made on the subsystem alone.

## Explanations

### L1 human

When two quantum systems are described together, one often wants to forget one of them and keep only what concerns the other.
The partial trace does this, much like computing a marginal distribution from a joint distribution of two random variables.
For a matrix written in blocks indexed by the basis of the first factor, it replaces each block by its trace.
For two maximally entangled qubits, the partial trace gives the completely mixed state $\tfrac12 I$, even though the joint state is pure.
