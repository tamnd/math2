---
tag: RQ39XYAG36
kind: definition
name: Spectral theory
msc: [47A10, 47B15, 47A60]
defines: K5VZ67T9J8
uses: [YG9NR68ZH3, BMKATJ802A, 0BQAA2BK3Q, 0N6960W0BV]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_theory
---

## Definition

*Spectral theory* is the part of [[operator theory|YG9NR68ZH3]] that studies a linear operator $T$ on a Banach or Hilbert space through its [[spectrum|BMKATJ802A]] $\sigma(T)$.
This is the set of complex numbers $\lambda$ for which $T - \lambda I$ has no bounded inverse.
It extends the theory of [[eigenvalues|0BQAA2BK3Q]] and [[eigenvectors|0N6960W0BV]] of matrices.
Its main topics are the location and the parts of the spectrum, the resolvent and functional calculus.
It also contains the spectral theorems, which represent operators as multiplication operators.

## Remarks

Example: for the diagonal operator $D(x_n) = (x_n / n)$ on $\ell^2$, spectral theory gives $\sigma(D) = \set{1/n : n \ge 1} \cup \set{0}$.
Each $1/n$ is an eigenvalue with eigenvector the $n$-th unit vector, and $0$ is in the spectrum without being an eigenvalue.

Non-example: the study of the solutions of a nonlinear equation such as $u'' = u^3$ is not spectral theory in this sense, since no linear operator and no spectrum are involved.
Only its linearisation can be studied spectrally.

The word "spectrum" was used by David Hilbert before quantum mechanics.
Only later did it turn out that the spectral lines of atoms correspond to differences of eigenvalues of a quantum Hamiltonian.

## Explanations

### L1 human

Spectral theory is the study of the "eigenvalues" of operators in infinite dimensions.
It explains what replaces eigenvalues and eigenvectors when an operator has too few of them.
