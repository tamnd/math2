---
tag: 7SSKBQYFW1
kind: statement
role: theorem
name: Sylvester's determinant identity
msc: ["15A15"]
topics: [DTBK11SR77]
audience: grad
uses: [00KDZRW4C0, 0BT9BYWVRY, 0310REJJY8, 0KA7A4ENVJ]
about: [00KDZRW4C0, 0BT9BYWVRY]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_determinant_identity
same_as:
  wikidata: Q65050391
  wikipedia: Sylvester's determinant identity
---

## Statement

Let $K$ be a [[commutative ring|0310REJJY8]], let $1 \le k < n$, and let $A = (a_{ij})$ be an $n \times n$ matrix over $K$.
Let $A_0$ be the $k \times k$ submatrix of $A$ formed by its first $k$ rows and its first $k$ columns.
For $k < i, j \le n$, let $b_{ij}$ be the [[minor|0BT9BYWVRY]] of $A$ with rows $1, \dots, k, i$ and columns $1, \dots, k, j$.
Let $B$ be the $(n-k) \times (n-k)$ matrix $(b_{ij})_{k < i, j \le n}$.
Then
$$\det B = (\det A_0)^{n-k-1} \det A,$$
where $\det$ is the [[determinant|0C3CFHDN6R]].

## Remarks

### A warning about the name

The name "Sylvester's determinant theorem" refers to two different identities in the literature.
Some authors use it for this identity on bordered minors.
Others use it for the [[Weinstein-Aronszajn identity|0G24VQ1088]], $\det(I_m + AB) = \det(I_n + BA)$, which is a different statement.

### Why each hypothesis is needed

The ring must be commutative, as in every use of the determinant.
The condition $k < n$ makes $B$ a matrix of size at least $1$.
No invertibility is needed: the [[proof|~c3ae09a4]] works with a generic matrix.

### Consequences

- For $k = n - 1$, the matrix $B$ is $1 \times 1$ with entry $\det A$, and the identity reads $\det A = (\det A_0)^0 \det A$.
- For $k = n - 2$, after the interior rows and columns are moved to the front, it is the [[Desnanot-Jacobi identity|~aa63b68e]].
- For $k = 1$, the entries of $B$ are the $2 \times 2$ minors $a_{11} a_{ij} - a_{i1} a_{1j}$, and $\det B = a_{11}^{n-2} \det A$.
- [[Dodgson condensation|RQ44FKS5QM]] applies the case $k = n - 2$ again and again.
- The [[Bareiss algorithm|ZDBW3AB587]] is fraction-free elimination over the integers: its intermediate entries are bordered minors, and the division by the previous pivot is exact.

### Converse

The identity holds for all $A$, so a converse in the usual sense does not apply.
When $\det A_0 = 0$ and $k < n - 1$, it gives $\det B = 0$ and no information on $\det A$.

### Generalizations

The same method with a [[Schur complement|0KA7A4ENVJ]] gives every minor of $B$ as a power of $\det A_0$ times a minor of $A$ that contains $A_0$.

## Explanations

### L1 human

Fix the top left corner block of a square matrix.
Build a smaller matrix whose entries are determinants of this corner block bordered by one more row and one more column.
The determinant of the new matrix equals the determinant of the original matrix times a power of the determinant of the corner block.

### L2 human

Take $A = \begin{pmatrix} 2 & 1 & 3 \\ 1 & 4 & 1 \\ 3 & 2 & 5 \end{pmatrix}$ and $k = 1$, so $A_0 = (2)$.

1. $b_{22} = 2 \cdot 4 - 1 \cdot 1 = 7$ and $b_{23} = 2 \cdot 1 - 3 \cdot 1 = -1$.
2. $b_{32} = 2 \cdot 2 - 1 \cdot 3 = 1$ and $b_{33} = 2 \cdot 5 - 3 \cdot 3 = 1$.
3. So $\det B = 7 \cdot 1 - (-1) \cdot 1 = 8$.
4. The identity gives $\det A = \det B / a_{11}^{1} = 8 / 2 = 4$.
5. Check by the [[rule of Sarrus|~ca424b6f]]: $40 + 3 + 6 - 36 - 4 - 5 = 4$.
The typical use is a proof that the bordered minors of an integer matrix are divisible by powers of $\det A_0$, as in fraction-free elimination.
A trap: the minors $b_{ij}$ all contain the whole block $A_0$; they are not the $2 \times 2$ minors of $A$ unless $k = 1$.

### L3 human

With $k$ fixed, the map $A \mapsto B$ is the Schur complement scaled by $\det A_0$.
The identity is the reason that the entries of fraction-free elimination stay in the ring.
