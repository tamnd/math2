---
tag: 2WAZF1RV2Y
kind: concept
name: Ideal of compact operators
msc: [47L20, 47B07, 46L05]
specializes: [0CD87SFM2N]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_operator_on_Hilbert_space
---

## Summary

The compact operators on a Hilbert space $H$ form a set $\mathcal{K}(H)$.
It is a norm-closed two-sided ideal of the algebra $\mathcal{B}(H)$ of bounded operators, closed under taking adjoints.
It is the norm closure of the [[finite-rank operators|Z8FABSYQTS]], and it is a C*-algebra in its own right.
For a separable infinite-dimensional $H$, it is the only closed two-sided ideal of $\mathcal{B}(H)$ other than $\set{0}$ and $\mathcal{B}(H)$, a theorem of Calkin.
The quotient $\mathcal{B}(H)/\mathcal{K}(H)$ is the [[Calkin algebra|6FE7JZ2VF1]], the setting of Fredholm theory.

## Explanations

### L1 human

Compact operators behave like small perturbations: adding or composing with a bounded operator keeps them compact.
That is what it means to be a two-sided ideal: a product $AK$ or $KA$ of a bounded operator and a compact one is again compact.
Working modulo this ideal ignores compact perturbations, which is the right point of view for questions such as whether an operator is invertible up to a finite-dimensional error.
