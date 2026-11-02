---
tag: ECS1GDJ734
kind: conjecture
name: Hilbert–Pólya conjecture
msc: [11M26, 47B25, 81Q10]
uses: [1XWBY4N0VT, VCGF9YR36X, HM2HHE3J51, 86B7HF79PQ, 0BQAA2BK3Q]
about: [1XWBY4N0VT, VCGF9YR36X]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93P%C3%B3lya_conjecture
same_as:
  wikidata: Q2993323
  wikipedia: Hilbert–Pólya conjecture
history:
  posed_by: "George Pólya"
  first_stated: "1912–1914"
---

## Statement

There is a complex [[Hilbert space|HM2HHE3J51]] $H$ with a self-adjoint operator $T$ on $H$ that has the following property.
Here self-adjoint means $T = T^*$, where $T^*$ is the [[adjoint|86B7HF79PQ]] of $T$.
A complex number $\rho$ with $0 < \operatorname{Re} \rho < 1$ is a zero of the [[Riemann zeta function|1XWBY4N0VT]] if and only if $\rho = \tfrac{1}{2} + i t$ for an [[eigenvalue|0BQAA2BK3Q]] $t$ of $T$.

## Remarks

The eigenvalues of a self-adjoint operator are real, so the conjecture implies the [[Riemann hypothesis|VCGF9YR36X]]: every nontrivial zero $\rho = \tfrac{1}{2} + it$ then has real part $\tfrac{1}{2}$.
The conjecture is open.
As stated above, it is in fact equivalent to the Riemann hypothesis, since under that hypothesis a diagonal operator with the required eigenvalues can be written down directly.
So the real content of the idea lies in finding a natural operator, for instance one coming from geometry or physics, whose spectrum is given by the zeros.
Evidence for the approach comes from random matrix theory.
Montgomery's pair correlation conjecture of 1973 and Odlyzko's numerical computations indicate that the imaginary parts of the zeros are spaced like the eigenvalues of large random Hermitian matrices.
The idea is attributed to Hilbert and Pólya.
It is known through a 1982 letter of Pólya to Odlyzko, in which Pólya recalled suggesting it in Göttingen around 1912 to 1914.

## Explanations

### L1 human

The Riemann hypothesis says that all the interesting zeros of the zeta function lie on one vertical line in the complex plane.
Symmetric matrices, and more generally self-adjoint operators, always have real eigenvalues.
The Hilbert–Pólya idea is to find an operator whose eigenvalues are the heights of the zeros on that line.
Reality of the eigenvalues would then put all the zeros on the line.
No such natural operator is known.
