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

A real [[quadratic form|0RBQS1JJCR]] can be diagonalized in many ways, and its coefficients change each time, but the counts of positive, negative and zero coefficients do not.
These three counts form the signature $(p, q, r)$, with $p + q + r = n$ for a form on a real space of finite dimension $n$; see [[the definition|0KQZYGEJTF]].
For example, $x^2 + 2xy = (x + y)^2 - y^2$ has signature $(1, 1, 0)$ on $\mathbb{R}^2$.
[[Sylvester's law of inertia|0WFED3K3DQ]] shows that the triple does not depend on the diagonal form, and that two real forms are equivalent exactly when their triples are equal.
The rank of $Q$ is $p + q$.
Some books call the single number $p - q$ the signature, and for a known $n$ the rank and $p - q$ together give back $(p, q, r)$.

## Motivation

[[Diagonalization|0Z3FEWZ8HA]] writes a form as $\sum_i a_i x_i^2$ in many ways, and the coefficients $a_i$ change from one way to another.
Over $\mathbb{R}$ the signs of the $a_i$ do not change, and the signature collects them.
So the signature answers the question of when two real quadratic forms are the same after a change of variables.

It also tells you the shape of the level sets.
In $\mathbb{R}^3$, the surface $Q = 1$ is an ellipsoid for signature $(3, 0, 0)$, a hyperboloid of one sheet for $(2, 1, 0)$ and a hyperboloid of two sheets for $(1, 2, 0)$.
In relativity, spacetime carries a form of signature $(3, 1, 0)$ or $(1, 3, 0)$, depending on the sign convention.

## Notation

The triple $(p, q, r)$ is also written $(n_+, n_-, n_0)$, and some sources put the zero count first.
For nondegenerate forms, where $r = 0$, the pair $(p, q)$ is common, as in the space $\mathbb{R}^{p, q}$ and the group $O(p, q)$.
The number $\operatorname{sgn} Q = p - q$ is the signature in many books and in the theory of the Witt group.
In physics a sign pattern such as $(+, -, -, -)$ or $(-, +, +, +)$ is usual.

Watch out: "signature" means the triple, the pair $(p, q)$ or the number $p - q$, depending on the book.
The form $x^2 - y^2 - z^2$ has $(p, q) = (1, 2)$ and $p - q = -1$.
Read the definition in each source before you use its formulas.

## Remarks

### Examples

The form $x^2 + y^2 + z^2$ on $\mathbb{R}^3$ has signature $(3, 0, 0)$.
The form $x^2 + 2xy + 2xz + 4yz$ has signature $(1, 1, 1)$, and [[we compute it in two ways|Z9HTG1ESVD]].
[[The form of the completing squares example|Z762YHP338]], $x^2 + 4xy + 2xz + 5y^2 + 8yz + 2z^2$, has signature $(2, 1, 0)$.
[[The determinant on $2 \times 2$ matrices|BQQZX1QS4S]] is a quadratic form on a space of dimension $4$ with signature $(2, 2, 0)$.
[[The Minkowski form|84NG83XQJ7]] $x^2 + y^2 + z^2 - t^2$ on $\mathbb{R}^4$ has signature $(3, 1, 0)$.

The zero count depends on the space.
The form $x^2$ has signature $(1, 0, 0)$ on $\mathbb{R}$, but $(1, 0, 1)$ as a form on $\mathbb{R}^2$, where it does not involve $y$.

### Non-examples

The signs of the diagonal entries of a matrix that is not diagonal do not give the signature.
[[The form $x^2 + 4xy + y^2$|WE1ZY9FZJG]] has diagonal entries $1$ and $1$, but signature $(1, 1, 0)$.

Over $\mathbb{C}$ there is no signature, because $x^2$ and $-x^2$ are equivalent through $x \mapsto ix$.
Only the rank is an invariant there, by [[the complex classification|0CEX9BRXRZ]].

### Basic properties

The rank $p + q$ is the rank of the symmetric matrix $A$ of $Q$, and $r$ is the dimension of the radical $\{ v : B(v, w) = 0 \text{ for all } w \}$ of the associated bilinear form $B$.
The number $p$ is the largest dimension of a subspace on which $Q$ is [[positive definite|0RP20HFYM3]], and $q$ is the largest dimension of a subspace on which $Q$ is negative definite.
By [[the principal axis theorem|0PR5P9Z4KM]], $p$, $q$ and $r$ are the numbers of positive, negative and zero eigenvalues of $A$, counted with multiplicity.

The signature behaves well under the basic operations.
The form $-Q$ has signature $(q, p, r)$.
For an orthogonal sum $Q_1 \perp Q_2$, the triples add, because diagonal forms of $Q_1$ and $Q_2$ together give a diagonal form of the sum.
The form $Q$ is positive definite exactly when its signature is $(n, 0, 0)$, and positive semidefinite exactly when $q = 0$.
For each $n$, the real forms in $n$ variables fall into $(n + 1)(n + 2)/2$ classes, one for each triple.

### Common errors

A frequent error is to count eigenvalues of a matrix that is not symmetric.
For the form $x_1 x_2$, the matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ gives the right values, but it has only the eigenvalue $0$.
The symmetric matrix $\begin{pmatrix} 0 & 1/2 \\ 1/2 & 0 \end{pmatrix}$ has eigenvalues $\tfrac{1}{2}$ and $-\tfrac{1}{2}$, and the signature is $(1, 1, 0)$.
Check: $x_1 x_2 = \bigl(\tfrac{x_1 + x_2}{2}\bigr)^2 - \bigl(\tfrac{x_1 - x_2}{2}\bigr)^2$.

## Explanations

### L1 human

Write a real quadratic form as a sum of squares with plus and minus signs.
The signature counts the plus signs, the minus signs and the missing squares.
For example, $x^2 + 2xy = (x + y)^2 - y^2$ has one plus and one minus, so in two variables its signature is $(1, 1, 0)$.
Every correct way of writing it gives the same counts.

### L2 human

There are three ways to compute a signature.

1. Complete squares, and count the signs of the coefficients.
2. Find the eigenvalues of the symmetric matrix, and count their signs.
3. Use symmetric row and column operations to reach a diagonal matrix, and count the signs of its diagonal entries.

For $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, completing squares gives $2(x + \tfrac{1}{2} y)^2 + \tfrac{3}{2} y^2$, and the eigenvalues are $3$ and $1$.
Both give $(2, 0, 0)$.
Watch out: method 2 needs the symmetric matrix, so the matrix of $x^2 + xy$ has the entries $\tfrac{1}{2}$ off the diagonal.

Try it: find the signature of $x^2 - 2xy$ on $\mathbb{R}^2$.
Completing the square gives $(x - y)^2 - y^2$, so it is $(1, 1, 0)$.

### L3 human

For nondegenerate forms, $p - q$ gives the signature homomorphism from the Witt group of $\mathbb{R}$ to $\mathbb{Z}$, and it is an isomorphism.
The pair $(p, q)$ is the type of the pseudo-Euclidean space $\mathbb{R}^{p, q}$, whose isometry group is [[the indefinite orthogonal group|M2900DMEW6]] $O(p, q)$.
At a nondegenerate critical point of a smooth function, the number $q$ for the Hessian is the Morse index.
Over $\mathbb{Q}$, the signature is the local invariant at the real place in [[the Hasse-Minkowski theorem|R8HCWA981S]].
