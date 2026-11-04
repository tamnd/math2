---
tag: QNWCC0BB5M
kind: proof
name: Proof of the derivative of sine by term-by-term differentiation
msc: [33B10, 26A24]
proves: 00R4MWW532
uses: [0WB57D9488, 0QNY6ZBXPN, 0VVY4H92G2, 0S4JF619V7, 0660QX1VPR, 002X7EK91H, 0WFCGVMRRC]
sources:
  - url: https://proofwiki.org/wiki/Derivative_of_Sine_Function
    locator: Proof 1
---

## Proof

1. By the [[definition of sine|0WB57D9488]], $\sin x = \sum_{m=0}^{\infty} c_m x^m$, where $c_{2n+1} = \frac{(-1)^n}{(2n+1)!}$ and $c_{2n} = 0$ for $n \ge 0$. Here $k!$ is the [[factorial|0WFCGVMRRC]].
2. Let $r > 0$, and let $t_n = \frac{r^{2n+1}}{(2n+1)!} > 0$. Then $\frac{t_{n+1}}{t_n} = \frac{r^2}{(2n+2)(2n+3)} \to 0$.
3. By the [[ratio test|0QNY6ZBXPN]], $\sum_n t_n$ converges. The series $\sum_m \abs{c_m} r^m$ is this series with zero terms inserted, so it converges too.
4. By the [[term test|0VVY4H92G2]], $\abs{c_m} r^m \to 0$. So the sequence $(\abs{c_m} r^m)$ is [[bounded|0S4JF619V7]].
5. This holds for every $r > 0$. By the [[definition of the radius of convergence|0660QX1VPR]], the radius of convergence of the sine series is $\infty$.
6. By [[term-by-term differentiation|002X7EK91H]], $\sin$ is differentiable on $\mathbb{R}$, and $\sin'(x) = \sum_{m=1}^{\infty} m c_m x^{m-1}$.
7. The terms with even $m$ vanish. For $m = 2n + 1$ the term is $(2n+1) \frac{(-1)^n}{(2n+1)!} x^{2n} = \frac{(-1)^n x^{2n}}{(2n)!}$.
8. Removing the zero terms does not change the sum. So $\sin'(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$.
9. By the definition of cosine, this sum is $\cos x$. So $\sin'(x) = \cos x$ for every real $x$.

## Idea

Sine is defined by a power series that converges everywhere, and such a series can be differentiated term by term. Differentiating $\frac{x^{2n+1}}{(2n+1)!}$ gives $\frac{x^{2n}}{(2n)!}$, so each term of the sine series becomes the matching term of the cosine series.
