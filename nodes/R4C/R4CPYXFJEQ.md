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

The Cayley-Hamilton theorem gives every square matrix a polynomial equation, and that one equation lets you invert the matrix and compute its high powers using only $I, A, \dots, A^{n-1}$.
Let $A$ be an $n \times n$ matrix over a field $F$ with [[characteristic polynomial|0VSSPAFM2C]] $p_A(t) = t^n + c_{n-1} t^{n-1} + \cdots + c_1 t + c_0$.
By the [[Cayley-Hamilton theorem|0F765KFC2J]],
$$A^n + c_{n-1} A^{n-1} + \cdots + c_1 A + c_0 I = 0.$$
If $A$ is invertible, then $c_0 = (-1)^n \det A \ne 0$, and moving $c_0 I$ to the other side gives
$$A^{-1} = -\frac{1}{c_0} \left( A^{n-1} + c_{n-1} A^{n-2} + \cdots + c_1 I \right).$$
For powers, divide $t^k$ by $p_A$ with remainder, $t^k = q(t) p_A(t) + r(t)$ with $\deg r < n$, and then $A^k = r(A)$.

## Motivation

Row reduction finds an inverse, and repeated multiplication finds a power, but both hide the structure of the answer.
The Cayley-Hamilton theorem shows that the inverse and every power are [[polynomials in A|0E3MV6E6MG]] of degree less than $n$.
So a whole infinite list of matrices $A^2, A^3, \dots$ lives in a space of dimension at most $n$, and you only need to track $n$ coefficients.

This has practical uses.
A closed formula for $A^k$ solves a linear recurrence, such as the one for the Fibonacci numbers, and the same reduction gives $e^{sA}$ for small $n$ in the study of linear differential equations.
It also shows that $A^{-1}$ commutes with every matrix that commutes with $A$, since $A^{-1}$ is a polynomial in $A$.

## Notation

The remainder of $t^k$ on division by $p_A$ is written $t^k \bmod p_A$, and we write $t^k \equiv r(t)$ when $t^k - r(t)$ is a multiple of $p_A$.
Any polynomial that kills $A$ can replace $p_A$, in particular the [[minimal polynomial|03NDVCSHSB]], which can give a shorter formula.
Watch the constant term: some books define the characteristic polynomial as $\det(A - tI)$, which multiplies every coefficient by $(-1)^n$.

## Remarks

### A first inverse

Take $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$, with trace $5$ and determinant $-2$, so $p_A(t) = t^2 - 5t - 2$.
The theorem gives $A^2 - 5A - 2I = 0$, which we rewrite as
$$A (A - 5I) = 2I, \qquad \text{so} \qquad A^{-1} = \tfrac{1}{2}(A - 5I) = \begin{pmatrix} -2 & 1 \\ \tfrac{3}{2} & -\tfrac{1}{2} \end{pmatrix}.$$
The [[2 by 2 inverse example|775NRHBDQR]] checks this product.
For every $2 \times 2$ matrix the same steps give $A^{-1} = \frac{1}{\det A} \left( (\operatorname{tr} A) I - A \right)$, which is the adjugate formula in disguise.
For size $3$ the formula needs $A^2$, as in the [[3 by 3 inverse example|ZD5XSYAT9W]], where $A^{-1} = \tfrac{1}{4}(A^2 - 5A + 8I)$.

### Reducing powers

To find $A^5$ for the same matrix, reduce powers of $t$ with the rule $t^2 \equiv 5t + 2$:
$$t^3 \equiv 5t^2 + 2t \equiv 27t + 10, \qquad t^4 \equiv 27t^2 + 10t \equiv 145t + 54, \qquad t^5 \equiv 145t^2 + 54t \equiv 779t + 290.$$
So $A^5 = 779A + 290I$, and the [[powers example|82VDZSGDRK]] confirms this by direct multiplication.
Each step multiplies the remainder by $t$ and replaces $t^2$ once, so only two numbers change at each step.

When $p_A$ has $n$ distinct roots $\lambda_1, \dots, \lambda_n$ in $F$, there is a shortcut.
The remainder $r$ agrees with $t^k$ at each root, because $p_A(\lambda_i) = 0$, so $r$ is the polynomial of degree less than $n$ with $r(\lambda_i) = \lambda_i^k$.
For $B = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ with roots $1$ and $3$, this gives $B^k = \frac{3^k - 1}{2} B + \frac{3 - 3^k}{2} I$.

### When the method fails

The inverse formula divides by $c_0$, so it fails exactly when $c_0 = 0$, that is, when $A$ is singular.
For $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ the polynomial is $t^2 - 5t$, and the [[singular example|H7CPHN6GGK]] shows that the equation $A^2 = 5A$ has no multiple of $I$ to isolate.
The reduction of powers still works there: $A^k = 5^{k-1} A$ for $k \ge 1$.

Over the integers the formula can leave the integers, because it divides by $c_0 = \pm \det A$.
For $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ it gives the inverse $\operatorname{diag}(\tfrac{1}{2}, 1)$, and the inverse has integer entries only when $\det A = \pm 1$.

### A shorter polynomial can help

The minimal polynomial gives the same results with less work when it has lower degree.
For $A = 2 I_3$, the characteristic polynomial $(t - 2)^3$ leads to a formula for $A^{-1}$ of degree $2$ in $A$.
The minimal polynomial $t - 2$ gives $A - 2I = 0$ at once, so $A^{-1} = \tfrac{1}{2} I$.

### Watch out

The constant term is $c_0 = p_A(0) = \det(-A) = (-1)^n \det A$, not $\det A$.
For the $3 \times 3$ example above, $\det A = 4$ but $c_0 = -4$, and using $+4$ gives $-A^{-1}$ in place of $A^{-1}$.
Also keep the identity matrix in every constant term: $A^2 - 5A - 2$ has no meaning, and the correct expression is $A^2 - 5A - 2I$.

### History

The method rests on the Cayley-Hamilton theorem, which Cayley stated in 1858 and Frobenius proved in general in 1878.

### Try it

First, invert $A = \begin{pmatrix} 3 & 1 \\ 2 & 1 \end{pmatrix}$ with the theorem.
Here $\operatorname{tr} A = 4$ and $\det A = 1$, so $A^2 - 4A + I = 0$ and $A^{-1} = 4I - A = \begin{pmatrix} 1 & -1 \\ -2 & 3 \end{pmatrix}$.

Second, find $R^{10}$ for the quarter turn $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
Its polynomial is $t^2 + 1$, so $R^2 = -I$ and $R^{10} = (R^2)^5 = -I$.

Third, can the theorem invert $\begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$?
No: its polynomial is $t^2 - 4t$, with constant term $0$, and indeed the determinant is $0$.

## Explanations

### L1 human

For a $2 \times 2$ matrix the Cayley-Hamilton theorem gives an equation such as $A^2 = 5A + 2I$.
You can use it like a rule for rewriting: each time $A^2$ appears, replace it by $5A + 2I$.
After a few rewrites, any power of $A$ becomes "some number times $A$ plus some number times $I$".
If the equation has a nonzero constant term, the same rule also tells you how to undo $A$.

### L2 human

Here is a typical problem: find $A^{-1}$ and $A^3$ for $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$.
The trace is $3$ and the determinant is $1$, so $p_A(t) = t^2 - 3t + 1$ and the theorem gives $A^2 = 3A - I$.
Rewrite this as $A(3I - A) = I$, which shows
$$A^{-1} = 3I - A = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix}.$$
Check: $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 2 - 1 & -2 + 2 \\ 1 - 1 & -1 + 2 \end{pmatrix} = I$.
For the cube, multiply the equation by $A$ and reduce again:
$$A^3 = 3A^2 - A = 3(3A - I) - A = 8A - 3I = \begin{pmatrix} 13 & 8 \\ 8 & 5 \end{pmatrix}.$$
Check: $A^2 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}$, and $A^2 A = \begin{pmatrix} 13 & 8 \\ 8 & 5 \end{pmatrix}$.
The numbers $1, 1, 2, 3, 5, 8, 13$ are Fibonacci numbers, and that is no accident, since the recurrence $a_{k+1} = 3a_k - a_{k-1}$ from $t^2 = 3t - 1$ picks out every second one.
The method is best for small matrices by hand, and for proving that the inverse is a polynomial in $A$.

### L3 human

The ring $F[A]$ of polynomials in $A$ is isomorphic to $F[t]/(m_A)$, where $m_A$ is the minimal polynomial.
In this ring $A$ is a unit exactly when $t$ and $m_A$ are coprime, that is, when $m_A(0) \ne 0$, and the extended Euclidean algorithm writes $1 = u(t) t + v(t) m_A(t)$ so that $A^{-1} = u(A)$.
The same idea computes a function of $A$ given by a power series, such as $e^{sA}$, as $r(A)$ for a polynomial $r$ of degree less than $n$ that agrees with the function at the eigenvalues, when these are distinct.
The sub-area on canonical forms explains what happens at repeated eigenvalues, where derivatives of the function enter.
