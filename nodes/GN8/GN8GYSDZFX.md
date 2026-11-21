---
tag: GN8GYSDZFX
kind: topic
name: Linear algebra
msc: ["15Axx", "97H60"]
---

## Summary

Linear algebra begins with a question every student has met: how do you solve several linear equations at once?
Answering it well leads to matrices, which store the equations, and then to vector spaces and linear maps, which explain what the matrices mean.
A vector space over a field is a set with an addition and a multiplication by scalars that obey the familiar rules of arithmetic, and a linear map is a map that respects these two operations.
The same few ideas, span, independence, basis, dimension, rank, eigenvalue and orthogonality, then answer questions about systems, geometry, differential equations, data and much more.
That is why linear algebra is used in almost every part of mathematics and in physics, statistics, engineering and computer science: many problems become linear in a first approximation, and linear problems can be solved completely.
This topic collects the linear algebra pages of math2, from arrows in the plane to the spectral theorem and quadratic forms.

## Remarks

### What the area is about

The area studies vector spaces over a field, the linear maps between them and the matrices that represent those maps, in finite dimension.
It has three faces that keep turning into one another.
A system of equations $Ax = b$ is a question about a matrix, and a matrix is a linear map written in a basis.
So row reduction, matrix algebra and the theory of linear maps describe the same objects in three languages.
Determinants measure how a map changes volume and decide when it is invertible.
Eigenvalues and canonical forms describe a map from one space to itself in the simplest possible basis.
Inner products add lengths and angles, and with them come orthogonal projections, least squares and the spectral theorems.
Bilinear and quadratic forms close the area, and a last sub-area shows the ideas at work in applications.

### History

The Chinese text The Nine Chapters on the Mathematical Art, compiled about two thousand years ago, already solved systems of linear equations by elimination.
Cramer published his rule for solving systems with determinants in 1750.
In the 1840s the subject moved toward vectors: Hamilton found the quaternions in 1843, and Grassmann's theory of extension of 1844 contained many of the ideas now central to linear algebra.
Sylvester introduced the word "matrix" in 1850, and Cayley's memoir of 1858 treated matrices as objects that can be added and multiplied.
Peano gave the axioms of a vector space in 1888, and in the 1880s Gibbs and Heaviside shaped the vector analysis of dot and cross products that physics still uses.
In the twentieth century linear algebra became a standard first course, and the Linear Algebra Curriculum Study Group, which met in 1990, published recommendations for it in 1993.

### How to read the area

Start with the first sub-area, which surveys the whole subject and then works with vectors in the plane and in space.
A reader who wants computations first can continue with systems, matrices and invertible matrices before the abstract theory.
A reader who prefers structure first can go from vectors straight to vector spaces and linear maps, and return to matrices as their coordinates.
Both routes meet at rank and change of basis, and from there determinants, eigenvalues, inner products and forms build on each other in the order below.

1. [[Overview and vectors in the plane and in space|VKVAJ94SKZ]]
1. [[Systems of linear equations and row reduction|DXSXFVDMXQ]]
1. [[Matrices and the operations on them|Y1ESNQ2V52]]
1. [[Invertible matrices and matrix factorizations|P8J6QR66TJ]]
1. [[Vector spaces, span, independence, bases and dimension|MVH97H8B2J]]
1. [[Linear maps|9080WQTZ3M]]
1. [[Direct sums, complements and quotient spaces|QHKTJ89V6S]]
1. [[Matrices of linear maps, rank and change of basis|S6559D61BP]]
1. [[Dual spaces and duality|9K7FFF26QR]]
1. [[Determinants|DTBK11SR77]]
1. [[Eigenvalues, the characteristic polynomial and the minimal polynomial|6R1D6QPY3S]]
1. [[Diagonalization, triangularization and invariant subspaces|Z6S6PWMJPH]]
1. [[Canonical forms under similarity|GEBYZKYV3D]]
1. [[Inner product spaces|1D4JTZ9VS3]]
1. [[Orthogonal complements, projections and least squares|8GQVME4SZZ]]
1. [[Adjoints, normal operators and the spectral theorems|3YM9EK6VMB]]
1. [[Isometries and the orthogonal and unitary groups|AZS5BPF5H3]]
1. [[Positive definite matrices and the singular value decomposition|SS4EVPKT3A]]
1. [[Bilinear and sesquilinear forms|DYAK7YMK7B]]
1. [[Quadratic forms over fields and the principal axis theorem|6TSCEW8QMK]]
1. [[Applications of linear algebra|K0FNC6CWZN]]

### Related areas

Several neighbors take over where this area stops.
[[Matrix theory and multilinear algebra|WMBK7M313V]] studies matrix norms, eigenvalue inequalities, matrix functions and tensor products.
[[Numerical analysis|FJEK0GMJ2J]] turns elimination, the QR decomposition and eigenvalue computations into algorithms that survive round-off.
[[Rings and modules|G7N6BDTEZ2]] replaces the field of scalars by a ring, and [[functional analysis|AFJZYWP3WQ]] lets the dimension be infinite.
The matrix groups become Lie groups in [[Lie theory and topological groups|K80DB44C78]], and linear maps that respect a group action are the subject of [[representation theory|S60Z63NM98]].
The geometry of the first sub-area continues in [[Euclidean geometry|D1SR8GDYJX]], and the story of the subject is told in [[history of mathematics|EJZNJJ6M7S]].
