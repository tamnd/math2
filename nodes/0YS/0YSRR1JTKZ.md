---
tag: 0YSRR1JTKZ
kind: counterexample
name: x^n converges pointwise but not uniformly on [0, 1]
msc: [40A30]
uses: [056FSKG32J, 08FPABDQ4C, 0X9XT05JVC, 0MNM54WB99]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
    locator: Examples
---

## Counterexample

Let $f_n(x) = x^n$ on $[0, 1]$. Let $f(x) = 0$ for $0 \le x < 1$ and $f(1) = 1$.
For $0 \le x < 1$, $x^n \to 0$ by the [[geometric sequence limit|0MNM54WB99]]. So $f_n \to f$ [[pointwise|056FSKG32J]] on $[0, 1]$.
But $\sup_{0 \le x < 1} |x^n - 0| = 1$ for every $n$. So the convergence is not [[uniform|08FPABDQ4C]].

## Remarks

Each $f_n$ is continuous, but $f$ is not. This also shows the failure, by the [[uniform limit theorem|0X9XT05JVC]].
On $[0, r]$ with $0 < r < 1$, the convergence is uniform, since $\sup_{[0, r]} x^n = r^n \to 0$.

## Explanations

### L1 human

Near $x = 1$, the values $x^n$ stay close to $1$ for a long time before they drop to $0$.
So no single $n$ makes all the values small at once.
