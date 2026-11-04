---
tag: HE1M4NDE1J
kind: proof
name: Proof of Cauchy's integral formula for derivatives
msc: ["30E20"]
proves: 0F0H5P5DED
uses: [0DG0Z72CQD, 0DG10TVYPN, 0QEBN8DGVE, 0T7ABX4CWE, 05APWSX53S, 07PFYV65MB, 0V4DET59NW, 0DJMGPN8K9, 0Q7K4AXE53, 0YMP521ZR5, 045EWAXY9P, 0FJZMBX0ZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Analyticity_of_holomorphic_functions
    locator: Proof
---

## Proof

We expand $f$ in a power series around $a$ using the circle $\abs{z - c} = r$, and read off the derivatives.

1. Put $\delta = r - \abs{a - c} > 0$ and $D_a = \set{w : \abs{w - a} < \delta}$. For $w \in D_a$, $\abs{w - c} \le \abs{w - a} + \abs{a - c} < r$ by the [[triangle inequality|0FJZMBX0ZZ]].
2. For $w \in D_a$, [[Cauchy's integral formula|0DG10TVYPN]] gives $f(w) = \frac{1}{2 \pi i} \oint_{\abs{z - c} = r} \frac{f(z)}{z - w} \, dz$, a [[circle integral|0T7ABX4CWE]].
3. For $z$ on the circle, $\abs{z - a} \ge \abs{z - c} - \abs{a - c} = \delta$. Put $u = (w - a)/(z - a)$. Then $\abs{u} \le q$, where $q = \abs{w - a}/\delta < 1$.
4. Since $z - w = (z - a)(1 - u)$, the [[finite geometric sum|05APWSX53S]] gives $\frac{f(z)}{z - w} = \sum_{n=0}^{N} \frac{f(z)}{(z - a)^{n+1}} (w - a)^n + T_N(z)$, with $T_N(z) = \frac{f(z) \, u^{N+1}}{(z - a)(1 - u)}$.
5. The circle is [[compact|07PFYV65MB]], so $\abs{f} \le M$ on it for some $M$, by the [[extreme value theorem|0V4DET59NW]]. Since $\abs{1 - u} \ge 1 - q$, we get $\abs{T_N(z)} \le \frac{M q^{N+1}}{\delta (1 - q)}$.
6. Put $b_n = \frac{1}{2 \pi i} \oint_{\abs{z - c} = r} \frac{f(z)}{(z - a)^{n+1}} \, dz$. Integrating step 4 and using the [[estimation lemma|0DJMGPN8K9]] with length $2 \pi r$, we get $\abs{f(w) - \sum_{n=0}^{N} b_n (w - a)^n} \le \frac{r M q^{N+1}}{\delta (1 - q)}$.
7. Since [[powers of $q$ tend to zero|0Q7K4AXE53]], $f(w) = \sum_{n=0}^{\infty} b_n (w - a)^n$ for every $w \in D_a$.
8. For $0 < s < \delta$ the series converges at $w = a + s$, so $(\abs{b_n} s^n)$ is bounded. So its [[radius of convergence|045EWAXY9P]] is at least $\delta$. Let $S$ be its sum on $D_a$.
9. Since [[power series are holomorphic in the disc of convergence|0YMP521ZR5]], $S'$ is again a power series on $D_a$ with the same radius. By induction on $k$, $S^{(k)}(w) = \sum_{n \ge k} n (n-1) \cdots (n - k + 1) b_n (w - a)^{n-k}$ on $D_a$.
10. At $w = a$, only the term $n = k$ survives. So $S^{(k)}(a) = k! \, b_k$.
11. The derivatives $f^{(k)}$ exist on $U$, since [[holomorphic functions are infinitely differentiable|0QEBN8DGVE]]. We show $f^{(k)} = S^{(k)}$ on $D_a$ by induction. For $k = 0$ this is step 7.
12. If $f^{(k)} = S^{(k)}$ on the open set $D_a$, then for $w \in D_a$ the difference quotients of both at $w$ agree for small $h$. So $f^{(k+1)}(w) = S^{(k+1)}(w)$.
13. By steps 10 and 12, $f^{(n)}(a) = n! \, b_n = \frac{n!}{2 \pi i} \oint_{\abs{z - c} = r} \frac{f(z)}{(z - a)^{n+1}} \, dz$.

## Idea

The circle $\abs{z - c} = r$ stays at distance at least $\delta$ from $a$. So the Cauchy kernel $1/(z - w)$ can be expanded in powers of $w - a$ for $w$ near $a$. This writes $f$ as a power series around $a$, and the $n$-th coefficient of a power series is the $n$-th derivative divided by $n!$.
