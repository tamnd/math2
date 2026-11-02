---
tag: SQH9X0X8N1
kind: definition
name: Remez algorithm
msc: [65D15, 41A50, 41A10]
defines: H129B6DA0F
uses: [ASWF03X5AM, 0X3WGX95FE, 0DPF6WRZW6]
sources:
  - url: https://en.wikipedia.org/wiki/Remez_algorithm
---

## Definition

Let $f \colon [a, b] \to \R$ be [[continuous|0X3WGX95FE]], let $n \ge 0$, and let $\mathcal{P}_n$ be the real polynomials of [[degree|0DPF6WRZW6]] at most $n$.
The *Remez algorithm* computes the [[minimax approximation|ASWF03X5AM]] of $f$ in $\mathcal{P}_n$ by the following iteration.

1. Choose a reference set of $n + 2$ points $a \le x_0 < x_1 < \cdots < x_{n+1} \le b$.
2. Solve the linear system $p(x_i) + (-1)^i E = f(x_i)$, $i = 0, \dots, n + 1$, for the $n + 1$ coefficients of $p \in \mathcal{P}_n$ and the number $E$.
3. Let $e = f - p$. Replace the reference set by $n + 2$ points $y_0 < \cdots < y_{n+1}$ in $[a, b]$ at which $e$ alternates in sign, $\abs{e(y_i)} \ge \abs{E}$ for all $i$, and $\abs{e(y_j)} = \max_{[a, b]} \abs{e}$ for some $j$.
4. Repeat steps 2 and 3 until $\max_{[a, b]} \abs{e} - \abs{E}$ is below a chosen tolerance.

## Remarks

The system in step 2 has a unique solution for any $n + 2$ distinct points.
After each step 2, the minimax error $E_n(f)$ satisfies $\abs{E} \le E_n(f) \le \max_{[a, b]} \abs{e}$, so the gap between the two bounds measures the progress.

Example: $f(x) = x^2$ on $[-1, 1]$, $n = 1$, reference set $-1, 0, 1$.
Step 2 for $p(x) = c_0 + c_1 x$ gives $c_0 - c_1 + E = 1$, $c_0 - E = 0$ and $c_0 + c_1 + E = 1$, so $c_1 = 0$ and $c_0 = E = 1/2$.
The error $x^2 - 1/2$ has maximum $1/2 = \abs{E}$, so the algorithm stops with the minimax line $p = 1/2$.

Non-example: solving $p(x_i) = f(x_i)$ at $n + 1$ points is plain interpolation, not a Remez step.
It lacks the levelled error term $(-1)^i E$, and its error need not alternate in sign with equal size.

For continuous $f$ the iterates converge to the minimax polynomial.
The method also applies to rational approximation and to other Chebyshev systems in place of $\mathcal{P}_n$.
