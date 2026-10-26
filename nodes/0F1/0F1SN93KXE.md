---
tag: 0F1SN93KXE
kind: definition
name: Conditional variance
msc: [60A10]
defines: 0VGPX25NXQ
uses: [0YAMJRK04E, 007QED3E0Y]
sources:
  - url: https://en.wikipedia.org/wiki/Conditional_variance
    locator: Definition
---

## Definition

Let $X$ be a real random variable on $(\Omega, \mathcal{F}, P)$ with $E[X^2] < \infty$, and let $\mathcal{G} \subseteq \mathcal{F}$ be a σ-algebra.
The conditional variance of $X$ given $\mathcal{G}$ is the random variable
$$\operatorname{Var}(X \mid \mathcal{G}) = E\left[\left(X - E[X \mid \mathcal{G}]\right)^2 \,\middle|\, \mathcal{G}\right],$$
where $E[\cdot \mid \mathcal{G}]$ is the [[conditional expectation|0YAMJRK04E]]. For a random variable $Y$, $\operatorname{Var}(X \mid Y) = \operatorname{Var}(X \mid \sigma(Y))$.

## Remarks

As for the [[variance|007QED3E0Y]], $\operatorname{Var}(X \mid \mathcal{G}) = E[X^2 \mid \mathcal{G}] - (E[X \mid \mathcal{G}])^2$ almost surely.
For a discrete $Y$ and $y$ with $P(Y = y) > 0$, $\operatorname{Var}(X \mid Y)$ takes the value $\operatorname{Var}(X \mid Y = y)$ on $\{Y = y\}$. This is the variance of $X$ under $P(\cdot \mid Y = y)$.
$\operatorname{Var}(X \mid \mathcal{G}) = 0$ almost surely if and only if $X$ is equal almost surely to a $\mathcal{G}$-measurable random variable.

## Explanations

### L1 human

The conditional variance tells how uncertain $X$ still is after you learn some information.
For example, the variance of the height of a person given the sex of that person is the spread of heights within each group.
