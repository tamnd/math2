---
tag: RVKNX8HN1V
kind: statement
role: proposition
name: Hamilton's rule
msc: [92D15, 92D50]
uses: [NA4JQGNMAZ, 0KBFAWYRTE, 0477R9PYAE, CCN582E2C4]
about: [CCN582E2C4]
sources:
  - url: https://en.wikipedia.org/wiki/Kin_selection
---

## Statement

Let a population consist of $n$ individuals.
Each individual $i$ has a genetic value $g_i \in \R$, its level of altruism.
Each individual $i$ also has a social partner $\pi(i)$, where $\pi$ is a map from the population to itself.
Assume that the fitness of $i$ is $w_i = w_0 - C g_i + B g_{\pi(i)}$, where $w_0$, $C$ and $B$ are constants.
So an altruist pays the cost $C$ per unit of $g$, and its partner gains the benefit $B$.
Assume that genetic values are transmitted without bias, so that $\operatorname{E}(w \Delta g) = 0$ in the [[Price equation|NA4JQGNMAZ]], and that $\operatorname{Var}(g) > 0$ and $\bar w > 0$.
Let $r = \operatorname{Cov}(g_{\pi}, g) / \operatorname{Var}(g)$ be the relatedness.
It is the regression coefficient of the partner's genetic value on one's own.
Here the [[covariance|0KBFAWYRTE]] and the [[variance|0477R9PYAE]] are taken over the population with equal weights.
Then the mean genetic value increases, $\Delta \bar g > 0$, if and only if
$$r B > C.$$

## Remarks

By the Price equation with no transmission term, $\bar w \Delta \bar g = \operatorname{Cov}(w, g) = -C \operatorname{Var}(g) + B \operatorname{Cov}(g_\pi, g)$.
Dividing by $\operatorname{Var}(g) > 0$ shows that $\Delta \bar g$ has the sign of $rB - C$.
For example, between full siblings in a randomly mating diploid population one has $r = 1/2$ for an additive gene.
So helping a sibling pays when the benefit is more than twice the cost.
If the partners are random members of a large population, $r$ is near $0$ and altruism with $C > 0$ cannot spread.
The exact form of the rule depends on the fitness model; with nonadditive interactions the coefficients $B$ and $C$ must be defined as partial regression coefficients.

## Explanations

### L1 human

Helping others costs the helper, so how can a gene for helping spread?
Hamilton's rule answers: when the helped individual is likely to carry the same gene.
The help pays off for the gene when relatedness times benefit exceeds cost.
J. B. S. Haldane's quip that he would give his life for two brothers or eight cousins expresses the same arithmetic.

### L2 human

The rule is the basis of kin selection theory.
In the form above it is a direct consequence of the Price equation.
One only writes fitness as a linear function of one's own genetic value and that of the partner.
Relatedness here is a regression coefficient, not a pedigree count; pedigree relatedness is one way to compute it under random mating and weak selection.
The same framework explains why population structure, which makes partners similar, can favour cooperation.
