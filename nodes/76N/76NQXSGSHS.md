---
tag: 76NQXSGSHS
kind: definition
name: Solution of recurrences by generating functions
msc: [39A06, 05A15]
defines: WS2E29RZD5
uses: [0PHAC833JF, 033WGN00BF, 081THG13JZ]
sources:
  - url: https://en.wikipedia.org/wiki/Generating_function
---

## Definition

Let $K$ be a field and let $(u_n)_{n \ge 0}$ be a sequence in $K$ that satisfies a recurrence relation for $n \ge 0$.
The *generating function method* for this recurrence consists of these steps.

1. Form the [[generating function|0PHAC833JF]] $U(x) = \sum_{n \ge 0} u_n x^n$ in the ring $K[\![x]\!]$ of [[formal power series|033WGN00BF]].
2. Multiply the recurrence for index $n$ by a suitable power $x^{n+d}$ and sum over $n \ge 0$. This gives an equation for $U(x)$ that involves the initial values.
3. Solve this equation for $U(x)$.
4. Read off $u_n$ as the coefficient of $x^n$ in the solution.

For a [[linear recurrence with constant coefficients|081THG13JZ]] $u_{n+d} = c_{d-1} u_{n+d-1} + \cdots + c_0 u_n$, step 3 gives
$$U(x) = \frac{P(x)}{1 - c_{d-1} x - c_{d-2} x^2 - \cdots - c_0 x^d},$$
where $P$ is a polynomial of degree less than $d$ determined by $u_0, \dots, u_{d-1}$.

## Remarks

Example: the [[Fibonacci sequence|0GA9K57A39]] has $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$.
Multiplying by $x^{n+2}$ and summing gives $F(x) - x = x F(x) + x^2 F(x)$, so $F(x) = x/(1 - x - x^2)$.
Partial fractions with the roots of $1 - x - x^2$ then give $F_n = (\varphi^n - \psi^n)/\sqrt{5}$, where $\varphi, \psi$ are the roots of $X^2 - X - 1$.
Non-example: for the nonlinear recurrence $u_{n+1} = u_n^2$, step 2 does not give an equation in $U$ alone.
The series $\sum u_n^2 x^n$ is not a simple function of $U(x)$, so the method does not apply directly.
The denominator in the constant-coefficient case is $x^d \chi(1/x)$, where $\chi$ is the [[characteristic polynomial|0YA7X86K05]] of the recurrence.
Other generating functions, such as exponential ones, suit other recurrences, for example those with factors $n$ in the coefficients.
