---
tag: ENV6YZEMXB
kind: proof
name: Proof that the solutions of Pell's equation are powers of the fundamental solution
msc: [11D09]
proves: 0J1TT091TN
uses: [0AF3DANJ76, 0KCYJSB9FW, 0N10YRNNWV, 0A3GWZ86AY]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/ugradnumthy/pelleqn1.pdf
    locator: Theorem 5.3
---

## Proof

Let $\mathbb{Z}[\sqrt{d}] = \set{a + b\sqrt{d} : a, b \in \Z}$.

1. Since $d$ is not a perfect square, $\sqrt{d}$ is irrational by [[the irrationality of square roots of non-squares|0N10YRNNWV]]. So $a + b\sqrt{d} = a' + b'\sqrt{d}$ with integers $a, b, a', b'$ implies $a = a'$ and $b = b'$.
2. For $\gamma = a + b\sqrt{d}$ in $\mathbb{Z}[\sqrt{d}]$, put $\bar\gamma = a - b\sqrt{d}$ and $N(\gamma) = \gamma \bar\gamma = a^2 - d b^2$. By step 1 these are well defined.
3. The set $\mathbb{Z}[\sqrt{d}]$ is closed under products. For $\gamma = a + b\sqrt{d}$ and $\delta = c + e\sqrt{d}$, $\gamma\delta = (ac + dbe) + (ae + bc)\sqrt{d}$ and $\bar\gamma \bar\delta = (ac + dbe) - (ae + bc)\sqrt{d}$. So $\overline{\gamma\delta} = \bar\gamma \bar\delta$ and $N(\gamma\delta) = N(\gamma) N(\delta)$.
4. So a pair $(a, b)$ of integers solves [[Pell's equation|0AF3DANJ76]] exactly when $N(a + b\sqrt{d}) = 1$, and products of such numbers again have norm $1$.
5. Lemma 1: if $N(\eta) = 1$ and $\eta = a + b\sqrt{d} > 1$, then $a > 1$ and $b \ge 1$. Indeed $\bar\eta = 1/\eta \in (0, 1)$. So $a = (\eta + \bar\eta)/2 > 0$ and $b\sqrt{d} = (\eta - \bar\eta)/2 > 0$. Then $b \ge 1$ and $a^2 = 1 + db^2 > 1$, so $a > 1$.
6. Lemma 2: let $(a, b)$ and $(c, e)$ be solutions with $a, b, c, e \ge 1$ and $a < c$. Then $b < e$, because $d b^2 = a^2 - 1 < c^2 - 1 = d e^2$. Hence $a + b\sqrt{d} < c + e\sqrt{d}$.
7. Let $\varepsilon = x_1 + y_1\sqrt{d}$. By the definition of the [[fundamental solution|0KCYJSB9FW]], $x_1 > 1$ and $y_1 > 0$, so $\varepsilon > 1$, and $N(\varepsilon) = 1$.
8. By step 3, $\bar\varepsilon = x_1 - y_1\sqrt{d}$ lies in $\mathbb{Z}[\sqrt{d}]$ and $\varepsilon \bar\varepsilon = 1$. So $\varepsilon^{-n} = \bar\varepsilon^{\,n}$ lies in $\mathbb{Z}[\sqrt{d}]$ and has norm $1$ for each $n \ge 0$.
9. Let $\xi = x + y\sqrt{d}$. Since $x \ge 1$ and $y \ge 0$, we have $\xi \ge 1$.
10. Since $\varepsilon > 1$, the powers $\varepsilon^0 = 1 < \varepsilon < \varepsilon^2 < \cdots$ increase. By induction on $n$, $\varepsilon^n \ge 1 + n(\varepsilon - 1)$. By the [[Archimedean property|0A3GWZ86AY]], the powers $\varepsilon^n$ are unbounded.
11. So there is a largest natural number $n$ with $\varepsilon^n \le \xi$, and for it $\varepsilon^n \le \xi < \varepsilon^{n+1}$.
12. Put $\zeta = \xi \varepsilon^{-n} = \xi \bar\varepsilon^{\,n}$. By steps 3 and 8, $\zeta = a + b\sqrt{d}$ with integers $a$, $b$, and $N(\zeta) = 1$.
13. Dividing step 11 by $\varepsilon^n > 0$ gives $1 \le \zeta < \varepsilon$.
14. Suppose $\zeta > 1$. By Lemma 1, $a > 1$ and $b \ge 1$, so $(a, b)$ is a solution with $a > 1$ and $b > 0$. By the minimality of $x_1$, $a \ge x_1$.
15. If $a = x_1$, then $d b^2 = a^2 - 1 = d y_1^2$, so $b = y_1$ and $\zeta = \varepsilon$. If $a > x_1$, then $\zeta > \varepsilon$ by Lemma 2. Both contradict step 13.
16. So $\zeta = 1$, that is, $x + y\sqrt{d} = \varepsilon^n = (x_1 + y_1\sqrt{d})^n$.
17. Uniqueness: if also $\xi = \varepsilon^m$ with $m \ge 0$, then $\varepsilon^m = \varepsilon^n$. Since the powers of $\varepsilon$ strictly increase, $m = n$.

## Idea

Solutions of Pell's equation are the numbers $a + b\sqrt{d}$ of norm $1$, and these are closed under products and inverses.
Divide a given solution by the largest power of $\varepsilon = x_1 + y_1\sqrt{d}$ below it.
The quotient is a solution between $1$ and $\varepsilon$, and no solution other than $1$ lies there, because $\varepsilon$ is the smallest solution above $1$.
