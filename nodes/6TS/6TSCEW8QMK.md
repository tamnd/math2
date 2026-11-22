---
tag: 6TSCEW8QMK
kind: topic
name: Quadratic forms over fields and the principal axis theorem
msc: ["15A63", "11E04"]
topics: [GN8GYSDZFX]
---

## Summary

A quadratic form is a homogeneous polynomial of degree $2$, such as $x^2 + 4xy + y^2$, viewed as a function on a vector space of finite dimension.
This part of [[linear algebra|GN8GYSDZFX]] asks when two such forms are the same after a change of variables.
When $2$ is invertible in the field, each form comes from a unique symmetric bilinear form, its polar form, and so from a symmetric matrix with half of each cross coefficient off the diagonal.
Completing squares, or an orthogonal basis, then turns every form into a sum $a_1 x_1^2 + \cdots + a_n x_n^2$.
The coefficients $a_i$ are not unique, and the rest of the story is about what survives.
Over $\mathbb{C}$ only the number of nonzero coefficients survives, the rank.
Over $\mathbb{R}$ the counts of positive and negative coefficients also survive, by Sylvester's law of inertia, and they form the signature.
Over a finite field of odd characteristic, the rank and the discriminant, the determinant modulo squares, classify the forms.
The real case comes back with more structure through the principal axis theorem.
An orthogonal change of variables keeps the dot product and turns a real form into $\sum_i \lambda_i y_i^2$, with the eigenvalues $\lambda_i$ of its matrix.
This decides whether a form is positive definite, finds its extreme values on the unit sphere, and sorts plane conics and quadric surfaces into their types.

## Remarks

### Reading order

1. [[Quadratic form|0RBQS1JJCR]]: what a quadratic form is, and how a polynomial of degree $2$ gives a symmetric matrix.
2. [[Polar form|0HYFWKKY3C]]: how a form and its symmetric bilinear form determine each other, and why characteristic $2$ is different.
3. [[Diagonalization of quadratic forms|0Z3FEWZ8HA]]: how to remove all cross terms by completing squares or by an orthogonal basis.
4. [[Sylvester's law of inertia|0WFED3K3DQ]]: why every diagonal form of a real form has the same numbers of positive and negative coefficients.
5. [[Signature and inertia|07EZA80NEH]]: the triple $(p, q, r)$, its conventions, and the classification of real forms it gives.
6. [[Classification over C and algebraically closed fields|0CEX9BRXRZ]]: why the rank is the only invariant when every number is a square.
7. [[Quadratic forms over finite fields|2HBR7137AD]]: how the dimension and the discriminant classify forms over a finite field of odd characteristic.
8. [[Discriminant of a quadratic form|MZFRXECCMC]]: the determinant modulo nonzero squares, and how it relates to $b^2 - 4ac$.
9. [[Positive definite quadratic form|0RP20HFYM3]]: how to test positivity by eigenvalues, by leading minors and by completing squares.
10. [[Definite, semidefinite and indefinite forms|01RBSSGMY5]]: the five types of real forms, and their use in the second derivative test.
11. [[Principal axis theorem|0PR5P9Z4KM]]: how an orthogonal change of variables turns a real form into $\sum_i \lambda_i y_i^2$ with the eigenvalues.
12. [[Conics by quadratic forms|1DGT7X9E35]]: how a rotation and a translation bring a plane conic to its standard equation.
13. [[Quadric surfaces by quadratic forms|F42W4DQHBK]]: how the signs of the eigenvalues sort the quadric surfaces in space.
14. [[Extreme values on unit vectors|YS4HT1EYE5]]: why the largest and smallest values of a form on the unit sphere are its extreme eigenvalues.

### Prerequisites

- [[Bilinear and sesquilinear forms|DYAK7YMK7B]]: bilinear forms, their matrices, congruence and orthogonality, which the whole topic uses.
- [[Adjoints, normal operators and the spectral theorems|3YM9EK6VMB]]: the spectral theorem for real symmetric matrices, which the principal axis theorem rests on.
