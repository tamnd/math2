---
tag: 2MNSMHNRXC
kind: proof
name: Proof of Legendre's theorem on continued fractions
msc: [11J70]
proves: 0JXTQ392ZM
uses: [0SJ7Z6VKWK, 0SRWNR42BQ, 06XF7BCFFJ, 0YVRNEDSVG, 0PMY0YQYXX, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_continued_fraction
    locator: Legendre's theorem on continued fractions
---

## Proof

We follow the argument of Hardy and Wright.
For integers $c_0$ and $c_1, \dots, c_m \ge 1$, let $P_k$ and $Q_k$ ($-2 \le k \le m$) be given by the recurrences in the definition of [[convergents|0SRWNR42BQ]] with terms $c_k$.

1. Fact 1: $P_k Q_{k-1} - P_{k-1} Q_k = (-1)^{k+1}$ for $-1 \le k \le m$. For $k = -1$ the left side is $1$. For $k \ge 0$, inserting the recurrences shows that the left side is minus its value at $k - 1$.
2. Fact 2: $Q_k \ge Q_{k-1} \ge 0$ and $Q_k \ge 1$ for $0 \le k \le m$. Indeed $Q_{-1} = 0$, $Q_0 = 1$, and $Q_k = c_k Q_{k-1} + Q_{k-2} \ge Q_{k-1}$ for $k \ge 1$, by [[induction|0ASJVEFA9J]].
3. Fact 3: let $y_{m+1} > 0$ be real and put $y_k = c_k + 1/y_{k+1}$ for $k = m, m-1, \dots, 0$. Then $y_0 = \dfrac{y_{k+1} P_k + P_{k-1}}{y_{k+1} Q_k + Q_{k-1}}$ for $-1 \le k \le m$.
4. Proof of fact 3, by induction on $k$. For $k = -1$ the right side is $y_0$. For the step, substitute $y_k = c_k + 1/y_{k+1}$ into the formula for $k - 1$ and multiply above and below by $y_{k+1}$. The recurrences turn the result into the formula for $k$.
5. Fact 4: in fact 3, assume $y_{m+1} > 1$. Then the [[continued fraction expansion|0SJ7Z6VKWK]] of $y_0$ has at least $m + 2$ terms, and its first $m + 1$ terms are $c_0, \dots, c_m$.
6. Proof of fact 4. First, $y_k > 1$ for $1 \le k \le m + 1$: this holds for $k = m + 1$, and $y_k = c_k + 1/y_{k+1} > c_k \ge 1$ for $1 \le k \le m$.
7. For $0 \le k \le m$ we have $0 < 1/y_{k+1} < 1$. So the [[floor|0YVRNEDSVG]] of $y_k = c_k + 1/y_{k+1}$ is $c_k$, and $y_k \ne c_k$.
8. Let $x_k$, $a_k$ be the complete and partial quotients of $y_0$. By induction on $k$, step 7 gives $x_k = y_k$ and $a_k = c_k$ for $0 \le k \le m$, and the process does not stop before step $m + 1$. This proves fact 4.
9. Fact 5: by fact 4, the $m$-th convergent of $y_0$ is $P_m / Q_m$, because $P_m$ and $Q_m$ depend only on $c_0, \dots, c_m$.
10. Now the proof. Write $p/q = p'/q'$ in lowest terms with $q' \ge 1$. Then $q' \le q$, so $\abs{\alpha - p'/q'} < \frac{1}{2q^2} \le \frac{1}{2q'^2}$. So we may assume that $\gcd(p, q) = 1$.
11. The [[expansion|0SJ7Z6VKWK]] of $p/q$ is finite by [[the termination theorem|0PMY0YQYXX]]. Say it is $[a_0; a_1, \dots, a_n]$, a [[simple continued fraction|06XF7BCFFJ]], and the process stops with $x_n = a_n$.
12. By fact 3 with $m = n - 1$ and $y_n = x_n = a_n$, we get $p/q = \dfrac{a_n p_{n-1} + p_{n-2}}{a_n q_{n-1} + q_{n-2}} = p_n / q_n$. For $n = 0$ this reads $p/q = a_0 = p_0/q_0$.
13. If $n \ge 1$, then $a_n = x_n = 1/(x_{n-1} - a_{n-1}) > 1$, so $a_n \ge 2$.
14. Consider also the list $a_0, \dots, a_{n-1}, a_n - 1, 1$ of length $n + 2$. Its terms after the first are positive integers by step 13. Its numerators $p'_k$ satisfy $p'_k = p_k$ for $k \le n - 1$, $p'_n = p_n - p_{n-1}$ and $p'_{n+1} = p'_n + p_{n-1} = p_n$. In the same way $q'_{n+1} = q_n$.
15. So we have two lists $c_0, \dots, c_m$, with $m = n$ and $m = n + 1$, whose terms after the first are positive. For both, $P_m / Q_m = p_n / q_n = p/q$.
16. By fact 1, $\gcd(P_m, Q_m) = 1$, and $Q_m \ge 1$ by fact 2. Since also $\gcd(p, q) = 1$ and $q \ge 1$, we get $P_m = p$ and $Q_m = q$ for both lists.
17. If $\alpha = p/q$, then by step 11 the expansion of $\alpha$ is $[a_0; \dots, a_n]$, and its $n$-th convergent is $p_n / q_n = p/q$. We are done in this case.
18. Otherwise write $\alpha - p/q = \sigma \theta / q^2$ with $\sigma \in \set{1, -1}$ and $0 < \theta < \frac{1}{2}$. This is possible by the hypothesis.
19. The two values of $m$ in step 15 differ by one. Choose the list with $(-1)^m = \sigma$.
20. Put $\omega = \dfrac{1}{\theta} - \dfrac{Q_{m-1}}{Q_m}$. By fact 2, $0 \le Q_{m-1}/Q_m \le 1$. Since $1/\theta > 2$, we get $\omega > 1$.
21. Put $\beta = \dfrac{\omega P_m + P_{m-1}}{\omega Q_m + Q_{m-1}}$. By the choice of $\omega$, $\omega Q_m + Q_{m-1} = Q_m / \theta > 0$.
22. Over a common denominator, $\beta - \dfrac{P_m}{Q_m} = \dfrac{Q_m P_{m-1} - P_m Q_{m-1}}{Q_m (\omega Q_m + Q_{m-1})}$. By fact 1 the numerator is $(-1)^m = \sigma$.
23. With step 21 and $Q_m = q$, this gives $\beta - p/q = \sigma \theta / q^2 = \alpha - p/q$. So $\beta = \alpha$.
24. By fact 3 with $y_{m+1} = \omega$, the number $y_0$ of fact 3 equals $\beta = \alpha$.
25. Since $\omega > 1$, fact 5 shows that the $m$-th convergent of $\alpha$ is $P_m / Q_m = p/q$.

## Idea

Write $p/q$ as a finite continued fraction; there are two ways, of lengths differing by one, so the parity of the length can be chosen.
Then $\alpha$ is that finite continued fraction with one extra real tail $\omega$.
The bound $\frac{1}{2q^2}$ makes $\omega > 1$, and a tail bigger than $1$ does not change the earlier partial quotients.
So $p/q$ appears among the convergents of $\alpha$.
