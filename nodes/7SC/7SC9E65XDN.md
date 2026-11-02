---
tag: 7SC9E65XDN
kind: counterexample
name: Stein's example
msc: [62C15, 62F10, 62J07]
uses: [0XN3K7RSZY, N26TSVRH2S, DSTF6X8DRJ, 709T196XCT, 30XVCMK916]
sources:
  - url: https://en.wikipedia.org/wiki/Stein's_example
same_as:
  wikidata: Q3895097
  wikipedia: Stein's example
---

## Counterexample

Let $p \ge 3$ and let $X$ have the [[multivariate normal distribution|0XN3K7RSZY]] on $\R^p$ with unknown mean $\theta \in \R^p$ and covariance matrix the identity $I_p$.
Estimate $\theta$ under the loss $L(\theta, a) = \norm{a - \theta}^2$, the squared Euclidean distance.

The estimator $\delta_0(X) = X$ has [[risk|N26TSVRH2S]] $R(\theta, \delta_0) = E_\theta \norm{X - \theta}^2 = p$ for every $\theta$.
It is not [[admissible|DSTF6X8DRJ]].
The [[James–Stein estimator|709T196XCT]]
$$\delta_{JS}(X) = \Big( 1 - \frac{p - 2}{\norm{X}^2} \Big) X$$
has risk
$$R(\theta, \delta_{JS}) = p - (p - 2)^2 \, E_\theta\Big[ \frac{1}{\norm{X}^2} \Big].$$
For $p \ge 3$ the expectation is finite and positive, so $R(\theta, \delta_{JS}) < p$ for every $\theta$.
Thus $\delta_{JS}$ dominates $X$.

Check of the risk formula: write $\delta_{JS}(X) = X + g(X)$ with $g(x) = -(p - 2) x / \norm{x}^2$.
Then $\norm{g(x)}^2 = (p - 2)^2 / \norm{x}^2$ and $\sum_i \partial_i g_i(x) = -(p - 2)^2 / \norm{x}^2$.
[[Stein's unbiased risk estimate|30XVCMK916]] gives $R(\theta, \delta_{JS}) = E_\theta\big[p + \norm{g(X)}^2 + 2 \sum_i \partial_i g_i(X)\big]$, which is the formula above.

## Remarks

For $p = 1$ and $p = 2$, the estimator $X$ is admissible, so the dimension bound is sharp.
The improvement is largest near $\theta = 0$, the point toward which $\delta_{JS}$ shrinks: there $E_0[1/\norm{X}^2] = 1/(p - 2)$, so the risk is $2$ instead of $p$.
Any fixed point can replace $0$ as the target of the shrinkage.

## Explanations

### L1 human

To estimate three or more unrelated averages at once, the obvious method is to use each observed value as its own estimate.
Stein showed that this obvious method can be beaten for every possible truth, by pulling all estimates a little toward a common point.
The total squared error goes down, even though the quantities have nothing to do with each other.
This surprising fact changed how statisticians think about estimating many parameters together.
