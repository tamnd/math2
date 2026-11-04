---
tag: D87SHCXR69
kind: statement
role: theorem
name: André's theorem
sources:
  - wikipedia: en:4813617@r1362588099
    locator: Alternating permutation, section André's theorem
    note: adopted
    mention: wikipedia://en/4813617#EUIY
    sections: [Statement]
inventory: [SCBJABMKSB]
---

## Statement

The determination of the number *A*<sub>*n*</sub> of alternating permutations of the set {1, ..., *n*} is called *André's problem*. The numbers *A*<sub>*n*</sub> are variously known as *Euler numbers*, *zigzag numbers*, *up/down numbers*, or by some combinations of these names. The name Euler numbers in particular is sometimes used for a closely related sequence. The first few values of *A*<sub>*n*</sub> are 1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936, 50521, ... .

These numbers satisfy a simple recurrence, similar to that of the [[Catalan numbers|0YWZJEABB2]]: by splitting the set of alternating permutations (both down-up and up-down) of the set { 1, 2, 3, ..., *n*, *n* + 1 } according to the position *k* of the largest entry $n + 1$, one can show that

$$2A_{n+1} = \sum_{k=0}^n \binom{n}{k} A_k A_{n-k}$$

for all $n \ge 1$. (André 1881) used this recurrence to give a [[differential equation|003R0V5M7V]] satisfied by the exponential generating function

$$A(x) = \sum_{n=0}^\infty A_n \frac{x^n}{n!}$$

for the sequence $A_{n}$. In fact, the recurrence gives:

$$2\sum_{n\geq 1} A_{n+1} \frac{x^{n+1}}{(n+1)!} = \sum_{n\geq 1} \sum_{k=0}^n \frac{A_k}{k!} \frac{A_{n-k}}{(n-k)!} \frac{x^{n+1}}{n+1} = \int \left(\sum_{k\geq 0}A_k \frac{x^k}{k!}\right) \left(\sum_{j\geq 0}A_j \frac{x^j}{j!}\right) \, dx - x$$

where we substitute $j = n-k$ and $\frac{x^{n+1}}{n+1}=\int x^{k+j}\,dx$. This gives the integral equation

$$2(A(x) - 1 - x) = \int A(x)^2\,dx - x,$$

which after differentiation becomes $2\frac{dA}{dx} - 2 = A^2-1$. This differential equation can be solved by separation of variables (using the initial condition $A(0)=A_0/0!=1$), and simplified using a tangent half-angle formula, giving the final result

$$A(x) = \tan \left(\frac\pi4 + \frac x2\right) = \sec x + \tan x,$$

the sum of the secant and tangent functions. This result is known as *André's theorem*. A geometric interpretation of this result can be given using a generalization of a theorem by Johann Bernoulli.

It follows from André's theorem that the [[radius of convergence|0N288P2TB5]] of the series $A(x)$ is $\pi$/2. This allows one to compute the asymptotic expansion

$$A_n \sim 2 \left(\frac{2}{\pi}\right)^{n + 1} n!\,.$$
