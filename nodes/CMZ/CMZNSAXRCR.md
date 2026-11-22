---
tag: CMZNSAXRCR
kind: proof
name: Proof that skew-symmetric matrices of odd size are singular
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug2
proves: 55RX9C0ZTH
methods: [0NTF6DMVAP]
uses: [0ZZQ2E1MTE, 01EXSMK864, 0K26YKNBSA, 0Q9EZS90GY, 03Q7RE2HXR]
sources:
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
---

## Proof

For part 1 we compare $\det A$ with $\det(-A)$, and for part 2 we reduce to part 1 with the matrix of indeterminates.

*Part 1.*

1. Let $A^{\mathsf{T}} = -A$.
   By the [[rule for the transpose|0ZZQ2E1MTE]], $\det A = \det A^{\mathsf{T}} = \det(-A)$.
2. By the [[rule for a scalar multiple|01EXSMK864]], $\det(-A) = (-1)^n \det A$.
   Since $n$ is odd, this is $-\det A$.
3. Steps 1 and 2 give $\det A = -\det A$, so $2 \det A = 0$.
4. Since $2$ is not a [[zero divisor|0K26YKNBSA]] in $K$, we conclude $\det A = 0$.
   This proves part 1.

*Part 2.*

5. Let $R = \mathbb{Z}[x_{ij} : 1 \le i < j \le n]$ be the [[polynomial ring|0Q9EZS90GY]] in one variable for each pair $i < j$.
6. Let $X$ be the $n \times n$ matrix over $R$ with entries $x_{ij}$ for $i < j$, $-x_{ji}$ for $i > j$, and $0$ on the diagonal.
   Then $X^{\mathsf{T}} = -X$.
7. The element $2$ is not a zero divisor in $R$.
   If $2g = 0$ for a polynomial $g$, then $2c = 0$ in $\mathbb{Z}$ for each coefficient $c$ of $g$, so $c = 0$ and $g = 0$.
8. By part 1 applied over $R$, $\det X = 0$.
9. Now let $A$ be an alternating matrix over $K$.
   Let $\varphi \colon R \to K$ be the ring homomorphism with $\varphi(x_{ij}) = a_{ij}$ for $i < j$.
10. Applying $\varphi$ to each entry of $X$ gives $A$, because $a_{ji} = -a_{ij}$ for $i > j$ and $a_{ii} = 0$.
11. The determinant is a polynomial in the entries with integer coefficients, so it commutes with $\varphi$, by the [[naturality of the determinant|03Q7RE2HXR]].
    Hence $\det A = \varphi(\det X) = \varphi(0) = 0$, which proves part 2.

## Idea

Transposing a matrix keeps its determinant, and negating a matrix of odd size negates its determinant.
A skew-symmetric matrix of odd size does both at once, so its determinant equals its own negative, and $2 \det A = 0$.
That is enough when $2$ can be cancelled.
For alternating matrices we pass to the matrix of indeterminates over $\mathbb{Z}[x_{ij}]$, where $2$ can be cancelled, and every other alternating matrix is a specialization of it.

## Variants

A direct proof of part 2 pairs the terms of the Leibniz formula.
The term of $\sigma^{-1}$ is $\prod_i a_{\sigma(i) i} = \prod_i (-a_{i \sigma(i)}) = (-1)^n \prod_i a_{i \sigma(i)}$, and $\sigma^{-1}$ has the same sign as $\sigma$.
Since $n$ is odd, the terms of $\sigma$ and $\sigma^{-1}$ cancel whenever $\sigma \ne \sigma^{-1}$.
If $\sigma = \sigma^{-1}$, then $\sigma$ is a product of disjoint transpositions, and in odd size it has a fixed point $i$, so its term contains $a_{ii} = 0$.
So all terms cancel or vanish, over every commutative ring.

Over a field, part 2 also follows from the normal form of an alternating form: its rank is even, so in odd size it is less than $n$.
Over $\mathbb{F}_2$, the $1 \times 1$ matrix $(1)$ shows that part 1 fails without its hypothesis on $2$.
