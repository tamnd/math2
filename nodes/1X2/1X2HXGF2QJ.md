---
tag: 1X2HXGF2QJ
kind: proof
name: Proof of the derivative of cosine by term-by-term differentiation
msc: [33B10, 26A24]
proves: 0V2DV29EGT
uses: [0WB57D9488, 0QNY6ZBXPN, 0VVY4H92G2, 0S4JF619V7, 0660QX1VPR, 002X7EK91H, 0WFCGVMRRC]
sources:
  - url: https://proofwiki.org/wiki/Derivative_of_Cosine_Function
---

## Proof

1. By the [[definition of cosine|0WB57D9488]], $\cos x = \sum_{m=0}^{\infty} d_m x^m$, where $d_{2n} = \frac{(-1)^n}{(2n)!}$ and $d_{2n+1} = 0$ for $n \ge 0$. Here $k!$ is the [[factorial|0WFCGVMRRC]].
2. Let $r > 0$, and let $t_n = \frac{r^{2n}}{(2n)!} > 0$. Then $\frac{t_{n+1}}{t_n} = \frac{r^2}{(2n+1)(2n+2)} \to 0$.
3. By the [[ratio test|0QNY6ZBXPN]], $\sum_n t_n$ converges. The series $\sum_m \abs{d_m} r^m$ is this series with zero terms inserted, so it converges too.
4. By the [[term test|0VVY4H92G2]], $\abs{d_m} r^m \to 0$. So the sequence $(\abs{d_m} r^m)$ is [[bounded|0S4JF619V7]].
5. This holds for every $r > 0$. By the [[definition of the radius of convergence|0660QX1VPR]], the radius of convergence of the cosine series is $\infty$.
6. By [[term-by-term differentiation|002X7EK91H]], $\cos$ is differentiable on $\mathbb{R}$, and $\cos'(x) = \sum_{m=1}^{\infty} m d_m x^{m-1}$.
7. The terms with odd $m$ vanish. For $m = 2n$ with $n \ge 1$, the term is $2n \frac{(-1)^n}{(2n)!} x^{2n-1} = \frac{(-1)^n x^{2n-1}}{(2n-1)!}$.
8. Put $k = n - 1 \ge 0$. The term becomes $-\frac{(-1)^k x^{2k+1}}{(2k+1)!}$.
9. Removing the zero terms does not change the sum. So $\cos'(x) = -\sum_{k=0}^{\infty} \frac{(-1)^k x^{2k+1}}{(2k+1)!}$.
10. By the definition of sine, this is $-\sin x$. So $\cos'(x) = -\sin x$ for every real $x$.

## Idea

Cosine is defined by a power series that converges everywhere, so it can be differentiated term by term. The constant term disappears, and each later term $\frac{(-1)^n x^{2n}}{(2n)!}$ turns into a term of the sine series with the opposite sign.
