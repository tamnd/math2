---
tag: S7A8YFGG8X
kind: statement
role: theorem
name: Hardy's inequality
msc: [26D15, 26D10]
uses: [0CVVKY7GY2]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy%27s_inequality
same_as:
  wikidata: Q944228
  wikipedia: Hardy's inequality
---

## Statement

Let $p > 1$ be a real number.

1. (Discrete form.) Let $a_1, a_2, \dots$ be nonnegative real numbers. Then
$$\sum_{n=1}^{\infty} \Big( \frac{a_1 + a_2 + \dots + a_n}{n} \Big)^{p} \le \Big( \frac{p}{p - 1} \Big)^{p} \sum_{n=1}^{\infty} a_n^{p}.$$
2. (Integral form.) Let $f \colon (0, \infty) \to [0, \infty)$ be a measurable function, and let $F(x) = \frac{1}{x} \int_0^x f(t) \, dt$ for $x > 0$. Then
$$\int_0^{\infty} F(x)^{p} \, dx \le \Big( \frac{p}{p - 1} \Big)^{p} \int_0^{\infty} f(x)^{p} \, dx.$$

Here the [[series|0CVVKY7GY2]] and integrals take values in $[0, \infty]$.

## Remarks

Proof idea for the integral form: substitute $t = s x$ to get $F(x) = \int_0^1 f(s x) \, ds$, an average of the dilates of $f$.
By Minkowski's integral inequality, the continuous form of the [[Minkowski inequality|N4QZS912MT]], $\norm{F}_p \le \int_0^1 \norm{f(s \, \cdot)}_p \, ds$.
Since $\norm{f(s \, \cdot)}_p = s^{-1/p} \norm{f}_p$ and $\int_0^1 s^{-1/p} \, ds = \frac{p}{p-1}$, the result follows.

The constant $\big(\frac{p}{p-1}\big)^p$ is the best possible in both forms.

The hypothesis $p > 1$ is needed.
For $p = 1$ and $f$ the indicator function of $(0, 1]$, one gets $F(x) = 1/x$ for $x > 1$, so the left side is infinite while the right side is $1$.

## Explanations

### L1 human

Take a sequence of nonnegative numbers and replace each term by the average of the terms up to it.
Hardy's inequality says the new sequence is not much larger than the old one, when size is measured by the sum of $p$-th powers.
The loss is at most the factor $\big(\frac{p}{p-1}\big)^p$, which is $4$ for $p = 2$.

### L2 human

In operator language, the averaging operator $f \mapsto F$ is bounded on the Lp space $L^p(0, \infty)$ for $1 < p < \infty$, with norm $\frac{p}{p-1}$.
It is a basic example of a bounded integral operator, and it is used in Sobolev-type estimates and in the theory of weighted inequalities.
Letting $p \to \infty$ after replacing $a_n$ by $a_n^{1/p}$ leads to [[Carleman's inequality|B54HPY6C5Z]].
