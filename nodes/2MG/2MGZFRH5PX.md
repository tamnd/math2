---
tag: 2MGZFRH5PX
kind: concept
name: Weak mixing
msc: [37A25, 28D05]
specializes: [AZRPHS478B]
sources:
  - url: https://en.wikipedia.org/wiki/Mixing_(mathematics)
---

## Summary

A [[measure-preserving transformation|556WBDAHNP]] is weakly mixing when the correlations $\mu(T^{-n}A \cap B) - \mu(A)\mu(B)$ tend to $0$ on average over $n$, in absolute value.
It sits strictly between [[mixing|S3RJQ9CX2P]] and [[ergodicity|AZRPHS478B]].
Weak mixing has a clean spectral meaning: the [[Koopman operator|37TRG5DBQC]] has no eigenfunctions other than the constants.
It describes a system with no rotation hidden inside it.

## Explanations

### L1 human

A weakly mixing system mixes sets together at almost all times, though it may fail to mix at some rare times.
The rare bad times have zero density among all times.
Rotations of a circle are not weakly mixing: they turn the space rigidly, and the function $e^{2\pi i x}$ just gets multiplied by a constant at each step.
Weak mixing says that no function on the space behaves in this rigid, periodic way.
