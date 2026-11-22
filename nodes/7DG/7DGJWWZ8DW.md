---
tag: 7DGJWWZ8DW
kind: example
name: Invariant subspaces of the derivative on cubic polynomials
msc: ["15A04"]
topics: [Z6S6PWMJPH]
audience: ug1
instance_of: [0ACX5QT8TE, 0KN7EPH7Z0, 01H6QKWGDH, 063D5Z2C70]
illustrates: [ENVF51H5S3]
uses: [0EP59ESQ94, 0PFPWKBDTJ, 0SAAHC36J9, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Example

Let $V$ be the space of real polynomials of degree at most $3$, with the basis $1, x, x^2, x^3$.
Let $D \colon V \to V$ be the derivative, $D(p) = p'$.
For $k = 0, 1, 2, 3, 4$, let $U_k$ be the subspace of polynomials of degree less than $k$, so $U_0 = \{0\}$, $U_2 = \operatorname{span}(1, x)$ and $U_4 = V$.
We work mostly with $U = U_2$.

1. The subspace $U$ is [[invariant|0ACX5QT8TE]].
   Its spanning vectors go to $D(1) = 0$ and $D(x) = 1$, and both lie in $U$.
2. The [[matrix|0YQSGNYE3K]] of $D$ has the columns $D(1) = 0$, $D(x) = 1$, $D(x^2) = 2x$ and $D(x^3) = 3x^2$:
$$[D] = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
   The lower left $2 \times 2$ block is zero, which is step 1 in matrix form.
3. The [[restriction|0KN7EPH7Z0]] $D|_U$ sends $a + bx$ to $b$.
   Its matrix in the basis $1, x$ is the upper left block $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
4. The quotient $V / U$ has the basis $x^2 + U, x^3 + U$.
   The quotient operator sends $x^2 + U$ to $2x + U$, which is the zero coset because $2x \in U$.
   It sends $x^3 + U$ to $3x^2 + U = 3(x^2 + U)$, so its matrix is the lower right block $\begin{pmatrix} 0 & 3 \\ 0 & 0 \end{pmatrix}$.
5. The characteristic polynomials are $t^2$ for $D|_U$, $t^2$ for the quotient operator and $t^4$ for $D$.
   So $p_D = t^2 \cdot t^2$, as the [[block triangular form|ENVF51H5S3]] says.
6. The map $D$ is [[nilpotent|063D5Z2C70]]: four derivatives of a polynomial of degree at most $3$ give $0$, so $D^4 = 0$.
7. The polynomial $x^2$ is a [[generalized eigenvector|01H6QKWGDH]] for the eigenvalue $0$ of rank $3$.
   Indeed, $D(x^2) = 2x$, $D^2(x^2) = 2$ and $D^3(x^2) = 0$, while $D^2(x^2) \ne 0$.
8. Every $U_k$ is invariant, since $D$ lowers the degree.
   Conversely, let $W$ be any invariant subspace, of dimension $k$.
   The restriction $D|_W$ is nilpotent on a space of dimension $k$, so $D^k$ kills $W$, and $W \subseteq \ker D^k = U_k$.
   Both have dimension $k$, so $W = U_k$.

## Remarks

Step 8 shows that the five subspaces $U_0 \subset U_1 \subset U_2 \subset U_3 \subset U_4$ are the only invariant subspaces of $D$.
They form a flag, and $D(U_k) \subseteq U_{k-1}$, which is why $[D]$ is strictly upper triangular.
Step 8 used the fact that a nilpotent map on a space of dimension $k$ satisfies $D^k = 0$, from the [[characterizations of nilpotent endomorphisms|FSKECQK1GW]].

If $V$ is replaced by the space of all real polynomials, each $U_k$ is still invariant, but $D$ is no longer nilpotent, since no power of $D$ kills every polynomial.
If $D$ is replaced by $D + I$, the invariant subspaces do not change, because a subspace is invariant under $D + I$ exactly when it is invariant under $D$.

## Explanations

### L1 human

Taking the derivative of a polynomial lowers its degree by one.
So the derivative never takes a polynomial of small degree to one of larger degree.
For example, the derivative of $5 + 7x$ is $7$, which again has degree at most $1$.
This means that the polynomials of degree at most $1$ form a part of the space that the derivative never leaves.

### L2 human

The same computation works for the other subspaces of the flag.
Take $U_3$, the polynomials of degree at most $2$.
Its spanning vectors go to $D(1) = 0$, $D(x) = 1$ and $D(x^2) = 2x$, all in $U_3$, so $U_3$ is invariant.
The quotient $V / U_3$ is spanned by $x^3 + U_3$, and
$$D(x^3) + U_3 = 3x^2 + U_3 = 0 + U_3,$$
so the quotient operator is $0$.
The restriction has characteristic polynomial $t^3$ and the quotient has $t$, and their product is $t^4 = p_D$.
Watch out: the image $3x^2$ is not zero in $V$, but it is zero in $V / U_3$, because it lies in $U_3$.
