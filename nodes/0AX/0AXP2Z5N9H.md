---
tag: 0AXP2Z5N9H
kind: definition
name: Marginal distribution
msc: [62H05]
defines: 0MXT6PRZZ6
uses: [0QAR0XDZH4, 0TST4MHA3A]
sources:
  - url: https://en.wikipedia.org/wiki/Marginal_distribution
    locator: Definition
---

## Definition

Let $\mu$ be a probability distribution on $\mathbb{R}^2$, for example the [[joint distribution|0QAR0XDZH4]] of real random variables $X$ and $Y$.
The first marginal distribution of $\mu$ is the distribution $\mu_1$ on $\mathbb{R}$ with $\mu_1(A) = \mu(A \times \mathbb{R})$ for each Borel set $A \subseteq \mathbb{R}$. The second marginal is $\mu_2(B) = \mu(\mathbb{R} \times B)$.
If $\mu$ is the law of $(X, Y)$, then $\mu_1$ is the law of $X$ and $\mu_2$ is the law of $Y$.

## Remarks

The same definition works on a product $E_1 \times E_2$ of measurable spaces, and for $n$ variables with the projections onto some of the coordinates.
In the discrete case, $P(X = x) = \sum_{y} P(X = x, Y = y)$. In the case of a joint density $f(x, y)$, $X$ has the density $f_X(x) = \int_{-\infty}^{\infty} f(x, y) \, dy$.
The name comes from tables: the sums of the rows and the columns of a joint table are written in its margins.

## Explanations

### L1 human

To get the marginal distribution of $X$ from a joint table of $X$ and $Y$, add up each row.
You lose the information about how $X$ and $Y$ are linked, and you keep only the chances of the values of $X$.
