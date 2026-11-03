---
tag: EJVKSYHSMJ
kind: statement
role: theorem
name: Kalman decomposition
msc: [93B10, 93B05, 93B07]
uses: [A9WFM77Z4P, C4HN3EAQWM, 9NSCZ2KBEB, 0EB9N0S33C, 0ACX5QT8TE, 0S23E6YE83, 86JKV3TRFD]
about: [A9WFM77Z4P, C4HN3EAQWM]
sources:
  - url: https://en.wikipedia.org/wiki/Kalman_decomposition
same_as:
  wikidata: Q9205611
  wikipedia: Kalman decomposition
---

## Statement

Let $n, m, p \ge 1$, and let $A$, $B$, $C$ be real matrices of sizes $n \times n$, $n \times m$ and $p \times n$, for the system $x' = Ax + Bu$, $y = Cx$.
Then there is an [[invertible|0EB9N0S33C]] $n \times n$ matrix $T$ with the following property.
Split the coordinates $z = T^{-1} x$ into blocks $z = (z_1, z_2, z_3, z_4)$ of sizes $n_1, n_2, n_3, n_4 \ge 0$, with $n_1 + n_2 + n_3 + n_4 = n$.
Then
$$T^{-1} A T = \begin{pmatrix} A_{11} & 0 & A_{13} & 0 \\ A_{21} & A_{22} & A_{23} & A_{24} \\ 0 & 0 & A_{33} & 0 \\ 0 & 0 & A_{43} & A_{44} \end{pmatrix}, \quad T^{-1} B = \begin{pmatrix} B_1 \\ B_2 \\ 0 \\ 0 \end{pmatrix}, \quad C T = \begin{pmatrix} C_1 & 0 & C_3 & 0 \end{pmatrix},$$
and moreover:

1. the pair $\left( \begin{pmatrix} A_{11} & 0 \\ A_{21} & A_{22} \end{pmatrix}, \begin{pmatrix} B_1 \\ B_2 \end{pmatrix} \right)$ is [[controllable|A9WFM77Z4P]];
2. the system with matrices $\begin{pmatrix} A_{11} & A_{13} \\ 0 & A_{33} \end{pmatrix}$ and $\begin{pmatrix} C_1 & C_3 \end{pmatrix}$ is [[observable|C4HN3EAQWM]];
3. the subsystem $(A_{11}, B_1, C_1)$ is controllable and observable;
4. $C (sI - A)^{-1} B = C_1 (sI - A_{11})^{-1} B_1$ as [[transfer functions|86JKV3TRFD]].

Here $n_1 + n_2$ is the dimension of the reachable subspace and $n_2 + n_4$ is the dimension of the unobservable subspace.

## Remarks

Let $\mathcal{R}$ be the column space of $\begin{pmatrix} B & AB & \cdots & A^{n-1} B \end{pmatrix}$ and let $\mathcal{N}$ be the [[kernel|0S23E6YE83]] of the matrix with block rows $C, CA, \ldots, CA^{n-1}$.
Both are [[invariant subspaces|0ACX5QT8TE]] of $A$, with $\im B \subseteq \mathcal{R}$ and $\mathcal{N} \subseteq \ker C$.
Choose a basis of $\mathcal{R} \cap \mathcal{N}$ for the block $z_2$.
Extend it to a basis of $\mathcal{R}$ by adding $z_1$, and to a basis of $\mathcal{N}$ by adding $z_4$.
Complete it to a basis of $\R^n$ by adding $z_3$; the zero blocks express the invariances.
The [[Kalman rank condition|9NSCZ2KBEB]] and its dual then give parts 1 to 3, and part 4 follows by block elimination.
Example: for $x_1' = -x_1 + u$, $x_2' = 2 x_2$, $y = x_1$, one can take $T = I$ with $n_1 = n_4 = 1$ and $n_2 = n_3 = 0$.
Here $z_1 = x_1$ is controllable and observable, $z_4 = x_2$ is neither reachable nor seen in the output, and the transfer function is $1/(s + 1)$, which does not show the unstable mode $x_2$.

## Explanations

### L1 human

Every linear system splits into four parts.
One part can be steered and seen, one can be steered but not seen, one can be seen but not steered, and one can be neither steered nor seen.
Only the first part shows up in the relation between input and output.
So the transfer function cannot reveal the other three parts, however long one experiments.

### L2 human

The decomposition explains why a state-space model can be larger than its input-output behaviour requires.
Deleting all but the controllable and observable part gives a model with the same transfer function and the smallest possible state dimension, a minimal realization.
It also explains stabilizability and detectability: they ask that the parts that are not controllable, or not observable, have only eigenvalues with negative real part.
Hidden unstable modes in the other parts are dangerous, because a transfer function computation alone does not show them.
