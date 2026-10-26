---
tag: 0EKGKY5TGH
kind: statement
role: proposition
name: Epsilon-delta continuity in metric spaces
msc: ["54E35"]
uses: [07N7W5C29X, 0A26X79RTB, 0DC3MPR7C9]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Continuous functions between metric spaces
---

## Statement

Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]], let $f \colon X \to Y$ be a function and let $a \in X$.
Then $f$ is [[continuous at|07N7W5C29X]] $a$ if and only if for each real $\varepsilon > 0$ there is a real $\delta > 0$ such that
$$d_X(x, a) < \delta \implies d_Y\bigl(f(x), f(a)\bigr) < \varepsilon \quad \text{for all } x \in X.$$

## Remarks

In terms of [[open balls|0DC3MPR7C9]], the condition says: for each $\varepsilon > 0$ there is $\delta > 0$ with $f(B(a, \delta)) \subseteq B(f(a), \varepsilon)$.
The number $\delta$ can depend on $\varepsilon$ and on $a$. When one $\delta$ works for all $a$, the map is [[uniformly continuous|0FHSDCQACY]].
For $X = Y = \mathbb{R}$, this is the epsilon-delta definition of continuity from calculus.

## Explanations

### L1 human

You can make $f(x)$ as close to $f(a)$ as you want by taking $x$ close enough to $a$.
The tolerance $\varepsilon$ for the output comes first, and then you find a tolerance $\delta$ for the input.
