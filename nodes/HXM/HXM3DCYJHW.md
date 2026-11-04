---
tag: HXM3DCYJHW
kind: proof
name: Proof that the convergents of an irrational number converge to it
msc: [11A55]
proves: 0E70M92FE3
uses: [0SJ7Z6VKWK, 0SRWNR42BQ, 0YVRNEDSVG, 0PMY0YQYXX, 0ASJVEFA9J]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_continued_fraction
    locator: Infinite continued fractions and convergents
---

## Proof

Let $x_n$ and $a_n$ be the complete quotients and partial quotients of the [[continued fraction expansion|0SJ7Z6VKWK]] of $x$: $x_0 = x$, $a_n = \floor{x_n}$, $x_{n+1} = 1/(x_n - a_n)$.
Let $p_n$ and $q_n$ be given by the recurrences in the definition of [[convergents|0SRWNR42BQ]].

1. Since $x$ is irrational, its expansion is infinite by [[the termination theorem|0PMY0YQYXX]]. So $x_n$ and $a_n$ exist for all $n \ge 0$.
2. Each $x_n$ is irrational. Indeed $x_0 = x$, and if $x_{n+1}$ were rational then $x_n = a_n + 1/x_{n+1}$ would be rational.
3. So $x_n$ is not an integer, and $x_n > \floor{x_n} = a_n$ for each $n$. For $n \ge 1$ this gives $x_n > a_n \ge 1$.
4. Claim A: $p_n q_{n-1} - p_{n-1} q_n = (-1)^{n+1}$ for $n \ge -1$. We argue by [[induction|0ASJVEFA9J]] on $n$.
5. For $n = -1$: $p_{-1} q_{-2} - p_{-2} q_{-1} = 1 \cdot 1 - 0 \cdot 0 = 1$.
6. For $n \ge 0$, the recurrences give $p_n q_{n-1} - p_{n-1} q_n = (a_n p_{n-1} + p_{n-2}) q_{n-1} - p_{n-1} (a_n q_{n-1} + q_{n-2})$. This equals $-(p_{n-1} q_{n-2} - p_{n-2} q_{n-1})$, so the sign flips at each step. This proves claim A.
7. Claim B: $x = \dfrac{x_{n+1} p_n + p_{n-1}}{x_{n+1} q_n + q_{n-1}}$ for $n \ge -1$, with a positive denominator. We argue by induction on $n$.
8. For $n = -1$ the right side is $\dfrac{x_0 \cdot 1 + 0}{x_0 \cdot 0 + 1} = x_0 = x$.
9. Claim C: $q_n \ge 1$ for $n \ge 0$, $q_n \ge q_{n-1} \ge 0$ for $n \ge 0$, and $q_n \ge n$ for $n \ge 1$. Indeed $q_0 = a_0 \cdot 0 + 1 = 1$ and $q_1 = a_1 q_0 + q_{-1} = a_1 \ge 1$. For $n \ge 2$, $q_n = a_n q_{n-1} + q_{n-2} \ge q_{n-1} + 1$, using $a_n \ge 1$ and $q_{n-2} \ge 1$.
10. In claim B the denominators are positive: $x_{n+1} > 0$, $q_n \ge 1$ and $q_{n-1} \ge 0$ for $n \ge 0$.
11. Induction step for claim B. Assume it for $n - 1$, where $n \ge 0$: $x = \dfrac{x_n p_{n-1} + p_{n-2}}{x_n q_{n-1} + q_{n-2}}$. Substitute $x_n = a_n + 1/x_{n+1}$ and multiply the numerator and the denominator by $x_{n+1} > 0$.
12. The numerator becomes $x_{n+1}(a_n p_{n-1} + p_{n-2}) + p_{n-1} = x_{n+1} p_n + p_{n-1}$. In the same way the denominator becomes $x_{n+1} q_n + q_{n-1}$. This proves claim B.
13. Let $n \ge 0$. By claim B, $x - \dfrac{p_n}{q_n} = \dfrac{q_n p_{n-1} - p_n q_{n-1}}{q_n (x_{n+1} q_n + q_{n-1})}$, after putting both fractions over a common denominator.
14. By claim A, the numerator in step 13 is $-(-1)^{n+1} = (-1)^n$. So $\abs{x - \dfrac{p_n}{q_n}} = \dfrac{1}{q_n (x_{n+1} q_n + q_{n-1})}$.
15. By step 3, $x_{n+1} > a_{n+1}$. Since $q_n \ge 1$, we get $x_{n+1} q_n + q_{n-1} > a_{n+1} q_n + q_{n-1} = q_{n+1}$.
16. By steps 14 and 15, $\abs{x - p_n/q_n} < \dfrac{1}{q_n q_{n+1}}$.
17. By claim C, $q_{n+1} \ge q_n \ge 1$, so $\dfrac{1}{q_n q_{n+1}} \le \dfrac{1}{q_n^2}$.
18. By claim C, $q_n \ge n$ for $n \ge 1$, so $\abs{x - p_n/q_n} < 1/n^2$ for $n \ge 1$. This tends to $0$, so $p_n / q_n \to x$ as $n \to \infty$.

## Idea

The number $x$ is the convergent formula with the last partial quotient replaced by the exact complete quotient $x_{n+1}$.
The determinant identity $p_n q_{n-1} - p_{n-1} q_n = \pm 1$ then makes the error exactly $1/(q_n(x_{n+1} q_n + q_{n-1}))$.
Since $x_{n+1} > a_{n+1}$, this is less than $1/(q_n q_{n+1})$, and the denominators grow.
