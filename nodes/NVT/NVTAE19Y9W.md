---
tag: NVTAE19Y9W
kind: proof
name: Proof that an iterate of the Picard operator is a contraction
msc: [34A12, 47H10]
proves: 08XDXP86XE
uses: [00WAVB68F9, 0J7HF2PF1H, 055VVSN00V, 080RWVVSB6, 0MBWQKM8QR, 0RFWW56Y22, 0MT2S0ZX4Y]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Detailed proof
---

## Proof

We argue by induction on $m$, with a pointwise bound. Write $d = d(\gamma, \delta)$.

1. Lemma. Let $c \le e$, let $h : [c, e] \to \R^n$ be integrable, and let $\phi : [c, e] \to \R$ be integrable with $\norm{h(s)} \le \phi(s)$. Then $\norm{\int_c^e h(s)\, ds} \le \int_c^e \phi(s)\, ds$.
2. Proof of the lemma. Let $v = \int_c^e h(s)\, ds$ and assume $v \ne 0$. By [[linearity of the integral|080RWVVSB6]], $\norm{v}^2 = \sum_i v_i \int_c^e h_i = \int_c^e v \cdot h(s)\, ds$.
3. By the [[Cauchy–Schwarz inequality|0RFWW56Y22]], $v \cdot h(s) \le \norm{v} \norm{h(s)} \le \norm{v} \phi(s)$. By [[monotonicity of the integral|0MBWQKM8QR]], $\norm{v}^2 \le \norm{v} \int_c^e \phi$. Dividing by $\norm{v}$ proves the lemma.
4. Claim: for each $m \ge 0$ and each $t \in J$, $\norm{(P^m \gamma)(t) - (P^m \delta)(t)} \le \frac{(K \abs{t - t_0})^m}{m!}\, d$.
5. For $m = 0$, $P^0$ is the identity, and $\norm{\gamma(t) - \delta(t)} \le d$ by the definition of $d$.
6. Assume the claim for $m$. Let $\gamma_m = P^m \gamma$ and $\delta_m = P^m \delta$. They lie in $X$, so their values lie in the ball $B$ of radius $a$ around $x_0$.
7. For $s \in J$, condition (1) of the [[Picard–Lindelöf hypotheses|0J7HF2PF1H]] says $f(s, \cdot)$ is $K$-[[Lipschitz|055VVSN00V]] on $B$. With the claim for $m$, $\norm{f(s, \gamma_m(s)) - f(s, \delta_m(s))} \le K \frac{(K \abs{s - t_0})^m}{m!}\, d$.
8. By the definition of the [[Picard operator|00WAVB68F9]], $(P^{m+1} \gamma)(t) - (P^{m+1} \delta)(t) = \int_{t_0}^{t} \left(f(s, \gamma_m(s)) - f(s, \delta_m(s))\right) ds$.
9. Let $t \ge t_0$. The lemma with the bound of step 7 gives the estimate $\int_{t_0}^{t} \frac{K^{m+1} (s - t_0)^m}{m!}\, d\, ds = \frac{(K (t - t_0))^{m+1}}{(m + 1)!}\, d$.
10. For $t < t_0$, the integral is $-\int_t^{t_0}$, and the same computation with $t_0 - s$ gives $\frac{(K (t_0 - t))^{m+1}}{(m+1)!}\, d$. This proves the claim for $m + 1$.
11. Each $t \in J$ has $\abs{t - t_0} \le T$. Taking the supremum over $t$ in the claim gives $d(P^m \gamma, P^m \delta) \le \frac{(K T)^m}{m!}\, d(\gamma, \delta)$.
12. Let $q_m = (K T)^m / m!$. If $K T = 0$, then $q_1 = 0 < 1$.
13. Otherwise choose an integer $N \ge 2 K T$. For $m \ge N$, $q_{m+1} = q_m \frac{K T}{m + 1} \le q_m / 2$. So $q_{N + j} \le q_N / 2^j$, which is less than $1$ for large $j$.
14. In both cases there is $m \ge 1$ with $q_m < 1$. By step 11, $P^m$ is a [[contraction|0MT2S0ZX4Y]] of $X$ with constant $q_m$.

## Idea

Each application of $P$ integrates the previous error bound once more. Integrating $\abs{s - t_0}^m / m!$ produces $\abs{t - t_0}^{m+1}/(m+1)!$. The factorial eventually beats the power $(K T)^m$, so a high enough iterate shrinks distances.
