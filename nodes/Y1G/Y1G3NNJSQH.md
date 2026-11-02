---
tag: Y1G3NNJSQH
kind: statement
role: theorem
name: Symmetric successive over-relaxation
msc: [65F10, 65F08]
uses: [0GT4WWGWH2, 0KX66CZMBB, 9V7YQA85PC, 6KQJR85ZC6, 2RPE77ACER, KE98SW3SBD]
about: [6KQJR85ZC6, KE98SW3SBD]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_successive_over-relaxation
same_as:
  wikidata: Q16937163
  wikipedia: Symmetric successive over-relaxation
---

## Statement

Let $A$ be a real symmetric $n \times n$ matrix with positive diagonal entries, and let $b \in \R^n$.
Write $A = D + L + L^T$, with $D$ diagonal and $L$ strictly lower triangular, and let $0 < \omega < 2$.
One step of *symmetric successive over-relaxation* (SSOR) is a forward [[SOR|6KQJR85ZC6]] sweep in the order $1, \dots, n$.
It is followed by a backward SOR sweep in the order $n, \dots, 1$.
In matrix form it is $x^{(k+1)} = x^{(k)} + M_\omega^{-1} \left( b - A x^{(k)} \right)$, where
$$M_\omega = \frac{1}{\omega (2 - \omega)} \, (D + \omega L) \, D^{-1} \, (D + \omega L^T).$$
Then $M_\omega$ is symmetric and positive definite.
If moreover $A$ is [[positive definite|0KX66CZMBB]], then the iteration matrix $I - M_\omega^{-1} A$ has [[spectral radius|9V7YQA85PC]] less than $1$.
So for every $b$ and every $x^{(0)}$ the iterates converge to $A^{-1} b$.

## Remarks

The matrix $M_\omega$ is symmetric by its form, and it is positive definite because $D$ is and $D + \omega L$ is invertible.
When $A$ is positive definite, each of the two SOR sweeps strictly decreases the energy norm $\norm{e}_A$ of the error, so their product contracts too.
Example: for $n = 1$ and $A = (a)$ with $a > 0$, one has $M_\omega = a / (\omega (2 - \omega))$.
The iteration matrix is $1 - \omega (2 - \omega) = (1 - \omega)^2$, which lies in $[0, 1)$ exactly when $0 < \omega < 2$.
As a stand-alone method, SSOR is usually no faster than SOR.
Its value is that $M_\omega$ is a symmetric positive definite [[preconditioner|KE98SW3SBD]], so it can be combined with the conjugate gradient method, unlike plain SOR.

## Explanations

### L1 human

SOR sweeps through the unknowns in one direction, which treats the system unevenly.
SSOR sweeps forward and then backward, so the combined step is symmetric.
This symmetry is what makes it useful together with methods that need symmetric operators.

### L2 human

The formula for $M_\omega$ shows that applying SSOR costs one forward and one backward triangular solve with the sparsity of $A$.
For $\omega = 1$ the method is symmetric Gauss–Seidel, with $M_1 = (D + L) D^{-1} (D + L^T)$.
SSOR belongs to the family of stationary [[iterative methods|2RPE77ACER]] given by a splitting $A = M_\omega - (M_\omega - A)$.
