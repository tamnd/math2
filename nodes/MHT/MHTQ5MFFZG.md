---
tag: MHTQ5MFFZG
kind: definition
name: Complete set of commuting observables
msc: ["81Q10", "47B15"]
defines: 11P6PR0HYQ
uses: [DF5RN297GE, 8G3X8MPG7E, 0G0RFPG8HR, 0S9GGTR0EX, PSFWQVZ0FS]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_set_of_commuting_observables
---

## Definition

Let $\mathcal{H}$ be a finite-dimensional complex Hilbert space, and let $A_1, \dots, A_k$ be [[observables|DF5RN297GE]] on $\mathcal{H}$, that is, self-adjoint operators.
The set $\set{A_1, \dots, A_k}$ is a *complete set of commuting observables* if:

1. $A_i A_j = A_j A_i$ for all $i, j$;
2. for every $(\lambda_1, \dots, \lambda_k) \in \R^k$, the joint [[eigenspace|0G0RFPG8HR]] $\set{\psi \in \mathcal{H} : A_i\psi = \lambda_i\psi \text{ for } i = 1, \dots, k}$ has dimension at most $1$.

## Remarks

By clause 1, the $A_i$ are [[commuting|8G3X8MPG7E]] self-adjoint operators, so they have a common [[orthonormal basis|0S9GGTR0EX]] of eigenvectors.
Clause 2 says that this basis is unique up to order and phases, and that each basis vector is labelled by its tuple of eigenvalues.
Equivalently, every operator that commutes with all $A_i$ is a polynomial in $A_1, \dots, A_k$.
In infinite dimension, one asks that the spectral projections of the $A_i$ commute and that the [[von Neumann algebra|PSFWQVZ0FS]] they generate be maximal abelian.

Example: let $e_1, e_2$ be the standard basis of $\C^2$.
On $\C^2 \otimes \C^2 \cong \C^4$, let $A_1 = \sigma_z \otimes I$ and $A_2 = I \otimes \sigma_z$ with $\sigma_z = \mathrm{diag}(1, -1)$.
They commute, and the four joint eigenspaces for $(\pm 1, \pm 1)$ are spanned by the four vectors $e_a \otimes e_b$, each of dimension $1$.

Non-example: $\set{A_1}$ alone commutes with itself, but its eigenspace for the eigenvalue $1$ is spanned by $e_1 \otimes e_1$ and $e_1 \otimes e_2$, of dimension $2$, so clause 2 fails.
