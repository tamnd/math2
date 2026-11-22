---
tag: 0BQAA2BK3Q
kind: concept
name: Eigenvalue
aliases: [characteristic-value, characteristic-root, proper-value]
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
uses: [0J7H0YBFDJ, 0S23E6YE83, 0912EEEVCT]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: General definition
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
    locator: History
  - book: isbn:9783031410253
    locator: Chapter 5
  - book: isbn:9780134860244
  - book: isbn:9780135367971
---

## Summary

An eigenvalue of a linear map is a number by which the map stretches some direction without turning it.
On the line of that direction, the map is just multiplication by the eigenvalue, so eigenvalues show the simplest pieces of a map.
Let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]] of a vector space $V$ over a field $F$.
A scalar $\lambda \in F$ is an *eigenvalue* of $T$ when
$$T(v) = \lambda v \quad \text{for some vector } v \ne 0 \text{ in } V.$$
Equivalently, the map $T - \lambda \id_V$ has a nonzero [[kernel|0S23E6YE83]], that is, it is not injective.
An eigenvalue of an $n \times n$ matrix $A$ over $F$ is an eigenvalue of the map $x \mapsto Ax$ on $F^n$.
The [[formal definition|0ZND7NQ970]] states this, and in finite dimension the eigenvalues are the roots of the [[characteristic polynomial|0VSSPAFM2C]].

## Motivation

Most vectors change their direction when a linear map acts on them, and that makes the map hard to picture.
Some vectors only get longer, shorter or reversed.
If there are enough of these special directions, then in a basis made of them the matrix of the map is diagonal.
Powers, exponentials and limits of a diagonal matrix are easy, because each entry on the diagonal is handled on its own.

This is why eigenvalues appear wherever a linear rule is applied again and again.
They give the growth rate of a linear recurrence such as the Fibonacci numbers, the frequencies of a vibrating system of springs, and the long-run state of a Markov chain.
In this sub-area the eigenvalues lead to the characteristic and minimal polynomials, and the sub-area on [[diagonalization|Z6S6PWMJPH]] uses them to simplify matrices.

## Notation

Books write $\lambda$ for an eigenvalue and $\sigma(A)$ or $\operatorname{spec}(A)$ for the set of all eigenvalues, the [[spectrum|0XPX5NC67E]].
Older books say "characteristic value", "characteristic root" or "proper value" for the same idea.
In Lean's Mathlib the statement "$\lambda$ is an eigenvalue of $T$" is `Module.End.HasEigenvalue T λ`.
Watch the field: the same matrix of integers can have eigenvalues over $\mathbb{C}$ and none over $\mathbb{R}$, so always say where $\lambda$ lives.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ over $\mathbb{R}$.
A scalar $\lambda$ is an eigenvalue when $A - \lambda I$ is not invertible, so we need $\det(\lambda I - A) = 0$:
$$\det(\lambda I - A) = (\lambda - 2)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda - 1)(\lambda - 3).$$
So the eigenvalues are $1$ and $3$.
Check with vectors:
$$A \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \qquad A \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix} = 3 \begin{pmatrix} 1 \\ 1 \end{pmatrix}.$$
The [[symmetric matrix with rows (2, 1) and (1, 2)|Z6K3QPP7DY]] works this example out in full, and the method returns in [[computing eigenvalues and eigenvectors by hand|7JJE96MZQY]].

### Zero as an eigenvalue

The scalar $0$ is an eigenvalue exactly when $T(v) = 0$ for some $v \ne 0$, that is, when $T$ is not injective.
For $B = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$ the determinant is $4 - 4 = 0$, and
$$B \begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 2 - 2 \\ 4 - 4 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix},$$
so $0$ is an eigenvalue of $B$.
In finite dimension an injective endomorphism is bijective, by the theorem on [[injective, surjective and bijective endomorphisms|0912EEEVCT]].
So for a square matrix, $0$ is an eigenvalue if and only if the matrix is singular, if and only if its determinant is $0$.
In the same way, $\lambda$ is an eigenvalue of a square matrix $A$ if and only if $A - \lambda I$ is singular.

### Eigenvalues beyond matrices

The definition needs no basis and no finite dimension.
On the space of all sequences, the left shift sends $(1, \lambda, \lambda^2, \dots)$ to $(\lambda, \lambda^2, \lambda^3, \dots)$, so every scalar is an eigenvalue, while the right shift has none, as [[the shift operators on sequences|HBVWZ0FXWC]] show.
On smooth functions, the derivative sends $e^{\lambda x}$ to $\lambda e^{\lambda x}$, so every real number is an eigenvalue of [[the derivative|1SKH5XJ5RB]].
This is the reason why exponentials solve linear differential equations with constant coefficients.

### The rules you can use

In finite dimension $n \ge 1$, the eigenvalues are [[the roots of the characteristic polynomial|053QVHF6N7]], a polynomial of degree $n$, so there are at most $n$ of them.
Similar matrices have the same characteristic polynomial, so they have the same eigenvalues.
If $T(v) = \lambda v$, then $T^2(v) = T(\lambda v) = \lambda^2 v$, and in general $p(\lambda)$ is an eigenvalue of $p(T)$ for every polynomial $p$, by the theorem on [[eigenvalues of a polynomial in an endomorphism|F2S8WGVARA]].
When the characteristic polynomial splits, the eigenvalues counted with multiplicity add up to the [[trace|0NMXDCNNKR]] and multiply to the [[determinant|0C2F40MEBC]]; for $A$ above, $1 + 3 = 4$ and $1 \cdot 3 = 3$.
[[Over an algebraically closed field an eigenvalue always exists|08CJB2NQ92]] when $0 < \dim V < \infty$.
The eigenvalues are also exactly [[the roots of the minimal polynomial|0QF4ZEFG52]].

### What it is not

An eigenvalue depends on the field.
The [[rotation of the plane by an angle that is not a multiple of pi|5AE98D7959]] turns every line through the origin, so it has no real eigenvalue, although it has the complex eigenvalues $e^{\pm i\theta}$.
The diagonal entries of a matrix are not its eigenvalues in general.
The swap matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has the diagonal entries $0, 0$ and the eigenvalues $1, -1$, as [[the diagonal entries of a non-triangular matrix|FT8XA974H9]] shows.
Row reduction does not keep the eigenvalues either: reducing $A$ above to $\begin{pmatrix} 2 & 1 \\ 0 & 3/2 \end{pmatrix}$ suggests $2$ and $3/2$, which are wrong, as [[row reduction changes the eigenvalues|M1XGWNT48M]] explains.

### Watch out

The condition $v \ne 0$ is the heart of the definition.
Since $T(0) = 0 = \lambda \cdot 0$ for every $\lambda$, a definition that allowed $v = 0$ would make every scalar an eigenvalue.
A second trap is to treat eigenvalues like numbers that add.
The matrices $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ each have only the eigenvalue $0$, but their sum is the swap matrix, with the eigenvalues $1$ and $-1$.
So the eigenvalues of $A + B$ or of $AB$ are in general not sums or products of eigenvalues of $A$ and $B$.

### History

Euler studied the rotation of rigid bodies and saw the importance of their principal axes.
Lagrange then saw that the principal axes are the eigenvectors of the inertia matrix.
Cauchy proved that a real symmetric matrix has real eigenvalues, and he introduced the term "racine caractéristique", characteristic root.
Hilbert used the German word "eigen", meaning "own", in this sense in 1904, in his work on integral operators, and the mixed word "eigenvalue" became standard in English.

### Try it

First, is $4$ an eigenvalue of $\begin{pmatrix} 3 & 1 \\ 2 & 2 \end{pmatrix}$?
Yes: the vector $(1, 1)$ goes to $(3 + 1, 2 + 2) = (4, 4)$, which is $4$ times $(1, 1)$.

Second, let $T$ be invertible with eigenvalue $\lambda$; show that $\lambda^{-1}$ is an eigenvalue of $T^{-1}$.
From $T(v) = \lambda v$ with $v \ne 0$ we get $\lambda \ne 0$, since $T$ is injective, and applying $T^{-1}$ gives $v = \lambda T^{-1}(v)$, so $T^{-1}(v) = \lambda^{-1} v$.

## Explanations

### L1 human

A matrix moves the vectors of the plane, and most vectors get turned to a new direction.
A few special vectors stay on their own line and only get longer, shorter or flipped.
The stretch factor of such a vector is an eigenvalue.
For example, the matrix with rows $(2, 0)$ and $(0, 3)$ stretches the horizontal axis by $2$ and the vertical axis by $3$.
So $2$ and $3$ are its eigenvalues, and every other direction gets turned a little.

### L2 human

Here is a typical use: how fast do the Fibonacci numbers grow?
The rule $F_{k+1} = F_k + F_{k-1}$ says that the pair $(F_{k+1}, F_k)$ is $A$ times the pair $(F_k, F_{k-1})$, with
$$A = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}.$$
Its eigenvalues are the roots of
$$\det(tI - A) = (t - 1)t - 1 = t^2 - t - 1,$$
namely $\varphi = \tfrac{1 + \sqrt{5}}{2} \approx 1.618$ and $\psi = \tfrac{1 - \sqrt{5}}{2} \approx -0.618$.
Check: $A(\varphi, 1) = (\varphi + 1, \varphi)$, and $\varphi + 1 = \varphi^2$, so this is $\varphi (\varphi, 1)$.
Every starting pair is a combination of the two eigenvectors, and each step multiplies the parts by $\varphi$ and by $\psi$.
Since $|\psi| < 1$, the second part dies out, so $F_{k+1} / F_k$ tends to $\varphi$; for example $34 / 21 \approx 1.619$.
The largest eigenvalue in absolute value controls the long-run growth of any repeated linear rule.

### L3 human

An eigenvalue is a point $\lambda$ where the operator $T - \lambda$ fails to be injective.
In infinite dimension, injective and invertible differ, and the [[spectrum of an operator|XXXSST2DR5]] collects every $\lambda$ for which $T - \lambda$ is not invertible; the eigenvalues form only its point spectrum.
For example, the right shift on sequences is injective but not surjective, so $0$ lies in the spectrum without being an eigenvalue.
Algebraically, $V$ becomes a module over $F[x]$ with $x$ acting as $T$, and $\lambda$ is an eigenvalue exactly when the module contains a copy of $F[x]/(x - \lambda)$.
Estimates for eigenvalues, such as the [[Gershgorin circle theorem|0ETGP0XVCJ]] and the [[Perron-Frobenius theorem|62NS7PV1M9]], belong to matrix analysis.
