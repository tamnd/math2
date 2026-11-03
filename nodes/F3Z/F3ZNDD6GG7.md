---
tag: F3ZNDD6GG7
kind: concept
name: Conditional entropy
msc: [94A17]
sources:
  - url: https://en.wikipedia.org/wiki/Conditional_entropy
same_as:
  wikidata: Q813908
  wikipedia: Conditional entropy
---

## Summary

The conditional entropy $H(Y \mid X)$ measures how much uncertainty about $Y$ remains on average once the value of $X$ is known.
It is the average, over the values $x$ of $X$, of the [[Shannon entropy|Y86E072V0V]] of the conditional law of $Y$ given $X = x$.
It satisfies the chain rule $H(X, Y) = H(X) + H(Y \mid X)$ with the [[joint entropy|DZWEWHZ20N]], and $H(Y \mid X) \le H(Y)$: conditioning does not increase entropy on average.
It is $0$ exactly when $Y$ is almost surely a function of $X$.

## Explanations

### L1 human

Suppose a friend tells you the value of $X$, and you still have to guess $Y$.
The conditional entropy is how much guessing remains, on average.
If $X$ is the weather and $Y$ is whether someone carries an umbrella, knowing the weather removes much, but not all, of the doubt.
If $Y$ is a copy of $X$, nothing remains, and $H(Y \mid X) = 0$.
If $Y$ is independent of $X$, knowing $X$ does not help, and $H(Y \mid X) = H(Y)$.
