---
tag: 0BQAA2BK3Q
kind: concept
name: Eigenvalue
aliases: [characteristic-value, characteristic-root, proper-value]
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
uses: [0J7H0YBFDJ, 0S23E6YE83, 0912EEEVCT]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: General definition
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: History
  - book: isbn:9783031410253
    locator: Chapter 5
  - book: isbn:9780134860244
  - book: isbn:9780135367971
---

## Summary

Let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]] of a vector space $V$ over a field $F$.
A scalar $\lambda \in F$ is an eigenvalue of $T$ when $T(v) = \lambda v$ for some vector $v \ne 0$.
Equivalently, the map $T - \lambda \id_V$ has a nonzero [[kernel|0S23E6YE83]].
An eigenvalue of an $n \times n$ matrix $A$ is an eigenvalue of the map $x \mapsto Ax$ on $F^n$.
In finite dimension, the eigenvalues are the roots of the [[characteristic polynomial|0VSSPAFM2C]].

## Motivation

Most vectors change their direction under a linear map.
Some vectors only get multiplied by a scalar.
On the line through such a vector, the map is the multiplication by one number, the eigenvalue.
If there are enough of these lines, then the map is diagonal in a suitable basis, and powers, exponentials and limits become easy to compute.
Eigenvalues give the growth rates of linear recurrences, the frequencies of vibrating systems and the long-run state of Markov chains.

## Notation

The formal definition is the [[definition of an eigenvalue|0ZND7NQ970]].
The set of eigenvalues of a matrix $A$ is its [[spectrum|0XPX5NC67E]], written $\sigma(A)$ or $\operatorname{spec}(A)$.
Older books write "characteristic value", "characteristic root" or "proper value".
Mathlib writes `Module.End.HasEigenvalue T λ`.

## Remarks

### Examples

- [[The symmetric matrix with rows (2, 1) and (1, 2)|~300f406e]] has the eigenvalues $1$ and $3$.
- [[The spectrum depends on the field|~3e12f65b]]: the matrix with rows $(0, -1)$ and $(1, 0)$ has no eigenvalue over $\R$, the eigenvalues $\pm i$ over $\C$, and the eigenvalues $2$ and $3$ over $\mathbb{F}_5$.
- [[The left shift on sequences|~56ecd655]] has every scalar as an eigenvalue, and the right shift has none.
- [[The derivative on smooth functions|~358c3d83]] has every real number as an eigenvalue, with the eigenvector $e^{\lambda x}$.
- A triangular matrix has its diagonal entries as eigenvalues, as in [[a triangular example|~fa4b2e8e]].

### Non-examples

- [[A rotation of the plane by an angle that is not a multiple of pi|~805e3c17]] has no real eigenvalue.
- [[The diagonal entries of a non-triangular matrix|~7c7ab2bb]] are in general not its eigenvalues.
- [[Row reduction changes the eigenvalues|~19d290f5]]: the echelon form of a matrix has other eigenvalues.

### Basic properties

- $\lambda$ is an eigenvalue of $T$ if and only if $T - \lambda \id_V$ is not injective, by the definition.
- In finite dimension, this holds if and only if $T - \lambda \id_V$ is not invertible, by the theorem on [[injective, surjective and bijective endomorphisms|0912EEEVCT]].
- In finite dimension $n \ge 1$, the eigenvalues are [[the roots of the characteristic polynomial|053QVHF6N7]]. So there are at most $n$ of them.
- [[Over an algebraically closed field, an eigenvalue exists|08CJB2NQ92]] when $0 < \dim V < \infty$. Over $\R$ this fails for rotations.
- The eigenvalues are also [[the roots of the minimal polynomial|0QF4ZEFG52]].
- If $\lambda$ is an eigenvalue of $T$ and $p$ is a polynomial, then $p(\lambda)$ is an eigenvalue of $p(T)$, by the theorem on [[eigenvalues of a polynomial in an endomorphism|~ceb4bf0e]].
- Similar matrices have the same eigenvalues, because they have the same characteristic polynomial.
- The sum of the eigenvalues with multiplicity is the [[trace|0NMXDCNNKR]], and their product is the [[determinant|0C2F40MEBC]], when the characteristic polynomial splits.

### History

Euler studied the rotation of rigid bodies and saw the importance of the principal axes.
Lagrange saw that the principal axes are the eigenvectors of the inertia matrix.
Cauchy showed that a real symmetric matrix has real eigenvalues, in his work on quadric surfaces.
Cauchy also introduced the term "racine caractéristique", the characteristic root.
Hilbert used the German word "eigen" in this sense in his work on integral operators, in 1904.
The prefix "eigen" means "own" or "proper", and the hybrid word "eigenvalue" became standard in English.

### Common errors

- Allowing $v = 0$ in $T(v) = \lambda v$. This equation holds for every $\lambda$ when $v = 0$, so the definition requires $v \ne 0$.
- Excluding $\lambda = 0$. The scalar $0$ is an eigenvalue exactly when $T$ is not injective.
- Reading eigenvalues off the diagonal of a matrix that is not triangular.
- Forgetting the field. A real matrix can have no real eigenvalue and still have complex eigenvalues.

## Explanations

### L1 human

A matrix moves vectors in the plane or in space.
Most vectors get turned to a new direction.
Some special vectors stay on their own line and only get longer, shorter or flipped.
The stretch factor for such a vector is an eigenvalue.
For example, the matrix with rows $(2, 0)$ and $(0, 3)$ stretches the first axis by $2$ and the second axis by $3$.
So $2$ and $3$ are its eigenvalues.

### L2 human

We find the eigenvalues of $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.

1. The scalar $\lambda$ is an eigenvalue when $A - \lambda I$ is not invertible, that is, when $\det(\lambda I - A) = 0$.
2. $\det(\lambda I - A) = (\lambda - 2)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3)$.
3. So the eigenvalues are $1$ and $3$.
4. Check: $A (1, -1)^{\mathsf{T}} = (1, -1)^{\mathsf{T}}$ and $A (1, 1)^{\mathsf{T}} = (3, 3)^{\mathsf{T}} = 3 (1, 1)^{\mathsf{T}}$.

The typical use is to find directions in which a linear system decouples into independent scalar equations.
A trap: the eigenvalues of $A + B$ or $AB$ are in general not sums or products of eigenvalues of $A$ and $B$.

### L3 human

An eigenvalue is a point $\lambda$ where the operator $T - \lambda$ fails to be injective.
In infinite dimension, injective and invertible differ, and the [[spectrum of an operator|XXXSST2DR5]] collects all $\lambda$ where $T - \lambda$ is not invertible.
The eigenvalues then form only the point spectrum.
Algebraically, $V$ is a module over $F[x]$ with $x$ acting as $T$, and the eigenvalues are the $\lambda$ for which the module has the simple submodule $F[x]/(x - \lambda)$.
For matrix analysis results such as the [[Gershgorin disc theorem|0ETGP0XVCJ]] and the [[Perron-Frobenius theorem|62NS7PV1M9]], see the matrix analysis area.
