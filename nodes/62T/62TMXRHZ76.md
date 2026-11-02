---
tag: 62TMXRHZ76
kind: statement
role: theorem
name: Pickands–Balkema–De Haan theorem
msc: [62G32, 60G70]
uses: [Y3Z99461HJ, 0MXMS3AE13, 0AJN7WHBJZ, 0JDAQHWA9N]
about: [Y3Z99461HJ]
sources:
  - url: https://en.wikipedia.org/wiki/Pickands%E2%80%93Balkema%E2%80%93De_Haan_theorem
same_as:
  wikidata: Q7190748
  wikipedia: Pickands–Balkema–De Haan theorem
---

## Statement

Let $F$ be a [[cumulative distribution function|0MXMS3AE13]] on $\R$ and let $x_F = \sup\set{x : F(x) < 1} \le \infty$ be its right endpoint.
For $u < x_F$, let $F_u$ be the excess distribution over the threshold $u$:
$$F_u(y) = \frac{F(u + y) - F(u)}{1 - F(u)}, \qquad 0 \le y < x_F - u,$$
the law of $X - u$ given $X > u$ when $X$ has distribution function $F$.
For $\xi \in \R$ and $\beta > 0$, let $G_{\xi, \beta}$ be the generalised Pareto distribution function
$$G_{\xi, \beta}(y) = 1 - \Big(1 + \frac{\xi y}{\beta}\Big)^{-1/\xi} \ (\xi \ne 0), \qquad G_{0, \beta}(y) = 1 - e^{-y/\beta},$$
for $y \ge 0$ if $\xi \ge 0$ and for $0 \le y \le -\beta/\xi$ if $\xi < 0$.
Say that $F$ is in the maximum domain of attraction of $H_\xi(x) = \exp\big(-(1 + \xi x)^{-1/\xi}\big)$ (with $H_0(x) = \exp(-e^{-x})$) if, for [[i.i.d.|0AJN7WHBJZ]] $X_1, X_2, \dots$ with distribution function $F$, there are $a_n > 0$ and $b_n \in \R$ such that $(\max_{i \le n} X_i - b_n)/a_n$ [[converges in distribution|0JDAQHWA9N]] to $H_\xi$.

Then the following holds for each $\xi \in \R$.
The function $F$ is in the maximum domain of attraction of $H_\xi$ if and only if there is a positive measurable function $\beta(u)$ with
$$\lim_{u \uparrow x_F} \ \sup_{0 \le y < x_F - u} \abs{F_u(y) - G_{\xi, \beta(u)}(y)} = 0.$$

## Remarks

Idea of the proof.
Membership in the domain of attraction of $H_\xi$ is equivalent to the existence of a positive function $a(u)$ with $\frac{1 - F(u + a(u) y)}{1 - F(u)} \to (1 + \xi y)^{-1/\xi}$ as $u \uparrow x_F$, for each admissible $y$.
The left side is $1 - F_u(a(u) y)$, so this is pointwise convergence of rescaled excess laws to $G_{\xi, 1}$, and $\beta(u) = a(u)$ works.
Uniformity in $y$ follows because the functions are monotone and the limit is continuous.

Examples.
For the exponential law $F(x) = 1 - e^{-x}$, $F_u(y) = 1 - e^{-y}$ for every $u$, so $\xi = 0$ and $\beta(u) = 1$ give equality.
For the [[Pareto law|5N3P64YHQR]] $1 - F(x) = x^{-\alpha}$ for $x \ge 1$, $F_u(y) = 1 - (1 + y/u)^{-\alpha} = G_{1/\alpha, \, u/\alpha}(y)$ for $u \ge 1$.
For the uniform law on $[0, 1]$, $F_u(y) = y/(1 - u) = G_{-1, \, 1 - u}(y)$.

The hypothesis is not automatic: some laws lie in no domain of attraction, for example the Poisson and geometric laws.
Their excesses over high thresholds have no generalised Pareto limit.

## Explanations

### L1 human

Pick a high threshold, such as a flood level, and look only at how far the observations exceed it.
The theorem says that, for most continuous distributions met in practice, these excesses follow approximately a generalised Pareto law once the threshold is high enough.
This family has just two parameters: a shape $\xi$, which says how heavy the tail is, and a scale.
So one can model rare extreme events without knowing the full distribution.

### L2 human

The theorem is the threshold counterpart of the [[Fisher–Tippett–Gnedenko theorem|Y3Z99461HJ]], which describes the limit laws of maxima.
The same shape parameter $\xi$ appears in both.
One has $\xi > 0$ for heavy, Pareto-like tails, $\xi = 0$ for light tails such as the normal and exponential laws, and $\xi < 0$ for laws with a finite right endpoint.
In practice it justifies the peaks-over-threshold method of extreme value statistics.
One fits $G_{\xi, \beta}$ to the excesses over a high threshold by maximum likelihood and uses the fit to estimate high quantiles and tail probabilities.
