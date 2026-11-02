---
tag: KX3QRA3CEP
kind: concept
name: Exponential of a bounded operator
msc: [47A60, 47D06]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_exponential
---

## Summary

The exponential of a bounded operator $T$ on a Banach space is the operator $e^T = \sum_{n \ge 0} T^n / n!$.
It extends the [[matrix exponential|020M04FN1H]] to infinite dimensions.
The family $t \mapsto e^{tT}$ solves the linear differential equation $x' = Tx$ in the Banach space and is the simplest example of an operator semigroup.

## Explanations

### L1 human

The exponential of a number can be computed by the series $1 + t + t^2/2 + t^3/6 + \cdots$.
The same series makes sense when $t$ is replaced by a bounded operator, because the factorials make the terms shrink fast.
If $T$ multiplies the $n$-th coordinate of a sequence by $\lambda_n$, with $(\lambda_n)$ bounded, then $e^T$ multiplies it by $e^{\lambda_n}$.
This turns a rule of instantaneous change, $x' = Tx$, into the state at every later time, $x(t) = e^{tT} x(0)$.
