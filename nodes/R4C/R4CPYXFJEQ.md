---
tag: R4CPYXFJEQ
kind: concept
name: Inverse and powers by the Cayley-Hamilton theorem
aliases: [inverse-as-a-polynomial-in-the-matrix, reducing-powers-modulo-the-characteristic-polynomial]
msc: ["15A24", "15A09"]
topics: [6R1D6QPY3S]
audience: ug1
uses: [0F765KFC2J, 0VSSPAFM2C, 0E3MV6E6MG]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: Applications
  - url: https://en.wikipedia.org/wiki/Cayley%E2%80%93Hamilton_theorem
    locator: lead section
  - book: isbn:9780134860244
---

## Summary

Let $A$ be an $n \times n$ matrix over a field $F$ with [[characteristic polynomial|0VSSPAFM2C]] $p_A(t) = t^n + c_{n-1}t^{n-1} + \cdots + c_1 t + c_0$.
By the [[Cayley-Hamilton theorem|0F765KFC2J]], $A^n + c_{n-1}A^{n-1} + \cdots + c_1 A + c_0 I = 0$.
If $A$ is invertible, then $c_0 = (-1)^n \det A \ne 0$, and
$$A^{-1} = -\frac{1}{c_0}\left(A^{n-1} + c_{n-1}A^{n-2} + \cdots + c_1 I\right).$$
For every $k$, divide $t^k$ by $p_A$ to get $t^k = q(t)p_A(t) + r(t)$ with $\deg r < n$.
Then $A^k = r(A)$.

## Motivation

The method turns the inverse and high powers of $A$ into [[polynomials in A|0E3MV6E6MG]] of degree less than $n$.
It needs no row reduction and no eigenvectors.
It shows that $A^{-1}$ commutes with every matrix that commutes with $A$.
The same reduction gives closed formulas for $A^k$ and for functions such as $e^{tA}$ when $n$ is small.

## Notation

The remainder $r$ of $t^k$ modulo $p_A$ is written $t^k \bmod p_A$.
Any annihilating polynomial can replace $p_A$, in particular the [[minimal polynomial|03NDVCSHSB]], which gives a remainder of smaller degree.

## Remarks

### Examples

- [[The inverse of a 2 by 2 matrix from its characteristic polynomial|775NRHBDQR]]: for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, $A^{-1} = \frac{1}{2}(A - 5I)$.
- [[The inverse of a 3 by 3 matrix from its characteristic polynomial|ZD5XSYAT9W]]: $A^{-1} = \frac{1}{4}(A^2 - 5A + 8I)$.
- [[Powers of a 2 by 2 matrix by reduction|82VDZSGDRK]]: $A^5 = 779A + 290I$ for $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.
- For $n = 2$, $A^2 = (\tr A)A - (\det A)I$, and $A^{-1} = \frac{1}{\det A}\big((\tr A)I - A\big)$ when $\det A \ne 0$.

### Non-examples

- [[A singular matrix has no inverse from the Cayley-Hamilton theorem|H7CPHN6GGK]]: for $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, $c_0 = 0$, and the formula cannot be used.
- Over the integers, $A^{-1}$ need not have integer entries: the formula divides by $c_0 = \pm \det A$.

### Basic properties

- The formula for $A^{-1}$ is valid if and only if $c_0 \ne 0$, that is, if and only if $A$ is invertible.
- $A^k = r_k(A)$ with $r_k = t^k \bmod p_A$, and $r_{k+1} = (t\, r_k) \bmod p_A$. So each step costs one multiplication by $t$ and one reduction.
- If $p_A$ has $n$ distinct roots $\lambda_i$, then $r_k$ is the polynomial of degree less than $n$ with $r_k(\lambda_i) = \lambda_i^k$ for all $i$, by Lagrange interpolation.
- $A^{-1}$ lies in $F[A]$, so it commutes with every matrix that commutes with $A$.

### History

Cayley stated the Cayley-Hamilton theorem in 1858, and Frobenius gave the first general proof in 1878.
The formula for the inverse appears among the applications in the Wikipedia article on the Cayley-Hamilton theorem.

### Common errors

- Writing $c_0$ as $\det A$. In fact $c_0 = p_A(0) = \det(-A) = (-1)^n \det A$.
- Using $\det(A - tI)$ and forgetting the sign $(-1)^n$, which changes every coefficient.
- Dropping the identity: $A^2 - 5A - 2$ must be read as $A^2 - 5A - 2I$.

## Explanations

### L1 human

The Cayley-Hamilton theorem gives an equation such as $A^2 = 5A + 2I$.
Such an equation lets us replace $A^2$ by a simpler expression, again and again.
So every power of $A$ is a short combination of $I, A, \dots, A^{n-1}$.
If the constant term is not zero, the same equation also gives $A^{-1}$.

### L2 human

We find $A^{-1}$ and $A^3$ for $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$.

1. $\tr A = 3$ and $\det A = 1$, so $p_A(t) = t^2 - 3t + 1$ and $A^2 = 3A - I$.
2. Rewrite as $A(3I - A) = I$. So $A^{-1} = 3I - A = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}$.
3. Check: $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 2 - 1 & -2 + 2 \\ 1 - 1 & -1 + 2 \end{pmatrix} = I$.
4. $A^3 = A \cdot A^2 = 3A^2 - A = 3(3A - I) - A = 8A - 3I = \begin{pmatrix} 13 & 8 \\ 8 & 5 \end{pmatrix}$.
5. Check: $A^2 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}$, and $A^2 A = \begin{pmatrix} 10 + 3 & 5 + 3 \\ 6 + 2 & 3 + 2 \end{pmatrix} = \begin{pmatrix} 13 & 8 \\ 8 & 5 \end{pmatrix}$.

The typical use is to find $A^{-1}$ or $A^k$ for a small matrix by hand.
A trap: the constant term of $p_A$ is $(-1)^n \det A$, so the sign depends on $n$.

### L3 human

$F[A] \cong F[t]/(m_A)$, and $A$ is a unit of this ring exactly when $t$ is coprime to $m_A$.
The inverse is then found by the extended Euclidean algorithm for $t$ and $m_A$, which is the formula above when $m_A = p_A$.
