---
tag: X1CJK3QWTG
kind: proof
name: Proof of the weak law of large numbers by characteristic functions
msc: [60F05]
proves: 0BFDHF2H7N
uses: [0AJN7WHBJZ, 0MYDNRT7PP, 02JGYG0T7M, 0FPWF7TTMB, 0T8BYAFEXX, 0JDAQHWA9N, 0EFDDXTVD6, 0MXMS3AE13, BYNV84PF86, 0NHGY0N0JB, 0WM7DJCM6G, 0P7PTC8DDE]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_large_numbers
    locator: Proof using convergence of characteristic functions
---

## Proof

We show that the characteristic function of $\bar{X}_n$ tends to that of the constant $\mu$. Then we use Lévy's continuity theorem.

1. Let $\varphi(t) = E[e^{itX_1}]$ be the [[characteristic function|0MYDNRT7PP]] of $X_1$. The $X_i$ are [[i.i.d.|0AJN7WHBJZ]], so each $X_i$ has the characteristic function $\varphi$, because it depends only on the law.
2. Claim: $\abs{e^{ix} - 1} \le \abs{x}$ for real $x$. By the [[fundamental theorem of calculus|0NHGY0N0JB]], applied to the real and imaginary parts, $e^{ix} - 1 = \int_0^x i e^{iu} \, du$. The integrand has modulus $1$.
3. Claim: $\abs{e^{ix} - 1 - ix} \le \min(x^2/2, \, 2\abs{x})$ for real $x$. In the same way, $e^{ix} - 1 - ix = \int_0^x i (e^{iu} - 1) \, du$, and by step 2 its modulus is at most $\abs{\int_0^x \abs{u} \, du} = x^2/2$.
4. Also $\abs{e^{ix} - 1 - ix} \le \abs{e^{ix} - 1} + \abs{x} \le 2\abs{x}$, by step 2. This proves the claim.
5. For $s \ne 0$, let $r(s) = E\left[\min\left(\abs{s} X_1^2/2, \, 2\abs{X_1}\right)\right]$. By [[linearity of expectation|0P7PTC8DDE]] and step 3 with $x = sX_1$, $\abs{\varphi(s) - 1 - i\mu s} \le E\abs{e^{isX_1} - 1 - isX_1} \le \abs{s} \, r(s)$.
6. Claim: $r(s) \to 0$ as $s \to 0$. Let $s_j \to 0$. The integrand tends to $0$ at each $\omega$, since it is at most $\abs{s_j} X_1^2/2$. It is bounded by $2\abs{X_1}$, which is integrable.
7. By [[dominated convergence|BYNV84PF86]], $r(s_j) \to 0$. Since the sequence $s_j$ was arbitrary, the claim holds.
8. By step 3 with $x = \mu s$, $\abs{e^{i\mu s} - 1 - i\mu s} \le \mu^2 s^2/2$. With step 5, $\abs{\varphi(s) - e^{i\mu s}} \le \abs{s} \, r(s) + \mu^2 s^2/2$.
9. Claim: for complex $z, w$ with $\abs{z} \le 1$ and $\abs{w} \le 1$, $\abs{z^n - w^n} \le n \abs{z - w}$. Indeed $z^n - w^n = (z - w) \sum_{k=0}^{n-1} z^k w^{n-1-k}$, and each of the $n$ terms has modulus at most $1$.
10. Let $S_n = X_1 + \dots + X_n$, so $\bar{X}_n = S_n/n$. By the definition, $\varphi_{\bar{X}_n}(t) = E[e^{i(t/n) S_n}] = \varphi_{S_n}(t/n)$.
11. By the [[characteristic function of a sum of independent random variables|02JGYG0T7M]] and step 1, $\varphi_{\bar{X}_n}(t) = \varphi(t/n)^n$.
12. Fix $t \ne 0$. By the [[product of exponentials|0WM7DJCM6G]], $e^{i\mu t} = (e^{i\mu t/n})^n$. Also $\abs{\varphi(t/n)} \le 1$ and $\abs{e^{i\mu t/n}} = 1$.
13. Steps 9, 11, 12 and 8 give $\abs{\varphi_{\bar{X}_n}(t) - e^{i\mu t}} \le n \abs{\varphi(t/n) - e^{i\mu t/n}} \le \abs{t} \, r(t/n) + \mu^2 t^2/(2n)$.
14. By step 7, the right side tends to $0$. So $\varphi_{\bar{X}_n}(t) \to \psi(t) = e^{i\mu t}$. This also holds for $t = 0$, where both sides equal $1$.
15. The function $\psi$ is continuous at $0$. By [[Lévy's continuity theorem|0FPWF7TTMB]], $\psi$ is the characteristic function of a random variable $Y$, and $\bar{X}_n \to Y$ [[in distribution|0JDAQHWA9N]].
16. The constant random variable $\mu$ has the characteristic function $E[e^{it\mu}] = e^{i\mu t} = \psi(t)$. Since [[the characteristic function determines the distribution|0T8BYAFEXX]], $P(Y = \mu) = 1$.
17. So the [[cumulative distribution function|0MXMS3AE13]] $F_Y$ is $0$ on $(-\infty, \mu)$ and $1$ on $[\mu, \infty)$. It is continuous at every $x \ne \mu$.
18. Let $F_n$ be the cumulative distribution function of $\bar{X}_n$, and fix $\varepsilon > 0$. By step 17, $F_n(\mu - \varepsilon) \to 0$ and $F_n(\mu + \varepsilon) \to 1$.
19. The event $\set{\abs{\bar{X}_n - \mu} > \varepsilon}$ is contained in $\set{\bar{X}_n \le \mu - \varepsilon} \cup \set{\bar{X}_n > \mu + \varepsilon}$. So $P(\abs{\bar{X}_n - \mu} > \varepsilon) \le F_n(\mu - \varepsilon) + 1 - F_n(\mu + \varepsilon)$.
20. By step 18, the right side tends to $0$. Hence $\bar{X}_n \to \mu$ [[in probability|0EFDDXTVD6]].

## Idea

A finite mean gives the first-order expansion $\varphi(s) = 1 + i\mu s + o(s)$. Raising $\varphi(t/n)$ to the power $n$ then gives $e^{i\mu t}$, the characteristic function of the constant $\mu$. Convergence in distribution to a constant is the same as convergence in probability.
