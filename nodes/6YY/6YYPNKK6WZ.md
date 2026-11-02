---
tag: 6YYPNKK6WZ
kind: statement
role: theorem
name: Laurent phenomenon
msc: [13F60, 39A20]
uses: [TKK0TV2MYC, QMY5JTZZB8]
about: [TKK0TV2MYC]
sources:
  - url: https://en.wikipedia.org/wiki/Cluster_algebra
---

## Statement

Let $(\mathbf{x}, B)$ be a seed, with cluster $\mathbf{x} = (x_1, \dots, x_n)$ and a skew-symmetrizable integer matrix $B$, and let $\mathcal{A}(B)$ be the coefficient-free [[cluster algebra|TKK0TV2MYC]] it generates.
Then every cluster variable of $\mathcal{A}(B)$ is a Laurent polynomial with integer coefficients in $x_1, \dots, x_n$, that is, an element of the [[Laurent polynomial ring|QMY5JTZZB8]] $\Z[x_1^{\pm 1}, \dots, x_n^{\pm 1}]$.

## Remarks

The theorem is due to Fomin and Zelevinsky.
Each mutation divides by a cluster variable, so a priori the cluster variables are only rational functions of the initial ones.
The content of the theorem is that all these denominators are monomials.
The proof goes by induction on the length of a mutation sequence, and it uses that the exchange polynomials of neighbouring mutations are coprime.
Example: for $n = 2$ and $B = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, the cluster variables satisfy $x_{m+1} x_{m-1} = x_m + 1$.
Starting from $x_1, x_2$ one gets $x_3 = (x_2 + 1)/x_1$, $x_4 = (x_1 + x_2 + 1)/(x_1 x_2)$, $x_5 = (x_1 + 1)/x_2$, and then $x_6 = x_1$, $x_7 = x_2$.
All five are Laurent polynomials in $x_1, x_2$.
The special form of the exchange relations matters: a general rational recurrence produces denominators that are not monomials.

## Explanations

### L1 human

Some recurrences divide at every step, yet the result never has a real denominator.
The Laurent phenomenon says this happens for all the variables of a cluster algebra: only powers of the starting variables ever appear in the denominators.
Setting all starting variables to $1$ then gives integers, which explains why some nonlinear integer sequences stay integral.

### L2 human

The Laurent phenomenon is one of the founding results of the theory of cluster algebras.
Several nonlinear recurrences, such as the Somos-4 and Somos-5 recurrences, can be realized by mutations.
So their terms are Laurent polynomials in the initial values, which explains the integrality of the [[Somos sequences|27K5X7S4XN]] for $k = 4, 5$.
A stronger statement, that the coefficients of these Laurent polynomials are nonnegative, was conjectured by Fomin and Zelevinsky and later proved for skew-symmetric matrices $B$.
