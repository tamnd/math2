---
tag: WV3KXKPG7T
kind: proof
name: Proof of the ratio formula for the radius of convergence
msc: [30B10]
proves: 0JBMYAA9QH
uses: [0660QX1VPR, 0VP56B4EMX, 09G6KHS6GY, 0BTMQ04556, 0EHWPWGHB2, 0A3GWZ86AY]
sources:
  - url: https://en.wikipedia.org/wiki/Radius_of_convergence
    locator: Theoretical radius
---

## Proof

We compare consecutive terms $\abs{a_n} r^n$ directly, as in the ratio test.

1. Let $\sum a_n (x - c)^n$ be a real [[power series|0VP56B4EMX]]. Let $n_0$ be such that $a_n \ne 0$ for all $n \ge n_0$.
2. For $n \ge n_0$ let $\rho_n = \abs{a_{n+1}} / \abs{a_n}$. By hypothesis $\rho_n \to L \in [0, \infty]$. When $L = \infty$, this means that for each $K$ there is $N$ with $\rho_n > K$ for all $n \ge N$.
3. Let $T$ be the set of $r \ge 0$ for which $(\abs{a_n} r^n)$ is bounded. By the [[definition|0660QX1VPR]], $R = \sup T$, with $R = \infty$ when $T$ is not bounded above.
4. The number $0$ lies in $T$, since $\abs{a_n} 0^n = 0$ for $n \ge 1$.
5. Claim A: if $L < \infty$, $r > 0$ and $r L < 1$, then $r \in T$. To see this, pick $q$ with $r L < q < 1$. Then $L < q / r$.
6. By the [[epsilon-N form|09G6KHS6GY]] with $\varepsilon = q/r - L$, there is $N \ge n_0$ with $\rho_n < q / r$ for all $n \ge N$.
7. For $n \ge N$, step 6 gives $\abs{a_{n+1}} r^{n+1} = \rho_n r \abs{a_n} r^n < q \abs{a_n} r^n \le \abs{a_n} r^n$.
8. By induction on $n$, step 7 gives $\abs{a_n} r^n \le \abs{a_N} r^N$ for all $n \ge N$. The finitely many terms with $n < N$ are bounded by their maximum. So $r \in T$.
9. Claim B: if $L > 0$, $r > 0$ and $r L > 1$, then $r \notin T$. Here $r L > 1$ is read as true for all $r > 0$ when $L = \infty$.
10. Pick $q$ with $1 < q < r L$. When $L = \infty$, take $q = 2$. Then $q / r < L$.
11. If $L < \infty$, the epsilon-N form with $\varepsilon = L - q/r$ gives $N \ge n_0$ with $\rho_n > q/r$ for $n \ge N$. If $L = \infty$, step 2 with $K = q/r$ gives such an $N$.
12. For $n \ge N$, as in step 7, $\abs{a_{n+1}} r^{n+1} > q \abs{a_n} r^n$. By induction, $\abs{a_n} r^n \ge D q^{n - N}$ for all $n \ge N$, where $D = \abs{a_N} r^N > 0$.
13. By the [[binomial theorem|0EHWPWGHB2]], $q^j = (1 + (q - 1))^j \ge 1 + j (q - 1)$ for all natural numbers $j$, since every term of the expansion is nonnegative.
14. Let $C$ be a real number. The reals are [[Archimedean|0A3GWZ86AY]], so there is $j$ with $D j (q - 1) > C$. Then $n = N + j$ gives $\abs{a_n} r^n \ge D (1 + j(q-1)) > C$.
15. So $(\abs{a_n} r^n)$ is not bounded, and $r \notin T$.
16. Case $L = 0$. Claim A gives every $r > 0$ in $T$. So $T$ is not bounded above, and $R = \infty = 1/L$.
17. Case $L = \infty$. Claim B and step 4 give $T = \set{0}$. So $R = 0 = 1/L$.
18. Case $0 < L < \infty$. By Claim B, $1/L$ is an upper bound of $T$. By Claim A, every $r$ with $0 < r < 1/L$ lies in $T$.
19. So no number below $1/L$ is an upper bound of $T$. By the definition of the [[supremum|0BTMQ04556]], $R = 1/L$.
20. In all cases $R = 1/L$, with the conventions $1/0 = \infty$ and $1/\infty = 0$.

## Idea

If $\abs{a_{n+1}} / \abs{a_n}$ is close to $L$, then $\abs{a_n} r^n$ is eventually multiplied by about $L r$ at each step. When $L r < 1$ the terms shrink, and when $L r > 1$ they grow like a geometric sequence with ratio above $1$. So the cutoff is $r = 1/L$.
