---
tag: QQPC9ASQHR
kind: concept
name: Wigner D-matrix
msc: [33C80, "22E70", 81R05]
sources:
  - url: https://en.wikipedia.org/wiki/Wigner_D-matrix
same_as:
  wikidata: Q3299244
  wikipedia: Wigner D-matrix
---

## Summary

The Wigner D-matrix $D^j(\alpha, \beta, \gamma)$ is the matrix of a rotation, given by its Euler angles, in the irreducible representation of spin $j$ of [[SU(2)|E5P8AG6CK7]].
Its entries are functions of the three angles, and they factor as $e^{-i m' \alpha} d^j_{m' m}(\beta) e^{-i m \gamma}$.
The entries for all $j$ form an orthogonal basis of the square-integrable functions on $\mathrm{SU}(2)$.
Those with integer $j$ form such a basis for the rotation group $\mathrm{SO}(3)$.
They contain the [[spherical harmonics|3F32Y21HP4]] and the [[Legendre polynomials|QFYGJVA996]] as special cases, and they are the standard tool for rotations in quantum mechanics.

## Explanations

### L1 human

A rotation of space acts on functions on the sphere, and on states of a quantum system with angular momentum $j$.
In a fixed basis of $2j + 1$ states this action is a square matrix, and this matrix is the Wigner D-matrix.
For spin $j = 1/2$ it is a $2 \times 2$ unitary matrix; a rotation by $\beta$ about the $y$-axis gives the rows $(\cos \frac{\beta}{2}, -\sin \frac{\beta}{2})$ and $(\sin \frac{\beta}{2}, \cos \frac{\beta}{2})$.
The half angles show that a full turn by $2\pi$ gives $-1$ and not $1$, a famous feature of spin.
