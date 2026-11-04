---
tag: VQ7709JWXR
kind: proof
name: Proof that power series are holomorphic in the disc of convergence
msc: [30B10]
proves: 0YMP521ZR5
uses: [0VARVQ9ZW1, 045EWAXY9P, 0DG0Z72CQD, 0D1C9Y1EXA, 0QNY6ZBXPN, 04Z5G0THN6, 082MGNWNA8, 05APWSX53S, 0FJZMBX0ZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Power_series
    locator: Differentiation and integration
---

## Proof

We bound the error of the difference quotient by $\abs{h}$ times a convergent series.

1. Let $q \in [0, 1)$. The series $\sum_{n \ge 1} n q^{n-1}$ and $\sum_{n \ge 2} n (n-1) q^{n-2}$ converge. For $q = 0$ this is clear. For $q > 0$ the ratio of consecutive terms tends to $q < 1$, so the [[ratio test|0QNY6ZBXPN]] applies.
2. Let $0 \le s < R$, where $R$ is the [[radius of convergence|045EWAXY9P]]. Choose $t$ with $s < t < R$. Since $R$ is a supremum, some $t' > t$ has $(\abs{a_n} t'^n)$ bounded, say by $M$. Then $\abs{a_n} t^n \le M$ for all $n$.
3. Then $\abs{a_n} s^n \le M (s/t)^n$, $\ n \abs{a_n} s^{n-1} \le \frac{M}{t} n (s/t)^{n-1}$ and $n(n-1) \abs{a_n} s^{n-2} \le \frac{M}{t^2} n(n-1) (s/t)^{n-2}$.
4. By step 1 with $q = s/t$ and the [[comparison test|04Z5G0THN6]], the series $\sum \abs{a_n} s^n$, $\sum n \abs{a_n} s^{n-1}$ and $\sum n(n-1) \abs{a_n} s^{n-2}$ converge.
5. Let $z \in D$, and take $s = \abs{z - c}$ in step 4. The series $\sum a_n (z - c)^n$ and $\sum n a_n (z - c)^{n-1}$ converge absolutely. Since $\C$ is complete, [[they converge|082MGNWNA8]]. Put $g(z) = \sum_{n \ge 1} n a_n (z - c)^{n-1}$.
6. The series for $g$ is the [[power series|0VARVQ9ZW1]] $\sum_{m \ge 0} b_m (z - c)^m$ with $b_m = (m+1) a_{m+1}$. Let $R'$ be its radius of convergence.
7. If $0 < s < R$, the terms $\abs{b_m} s^m = (m+1) \abs{a_{m+1}} s^m$ are bounded, since their series converges by step 4. So $R' \ge R$.
8. If $s > 0$ and $\abs{b_m} s^m \le K$ for all $m$, then $\abs{a_{m+1}} s^{m+1} \le (m+1) \abs{a_{m+1}} s^{m+1} \le K s$ for all $m$. So $(\abs{a_n} s^n)$ is bounded and $s \le R$. Hence $R' \le R$, and $R' = R$.
9. Let $A, B \in \C$ and $n \ge 1$. Expanding the product and cancelling gives $A^n - B^n = (A - B) \sum_{k=0}^{n-1} A^k B^{n-1-k}$, as for the [[finite geometric sum|05APWSX53S]].
10. Assume $\abs{A}, \abs{B} \le s$. By step 9 and the [[triangle inequality|0FJZMBX0ZZ]], $\abs{A^k - B^k} \le k s^{k-1} \abs{A - B}$ for each $k \ge 1$. This also holds for $k = 0$.
11. Assume moreover $A \ne B$ and $n \ge 1$. By step 9, $\frac{A^n - B^n}{A - B} - n B^{n-1} = \sum_{k=0}^{n-1} (A^k - B^k) B^{n-1-k}$.
12. By step 10, the modulus of this sum is at most $\sum_{k=0}^{n-1} k s^{k-1} \abs{A - B} s^{n-1-k} = \frac{n(n-1)}{2} s^{n-2} \abs{A - B}$. For $n = 1$ the sum is $0$.
13. Fix $z \in D$ and choose $s$ with $\abs{z - c} < s < R$. Let $h \ne 0$ with $\abs{h} < s - \abs{z - c}$. Put $B = z - c$ and $A = z + h - c$. Then $\abs{A}, \abs{B} < s$, $A - B = h$, and $z + h \in D$.
14. Subtracting the convergent series termwise, $\frac{f(z + h) - f(z)}{h} - g(z) = \sum_{n \ge 1} a_n \left( \frac{A^n - B^n}{h} - n B^{n-1} \right)$.
15. By step 12, the modulus of this is at most $\frac{\abs{h}}{2} \sum_{n \ge 2} n (n-1) \abs{a_n} s^{n-2} = \frac{C \abs{h}}{2}$, where $C$ is finite by step 4.
16. So the difference quotient tends to $g(z)$ as $h \to 0$. Thus $f$ is [[complex differentiable|0D1C9Y1EXA]] at $z$ with $f'(z) = \sum_{n=1}^{\infty} n a_n (z - c)^{n-1}$.
17. This holds for each $z$ in the open disc $D$. So $f$ is [[holomorphic|0DG0Z72CQD]] on $D$, and by step 8 the series for $f'$ has radius $R$.

## Idea

Inside the disc we can compare with a geometric series, which makes even the series with extra factors $n$ and $n(n-1)$ converge. The error in the difference quotient of $z^n$ is at most about $n^2 s^{n-2} \abs{h}$, so the total error is a constant times $\abs{h}$.
