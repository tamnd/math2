---
tag: 0WRZ170YEH
kind: statement
role: proposition
name: Moment-generating function of a sum of independent random variables
msc: ["60E10"]
uses: [0NNRNGKMFM, 05AW1G0WE1, 0XCE070V8B]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_generating_function
    locator: Linear combination of independent random variables
---

## Statement

Let $X_1, \dots, X_n$ be [[independent|0XCE070V8B]] real random variables, and let $S = X_1 + \dots + X_n$.
Then for each $t \in \mathbb{R}$, the [[moment-generating functions|0NNRNGKMFM]] satisfy
$$M_S(t) = M_{X_1}(t) \, M_{X_2}(t) \cdots M_{X_n}(t),$$
in $(0, \infty]$.

## Remarks

Proof: $e^{tS} = e^{tX_1} \cdots e^{tX_n}$. The factors are nonnegative and independent, so the [[product rule for expectations|05AW1G0WE1]] applies.
For i.i.d. $X_i$, $M_S(t) = M_{X_1}(t)^n$.
Example: if $X_i \sim \operatorname{Exp}(\lambda)$ are independent, then $M_S(t) = (\lambda/(\lambda - t))^n$ for $t < \lambda$. This is the moment-generating function of the gamma distribution $\operatorname{Gamma}(n, \lambda)$.

## Explanations

### L1 human

When you add independent random variables, their moment-generating functions multiply.
This makes it easy to identify the law of a sum, if you know which law has the product as its moment-generating function.
