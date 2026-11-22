---
tag: K0FNC6CWZN
kind: topic
name: Applications of linear algebra
msc: ["15A99", "15A06"]
topics: [GN8GYSDZFX]
---

## Summary

Linear algebra earns its place in science and engineering because many real problems turn out to be linear.
This part of [[linear algebra|GN8GYSDZFX]] works through the standard applications, each as a real situation first and then as the theory that solves it.
It starts with linear systems: traffic flows, electric circuits, chemical equations, an economy, and curves through given points.
When the data does not fit exactly, least squares finds the best fit as an orthogonal projection.
Next come processes that repeat a step, such as populations, Markov chains, the ranking of web pages and differential equations, where eigenvalues and eigenvectors predict the long-run behavior.
Changes of basis then explain computer graphics, digital signals and image compression, and the singular value decomposition gives the best compression of low rank.
It ends with two less expected cases: a puzzle solved over the field with two elements, and graphs studied through their matrices.

## Remarks

### Reading order

1. [[Applications of linear systems|1QXFM0DNAH]]: you learn to turn traffic, circuits, chemical equations and an economy into one matrix equation.
2. [[Polynomial interpolation by a linear system|NR58EBS932]]: you see why exactly one polynomial passes through given points, and how the Lagrange basis writes it down at once.
3. [[Curve fitting and linear regression by least squares|C170QFW8QB]]: you learn to fit a line or a parabola to data, and to read $R^2$ as a projection length.
4. [[Linear recurrences by linear algebra|K00NJY6C33]]: you get closed formulas, such as Binet's formula, by diagonalizing one matrix.
5. [[Linear discrete dynamical systems|2F1B461YN7]]: you learn to predict the long-run behavior of predator-prey and age-structured populations from eigenvalues.
6. [[Steady-state vectors of Markov chains|Y9FRWY8YX4]]: you find the long-run shares of a random process, and you learn when they are unique.
7. [[PageRank as an eigenvector problem|9ZPQYZ5NDP]]: you see how a search engine ranks pages with one eigenvector and repeated multiplication.
8. [[Linear systems of ODEs by eigenvectors|DH7CQXQYJX]]: you solve systems of differential equations with exponentials along eigenvectors.
9. [[Linear algebra in computer graphics|REB4ZHN28T]]: you learn to move, turn and project pictures with products of matrices, and why the order matters.
10. [[Change of basis in signal and image processing|6NANBCYMG2]]: you see how a good basis makes most coordinates small, which is the idea behind JPEG.
11. [[Image compression by the SVD|9QB82PPEMV]]: you learn to compress an image by its largest singular values, with an exact error formula.
12. [[Lights Out puzzle|E8DZ9CPEEE]]: you solve a puzzle by a linear system over $\mathbb F_2$, and you see rank decide solvability.
13. [[Matrices of graphs as linear algebra examples|JFWP2SBCF0]]: you count walks with matrix powers and solve an electric network with the Laplacian.

### Prerequisites

Each page relies on one part of the theory.
[[Systems of linear equations and row reduction|DXSXFVDMXQ]] is needed for items 1, 2 and 12.
[[Orthogonal complements, projections and least squares|8GQVME4SZZ]] is needed for item 3.
[[Diagonalization, triangularization and invariant subspaces|Z6S6PWMJPH]] is needed for items 4 to 8.
[[Isometries and the orthogonal and unitary groups|AZS5BPF5H3]] is needed for items 9 and 10.
[[Positive definite matrices and the singular value decomposition|SS4EVPKT3A]] is needed for item 11.
