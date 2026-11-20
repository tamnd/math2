---
tag: 0RBQS1JJCR
kind: concept
name: Quadratic form
msc: [15A63, "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
uses: [0SQZMXB6GP, 2C3PAQ7H50, 0VR671PHE5]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Associated symmetric matrix
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: History
  - book: isbn:9780387728285
  - book: isbn:9780134860244
same_as:
  wikidata: Q736753
  wikipedia: Quadratic form
---

## Summary

Let $F$ be a field, and let $V$ be a vector space of finite dimension $n$ over $F$.
A *quadratic form* on $V$ is a map $Q \colon V \to F$ with two properties, as in [[the definition|0HZNE5QZDJ]].
First, $Q(av) = a^2 Q(v)$ for all $a \in F$ and $v \in V$.
Second, the map $(u, v) \mapsto Q(u + v) - Q(u) - Q(v)$ is a [[bilinear form|0SQZMXB6GP]] on $V$.
On $F^n$ the quadratic forms are exactly the [[homogeneous polynomials|2C3PAQ7H50]] of degree $2$, $Q(x) = \sum_{i \le j} c_{ij} x_i x_j$.
When the characteristic of $F$ is not $2$, each of them is $Q(x) = x^T A x$ for exactly one [[symmetric matrix|0VR671PHE5]] $A$.
Quadratic forms are the simplest functions after the linear ones, and they describe squared lengths, energies, conics and the second derivative of a function.

## Motivation

Many quantities in mathematics are of degree two in the coordinates.
The squared length $x_1^2 + x_2^2 + x_3^2$ of a vector, the kinetic energy $\frac12 m v^2$ and the left side of the ellipse equation $x^2 / 4 + y^2 = 1$ are examples.
Near a critical point, a smooth function of several variables looks like a quadratic form, by Taylor's formula.
In each case we ask the same questions.
Can a change of coordinates remove the cross terms $x_i x_j$?
Which signs and which coefficients remain after such a change?
The theory of quadratic forms answers these questions, and the answer depends on the field $F$.

## Notation

- We write $Q$ or $q$ for a quadratic form, and $b_Q(u, v) = Q(u + v) - Q(u) - Q(v)$ for its [[polar form|0HYFWKKY3C]].
- Outside characteristic $2$, the [[associated symmetric bilinear form|0KRVRV5V80]] is $B = \frac12 b_Q$, and $B(v, v) = Q(v)$.
- The *matrix* of $Q$ in a basis $(e_i)$ is the matrix $A = (B(e_i, e_j))$ of $B$. Then $Q(x) = x^T A x$ for the coordinate vector $x$.
- A warning: the off-diagonal entries of $A$ are half of the coefficients of the cross terms. So [[the matrix of $x^2 + xy$|V5AKNSKQNG]] has the entries $\frac12$ off the diagonal.
- Some books in number theory write $ax^2 + bxy + cy^2$ as $[a, b, c]$ and use the matrix $\begin{pmatrix} 2a & b \\ b & 2c \end{pmatrix}$ of the polar form instead.
- For a diagonal form $a_1 x_1^2 + \cdots + a_n x_n^2$, many books write $\langle a_1, \dots, a_n \rangle$.
- Two forms $Q$ on $V$ and $Q'$ on $V'$ are *equivalent* (or *isometric*) when $Q' = Q \circ T$ for a linear bijection $T \colon V' \to V$. In matrices, $A' = P^T A P$ with $P$ invertible: the matrices are [[congruent|WJWNYSQKK8]].

## Remarks

### Examples

- The squared length $x_1^2 + \cdots + x_n^2$ on $\R^n$ is a quadratic form with matrix $I_n$. It is the main example of a [[positive definite form|0RP20HFYM3]].
- [[The form $x^2 + xy$ on $\R^2$|V5AKNSKQNG]] is a quadratic form whose symmetric matrix has non-integer entries.
- [[The determinant of a $2 \times 2$ matrix|BQQZX1QS4S]] is a quadratic form on the $4$-dimensional space of $2 \times 2$ matrices.
- The Minkowski form $x^2 + y^2 + z^2 - t^2$ on $\R^4$ is a quadratic form that takes positive, negative and zero values.
- On the space of $n \times n$ matrices, $Q(X) = \operatorname{tr}(X^2)$ is a quadratic form. Indeed $Q(aX) = a^2 Q(X)$, and $Q(X + Y) - Q(X) - Q(Y) = 2 \operatorname{tr}(XY)$ is bilinear.
- Over the field $\F_2$ with two elements, $Q(x, y) = xy$ is a quadratic form, but [[it does not come from a symmetric bilinear form|ZEGSCCVGZF]].

### Non-examples

- $Q(x, y) = x^2 + y$ on $\R^2$ is not homogeneous. The condition $Q(av) = a^2 Q(v)$ fails: $Q(0, 2) = 2$, but $2^2 Q(0, 1) = 4$.
- $Q(x) = x^3$ on $\R$ fails the same condition: $Q(2) = 8 \ne 4 = 2^2 Q(1)$.
- [[The function $x^4 / (x^2 + y^2)$|AN5RQ78DD8]] satisfies $Q(av) = a^2 Q(v)$, but its polar form is not bilinear. So the second condition is needed.

### Basic properties

- $Q(0) = 0$ and $Q(-v) = Q(v)$. Take $a = 0$ and $a = -1$ in the first condition.
- The polar form is symmetric, and $b_Q(v, v) = Q(2v) - 2Q(v) = 2Q(v)$.
- Let $(e_1, \dots, e_n)$ be a basis. Applying $Q(u + v) = Q(u) + Q(v) + b_Q(u, v)$ to $u = x_1 e_1$ and the rest of the sum, and repeating, gives
$$Q\Bigl(\sum_i x_i e_i\Bigr) = \sum_i Q(e_i) x_i^2 + \sum_{i < j} b_Q(e_i, e_j)\, x_i x_j.$$
So every quadratic form is a homogeneous polynomial of degree $2$ in the coordinates.
- Conversely, $\sum_{i \le j} c_{ij} x_i x_j$ is a quadratic form: each monomial $x_i x_j$ has $Q(ax) = a^2 Q(x)$, and its polar form $x_i y_j + y_i x_j$ is bilinear.
- Outside characteristic $2$, quadratic forms and [[symmetric bilinear forms|0AXZNE5XNH]] [[correspond one to one|VN9AG8JKYT]]. In characteristic $2$ this fails.
- Under a change of basis with matrix $P$, the matrix $A$ of $Q$ becomes $P^T A P$, by [[the change of basis rule for bilinear forms|0SPYAGE7T0]].
- If $T \colon W \to V$ is linear, then $Q \circ T$ is a quadratic form on $W$. In particular, the restriction of $Q$ to a subspace is a quadratic form.
- Outside characteristic $2$, each quadratic form has [[a diagonal form|0Z3FEWZ8HA]] $a_1 x_1^2 + \cdots + a_n x_n^2$ in a suitable basis.

### History

The Wikipedia article on quadratic forms traces their study to questions about integers, such as Fermat's theorem on sums of two squares.
According to the same article, Gauss published the Disquisitiones Arithmeticae in 1801.
A large part of it is a theory of binary quadratic forms over the integers.
Forms over the integers and over number fields belong to number theory, in the topic on [[quadratic forms over local and global fields|NQC5CJZY4J]].

### Common errors

- Students put the full coefficient of $x_i x_j$ in both entries $a_{ij}$ and $a_{ji}$. The correct symmetric matrix has $a_{ij} = a_{ji} = \frac12 c_{ij}$.
- Students think that every function with $Q(av) = a^2 Q(v)$ is a quadratic form. [[The non-example above|AN5RQ78DD8]] shows that the bilinearity condition is also needed.
- Students carry the formula $B(u, v) = \frac12 (Q(u + v) - Q(u) - Q(v))$ to characteristic $2$, where $\frac12$ does not exist.

## Explanations

### L1 human

A quadratic form is a sum of terms that each have degree two, such as $3x^2 - 4xy + y^2$.
There are no constant terms and no terms of degree one.
If we double every variable, the value is multiplied by four.
For example, $3x^2 - 4xy + y^2$ is $3 - 4 + 1 = 0$ at $(1, 1)$, and it is also $12 - 16 + 4 = 0$ at $(2, 2)$.
At $(1, 0)$ the value is $3$, and at $(2, 0)$ it is $12 = 4 \cdot 3$.

### L2 human

Worked example: we find the symmetric matrix of $Q(x, y, z) = 2x^2 - 6xy + 4yz + z^2$.

1. The coefficients of the squares go on the diagonal: $a_{11} = 2$, $a_{22} = 0$ and $a_{33} = 1$.
2. The coefficient $-6$ of $xy$ is split into two halves: $a_{12} = a_{21} = -3$.
3. There is no $xz$ term, so $a_{13} = a_{31} = 0$. The coefficient $4$ of $yz$ gives $a_{23} = a_{32} = 2$.
4. So
$$A = \begin{pmatrix} 2 & -3 & 0 \\ -3 & 0 & 2 \\ 0 & 2 & 1 \end{pmatrix}.$$
5. Check: $x^T A x = 2x^2 + 2(-3)xy + 2(2)yz + z^2$, which is $Q$.

The typical use of the matrix is a change of variables $x = Py$, after which the matrix is $P^T A P$.
A trap: the matrix with $-6$ in position $(1, 2)$ and $0$ in position $(2, 1)$ also gives $Q$.
But it is not symmetric, and the theorems on symmetric matrices do not apply to it.

### L3 human

A quadratic form is a quadratic map in the sense of Mathlib's `QuadraticMap`, specialized to a vector space and its field of scalars.
The definition with the polar form works over any commutative ring, also in characteristic $2$, where quadratic forms carry more information than symmetric bilinear forms.
The pair $(V, Q)$ is a *quadratic space*.
Under the orthogonal sum, the classes of nondegenerate quadratic spaces form a monoid, and the [[Witt group|KFVY0RPGF2]] is built from this monoid.
The rest of this topic classifies quadratic forms over $\C$, over $\R$ and over finite fields, and uses the real case for conics and quadrics.
Over $\Q$ and over number fields the classification needs local invariants and the [[Hasse-Minkowski theorem|R8HCWA981S]], which belong to number theory.
