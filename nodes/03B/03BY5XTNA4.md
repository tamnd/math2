---
tag: 03BY5XTNA4
kind: statement
role: theorem
name: Law of total variance
aliases: [variance-decomposition-formula, eve-law]
msc: [60A10]
uses: [0F1SN93KXE, 0YAMJRK04E, 04RRB6HM00, 0NMF95YK8W]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_total_variance
    locator: General case
same_as:
  wikidata: Q1055879
  wikipedia: Law of total variance
---

## Statement

Let $X$ be a real random variable with $E[X^2] < \infty$, and let $Y$ be a random variable on the same probability space. Then
$$\operatorname{Var}(X) = E\left[\operatorname{Var}(X \mid Y)\right] + \operatorname{Var}\left(E[X \mid Y]\right).$$

## Remarks

Proof: by the [[variance formula|0NMF95YK8W]] in its conditional form, $E[X^2 \mid Y] = \operatorname{Var}(X \mid Y) + (E[X \mid Y])^2$. Take expectations with the [[law of total expectation|04RRB6HM00]], and subtract $(E[X])^2 = (E[E[X \mid Y]])^2$.
The same result holds with a σ-algebra $\mathcal{G}$ in place of $Y$.
The first term is the mean variance inside the groups. The second term is the variance between the group means.
A corollary: $\operatorname{Var}(E[X \mid Y]) \le \operatorname{Var}(X)$.

## Explanations

### L1 human

The total spread of $X$ has two parts: the spread inside each group, and the spread of the group averages.
This decomposition is the base of the analysis of variance in statistics.
