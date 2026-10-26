---
tag: 0WM7DJCM6G
kind: statement
role: theorem
name: Product of exponentials
aliases: [exponential-of-a-sum]
msc: [33B10]
uses: [09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Functional equation
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Complex exponential
---

## Statement

For all complex numbers $z$ and $w$,
$$e^{z + w} = e^{z} e^{w},$$
where $e^{z} = \sum_{n=0}^{\infty} z^n / n!$ is the complex exponential function.

## Remarks

The proof multiplies the two series and uses the binomial theorem.
It follows that $e^{z} \neq 0$ and $e^{-z} = 1 / e^{z}$ for each $z$.
With [[Euler's formula|04R3CY41VJ]], it gives the addition formulas for $\cos$ and $\sin$.

## Explanations

### L1 human

The exponential function turns sums into products, for complex numbers as for real numbers.
For example, $e^{i \theta} e^{i \varphi} = e^{i (\theta + \varphi)}$: turning by $\theta$ and then by $\varphi$ is turning by $\theta + \varphi$.
