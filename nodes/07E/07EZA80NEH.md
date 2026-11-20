---
tag: 07EZA80NEH
kind: concept
name: Signature of a quadratic form
msc: [15A63, "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
aliases: [inertia-of-a-quadratic-form, signature-and-inertia]
uses: [0RBQS1JJCR, 0Z3FEWZ8HA, 0WFED3K3DQ]
sources:
  - url: https://en.wikipedia.org/wiki/Metric_signature
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Real quadratic forms
  - url: https://en.wikipedia.org/wiki/Sylvester's_law_of_inertia
    locator: Statement
same_as:
  wikidata: Q1142562
  wikipedia: Metric signature
---

## Summary

The signature of a real [[quadratic form|0RBQS1JJCR]] records the numbers of positive, negative and zero coefficients in any diagonal form of it.
For $Q$ on a real space of dimension $n$, it is the triple $(p, q, r)$ with $p + q + r = n$; see [[the definition|0KQZYGEJTF]].
By [[Sylvester's law of inertia|0WFED3K3DQ]], the triple does not depend on the diagonal form.
It is a complete invariant: two real forms are equivalent exactly when their triples are equal.
The rank of $Q$ is $p + q$.
Some books call the number $p - q$ the signature; rank and $p - q$ together also determine $(p, q, r)$.

## Motivation

[[Diagonalization|0Z3FEWZ8HA]] writes a form as $\sum_i a_i x_i^2$ in many ways, and the coefficients $a_i$ change from one way to another.
Over $\R$ the signs of the $a_i$ do not change, and the signature collects them.
It answers the question of when two real quadratic forms are the same after a change of variables.
It also tells the shape of the level sets.
For example, $Q = 1$ is an ellipsoid for signature $(3, 0, 0)$ and a hyperboloid of one sheet for $(2, 1, 0)$.
In relativity, spacetime carries a form of signature $(3, 1, 0)$ or $(1, 3, 0)$, depending on the sign convention.

## Notation

- $(p, q, r)$, or $(n_+, n_-, n_0)$: the numbers of positive, negative and zero coefficients. Wikipedia uses the triple $(n_0, n_+, n_-)$ in its article on quadratic forms, with a different order.
- $(p, q)$: used for nondegenerate forms, where $r = 0$; for example $\R^{p, q}$ and the group $O(p, q)$.
- $\operatorname{sgn} Q = p - q$: used in many books, and in the theory of the Witt group.
- In physics, a sign pattern such as $(+, -, -, -)$ or $(-, +, +, +)$.

**Warning.** "Signature" means the pair $(p, q)$ in some books and the number $p - q$ in others.
Read the definition in each source before using its formulas.

## Remarks

### Examples

- $x^2 + y^2 + z^2$ on $\R^3$ has signature $(3, 0, 0)$, and $p - q = 3$.
- $x^2 + 2xy + 2xz + 4yz$ has signature $(1, 1, 1)$; [[we compute it in two ways|~6efc183f]].
- [[The form of completing squares|~eadb0c41]] $x^2 + 4xy + 2xz + 5y^2 + 8yz + 2z^2$ has signature $(2, 1, 0)$.
- [[The determinant on $2 \times 2$ matrices|~2d401abe]] has signature $(2, 2, 0)$.
- [[The Minkowski form|~3c5b95b1]] $x^2 + y^2 + z^2 - t^2$ on $\R^4$ has signature $(3, 1, 0)$, and $p - q = 2$.

### Non-examples

- [[The signs of the diagonal entries of a non-diagonal matrix|~26da1679]] do not give the signature: $x^2 + 4xy + y^2$ has positive diagonal entries but signature $(1, 1, 0)$.
- Over $\C$ there is no signature: $x^2$ and $-x^2$ are equivalent through $x \mapsto ix$. Only the rank is an invariant there, by [[the complex classification|0CEX9BRXRZ]].

### Basic properties

- $p + q$ is the rank of the symmetric matrix of $Q$, and $r$ is the dimension of the radical $\set{v : B(v, w) = 0 \text{ for all } w}$.
- $p$ is the largest dimension of a subspace on which $Q$ is positive definite, and $q$ is the same for negative definite.
- By [[the principal axis theorem|0PR5P9Z4KM]], $p$, $q$ and $r$ are the numbers of positive, negative and zero eigenvalues of the symmetric matrix, with multiplicity.
- The form $-Q$ has signature $(q, p, r)$.
- For an orthogonal sum $Q_1 \perp Q_2$, the triples add.
- $Q$ is [[positive definite|0RP20HFYM3]] exactly when its signature is $(n, 0, 0)$, and positive semidefinite exactly when $q = 0$.
- Classification: for each $n$, the real forms in $n$ variables fall into $(n + 1)(n + 2)/2$ classes, one for each triple.

### History

According to Wikipedia, the law of inertia, which makes the signature well defined, is named after Sylvester, who published its proof in 1852.

### Common errors

- Mixing the conventions $(p, q)$ and $p - q$. The form $x^2 - y^2 - z^2$ has $(p, q) = (1, 2)$ and $p - q = -1$.
- Reading the signs from the diagonal of a non-diagonal matrix.
- Counting eigenvalues of a matrix that is not symmetric. For $x_1 x_2$, the matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has only the eigenvalue $0$, but the signature is $(1, 1, 0)$.
- Forgetting the zero count $r$. The form $x^2$ has signature $(1, 0, 0)$ on $\R$, but $(1, 0, 1)$ as a form on $\R^2$.

## Explanations

### L1 human

Write a real quadratic form as a sum of squares with plus and minus signs.
The signature counts the plus signs, the minus signs and the missing squares.
For example, $x^2 + 2xy = (x + y)^2 - y^2$ has one plus and one minus, so in two variables its signature is $(1, 1, 0)$.
Every way of writing it gives the same counts.

### L2 human

To compute a signature, use one of three methods.

1. Complete squares, and count the signs of the coefficients.
2. Find the eigenvalues of the symmetric matrix, and count their signs.
3. Use symmetric row and column reduction to reach a diagonal matrix.

For $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, completing squares gives $2(x + \frac y2)^2 + \frac32 y^2$, and the eigenvalues are $3$ and $1$; both give $(2, 0, 0)$.
A trap: method 2 needs the symmetric matrix; the matrix of $x^2 + xy$ has entries $\frac12$.

### L3 human

For nondegenerate forms, $p - q$ is the signature homomorphism from the Witt group of $\R$ to $\Z$, and it is an isomorphism.
The pair $(p, q)$ is the type of the pseudo-Euclidean space $\R^{p, q}$, whose isometry group is [[the indefinite orthogonal group|M2900DMEW6]] $O(p, q)$.
For nondegenerate critical points of a smooth function, $q$ for the Hessian is the Morse index.
Over $\Q$, the signature is one of the local invariants in [[the Hasse-Minkowski theorem|R8HCWA981S]], the one at the real place.
