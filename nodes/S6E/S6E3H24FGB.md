---
tag: S6E3H24FGB
kind: definition
name: Shanks transformation
msc: [65B05, 65B10, 40A25]
defines: C0TXDZZMH7
uses: [0QE8STGJH2, 0C3CFHDN6R, 90ANMX55DP]
sources:
  - url: https://en.wikipedia.org/wiki/Shanks_transformation
---

## Definition

Let $(A_n)_{n \ge 0}$ be a [[sequence|0QE8STGJH2]] of real or complex numbers, and write $\Delta A_m = A_{m+1} - A_m$.
For $n \ge 1$, the *Shanks transformation* of $(A_n)$ is
$$S(A_n) = \frac{A_{n+1} A_{n-1} - A_n^2}{A_{n+1} - 2A_n + A_{n-1}},$$
defined when the denominator is not $0$.
More generally, let $k \ge 1$ and $n \ge k$.
The transformation of order $k$ is the quotient of two [[determinants|0C3CFHDN6R]]:
$$e_k(A_n) = \frac{\begin{vmatrix} A_{n-k} & \cdots & A_n \\ \Delta A_{n-k} & \cdots & \Delta A_n \\ \vdots & & \vdots \\ \Delta A_{n-1} & \cdots & \Delta A_{n+k-1} \end{vmatrix}}{\begin{vmatrix} 1 & \cdots & 1 \\ \Delta A_{n-k} & \cdots & \Delta A_n \\ \vdots & & \vdots \\ \Delta A_{n-1} & \cdots & \Delta A_{n+k-1} \end{vmatrix}}.$$
For $1 \le j \le k$, row $j$ of each determinant is $\Delta A_{n-k+j-1}, \dots, \Delta A_{n+j-1}$.
The denominator must not be $0$.
Thus $e_1(A_n) = S(A_n)$.

## Remarks

Check of $e_1 = S$: the numerator is $A_{n-1}\Delta A_n - A_n \Delta A_{n-1} = A_{n+1}A_{n-1} - A_n^2$ and the denominator is $\Delta A_n - \Delta A_{n-1}$.
Example: for the partial sums $A_0 = 1$, $A_1 = \frac23$, $A_2 = \frac{13}{15}$ of the Leibniz series,
$S(A_1) = \dfrac{\frac{13}{15} - \frac49}{\frac{13}{15} - \frac43 + 1} = \dfrac{19/45}{8/15} = \dfrac{19}{24}$.
Non-example: for an arithmetic sequence such as $A_n = n$ the denominator $A_{n+1} - 2A_n + A_{n-1}$ is $0$, so $S(A_n)$ is not defined.
Up to a shift of index, $S$ is [[Aitken's delta-squared process|R40BXAKSV4]]: $S(A_{n+1}) = A_n - \frac{(\Delta A_n)^2}{\Delta^2 A_n}$.
The transformation can be iterated, as in $S(S(A_n))$; this is different from $e_2$ in general.

## Explanations

### L1 human

The first-order formula uses three consecutive terms; the order-$k$ formula uses $2k + 1$ terms and fits a more flexible model of the error.
