---
tag: 2EASHBY4TX
kind: concept
name: Structured singular value
msc: [93B35, 93D09, 15A18]
sources:
  - url: https://en.wikipedia.org/wiki/Robust_control
---

## Summary

The structured singular value $\mu$ of a complex matrix $M$ is built from the smallest block-diagonal perturbation that makes a feedback loop around $M$ singular.
It lies between the [[spectral radius|9V7YQA85PC]] and the largest [[singular value|09VMDSRXWJ]] of the matrix, which are its values for the two extreme structures.
Evaluated at every frequency on the closed-loop transfer function, it gives an exact test of [[robust control|5MGHZRFCVR]] stability against structured uncertainty.
The [[small-gain theorem|1CF728E75M]] alone gives only a sufficient condition.

## Explanations

### L1 human

In a control loop, several uncertain parts can each be off by some amount, independently of each other.
The largest singular value treats the uncertainty as one big unknown matrix and is often too pessimistic.
The structured singular value takes into account that the uncertain parts sit in separate blocks.
Its reciprocal is the size of the smallest such perturbation that breaks the loop.
