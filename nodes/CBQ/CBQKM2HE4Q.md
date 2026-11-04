---
tag: CBQKM2HE4Q
kind: proof
name: Proof that power series are differentiable inside the radius of convergence
msc: [30B10, 26A24]
proves: 002X7EK91H
uses: [0VP56B4EMX, 0660QX1VPR, 0BTMQ04556, 0MVTCFW42K, 0RAM4E07NR, 0S4JF619V7, 0MH1WK89PP, 0RXX2PT1MQ, 0HXEX0DPRA, 0BWXV7GADW, 0TJ8QBJX5K]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/analysis_ii_thm_proof.pdf
    locator: Section 2.2, Power series
---

## Proof

First we show that the derived series has the same radius of convergence. Then we apply term-by-term differentiation on a closed interval around each point.

*Part 1: the derived series has radius $R$.*

1. Let $f(x) = \sum_{n=0}^{\infty} a_n (x - c)^n$ have [[radius of convergence|0660QX1VPR]] $R > 0$. For $m \ge 0$, let $b_m = (m + 1) a_{m+1}$. The derived series is $\sum_{n=1}^{\infty} n a_n (x - c)^{n-1} = \sum_{m=0}^{\infty} b_m (x - c)^m$.
2. Let $A = \set{ t \ge 0 : (|a_n| t^n) \text{ is bounded} }$ and $B = \set{ t \ge 0 : (|b_m| t^m) \text{ is bounded} }$. Then $R = \sup A$, and the derived series has radius $R' = \sup B$.
3. We show $B \subseteq A$. The constant sequence $(|a_n| 0^n)$ is bounded, so $0 \in A$. Let $t \in B$ with $t > 0$, and let $D$ bound $|b_m| t^m$. Then $|a_{m+1}| t^{m+1} = \frac{t \, |b_m| t^m}{m + 1} \le t D$ for all $m \ge 0$. So $(|a_n| t^n)$ is bounded, and $t \in A$.
4. By step 3, $R' = \sup B \le \sup A = R$.
5. Now let $0 < r < R$. As $r < R = \sup A$, $r$ is not an upper bound of $A$, by the definition of the [[supremum|0BTMQ04556]]. So there are $s \in A$ with $s > r$, and $C \ge 0$ with $|a_n| s^n \le C$ for all $n$.
6. Let $q = \frac{r}{s} \in (0, 1)$. For $m \ge 0$, step 5 gives
$$|b_m| r^m = (m + 1) |a_{m+1}| s^{m+1} \frac{r^m}{s^{m+1}} \le \frac{C}{s} (m + 1) q^m.$$
7. Let $\rho = \frac{1}{q} > 1$. Then $(m + 1) q^m = \frac{m}{\rho^m} + \frac{1}{\rho^m}$. Both terms tend to $0$, since [[exponentials dominate powers|0MVTCFW42K]]. By the [[sum rule|0RAM4E07NR]], $(m + 1) q^m \to 0$.
8. A [[convergent sequence is bounded|0S4JF619V7]]. So by steps 6 and 7, $(|b_m| r^m)$ is bounded, and $r \in B$.
9. Suppose that $R' < R$. Choose $r$ with $\max(R', 0) < r < R$. By step 8, $r \in B$, so $r \le \sup B = R'$. This is a contradiction. So $R' \ge R$, and with step 4, $R' = R$.

*Part 2: differentiability.*

10. Fix $x \in (c - R, c + R)$. Choose $r$ with $|x - c| < r < R$, and let $J = [c - r, c + r]$.
11. For $n \ge 0$ and real $t$, let $f_n(t) = a_n (t - c)^n$. Apply the [[derivative of a polynomial|0MH1WK89PP]] to $u \mapsto a_n u^n$, and the [[chain rule|0RXX2PT1MQ]] with $u = t - c$. So $f_n$ is differentiable on $\R$ with $f_n'(t) = n a_n (t - c)^{n-1}$ for $n \ge 1$, and $f_0' = 0$.
12. In particular, at the endpoints of $J$ the [[one-sided derivatives|0HXEX0DPRA]] of $f_n$ exist and equal $f_n'$. So each $f_n$ is differentiable on $J$.
13. At $t = c$, every term $f_n(c)$ with $n \ge 1$ is $0$. So $\sum_n f_n(c)$ converges, with sum $a_0$.
14. By step 11, $\sum_n f_n'$ is the derived series. By Part 1 it has radius $R > 0$. Since $0 < r < R$, it converges uniformly on $J$, because [[power series converge uniformly on smaller intervals|0BWXV7GADW]].
15. By steps 12 to 14, [[term-by-term differentiation|0TJ8QBJX5K]] applies on $J$. So $\sum_n f_n$ converges uniformly on $J$, its sum is differentiable on $J$, and the derivative is $\sum_n f_n'$.
16. The sum of $\sum_n f_n$ on $J$ is $f$ restricted to $J$. Since $x$ lies in the interior of $J$, the derivative of $f$ on $J$ at $x$ is the ordinary two-sided derivative of $f$ at $x$.
17. So $f$ is differentiable at $x$, and $f'(x) = \sum_{n=1}^{\infty} n a_n (x - c)^{n-1}$.
18. Since $x \in (c - R, c + R)$ was arbitrary, $f$ is differentiable on $(c - R, c + R)$ with this derivative. By Part 1, the derived series has radius of convergence $R$.

## Idea

Multiplying the coefficients by $n$ does not change the radius of convergence, because $n$ grows more slowly than any geometric factor $\rho^n$ with $\rho > 1$. So the derived series converges uniformly on each $[c - r, c + r]$ with $r < R$. The theorem on term-by-term differentiation then applies around each point.
