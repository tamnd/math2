---
tag: JEBXXWHW8M
kind: statement
role: theorem
name: Morita equivalence of a ring with its matrix rings
msc: [16D90, 16S50]
uses: [RD5WKA1VK7, 0FHVPRAE60, 0B1261B5ED, 0NZ8JA25WK, ZQ9ABBKF1N]
about: [RD5WKA1VK7, 0FHVPRAE60]
sources:
  - url: https://en.wikipedia.org/wiki/Morita_equivalence
---

## Statement

Let $R$ be a [[ring|0B1261B5ED]] with identity, let $n \ge 1$ be an integer, and let $M_n(R)$ be the [[ring of $n \times n$ matrices|0FHVPRAE60]] over $R$.
Then $R$ and $M_n(R)$ are [[Morita equivalent|RD5WKA1VK7]].
An equivalence from left $R$-[[modules|0NZ8JA25WK]] to left $M_n(R)$-modules sends $N$ to the module $N^n$ of columns of length $n$ over $N$.
On $N^n$ matrices act by matrix multiplication.

## Remarks

A quasi-inverse functor sends a left $M_n(R)$-module $L$ to $e_{11} L$, where $e_{11}$ is the matrix with $1$ in position $(1, 1)$ and $0$ elsewhere.
It is a left $R$-module through the scalar matrices.
The matrix units $e_{ij}$ give mutually inverse isomorphisms between $e_{11} L$ and $e_{jj} L$, and $L = e_{11} L \oplus \cdots \oplus e_{nn} L$, which shows that the two functors are inverse up to natural isomorphism.
In the language of [[progenerators|ZQ9ABBKF1N]], $P = R^n$ is a progenerator of right $R$-modules and its endomorphism ring is $M_n(R)$.
Example: a module over $M_2(\Z)$ is the same as a pair of copies of one abelian group $N$, glued by the matrix units, and the module is $N^2$.
So the ideal theory, the Artinian and Noetherian conditions and the homological dimensions of $M_n(R)$ match those of $R$.
Being commutative is not shared: $M_2(R)$ is not commutative for $R \ne 0$.

## Explanations

### L1 human

The ring of $n \times n$ matrices over $R$ looks much bigger than $R$, but its modules carry no new information.
Each module over the matrix ring is just $n$ stacked copies of a module over $R$.
So anything about modules over $R$ can be read off from modules over the matrix ring, and back.

### L2 human

This is the first example of Morita equivalence and the model for the general theory.
For a division ring $D$, it shows that $M_n(D)$, like $D$, has exactly one simple module up to isomorphism, namely $D^n$.
Morita's theorem says that every ring Morita equivalent to $R$ is of the form $e M_n(R) e$ for some $n$ and some idempotent $e$ with $M_n(R) e M_n(R) = M_n(R)$.
So matrix rings and full corners of them give all rings with the same module category as $R$.
