---
tag: 0T0X8GTYYS
kind: statement
role: proposition
name: Determinant is a coefficient of the characteristic polynomial
msc: ["15A15", "15A18"]
topics: [6R1D6QPY3S]
audience: ug1
uses: [039HF58KQ5, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
---

## Statement

The constant term of the characteristic polynomial is the determinant, up to the sign $(-1)^n$.
Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$.
Then the constant coefficient of the [[characteristic polynomial|0VSSPAFM2C]] $p_A(t) = \det(t I_n - A)$ is
$$p_A(0) = (-1)^n \det A,$$
where $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

### Why it holds

The constant coefficient of a polynomial is its value at $t = 0$.
Evaluation at $0$ is a ring homomorphism $K[t] \to K$, so it commutes with the Leibniz formula, and
$$p_A(0) = \det(0 \cdot I_n - A) = \det(-A) = (-1)^n \det A,$$
because each of the $n$ rows of $-A$ carries a factor $-1$.
For example, $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ has $p_A(t) = t^2 - 5t - 2$, and the constant term $-2$ equals $(-1)^2 \det A = -2$.

### What it gives you

Over a field, $0$ is a root of $p_A$ exactly when $\det A = 0$.
So $0$ is an eigenvalue of $A$ if and only if $A$ is singular.
When $p_A$ splits as $\prod_i (t - \lambda_i)$, the constant term is $(-1)^n \lambda_1 \cdots \lambda_n$, and comparing gives the rule that the [[determinant is the product of the eigenvalues|0C2F40MEBC]].
The general [[formula for all the coefficients|0FRYPZ6D0X]] contains this statement as its last case.

### Watch out

With the other convention $\det(A - tI)$, the constant term is $\det A$ itself, with no sign.
For $3 \times 3$ matrices the two conventions give opposite constant terms, so check which one a formula assumes.

## Explanations

### L1 human

The constant term of the characteristic polynomial is the determinant, up to a sign.
You see this by putting $t = 0$ into $\det(tI - A)$, which leaves $\det(-A)$.
So a matrix with determinant zero has the eigenvalue $0$, and a matrix with eigenvalue $0$ has determinant zero.
