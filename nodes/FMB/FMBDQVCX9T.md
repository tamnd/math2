---
tag: FMBDQVCX9T
kind: proof
name: Proof that moments are derivatives of the moment-generating function at zero
msc: ["60E10"]
proves: 0STK8KEY9G
uses: [0NNRNGKMFM, 0PH0VHTQS0, 0DCT0QZVQ1, 0P7PTC8DDE, 06JZGMYTYD, 0VP56B4EMX, 0660QX1VPR, 002X7EK91H]
sources:
  - url: https://en.wikipedia.org/wiki/Moment-generating_function
    locator: Calculations of moments
---

## Proof

We expand $e^{tX}$ in the exponential series, bound the tail, and then differentiate the resulting power series.

1. Let $X$ be a real random variable and let $h > 0$ with $M_X(t) = E[e^{tX}] < \infty$ for all $t \in (-h, h)$. Here $M_X$ is the [[moment-generating function|0NNRNGKMFM]].
2. We use two properties of the [[expected value|0DCT0QZVQ1]]. If $0 \le U \le W$ then $E[U] \le E[W]$. If $Y$ is integrable then $\abs{E[Y]} \le E[\abs{Y}]$.
3. Let $0 \le s < h$. One of $e^{sX}$ and $e^{-sX}$ equals $e^{s\abs{X}}$, and the other is positive. So $e^{s\abs{X}} \le e^{sX} + e^{-sX}$.
4. By steps 2 and 3, $E[e^{s\abs{X}}] \le M_X(s) + M_X(-s) < \infty$.
5. Fix $k \ge 0$ and $s \in (0, h)$. By the [[exponential series|06JZGMYTYD]], whose terms are nonnegative for a nonnegative argument, $e^{s\abs{x}} \ge (s\abs{x})^k / k!$.
6. So $\abs{X}^k \le k! \, s^{-k} e^{s\abs{X}}$. By steps 2 and 4, $E[\abs{X}^k] < \infty$. Thus $X$ has finite [[moments|0PH0VHTQS0]] of all orders.
7. Fix $t$ with $\abs{t} < h$. Choose $s$ with $\abs{t} < s < h$, and let $r = \abs{t}/s \in [0, 1)$.
8. For $N \ge 0$ and real $y$, let $P_N(y) = \sum_{k=0}^{N} y^k / k!$. By the exponential series, $\abs{e^y - P_N(y)} \le \sum_{k > N} \abs{y}^k / k!$.
9. For $k \ge N + 1$, $\abs{tX}^k = r^k \abs{sX}^k \le r^{N+1} \abs{sX}^k$, since $r < 1$.
10. By steps 8 and 9, $\abs{e^{tX} - P_N(tX)} \le r^{N+1} \sum_{k > N} \abs{sX}^k / k! \le r^{N+1} e^{s\abs{X}}$.
11. By step 6 and [[linearity of expectation|0P7PTC8DDE]], $P_N(tX)$ is integrable and $E[P_N(tX)] = \sum_{k=0}^{N} E[X^k] \, t^k / k!$.
12. The variable $e^{tX}$ is integrable, since $M_X(t) < \infty$. By steps 2, 10 and 11,
$$\abs{M_X(t) - \sum_{k=0}^{N} \frac{E[X^k]}{k!} t^k} \le r^{N+1} E[e^{s\abs{X}}].$$
13. By step 4, the right side is a finite constant times $r^{N+1}$, which tends to $0$ as $N \to \infty$.
14. So $M_X(t) = \sum_{k=0}^{\infty} E[X^k] \, t^k / k!$ for every $t \in (-h, h)$.
15. Let $a_k = E[X^k]/k!$. The [[power series|0VP56B4EMX]] $\sum a_k t^k$ converges at each $t \in (-h, h)$. So its terms $a_k t^k$ are bounded for each such $t$.
16. By the definition of the [[radius of convergence|0660QX1VPR]], the radius of $\sum a_k t^k$ is at least $\abs{t}$ for each $t \in (-h, h)$. So it is at least $h$.
17. [[Power series are differentiable inside the radius of convergence|002X7EK91H]], and the derived series has the same radius. By induction on $j$, $M_X$ is $j$ times differentiable on $(-h, h)$ for each $j$.
18. The same induction gives, for $\abs{t} < h$,
$$M_X^{(j)}(t) = \sum_{k=j}^{\infty} \frac{k!}{(k - j)!} \, a_k t^{k-j}.$$
19. At $t = 0$, only the term $k = j$ survives. So $M_X^{(j)}(0) = j! \, a_j = E[X^j]$ for each integer $j \ge 0$.
20. Together with step 6 and step 14, this proves all claims.

## Idea

Near $0$ the variable $e^{s\abs{X}}$ is integrable, and it dominates every power $\abs{X}^k$ and every tail of the series of $e^{tX}$ for $\abs{t} < s$. So the expectation can be taken term by term. Then $M_X$ is a power series with coefficients $E[X^k]/k!$, and its derivatives at $0$ read off these coefficients.
