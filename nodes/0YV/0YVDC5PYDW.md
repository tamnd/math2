---
tag: 0YVDC5PYDW
kind: definition
name: Conditional probability distribution
msc: ["60E05"]
defines: 0ZN9EZTEM6
uses: [0FJB06AD2P, 0QAR0XDZH4, 0AXP2Z5N9H, 0WF4EJP91W, 04YG690N5V]
sources:
  - url: https://en.wikipedia.org/wiki/Conditional_probability_distribution
    locator: Conditional discrete distributions
  - url: https://en.wikipedia.org/wiki/Conditional_probability_distribution
    locator: Conditional continuous distributions
---

## Definition

Let $X$ and $Y$ be random variables on one probability space.
Discrete case: let $X$ and $Y$ be discrete and let $x$ satisfy $P(X = x) > 0$. The conditional distribution of $Y$ given $X = x$ has the [[probability mass function|0WF4EJP91W]]
$$p_{Y \mid X}(y \mid x) = P(Y = y \mid X = x) = \frac{P(X = x, \, Y = y)}{P(X = x)}.$$
Continuous case: let $(X, Y)$ have a joint density $f_{X, Y}$, and let $f_X$ be the [[marginal|0AXP2Z5N9H]] density of $X$. For each $x$ with $f_X(x) > 0$, the conditional distribution of $Y$ given $X = x$ has the [[density|04YG690N5V]]
$$f_{Y \mid X}(y \mid x) = \frac{f_{X, Y}(x, y)}{f_X(x)}.$$

## Remarks

In the discrete case, $p_{Y \mid X}(\cdot \mid x)$ is the law of $Y$ under the [[conditional probability|0FJB06AD2P]] $P(\cdot \mid X = x)$.
In both cases, the joint law is the marginal times the conditional: $f_{X, Y}(x, y) = f_X(x) \, f_{Y \mid X}(y \mid x)$.
If $X$ and $Y$ are independent, the conditional distribution of $Y$ given $X = x$ is the law of $Y$, for each such $x$.
In general measure theory, one defines it as a regular conditional distribution. This is a probability kernel $\kappa$ with $P(X \in A, Y \in B) = \int_A \kappa(x, B) \, \mu_X(dx)$.

## Explanations

### L1 human

The conditional distribution answers the question: "If I know $X$, how is $Y$ distributed?"
For a person of height $180$ cm, it describes the possible weights of that person and their chances.
