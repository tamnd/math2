---
tag: PJS8KR6FAR
kind: proof
name: Proof of the integral test
msc: [40A05]
proves: 019QZ6RRVH
uses: [0VCTBJMEJF, 0Y12QYTJK3, 04YKAYDQPW, 05RCDKHZM6, 0MBWQKM8QR, 069HKV4X1E, 0MX1HZBBXJ, 0M8TGGP9JP]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_test_for_convergence
    locator: Proof
---

## Proof

1. Since $f$ is monotone, it is [[Riemann integrable|04YKAYDQPW]] on $[N, b]$ for each $b > N$. For $b \ge N$ let $F(b) = \int_N^b f(x)\, dx$, with $F(N) = 0$.
2. $F$ is increasing. For $N \le b < b'$, [[additivity over intervals|05RCDKHZM6]] gives $F(b') - F(b) = \int_b^{b'} f(x)\, dx$. This is at least $0$ by [[monotonicity of the integral|0MBWQKM8QR]], since $f \ge 0$.
3. Let $s_M = \sum_{n=N}^{M} f(n)$ for integers $M \ge N$. Since $f \ge 0$, by the [[criterion for nonnegative series|0MX1HZBBXJ]], the series converges if and only if $(s_M)$ is bounded above.
4. Let $M > N$ and apply the [[comparison of a series and an integral|069HKV4X1E]] with $a = N$ and $n = M - N$. It gives $s_M - f(N) \le F(M) \le s_{M-1}$.
5. Claim: the [[improper integral|0VCTBJMEJF]] converges if and only if $F$ is bounded above on $[N, \infty)$.
6. Assume first that the improper integral converges, with value $I$. By the definition of the [[limit at infinity|0Y12QYTJK3]] with $\varepsilon = 1$, there is $b_1 \ge N$ with $F(b) < I + 1$ for all $b > b_1$.
7. For $N \le b \le b_1$, step 2 gives $F(b) \le F(b_1 + 1) < I + 1$. So $F$ is bounded above by $I + 1$.
8. Assume now that $F$ is bounded above, and let $I = \sup \set{F(b) : b \ge N}$. Let $\varepsilon > 0$.
9. By the [[approximation property of the supremum|0M8TGGP9JP]], there is $b_0 \ge N$ with $I - \varepsilon < F(b_0)$. For $b > b_0$, step 2 gives $I - \varepsilon < F(b_0) \le F(b) \le I$.
10. So $\abs{F(b) - I} < \varepsilon$ for all $b > b_0$. Thus $\lim_{b \to \infty} F(b) = I$, and the claim of step 5 is proved.
11. Assume the series converges, and let $S$ be its sum, so $s_M \le S$ for all $M$. Let $b \ge N$ and let $M$ be an integer with $M > b$ and $M > N$. By steps 2 and 4, $F(b) \le F(M) \le s_{M-1} \le S$.
12. So $F$ is bounded above, and the improper integral converges by step 5.
13. Conversely, assume the improper integral converges. By step 5, $F(b) \le B$ for all $b \ge N$, for some real number $B$.
14. By step 4, $s_M \le f(N) + F(M) \le f(N) + B$ for all $M > N$, and $s_N = f(N)$. So $(s_M)$ is bounded above, and the series converges by step 3.

## Idea

The integral of $f$ from $N$ to $M$ lies between two partial sums of the series, which differ only by one term. Both the partial sums and the integrals increase, since $f \ge 0$. So one of them stays bounded exactly when the other does, and bounded increasing quantities converge.
