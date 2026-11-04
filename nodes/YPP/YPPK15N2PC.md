---
tag: YPPK15N2PC
kind: proof
name: Proof that pi is greater than 3 by the alternating series estimate
msc: [11Y60]
proves: 0R7SVNYTJS
uses: [0C1VYVNV2N, 0WB57D9488, 08W5RN375X, 0RAM4E07NR, 0VVY4H92G2, 0PK8QH1W1V, 0MH1WK89PP, 07J5X2T1ZX]
sources:
  - url: https://en.wikipedia.org/wiki/Alternating_series_test
    locator: Alternating series estimation theorem
---

## Proof

We show that $\cos x > 0$ for $0 \le x \le 3/2$. Then the zero $\pi/2$ of $\cos$ must lie beyond $3/2$.

1. Let $0 < x \le 3/2$, and let $u = x^2$. Then $0 < u \le 9/4$.
2. By the [[definition of cosine|0WB57D9488]], $\cos x = \sum_{n=0}^{\infty} v_n$ with $v_n = \frac{(-1)^n x^{2n}}{(2n)!}$. The series converges by the [[power series of cosine|08W5RN375X]].
3. The partial sums of the tail $\sum_{n \ge 2} v_n$ are those of $\sum v_n$ minus $v_0 + v_1$. By the [[limit of a sum|0RAM4E07NR]], the tail converges and $\cos x = 1 - \frac{u}{2} + T$, where $T = \sum_{n \ge 2} v_n$.
4. Write $T = \sum_{k=0}^{\infty} (-1)^k c_k$ with $c_k = \frac{x^{2k+4}}{(2k+4)!} > 0$. Here $c_k = \abs{v_{k+2}}$ and $(-1)^{k+2} = (-1)^k$.
5. We have $\frac{c_{k+1}}{c_k} = \frac{u}{(2k+5)(2k+6)} \le \frac{9/4}{30} < 1$. So $(c_k)$ is decreasing.
6. Since $\sum v_n$ converges, the [[term test|0VVY4H92G2]] gives $v_n \to 0$. So $c_k \to 0$.
7. By the [[alternating series test|0PK8QH1W1V]] with $N = 0$, $\abs{T - c_0} \le c_1$. So $T \ge c_0 - c_1 = \frac{u^2}{24} - \frac{u^3}{720}$.
8. By steps 3 and 7, $\cos x \ge p(u)$, where $p(u) = 1 - \frac{u}{2} + \frac{u^2}{24} - \frac{u^3}{720}$.
9. By the [[derivative of a polynomial|0MH1WK89PP]], $p'(u) = -\frac{1}{2} + \frac{u}{12} - \frac{u^2}{240}$. For $0 \le u \le 9/4$ this is at most $-\frac{1}{2} + \frac{3}{16} < 0$.
10. So $-p$ has positive derivative on $[0, 9/4]$. By [[this result|07J5X2T1ZX]], $-p$ is strictly increasing there, so $p$ is strictly decreasing.
11. Hence $p(u) \ge p(9/4)$. Over the common denominator $46080$, $p(9/4) = \frac{46080 - 51840 + 9720 - 729}{46080} = \frac{3231}{46080} > 0$.
12. So $\cos x > 0$ for $0 < x \le 3/2$. Also $\cos 0 = 1 > 0$, since only the first term of the series is nonzero at $0$.
13. By the [[definition of $\pi$|0C1VYVNV2N]], $\cos(\pi/2) = 0$ and $\pi/2 \in [0, 2]$. By step 12, $\pi/2 \notin [0, 3/2]$.
14. So $\pi/2 > 3/2$, that is, $\pi > 3$.

## Idea

The cosine series alternates, and from the term $x^4/4!$ on its terms decrease when $x \le 3/2$. So cutting the series after $x^6/6!$ gives a lower bound for $\cos x$. This lower bound stays positive up to $x = 3/2$, so the first zero $\pi/2$ of cosine comes later.
