---
tag: JC8B3E8NGT
kind: definition
name: Quantum contextuality
msc: [81P13, 81P05]
defines: 21Q9PMSKC4
uses: [HM2HHE3J51, DF5RN297GE, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_contextuality
---

## Definition

Let $\mathcal{H}$ be a finite-dimensional complex [[Hilbert space|HM2HHE3J51]] and let $\mathcal{O}$ be a set of [[observables|DF5RN297GE]], that is, self-adjoint operators on $\mathcal{H}$.
A *context* is a subset of $\mathcal{O}$ whose elements commute pairwise.
A *noncontextual value assignment* on $\mathcal{O}$ is a map $v \colon \mathcal{O} \to \R$ with these two properties:

1. $v(A)$ is an [[eigenvalue|0BQAA2BK3Q]] of $A$ for each $A \in \mathcal{O}$;
2. if $A_1, \dots, A_k$ lie in one context, $B \in \mathcal{O}$ and $B = f(A_1, \dots, A_k)$ for a real polynomial $f$, then $v(B) = f(v(A_1), \dots, v(A_k))$.

The set $\mathcal{O}$ is *contextual*, or a proof of *quantum contextuality*, if it has no noncontextual value assignment.

## Remarks

Example: the Peres–Mermin square on $\C^4 = \C^2 \otimes \C^2$ consists of nine products of Pauli matrices arranged in a $3 \times 3$ grid.
Its rows are $X \otimes I, I \otimes X, X \otimes X$, then $I \otimes Z, Z \otimes I, Z \otimes Z$, then $X \otimes Z, Z \otimes X, Y \otimes Y$.
The entries of each row and of each column commute, and every entry squares to the identity.
Each row multiplies to $I$, and the columns multiply to $I$, $I$ and $-I$.
A value assignment would give each entry a value $\pm 1$ whose products are $+1$ on each row and on the first two columns, but $-1$ on the last column.
The product of all nine values would then be $+1$ by rows and $-1$ by columns, so the set is contextual.
Non-example: any set of pairwise commuting observables is noncontextual, since a common eigenvector $\psi$ gives the assignment $A \mapsto$ eigenvalue of $A$ on $\psi$.
