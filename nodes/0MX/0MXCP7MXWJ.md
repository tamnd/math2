---
tag: 0MXCP7MXWJ
kind: problem
name: Coupon collector's problem
aliases: [coupon-collector-problem]
msc: [60C05]
uses: [0XCVV5Q500, 0P7PTC8DDE, 0DB0R4N5XX, 0V0778DCW9]
sources:
  - url: https://en.wikipedia.org/wiki/Coupon_collector's_problem
    locator: Calculating the expectation
  - url: https://en.wikipedia.org/wiki/Coupon_collector's_problem
    locator: Calculating the variance
same_as:
  wikidata: Q1148012
  wikipedia: Coupon collector's problem
history:
  posed_by: "Abraham de Moivre"
  first_stated: "1712"
---

## Problem

There are $n \ge 1$ different types of coupons. Each draw gives a coupon of a uniform random type, independently of the other draws.
Let $T$ be the number of draws needed to collect all $n$ types. Find $E[T]$.

## Remarks

Solution: write $T = t_1 + \dots + t_n$, where $t_i$ is the number of draws to get a new type when $i - 1$ types are known.
Each $t_i$ counts trials up to the first success, with success probability $p_i = (n - i + 1)/n$. So $E[t_i] = 1/p_i$ by the [[mean of the geometric distribution|0DB0R4N5XX]].
By [[linearity of expectation|0P7PTC8DDE]], $E[T] = n \left(\frac{1}{1} + \frac{1}{2} + \dots + \frac{1}{n}\right) = n H_n$, where $H_n$ is the $n$-th harmonic number. So $E[T] = n \ln n + \gamma n + \frac{1}{2} + o(1)$, with the Euler–Mascheroni constant $\gamma \approx 0.5772$.
The $t_i$ are independent, so $\operatorname{Var}(T) = \sum_i (1 - p_i)/p_i^2 < \pi^2 n^2 / 6$.

## Explanations

### L1 human

To collect all $n$ pictures of a series, you need about $n \ln n$ purchases, not $n$.
The last pictures are the slow ones: when only one type is missing, you wait on average $n$ draws for it. For $n = 50$, $E[T] = 50 H_{50} \approx 225$.
