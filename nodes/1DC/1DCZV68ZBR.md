---
tag: 1DCZV68ZBR
kind: proof
name: Proof of the Cauchy–Hadamard theorem
msc: [30B10]
proves: 07E5MB1CA2
uses: [0660QX1VPR, 0VP56B4EMX, 0P8BA7T7S5, 02V2GYAC8P, 09G6KHS6GY, 0M8TGGP9JP, 0BTMQ04556, 0EHWPWGHB2, 0A3GWZ86AY, 05FQ3VGAR9]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Hadamard_theorem
    locator: Theorem for one complex variable
---

## Proof

We work from the definition of the radius of convergence and compare $\abs{a_n}$ with powers $t^n$.

1. Let $\sum a_n (x - c)^n$ be a real [[power series|0VP56B4EMX]]. For $n \ge 1$ let $x_n = \abs{a_n}^{1/n} \ge 0$.
2. Let $\ell = \limsup_{n \to \infty} x_n$, the [[limit superior|0P8BA7T7S5]]. If $(x_n)$ is not bounded above, then $\ell = \infty$ by convention. Otherwise $(x_n)$ is [[bounded|05FQ3VGAR9]], since $x_n \ge 0$, and $0 \le \ell < \infty$.
3. Let $T$ be the set of $r \ge 0$ for which $(\abs{a_n} r^n)$ is bounded. By the [[definition|0660QX1VPR]], $R = \sup T$, with $R = \infty$ when $T$ is not bounded above.
4. The number $0$ lies in $T$, since $\abs{a_n} 0^n = 0$ for $n \ge 1$.
5. Claim A: if $\ell < \infty$, $r > 0$ and $r \ell < 1$, then $r \in T$. To see this, pick $t$ with $\ell < t < 1/r$.
6. When $\ell < \infty$, let $s_n = \sup \set{x_k : k \ge n}$. The sequence $(s_n)$ decreases and [[converges to its infimum|02V2GYAC8P]], which is $\ell$.
7. Since $t > \ell$, the [[epsilon-N form|09G6KHS6GY]] gives $N \ge 1$ with $s_N < t$. So $x_k < t$ for all $k \ge N$.
8. For $k \ge N$, step 7 gives $\abs{a_k} < t^k$. So $\abs{a_k} r^k < (t r)^k \le 1$, since $0 < t r < 1$.
9. The finitely many terms with $k < N$ are bounded by their maximum. So $(\abs{a_k} r^k)$ is bounded, and $r \in T$. This proves Claim A.
10. Claim B: if $r > 0$ and $r \ell > 1$, then $r \notin T$. Here $r \ell > 1$ is read as true for all $r > 0$ when $\ell = \infty$.
11. Pick $t$ with $1/r < t < \ell$. When $\ell = \infty$, take $t = 2/r$. We show that for each $n \ge 1$ there is $k \ge n$ with $x_k > t$.
12. If $\ell < \infty$, then $s_n \ge \ell > t$, because $\ell$ is the infimum of the $s_n$. The [[approximation property of the supremum|0M8TGGP9JP]] gives $k \ge n$ with $x_k > t$.
13. If $\ell = \infty$, then $(x_k)$ is not bounded above. So some $x_k$ exceeds $\max(t, x_1, \dots, x_n)$. Such a $k$ is not in $\set{1, \dots, n}$, so $k > n$ and $x_k > t$.
14. Let $q = t r > 1$. If $x_k > t$, then $\abs{a_k} > t^k$ and $\abs{a_k} r^k > q^k$.
15. By the [[binomial theorem|0EHWPWGHB2]], $q^k = (1 + (q - 1))^k \ge 1 + k (q - 1)$, since all the terms of the expansion are nonnegative.
16. Let $C$ be a real number. The reals are [[Archimedean|0A3GWZ86AY]], so there is $n \ge 1$ with $n (q - 1) > C$.
17. Steps 11 to 13 give $k \ge n$ with $x_k > t$. Steps 14 and 15 give $\abs{a_k} r^k > 1 + k (q - 1) > C$.
18. So $(\abs{a_k} r^k)$ is not bounded, and $r \notin T$. This proves Claim B.
19. Case $\ell = 0$. Claim A gives every $r > 0$ in $T$. So $T$ is not bounded above, and $R = \infty = 1/\ell$.
20. Case $\ell = \infty$. Claim B gives $T = \set{0}$, with step 4. So $R = 0 = 1/\ell$.
21. Case $0 < \ell < \infty$. By Claim B, every element of $T$ is at most $1/\ell$, so $1/\ell$ is an upper bound of $T$.
22. In this case, let $b < 1/\ell$. The number $r = (\max(b, 0) + 1/\ell)/2$ satisfies $b < r < 1/\ell$, and $r \in T$ by Claim A. So no number below $1/\ell$ is an upper bound.
23. By steps 21 and 22 and the definition of the [[supremum|0BTMQ04556]], $R = 1/\ell$.
24. In all cases $R = 1/\ell$. With the conventions $1/0 = \infty$ and $1/\infty = 0$, this is $1/R = \limsup_{n \to \infty} \abs{a_n}^{1/n}$.

## Idea

The number $\ell$ measures the exponential growth rate of $\abs{a_n}$: eventually $\abs{a_n} < t^n$ for each $t > \ell$, and $\abs{a_n} > t^n$ infinitely often for each $t < \ell$. So $\abs{a_n} r^n$ stays bounded when $r \ell < 1$ and grows without bound when $r \ell > 1$. The cutoff is $r = 1/\ell$.
