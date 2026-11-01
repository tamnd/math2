---
tag: VTZPSW07PQ
kind: definition
name: Empirical process
msc: [60F17, 62G30]
defines: XKFG1676CG
uses: [00MRN0FARV, 0H8H7ZTHW2, 0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Empirical_process
---

## Definition

Let $X_1, X_2, \dots$ be [[independent and identically distributed|00MRN0FARV]] real random variables with [[cumulative distribution function|0H8H7ZTHW2]] $F$.
For $n \ge 1$, the *empirical distribution function* is
$$F_n(x) = \frac{1}{n} \sum_{i=1}^{n} \mathbf{1}\{X_i \le x\}, \qquad x \in \R.$$
The *empirical process* is the [[stochastic process|0QH5ENKZM1]] indexed by $x \in \R$ given by
$$G_n(x) = \sqrt{n}\,\bigl(F_n(x) - F(x)\bigr).$$

## Remarks

For each fixed $x$, $n F_n(x)$ is binomial with parameters $n$ and $F(x)$.
So $E[G_n(x)] = 0$ and $\operatorname{Var}(G_n(x)) = F(x)(1 - F(x))$, and by the central limit theorem $G_n(x)$ converges in distribution to a normal law with these parameters.
For the uniform law on $[0, 1]$, [[Donsker's theorem|818832PMSV]] says that $G_n$ converges in distribution, as a random function, to a [[Brownian bridge|3MCVMBAGD1]].
A non-example: if $X_i = X_1$ for all $i$, the variables are not independent, $F_n(x) = \mathbf{1}\{X_1 \le x\}$ for all $n$, and $\sqrt{n}(F_n - F)$ does not have the behaviour above.
More generally, for a probability measure $P$ and a class $\mathcal{F}$ of functions, the empirical process indexed by $\mathcal{F}$ is $f \mapsto \sqrt{n}\bigl(\frac{1}{n}\sum_{i=1}^n f(X_i) - \int f \, dP\bigr)$; the case above takes the indicator functions $\mathbf{1}_{(-\infty, x]}$.
