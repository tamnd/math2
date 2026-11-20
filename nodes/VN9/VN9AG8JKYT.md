---
tag: VN9AG8JKYT
kind: statement
role: theorem
name: Correspondence between quadratic forms and symmetric bilinear forms
msc: [15A63, "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
about: [0RBQS1JJCR, 0AXZNE5XNH, 0HYFWKKY3C]
uses: [0HZNE5QZDJ, 0744CN4MDA, 0HYFWKKY3C, 0P24YW565F]
proofs: [VQWHWZED07]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Symmetric_bilinear_form
    locator: lead section
  - book: isbn:9780387728285
---

## Statement

Let $F$ be a field whose characteristic is not $2$, and let $V$ be a finite-dimensional vector space over $F$.

1. For each [[symmetric bilinear form|0744CN4MDA]] $B$ on $V$, the map $Q_B(v) = B(v, v)$ is a [[quadratic form|0HZNE5QZDJ]], and its [[polar form|0HYFWKKY3C]] is $2B$.
2. For each quadratic form $Q$ on $V$, the map $B_Q(u, v) = \frac12 \bigl( Q(u + v) - Q(u) - Q(v) \bigr)$ is a [[symmetric bilinear form|0744CN4MDA]] with $B_Q(v, v) = Q(v)$.
3. The maps $B \mapsto Q_B$ and $Q \mapsto B_Q$ are inverse bijections between the symmetric bilinear forms and the quadratic forms on $V$.
4. Let $(e_1, \dots, e_n)$ be a basis of $V$. For each quadratic form $Q$ there is exactly one symmetric matrix $A$ with $Q(\sum_i x_i e_i) = x^T A x$ for all $x \in F^n$. It is the [[matrix|0P24YW565F]] of $B_Q$.

## Remarks

### Why each hypothesis is needed

- The characteristic must not be $2$. Over the field $\F_2$, [[the form $xy$ is not $B(v, v)$ for any symmetric bilinear form $B$|ZEGSCCVGZF]], so $B \mapsto Q_B$ is not onto.
- In the same example, $x^2$ on $\F_2$ has polar form $0$, like the zero form. So $Q \mapsto b_Q$ is not one to one.
- In part 4 the matrix must be symmetric for uniqueness. The matrices $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$ both give $x^2 + xy$.

### Consequences

- Every notion for symmetric bilinear forms passes to quadratic forms: the matrix, [[orthogonality|01TXN7ETH2]], [[nondegeneracy|01NHFZF2SK]], rank and [[congruence|WJWNYSQKK8]] of matrices.
- [[The diagonalization theorem|0Z3FEWZ8HA]] can be stated for symmetric matrices or for quadratic forms, with the same content.
- The two maps are $F$-linear. So the quadratic forms on $V$ form a vector space of dimension $n(n + 1)/2$, like the symmetric $n \times n$ matrices.

### Converse

The statement is already a bijection in both directions.
In characteristic $2$, part 1 still holds, but parts 2 to 4 fail.

### Generalizations

The same proof works for modules over a commutative ring in which $2$ is invertible.
In characteristic $2$, every quadratic form is still $x^T A x$ for an upper triangular matrix $A$.
But $A$ is not unique, and the polar form $b_Q$ is alternating.

## History

Wikipedia states the correspondence for fields of characteristic not $2$ in its article on quadratic forms.
We give no date, because we found no source for its first statement.

## Explanations

### L1 human

A symmetric bilinear form takes two vectors and gives a number.
If we put the same vector in both places, we get a quadratic form.
Outside characteristic $2$ we can go back, with the formula $\frac12 (Q(u + v) - Q(u) - Q(v))$.
For $Q(x, y) = x^2 + y^2$ the formula gives the dot product $xx' + yy'$.

### L2 human

Worked example: we pass from $B$ to $Q$ and back.

1. Let $B(u, v) = 2u_1 v_1 + 3(u_1 v_2 + u_2 v_1)$ on $\R^2$. It is bilinear and symmetric.
2. Then $Q_B(v) = B(v, v) = 2v_1^2 + 6 v_1 v_2$.
3. Back: $Q_B(u + v) - Q_B(u) - Q_B(v) = 4u_1 v_1 + 6(u_1 v_2 + u_2 v_1)$, and half of it is $B(u, v)$.

The typical use is to read a quadratic form as a symmetric matrix, here $\begin{pmatrix} 2 & 3 \\ 3 & 0 \end{pmatrix}$.
A trap: the theorem fails in characteristic $2$, which matters for codes and for forms over $\F_2$.

### L3 human

The theorem says that, when $2$ is invertible, the functor that sends a symmetric bilinear space $(V, B)$ to the quadratic space $(V, Q_B)$ is an equivalence.
In characteristic $2$ the two theories separate, and quadratic forms carry more structure; the Arf invariant then plays the role of the discriminant.
This is why many texts on algebraic groups and on coding theory work with quadratic forms and not with symmetric bilinear forms.
