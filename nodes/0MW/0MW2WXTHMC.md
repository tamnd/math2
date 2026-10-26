---
tag: 0MW2WXTHMC
kind: definition
name: Equicontinuity
aliases: [equicontinuous-family]
msc: [54C35]
defines: 0XN66MZN0Y
uses: [063W5JMY85, 0EKGKY5TGH]
sources:
  - url: https://en.wikipedia.org/wiki/Equicontinuity
    locator: Equicontinuity between metric spaces
---

## Definition

Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]] and let $\mathcal{F}$ be a set of functions from $X$ to $Y$.
The family $\mathcal{F}$ is equicontinuous at a point $a \in X$ when the property that follows holds.
For each real $\varepsilon > 0$ there is a real $\delta > 0$ such that $d_Y(f(x), f(a)) < \varepsilon$ for all $f \in \mathcal{F}$ and all $x \in X$ with $d_X(x, a) < \delta$.
The family $\mathcal{F}$ is equicontinuous when it is equicontinuous at each point of $X$.

## Remarks

The number $\delta$ depends on $\varepsilon$ and $a$, but not on $f$.
Each finite set of continuous functions is equicontinuous.
The family of all functions $f \colon \mathbb{R} \to \mathbb{R}$ that are [[Lipschitz|0TMZ21WKCN]] with constant $1$ is equicontinuous: take $\delta = \varepsilon$.
The family $f_n(x) = x^n$ on $[0, 1]$ is not equicontinuous at $x = 1$.

## Explanations

### L1 human

Each continuous function has its own $\delta$ for each $\varepsilon$. An equicontinuous family has one $\delta$ that works for all functions in the family.
The functions $x^n$ become steeper and steeper near $1$, so no common $\delta$ exists there.
