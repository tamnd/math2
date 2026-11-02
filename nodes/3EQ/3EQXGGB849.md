---
tag: 3EQXGGB849
kind: definition
name: Baskakov operator
msc: [41A36, 41A35, 41A25]
defines: VXQ1Y50KTJ
uses: [AQDXWH4812, 092GEF38YD]
sources:
  - url: https://en.wikipedia.org/wiki/Baskakov_operator
---

## Definition

Let $f \colon [0, \infty) \to \R$ satisfy $\abs{f(t)} \le C (1 + t)^m$ for some constants $C \ge 0$, $m \ge 0$ and all $t \ge 0$.
For an integer $n \ge 1$, the *Baskakov operator* $V_n$ maps $f$ to the function
$$V_n(f)(x) = \sum_{k=0}^{\infty} \binom{n + k - 1}{k} \frac{x^k}{(1 + x)^{n + k}} \, f\left(\frac{k}{n}\right), \qquad x \ge 0,$$
where $\binom{n + k - 1}{k}$ is a [[binomial coefficient|092GEF38YD]].

## Remarks

With $y = x/(1 + x)$, the weights are $\binom{n + k - 1}{k} y^k (1 - y)^n$, the negative binomial probabilities, so they are nonnegative and sum to $1$.
Hence $V_n$ is a [[positive linear operator|AQDXWH4812]] with $V_n(1) = 1$.

Example: the mean of these probabilities is $n y / (1 - y) = n x$, so $V_n(t)(x) = x$.
Their variance is $n x (1 + x)$, which gives $V_n(t^2)(x) = x^2 + \frac{x(1 + x)}{n}$.
By Korovkin's theorem, $V_n f \to f$ uniformly on each interval $[0, b]$ for every bounded continuous $f$.

Non-example: $f(t) = e^{t}$ is not in the domain: the terms grow like $k^{n-1} (x/(1 + x))^k e^{k/n}$, which diverges when $\frac{x}{1 + x} e^{1/n} \ge 1$.

Baskakov's general construction takes functions $\varphi_n$ and sets $L_n(f)(x) = \sum_{k \ge 0} \frac{(-x)^k \varphi_n^{(k)}(x)}{k!} f(k/n)$.
The choice $\varphi_n(x) = (1 + x)^{-n}$ gives $V_n$, $\varphi_n(x) = e^{-nx}$ gives the Szász–Mirakyan operator, and $\varphi_n(x) = (1 - x)^n$ gives the Bernstein polynomials on $[0, 1]$.
