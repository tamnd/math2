---
tag: AE0EZQH4ZM
kind: statement
role: theorem
name: Marcinkiewicz–Zygmund inequality
msc: ["60E15", 60G50, 42B25]
uses: [0PNRKMRC55, 0GQ938GDE0, 0WQNRCNY3M, AGWMZ50SSZ]
about: [0GQ938GDE0]
sources:
  - url: https://en.wikipedia.org/wiki/Marcinkiewicz%E2%80%93Zygmund_inequality
same_as:
  wikidata: Q6757294
  wikipedia: Marcinkiewicz–Zygmund inequality
---

## Statement

Let $1 \le p < \infty$.
There are constants $0 < A_p \le B_p < \infty$, depending only on $p$, with the following property.
Let $N \ge 1$ and let $X_1, \dots, X_N$ be [[independent|0GQ938GDE0]] real or complex [[random variables|0PNRKMRC55]] with $\mathbb{E}[X_i] = 0$ and $\mathbb{E}[\abs{X_i}^p] < \infty$ for each $i$, where $\mathbb{E}$ is the [[expected value|0WQNRCNY3M]].
Then
$$A_p \, \mathbb{E}\left[ \left( \sum_{i=1}^N \abs{X_i}^2 \right)^{p/2} \right] \le \mathbb{E}\left[ \Big\vert \sum_{i=1}^N X_i \Big\vert^p \right] \le B_p \, \mathbb{E}\left[ \left( \sum_{i=1}^N \abs{X_i}^2 \right)^{p/2} \right].$$

## Remarks

The proof uses symmetrization and the [[Khintchine inequality|AGWMZ50SSZ]].
Let $(\varepsilon_i)$ be independent random signs, independent of the $X_i$.
Because the $X_i$ have mean zero, $\mathbb{E}\abs{\sum X_i}^p$ is comparable, with constants depending only on $p$, to $\mathbb{E}\abs{\sum \varepsilon_i X_i}^p$.
Conditioning on the $X_i$ and applying Khintchine's inequality to the signs gives the comparison with $\mathbb{E}(\sum \abs{X_i}^2)^{p/2}$.

For $p = 2$ the inequality is an identity with $A_2 = B_2 = 1$: independence and mean zero give $\mathbb{E}\abs{\sum X_i}^2 = \sum \mathbb{E}\abs{X_i}^2$.
The mean zero hypothesis is needed: if every $X_i = 1$, the middle term is $N^p$ while the outer terms are of order $N^{p/2}$, so the upper bound fails for large $N$.

## Explanations

### L1 human

A sum of independent random quantities with average zero has much cancellation.
The inequality says that its size, measured by a $p$-th moment, is comparable to the size of the square root of the sum of the squares of the terms.
So the sum behaves as if the terms were orthogonal, as in the Pythagorean theorem.

### L2 human

The inequality is the probabilistic counterpart of the [[Khintchine inequality|AGWMZ50SSZ]], which is the special case of random signs times constants.
It is a model for the Littlewood–Paley inequality: the dyadic pieces of a function play the role of independent terms, and the square function plays the role of $\left( \sum \abs{X_i}^2 \right)^{1/2}$.
Burkholder extended it to martingale differences for $1 < p < \infty$, which links it further with Littlewood–Paley theory.
It is used to bound moments of sums of independent variables, for example in proofs of laws of large numbers with rates.
