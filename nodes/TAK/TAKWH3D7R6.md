---
tag: TAKWH3D7R6
kind: problem
name: Learning with errors
msc: [94A60, 68Q17, 11H06]
uses: [03VFZ2WETT, 05AQE0QR0D, WN9V7WSJKF, 0JVJ2WCXZH, 749AFR4F7Q]
about: [WN9V7WSJKF]
sources:
  - url: https://en.wikipedia.org/wiki/Learning_with_errors
same_as:
  wikidata: Q6510239
  wikipedia: Learning with errors
history:
  posed_by: "Oded Regev"
  first_stated: "2005"
---

## Problem

Let $n \ge 1$ and $q \ge 2$ be integers, and work in $\Z_q = \Z/q\Z$, the [[integers modulo q|03VFZ2WETT]].
Let $\chi$ be a probability distribution on $\Z_q$, the error distribution, typically a discretized [[normal distribution|05AQE0QR0D]] of width proportional to $\alpha q$ for some $0 < \alpha < 1$.
Fix a secret $s \in \Z_q^n$ chosen uniformly.
An LWE sample is a pair $(a, \langle a, s \rangle + e)$, where $a \in \Z_q^n$ is uniform and $e \in \Z_q$ is drawn from $\chi$, all independently.

1. Search version: given polynomially many LWE samples, find $s$.
2. Decision version: distinguish LWE samples from pairs drawn uniformly from $\Z_q^n \times \Z_q$, with non-negligible advantage.

The question is whether these problems can be solved in time polynomial in $n$.

## Remarks

Without errors, $n$ samples with linearly independent vectors $a$ give $s$ by [[Gaussian elimination|0JVJ2WCXZH]] in polynomial time; the small errors are what make the problem hard.
Regev gave a [[quantum|749AFR4F7Q]] reduction for prime $q$ polynomial in $n$ and $\alpha q > 2\sqrt{n}$.
It turns any algorithm for LWE into a quantum algorithm for worst-case approximate problems on [[lattices|WN9V7WSJKF]] of dimension $n$.
Later work gave classical reductions for some parameters.
No polynomial-time algorithm, classical or quantum, is known for LWE with these parameters.
The problem is open: it is believed hard, and it is the basis of many encryption schemes.

## Explanations

### L1 human

Solving a system of linear equations is easy.
Now add a small random error to the right side of each equation, and the problem seems to become very hard.
Learning with errors asks for the secret vector behind such noisy equations modulo $q$.
Its believed hardness, even for quantum computers, makes it a foundation of post-quantum cryptography.
