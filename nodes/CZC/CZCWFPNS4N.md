---
tag: CZCWFPNS4N
kind: example
name: Special unitary group SU(n)
msc: ["22E15", "22C05", "20G20"]
instance_of: [9TFC6ADC1C]
uses: [0R9R0Y1HDK, 00KDZRW4C0, 7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Special_unitary_group
same_as:
  wikidata: Q684363
  wikipedia: Special unitary group
---

## Example

Let $n \ge 1$.
The *special unitary group* is
$$SU(n) = \set{U \in M_n(\C) : U^* U = I_n, \ \det U = 1},$$
where $U^*$ is the conjugate transpose of $U$ and $I_n$ is the identity matrix.
It is the kernel of the [[determinant|00KDZRW4C0]] $\det \colon U(n) \to U(1)$ on the [[unitary group|0R9R0Y1HDK]], so it is a normal subgroup of $U(n)$.

Check that it is a [[compact Lie group|9TFC6ADC1C]].
The two conditions are polynomial equations in the real and imaginary parts of the entries, so $SU(n)$ is closed in $GL_n(\C)$.
By the closed subgroup theorem it is a [[Lie group|7JBRGCVJRB]].
Each column of a unitary matrix is a unit vector, so $SU(n)$ is bounded in $M_n(\C)$, hence compact.

## Remarks

Its Lie algebra $\mathfrak{su}(n)$ consists of the skew-Hermitian $n \times n$ matrices with trace $0$, so its real dimension is $n^2 - 1$.
$SU(n)$ is connected and simply connected.
Its centre is the set of scalar matrices $\omega I_n$ with $\omega^n = 1$, a cyclic group of order $n$.
For $n \ge 2$ its Lie algebra is simple, of type $A_{n-1}$.
In Mathlib this group is `Matrix.specialUnitaryGroup`.

## Explanations

### L1 human

The special unitary group collects the complex matrices that keep lengths and also have determinant $1$.
The unitary group is a little larger: its determinants are all complex numbers of absolute value $1$.
Fixing the determinant to $1$ removes one real degree of freedom, a single overall phase.
For $n = 1$ the group is trivial, and for $n = 2$ it is a copy of the $3$-sphere.
The groups $SU(2)$ and $SU(3)$ are central in particle physics.
