---
tag: 969F3AWBKC
kind: definition
name: Statistical decision theory
msc: [62C05, 62A01]
defines: CPFSBBHXT5
uses: [K3AMMSY8DD, 3BTG6VVCGZ, N26TSVRH2S]
sources:
  - url: https://en.wikipedia.org/wiki/Decision_theory
---

## Definition

A *statistical decision problem* consists of the following data.

1. A [[statistical model|K3AMMSY8DD]] $\set{P_\theta : \theta \in \Theta}$ on a sample space $\mathcal{X}$, from which an observation $X$ is drawn.
2. A measurable space $\mathcal{A}$ of actions.
3. A [[loss function|3BTG6VVCGZ]] $L \colon \Theta \times \mathcal{A} \to [0, \infty)$.

A decision rule is a measurable map $\delta \colon \mathcal{X} \to \mathcal{A}$, and its performance is measured by its [[risk function|N26TSVRH2S]] $R(\theta, \delta) = E_\theta[L(\theta, \delta(X))]$.
*Statistical decision theory* is the study of decision problems through the comparison of the risk functions of decision rules.

## Remarks

A rule $\delta_1$ is at least as good as $\delta_2$ if $R(\theta, \delta_1) \le R(\theta, \delta_2)$ for all $\theta$.
This is only a partial order, so the theory adds criteria: admissibility, the minimax principle and the Bayes principle.
Randomized rules, which choose an action at random given the data, are often allowed; they make the set of risk functions convex.

Example: point estimation of a normal mean is the decision problem with $P_\theta$ the law of $n$ independent normal variables with mean $\theta$ and variance $1$.
Here $\Theta = \mathcal{A} = \R$ and $L(\theta, a) = (a - \theta)^2$.
The rule $\delta(X) = \bar X$ is a measurable map from $\R^n$ to $\mathcal{A}$, with risk $1/n$.

Non-example: a model and a set of estimators without a loss function do not form a decision problem.
Clause 3 is missing, so risks are undefined and rules cannot be compared.
