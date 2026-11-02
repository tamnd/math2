---
tag: CHHD44WDHJ
kind: concept
name: Robbins–Monro algorithm
msc: [62L20]
specializes: [ZPCPW4W1Y9]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_approximation
    locator: Robbins–Monro algorithm
---

## Summary

The Robbins–Monro algorithm is the first [[stochastic approximation|ZPCPW4W1Y9]] method, introduced by Herbert Robbins and Sutton Monro in 1951.
It finds the point where an increasing function, observed only through noisy measurements, takes a given value.
It updates the current guess by a step proportional to the observed error, with step sizes that shrink at a suitable rate.

## Explanations

### L1 human

Suppose the dose of a drug sets the average response, but each patient responds a bit differently.
To find the dose whose average response equals a target, give a dose and observe the response.
Then lower the dose if the response was too high, or raise it if it was too low.
The corrections shrink like $1/n$, so random errors cancel out over time.
With target $\alpha$, dose $\theta_n$ and observed response $N_n$, the update is $\theta_{n+1} = \theta_n - \frac{c}{n} (N_n - \alpha)$ for a constant $c > 0$.
