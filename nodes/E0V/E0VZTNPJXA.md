---
tag: E0VZTNPJXA
kind: concept
name: Discriminant of a number field
msc: [11R29, 11R04]
sources:
  - url: https://en.wikipedia.org/wiki/Discriminant_of_an_algebraic_number_field
same_as:
  wikidata: Q1228885
  wikipedia: Discriminant of an algebraic number field
---

## Summary

The discriminant of an [[algebraic number field|MWBDFS2KJ5]] $K$ is a nonzero integer $d_K$ that measures the size of the ring of integers of $K$.
View the ring of integers as a lattice in a real vector space.
Up to sign and a power of $2$, $d_K$ is the square of the volume of a fundamental domain of this lattice.
A prime number ramifies in $K$ exactly when it divides $d_K$.
The discriminant appears in the [[Minkowski bound|1TQ2F9CFVE]], the [[class number formula|55XX5A7XZV]] and the [[Dedekind zeta function|KXS5DQDFYD]].

## Explanations

### L1 human

Take a basis of the ring of integers of $K$ and place it inside the complex numbers in all possible ways.
The discriminant is the squared determinant of the square table of numbers that this gives.
For the Gaussian integers $\Z[i]$, with basis $1, i$, the table is $\begin{pmatrix} 1 & i \\ 1 & -i \end{pmatrix}$ and the discriminant is $(-2i)^2 = -4$.
The only prime dividing $-4$ is $2$, and $2 = -i(1+i)^2$ is the only prime that becomes a square in $\Z[i]$, up to a unit.
A large discriminant means that the field is arithmetically complicated.
