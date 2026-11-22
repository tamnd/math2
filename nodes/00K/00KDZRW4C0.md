---
tag: 00KDZRW4C0
kind: concept
name: Determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
uses: [0K6CH0MT0F, 0CP7YY6NAG, 06DW9BAWB1, 0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Definitions
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter Four, Determinants
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: History
same_as:
  wikidata: Q178546
  wikipedia: Determinant
---

## Summary

The determinant attaches one number to each square matrix.
That number tells you whether the matrix can be undone, and by what factor the matrix changes areas and volumes.
For a $2 \times 2$ matrix it is $ad - bc$, and for every size three rules fix it.
Let $K$ be a [[commutative ring|0310REJJY8]] and let $n \ge 1$.
The *determinant* is the unique function $\det \colon M_n(K) \to K$ on the $n \times n$ [[square matrices|0CP7YY6NAG]] that is linear in each column when the other columns are fixed, is zero when two columns are equal, and has the value $1$ on the [[identity matrix|06DW9BAWB1]] $I_n$.
In one phrase, it is the unique [[alternating multilinear map|0K6CH0MT0F]] of the columns with $\det I_n = 1$.
The [[formal definition|0C3CFHDN6R]] uses rows in place of columns, and the two versions give the same function.
Written out, it is the [[Leibniz formula|016PE4VZ8Q]]
$$\det A = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, a_{1 \sigma(1)} a_{2 \sigma(2)} \cdots a_{n \sigma(n)}.$$

## Motivation

A system of $n$ linear equations in $n$ unknowns has exactly one solution for every right side when one number built from the coefficients is not zero.
For two equations $ax + by = e$ and $cx + dy = f$, elimination of $y$ gives $(ad - bc)x = de - bf$, so everything depends on $ad - bc$.
The determinant is that number for every $n$.

Geometry asks for the same number in a second way.
The signed volume of the box spanned by $n$ vectors of $\mathbb{R}^n$ grows linearly when one edge grows, collapses to zero when two edges agree, and is $1$ for the unit cube.
These are exactly the three rules of the definition, so the determinant is the signed volume.
Later the determinant gives the [[characteristic polynomial|0VSSPAFM2C]] and so the eigenvalues, the [[orientation|0QJJAQ6ZYZ]] of a real space, and the volume factor in the change of variables formula of calculus.

## Notation

Books write $\det A$, $\det(A)$ or $\lvert A \rvert$, and they often replace the brackets of the matrix by vertical bars:
$$\det A = \begin{vmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & & \vdots \\ a_{n1} & \cdots & a_{nn} \end{vmatrix}.$$
The bars are not an absolute value, since a determinant can be negative.
When the columns $v_1, \dots, v_n$ are given, we also write $\det(v_1, \dots, v_n)$.
In Lean's Mathlib the function is `Matrix.det`, and it is defined by the Leibniz sum.

## Remarks

### The three rules on a 2 by 2 matrix

The three rules are enough to compute a determinant.
Write the columns of $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ as $a e_1 + c e_2$ and $b e_1 + d e_2$, where $e_1, e_2$ are the columns of $I_2$.
Linearity in each column splits the determinant into four pieces:
$$\det = ab \det(e_1, e_1) + ad \det(e_1, e_2) + cb \det(e_2, e_1) + cd \det(e_2, e_2).$$
The first and last pieces have two equal columns, so they are $0$.
The rules also give $\det(e_2, e_1) = -1$, because $0 = \det(e_1 + e_2, e_1 + e_2) = \det(e_1, e_2) + \det(e_2, e_1)$.
So the determinant is $ad - bc$, the [[2 by 2 formula|0ZN2J42SK7]].
For $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ it is $1 \cdot 4 - 2 \cdot 3 = -2$.

### Three definitions, one function

Books start from one of three definitions.
The axiomatic one uses the three rules above.
The Leibniz formula is the sum of $n!$ signed products, one entry from each row and each column.
The Laplace recursion expands along the first row, $\det A = \sum_{j} (-1)^{1+j} a_{1j} \det A_{1j}$, where $A_{1j}$ deletes row $1$ and column $j$, and it starts from $\det(a) = a$.
The [[equivalence theorem|W3JN0WPZ10]] proves that all three give the same number, and that rows and columns give the same number too.

Each definition is good for something.
The rules give structural results, the Leibniz formula gives the [[transpose rule|0ZZQ2E1MTE]], and the recursion gives proofs by induction on $n$.
For $A = \begin{pmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 1 & 1 & 2 \end{pmatrix}$, the recursion gives
$$\det A = 2(3 \cdot 2 - 2 \cdot 1) - 0 + 1(1 \cdot 1 - 3 \cdot 1) = 8 - 2 = 6.$$
The [[same matrix by three methods|7YSM0NJQX1]] gets $6$ from each definition.

### What the number means

Over $\mathbb{R}$, the matrix $\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$ stretches the unit square into a $2 \times 3$ rectangle, and its determinant is $6$.
In general $\lvert \det A \rvert$ is the [[factor by which A scales volume|RC5BTSG8T2]], and the sign says whether $A$ keeps or reverses orientation.
A [[rotation and a reflection of the plane|D3F3XAZA0M]] show both signs:
$$\det \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = \cos^2\theta + \sin^2\theta = 1, \qquad \det \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = -1.$$
A zero determinant means that the matrix squashes space into a smaller subspace.
For example, $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ has determinant $4 - 4 = 0$, and it sends the whole plane onto the line spanned by $(1, 2)$.

### The rules you can use

The determinant is [[linear in each row|0PPG793642]], and it is zero when the matrix has [[equal rows, a zero row or dependent rows|0K4VQB7HWR]].
Each [[row operation|09YB3WQG38]] changes it in a known way: a swap changes the sign, scaling a row by $c$ multiplies it by $c$, and adding a multiple of one row to another keeps it.
A [[triangular matrix|0K1KKMFHYH]] has the product of its diagonal entries as its determinant, so row reduction computes any determinant.
The [[transpose rule|0ZZQ2E1MTE]] $\det A^{\mathsf{T}} = \det A$ turns each rule about rows into a rule about columns.
The product rule $\det(AB) = \det A \det B$ is [[multiplicativity|04CPJ6AF00]], and it gives $\det(A^{-1}) = (\det A)^{-1}$, the [[determinant of the inverse|0783S9D0ZH]].
Over a field, $A$ is invertible exactly when $\det A \ne 0$, by the [[invertibility criterion|FBSAPTP1PR]].
Over a commutative ring the condition is that $\det A$ is a unit, by the [[ring version|03Q7RE2HXR]].

### What it is not

The [[permanent|X9B1XETBPF]] is the Leibniz sum without the signs.
It is multilinear and has the value $1$ on $I_n$, but for $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ it gives $1 + 1 = 2$, although the two rows are equal.
So it fails the alternating rule, as the [[permanent non-example|K9T8BNTZ2G]] shows.
The [[trace|0XC1RDBY7A]] is not the determinant either.
Over $\mathbb{R}$ with $n \ge 2$ it has $\operatorname{tr} I_n = n \ne 1$, and doubling one column of $I_2$ gives trace $3$, not $2 \cdot 2 = 4$, so it is not linear in each column.
A $2 \times 3$ matrix has no determinant at all, since the rules need $n$ columns in $K^n$.

### Watch out

The determinant is linear in each row separately, not in the whole matrix.
With $A = B = I_2$ we get
$$\det(A + B) = \det \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 4, \qquad \det A + \det B = 2,$$
so $\det(A + B) \ne \det A + \det B$ in general; the [[counterexample on sums|D5VBC7621G]] gives more.
For the same reason $\det(cA) = c^n \det A$, because each of the $n$ rows carries one factor $c$.
So $\det(2 I_3) = 8$, not $2$.
A third trap is the diagonal pattern of the [[rule of Sarrus|7H2P40X0MV]]: it works for $3 \times 3$ matrices only and gives wrong values for larger sizes.

### History

The Japanese mathematician Seki Takakazu used determinants to eliminate unknowns in 1683.
Leibniz used them for the same purpose in a letter of 1693.
Cramer published his rule for solving linear systems by determinants in 1750.
In 1812 Cauchy and Binet each proved the product rule, in the general form now called the [[Cauchy-Binet formula|08WE2W7DYS]].

### Try it

First, compute $\det \begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}$.
The answer is $3 \cdot 2 - 1 \cdot 5 = 1$, so the matrix keeps areas.

Second, a $3 \times 3$ matrix $A$ has $\det A = 5$; find $\det(2A)$.
Each of the three rows doubles, so $\det(2A) = 2^3 \cdot 5 = 40$.

Third, show that $\det \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} = 0$ without expanding.
Row $1$ plus row $3$ is $(8, 10, 12)$, which is twice row $2$, so the rows are dependent and the determinant is $0$.

## Explanations

### L1 human

Think of a $2 \times 2$ matrix as a rule that moves every point of the plane.
The unit square goes to a parallelogram, and the determinant is the area of that parallelogram, with a sign.
For rows $(3, 1)$ and $(1, 2)$ the number is $3 \cdot 2 - 1 \cdot 1 = 5$, so every shape gets $5$ times bigger.
A negative number means that the picture is also flipped, as in a mirror.
A zero means that the plane is squashed onto a line, and then the move cannot be undone.

### L2 human

Here is a typical use: for which numbers $t$ is the matrix below invertible?
$$A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & 4 & t \end{pmatrix}$$
Expand along the first row:
$$\det A = 1(2t - 12) - 1(t - 3) + 1(4 - 2) = 2t - 12 - t + 3 + 2 = t - 7.$$
So $A$ is invertible for every $t$ except $t = 7$.
Check: for $t = 7$, row $3$ minus row $2$ is $(0, 2, 4)$, and row $2$ minus row $1$ is $(0, 1, 2)$, so the rows are dependent.
One determinant answered the question for all $t$ at once, while row reduction would need a case split on $t$.
This is how determinants are used to find the eigenvalues of a matrix, as the values of $\lambda$ that make $\det(A - \lambda I)$ zero.

### L3 human

For a free module $V$ of rank $n$, the top exterior power $\Lambda^n V$ is free of rank $1$, so an endomorphism $T$ acts on it as multiplication by one scalar.
That scalar is the [[determinant of the endomorphism|0X0HQYSZ0K]], and it needs no basis.
The product rule makes $\det$ a group homomorphism $\mathrm{GL}_n(K) \to K^{\times}$ with kernel $\mathrm{SL}_n(K)$, and the Leibniz formula shows that it commutes with every ring homomorphism applied to the entries.
The same object appears as the Jacobian determinant in the change of variables formula and as the Wronskian of differential equations.
In a finite field extension $L$ of $K$, the norm $N_{L/K}(a)$ is the determinant of multiplication by $a$ on $L$.
