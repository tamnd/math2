---
tag: M3PFV1BX9V
kind: statement
role: theorem
name: Complete class theorem
msc: [62C07, 62C10, 62C15]
uses: [N26TSVRH2S, DSTF6X8DRJ, PP1A0JB47Q, VEBDNCJJTN, 02AS45T3H9]
about: [DSTF6X8DRJ, PP1A0JB47Q]
sources:
  - url: https://en.wikipedia.org/wiki/Admissible_decision_rule
---

## Statement

Let $\set{P_\theta : \theta \in \Theta}$ be a statistical model with a loss function, where $\Theta = \set{\theta_1, \dots, \theta_k}$ is finite.
Allow randomized decision rules, and assume that every rule has finite [[risk|N26TSVRH2S]] at every $\theta_i$.
Then every [[admissible|DSTF6X8DRJ]] rule $\delta$ is a [[Bayes rule|PP1A0JB47Q]] for some prior: there are weights $\pi_1, \dots, \pi_k \ge 0$ with $\sum_i \pi_i = 1$ such that
$$\sum_{i=1}^{k} \pi_i R(\theta_i, \delta) = \inf_{\delta'} \sum_{i=1}^{k} \pi_i R(\theta_i, \delta').$$

## Remarks

Consider the risk set $S = \set{(R(\theta_1, \delta), \dots, R(\theta_k, \delta))}$ in $\R^k$, over all randomized rules $\delta$.
Mixing two rules mixes their risk points, so $S$ is a [[convex set|02AS45T3H9]].
If $\delta$ is admissible, its risk point $x$ meets the convex set $\set{y : y_i \le x_i \text{ for all } i}$ in $S$ only at points equal to $x$.
A separating hyperplane through $x$ then has a normal vector with nonnegative entries, and normalizing it gives the prior $\pi$.
The minimized quantity is the [[Bayes risk|VEBDNCJJTN]] of $\pi$.

A class $\mathcal{C}$ of rules is called *complete* if every rule outside $\mathcal{C}$ is dominated by some rule in $\mathcal{C}$.
Complete class theorems are results of this kind, which show that the Bayes rules, or their limits, form a complete class.
For infinite $\Theta$, similar results hold under extra conditions, with limits of Bayes rules or generalized Bayes rules in place of Bayes rules.

Randomization matters in the proof: without it, the risk set need not be convex.

## Explanations

### L1 human

Any rule that cannot be beaten everywhere is, secretly, the best rule for some way of weighting the possible truths.
So when the set of possible truths is finite, a search for good rules can be restricted to Bayes rules.

### L2 human

The theorem gives a frequentist reason to use Bayesian methods: admissibility, a purely frequentist property, forces a rule to be Bayes.
It reduces the search for admissible rules to the study of Bayes rules for all priors.
The proof is a direct application of the separating hyperplane theorem to the convex risk set.
In infinite-dimensional problems the analogues are more delicate, and admissible rules are typically limits of Bayes rules.
