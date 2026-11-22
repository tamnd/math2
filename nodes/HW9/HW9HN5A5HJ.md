---
tag: HW9HN5A5HJ
kind: statement
role: proposition
name: Equivalent conditions for finite dimension
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [0ZHWKQMVX5]
uses: [018W3V3TCT, 0VTQTPQGAV, 0EVHJFTG9Z]
proofs: [3AMPZ016SQ]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Facts
  - book: isbn:9783031410253
    locator: Section 2B
---

## Statement

Four natural ways to say that a vector space is small all mean the same thing.
Let $F$ be a field and let $V$ be a vector space over $F$.
The following four conditions are equivalent.

1. $V$ is [[finite-dimensional|018W3V3TCT]], that is, $V$ has a finite spanning set.
2. $V$ has a finite [[basis|0VTQTPQGAV]].
3. There is an integer $N \ge 0$ such that every [[linearly independent|0EVHJFTG9Z]] family in $V$ has at most $N$ vectors.
4. $V$ is isomorphic to $F^n$ for some integer $n \ge 0$.

## Remarks

### Which condition to use

Each condition is the easiest one to check in some situation.
To show that a space is finite-dimensional, condition 1 is usually best: list a finite spanning set.
For example, the polynomials $p$ of degree at most $2$ with $p(0) = 0$ are the combinations of $x$ and $x^2$, so they form a finite-dimensional space.

To show that a space is infinite-dimensional, the negation of condition 3 is usually best: find independent families of every size.
In $F[x]$, the family $1, x, \dots, x^N$ has $N + 1$ independent vectors, so no bound $N$ works, and $F[x]$ is infinite-dimensional.
The same argument works for the sequence space $F^{\mathbb{N}}$ with $e_0, e_1, \dots, e_N$, and for $C[0, 1]$ with the monomials.

Condition 4 is the one that computations use: it turns every vector of $V$ into a column of $n$ numbers.

### A weaker form of condition 3

Condition 3 asks for one number $N$ that bounds all independent families at once.
For vector spaces, the weaker condition "every independent family is finite" is also equivalent to the four conditions.
The reason is that an infinite-dimensional space contains an infinite independent sequence.
Choose $v_1 \ne 0$, and when $v_1, \dots, v_k$ are chosen, choose $v_{k + 1}$ outside their span, which is possible because finitely many vectors do not span $V$.
By the [[dependence lemma|H75GS7QVPB]], no $v_j$ is a combination of the earlier ones, so the sequence is independent.
In $F[x]$ this procedure can produce $1, x, x^2, \dots$.

### Why the field is needed

Over a ring, the conditions come apart.
The group $\mathbb{Z}/2$ is finitely generated as a module over $\mathbb{Z}$, but it has no basis, since $2 \cdot \bar 1 = 0$ is a nontrivial relation.
The rationals $\mathbb{Q}$ as a module over $\mathbb{Z}$ satisfy condition 3 with $N = 1$, since $\tfrac{a}{b}$ and $\tfrac{c}{d}$ with $a, c \ne 0$ satisfy $cb \cdot \tfrac{a}{b} - ad \cdot \tfrac{c}{d} = 0$, but $\mathbb{Q}$ is not finitely generated over $\mathbb{Z}$.
The [[proof|3AMPZ016SQ]] uses division in $F$ through the [[dependence lemma|H75GS7QVPB]] and the [[Steinitz exchange lemma|08ZDRN6H41]].

### What it gives you

The integer $n$ in condition 4 is unique and equals $\dim V$, by the [[dimension theorem|0WK0Y8RH1M]], since an isomorphism carries a basis to a basis.
The smallest possible $N$ in condition 3 is also $\dim V$.
A space is infinite-dimensional exactly when it contains independent families of every finite size.

## Explanations

### L1 human

There are several ways to say that a space is "finite".
You can say that finitely many vectors build everything, or that it has a finite basis, or that it looks exactly like lists of $n$ numbers.
You can also say that you can never find more than some fixed number of independent vectors in it.
All four say the same thing.

### L2 human

Here is a typical use, for the space $V$ of real $2 \times 2$ matrices $A$ with $A^{\mathsf{T}} = A$.
Every such matrix is $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$, so it equals
$$a \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + b \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + c \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.$$
So condition 1 holds with three matrices, and these three are independent, since the combination is $0$ only for $a = b = c = 0$.
By condition 2 they form a basis, and by condition 4 the map $A \mapsto (a, b, c)$ is an isomorphism $V \cong \mathbb{R}^3$.
By condition 3, any four symmetric $2 \times 2$ matrices are dependent.
Watch out: three independent matrices alone show only that the dimension is at least $3$; it is the spanning property that rules out a fourth independent matrix.

### L3 human

The conditions express one fact from four points of view: span (1), structure (2), size (3) and coordinates (4).
For modules over a ring they split into separate notions: finitely generated, free of finite rank, and of finite rank in the sense of condition 3.
Over a field all of them coincide, which is one reason why linear algebra over a field is so much simpler than module theory.
