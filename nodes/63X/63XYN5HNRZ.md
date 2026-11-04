---
tag: 63XYN5HNRZ
kind: proof
name: Proof of variance under scaling
msc: [60A05]
proves: 0KVQ9D86BM
uses: [007QED3E0Y, 0DCT0QZVQ1, 0P7PTC8DDE]
sources:
  - url: https://en.wikipedia.org/wiki/Variance
    locator: Addition and multiplication by a constant
---

## Proof

We compute directly from the definition of the variance.

1. Let $X$ be a real random variable with finite [[variance|007QED3E0Y]], and let $a \in \R$.
2. By the definition of the variance, $X$ is integrable. Let $m = E[X]$. Then $E[(X - m)^2] = \operatorname{Var}(X) < \infty$.
3. By [[linearity of expectation|0P7PTC8DDE]], $aX$ is integrable and $E[aX] = a m$.
4. Pointwise, $(aX - am)^2 = a^2 (X - m)^2$.
5. The variable $(X - m)^2$ is integrable by step 2. By linearity of the [[expected value|0DCT0QZVQ1]], $E[a^2 (X - m)^2] = a^2 E[(X - m)^2]$.
6. By steps 3 to 5 and the definition of the [[variance|007QED3E0Y]], $\operatorname{Var}(aX) = E[(aX - am)^2] = a^2 \operatorname{Var}(X)$.

## Idea

Scaling $X$ by $a$ scales its mean by $a$, so the deviation from the mean is scaled by $a$. Squaring turns the factor $a$ into $a^2$.
