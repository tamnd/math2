---
tag: ERXF29KNPC
kind: definition
name: Hodges–Lehmann estimator
msc: [62G05, 62G35]
defines: T6KRQAQQ15
uses: [08W2CW8PKW, 0TTNRP5PFQ]
sources:
  - url: https://en.wikipedia.org/wiki/Hodges%E2%80%93Lehmann_estimator
---

## Definition

Let $x_1, \dots, x_n$ be real numbers.
The *Walsh averages* are the $n(n+1)/2$ numbers $(x_i + x_j)/2$ for $1 \le i \le j \le n$.
The *one-sample Hodges–Lehmann estimator* is the [[median|08W2CW8PKW]] of the Walsh averages:
$$\hat\theta = \operatorname{med}\Big\{ \frac{x_i + x_j}{2} : 1 \le i \le j \le n \Big\}.$$
For two samples $x_1, \dots, x_m$ and $y_1, \dots, y_n$, the *two-sample Hodges–Lehmann estimator* of the shift is $\hat\Delta = \operatorname{med}\set{y_j - x_i : 1 \le i \le m, \ 1 \le j \le n}$.

## Remarks

It is an [[estimator|0TTNRP5PFQ]] of the centre of symmetry $\theta$ in the model of the [[Wilcoxon signed-rank test|38SETDT2HN]].
The estimate $\hat\theta$ is the value of $t$ for which the signed-rank statistic of $x_1 - t, \dots, x_n - t$ is closest to its null mean $n(n+1)/4$.
Its asymptotic breakdown point is $1 - 1/\sqrt{2} \approx 0.29$.

Example: data $(1, 2, 9)$.
The Walsh averages are $1, 2, 9$ (for $i = j$) and $1.5, 5, 5.5$ (for $i < j$); sorted, $1, 1.5, 2, 5, 5.5, 9$.
Their median is $(2 + 5)/2 = 3.5$.

Non-example: the median of the averages $(x_i + x_j)/2$ over $i < j$ only, without the terms $i = j$, is a different estimator; for $(1, 2, 9)$ it gives $5$.
Both versions appear in the literature, so the convention should be stated.
