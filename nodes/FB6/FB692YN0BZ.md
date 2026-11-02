---
tag: FB692YN0BZ
kind: statement
role: proposition
name: Bayes risk is at most minimax risk
msc: [62C20, 62C10]
uses: [N26TSVRH2S, VEBDNCJJTN, 8EG1M1WZ9C]
about: [VEBDNCJJTN, 8EG1M1WZ9C]
sources:
  - url: https://en.wikipedia.org/wiki/Minimax_estimator
---

## Statement

Let $\set{P_\theta : \theta \in \Theta}$ be a statistical model with a loss function, with [[risk function|N26TSVRH2S]] $R(\theta, \delta)$.
Let $\pi$ be a prior on $\Theta$ such that $\theta \mapsto R(\theta, \delta)$ is measurable for every rule $\delta$.
Then the [[Bayes risk|VEBDNCJJTN]] of $\pi$ is at most the [[minimax risk|8EG1M1WZ9C]]:
$$r(\pi) = \inf_\delta \int_\Theta R(\theta, \delta) \, \pi(d\theta) \le \inf_\delta \sup_{\theta \in \Theta} R(\theta, \delta).$$

## Remarks

For each fixed rule $\delta$, an average of $R(\cdot, \delta)$ is at most its supremum, so $\int R(\theta, \delta) \, \pi(d\theta) \le \sup_\theta R(\theta, \delta)$.
Taking the infimum over $\delta$ on both sides gives the claim.
Hence also $\sup_\pi r(\pi) \le R^*$, where $R^*$ is the minimax risk.

This inequality is the standard way to prove lower bounds for the minimax risk.
If a rule $\delta^*$ has $\sup_\theta R(\theta, \delta^*) = r(\pi)$ for some prior $\pi$, then $\delta^*$ is minimax.
For instance, a Bayes rule with constant risk is minimax, as for the binomial proportion with the beta prior of parameters $\sqrt{n}/2$ and $\sqrt{n}/2$.

## Explanations

### L1 human

The worst case is always at least as bad as any average.
So the best achievable average risk, for any choice of prior, is never more than the best achievable worst-case risk.

### L2 human

To show that no estimator can do better than some value in the worst case, it is enough to find a prior whose Bayes risk equals that value.
This is the Bayesian route to minimax lower bounds, often used with a sequence of priors whose Bayes risks increase to the candidate value.
For a finite parameter set with randomized rules allowed, minimax theorems show that the two sides are equal when the supremum over priors is taken.
