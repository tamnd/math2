---
tag: KV0GW9K7JS
kind: statement
role: theorem
name: Denjoy–Carleman theorem
msc: ["26E10"]
uses: [YF1KAWB5MB, 0BE3QDH73A, 0JD5ZNW0F4, HS65DW0HXH]
about: [YF1KAWB5MB]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-analytic_function
    locator: The Denjoy–Carleman theorem
---

## Statement

Let $a < b$ and let $M = (M_k)_{k \ge 0}$ be a sequence of positive real numbers with $M_0 = 1$.
Assume that $M$ is logarithmically convex: $M_k^2 \le M_{k-1} M_{k+1}$ for all $k \ge 1$.
Let $C^M([a, b])$ be the class of smooth functions $f$ on $[a, b]$ with $\abs{f^{(k)}} \le A B^k M_k$ on $[a, b]$ for some constants $A, B > 0$ and all $k \ge 0$.
Then the following three conditions are equivalent.

1. The class $C^M([a, b])$ is [[quasi-analytic|YF1KAWB5MB]].
2. $\sum_{k=1}^{\infty} M_k^{-1/k} = \infty$.
3. $\sum_{k=1}^{\infty} \dfrac{M_{k-1}}{M_k} = \infty$.

## Remarks

When the series converge, one builds a nonzero function of the class that vanishes outside a small interval.
A standard construction is an infinite convolution of normalized indicator functions of short intervals, whose lengths are related to the ratios $M_{k-1}/M_k$.
Carleman's proof of the direction from divergence to quasi-analyticity uses complex analysis.
Without log-convexity, condition 1 is still equivalent to condition 2 with $M_k^{1/k}$ replaced by $\inf_{j \ge k} M_j^{1/j}$.
Condition 3 then has to be applied to the largest log-convex minorant of $M$ instead of $M$.

Example: for $M_k = k!$, the sequence is log-convex since $(k!)^2 \le (k-1)! \, (k+1)!$.
The ratios $M_{k-1}/M_k = 1/k$ have a divergent sum, so the class is quasi-analytic; this is the class of [[analytic functions|0JD5ZNW0F4]] on $[a, b]$.
For $M_k = (k!)^s$ with $s > 1$, the ratios are $k^{-s}$, and the sum converges.
So these classes contain nonzero [[bump functions|HS65DW0HXH]].

## Explanations

### L1 human

Analytic functions are determined by their derivatives at one point, while general smooth functions are not.
The theorem finds the exact border between these two behaviours.
If the derivatives of the functions in a class may grow only a little faster than $k!$, uniqueness survives.
If they may grow a bit faster still, bump functions appear and uniqueness is lost.

### L2 human

The test is a single series, much like a convergence test for ordinary series.
Divergence of $\sum M_{k-1}/M_k$ means that the allowed growth is slow, and the class behaves like the analytic functions.
Convergence means that cut-off functions exist in the class, so it supports partitions of unity, as needed in the theory of ultradistributions.
The case $M_k = (k!)^s$ gives the Gevrey classes, which appear in the study of partial differential equations.
