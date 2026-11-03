---
tag: T3Q8G4HBHV
kind: example
name: K1 of a Euclidean domain
msc: [19B99]
instance_of: [SXVNJY4XFY]
uses: [0CHS7RBD39, 07C6ECNJET, E5JXB0E324, 00KDZRW4C0, AAB05HS00Y]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
    locator: K1
---

## Example

Let $R$ be a [[Euclidean domain|0CHS7RBD39]] with [[group of units|07C6ECNJET]] $R^\times$.
Then the [[determinant|00KDZRW4C0]] induces an isomorphism $K_1(R) \cong R^\times$, that is, $SK_1(R) = 0$.
Check: let $A \in SL_n(R)$.
In the first column, run the Euclidean algorithm with operations "add a multiple of one row to another".
That is, subtract multiples of the row with the entry of smallest size from the others, until only one nonzero entry remains.
That entry is then a greatest common divisor of the first column, which is a unit $u$ because $A$ is invertible.
More operations of the same kind move it to the top left.
Adding multiples of the first column to the other columns then clears the rest of the first row.
Column operations are allowed since they are right multiplications by elementary matrices.
This leaves $\mathrm{diag}(u, B)$ with $B \in GL_{n-1}(R)$.
By induction, $A$ is reduced to $\mathrm{diag}(u_1, \dots, u_n)$ with $u_1 \cdots u_n = 1$, and such a diagonal matrix lies in the [[elementary subgroup|E5JXB0E324]], because $\mathrm{diag}(u, u^{-1}) \in E_2(R)$ for every unit $u$.
Hence $A \in E_n(R)$ and [[SK1|AAB05HS00Y]] of $R$ vanishes.
For example, $K_1(\Z) \cong \set{\pm 1}$, $K_1(\Z[i]) \cong \set{\pm 1, \pm i}$, and $K_1(F[x]) \cong F^\times$ for a field $F$.

## Explanations

### L1 human

In a Euclidean domain one can divide with remainder, and this lets row operations act like the Euclidean algorithm.
So any matrix of determinant $1$ can be reduced to the identity by row operations.
As for fields, $K_1$ is then just the group of units: the integers give the two-element group $\set{\pm 1}$.
