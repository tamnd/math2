---
tag: 0YF82GBTND
kind: statement
role: theorem
name: Continuity via open sets
msc: ["54E35"]
uses: [0SY9ECQ19Q, 0A26X79RTB, 0EKGKY5TGH]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Continuous functions between metric spaces
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Continuous functions between topological spaces
---

## Statement

Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]] and let $f \colon X \to Y$ be a function.
Then the following two conditions are equivalent:

1. For each $a \in X$ and each $\varepsilon > 0$ there is $\delta > 0$ such that $d_X(x, a) < \delta$ implies $d_Y(f(x), f(a)) < \varepsilon$ for all $x \in X$.
2. For each [[open set|01ZQQDCERP]] $V$ of $Y$, the [[preimage|0FGCFY1AZX]] $f^{-1}(V)$ is open in $X$.

## Remarks

Condition 2 is the definition of a [[continuous map|0SY9ECQ19Q]] between topological spaces. Thus, for metric spaces, the epsilon-delta definition and the topological definition agree.
Proof that 1 implies 2: let $a \in f^{-1}(V)$. Choose $\varepsilon$ with $B(f(a), \varepsilon) \subseteq V$, then $\delta$ from condition 1. Then $B(a, \delta) \subseteq f^{-1}(V)$.
Images of open sets need not be open: the constant map $\mathbb{R} \to \mathbb{R}$, $x \mapsto 0$, is continuous, but the image of $\mathbb{R}$ is $\{0\}$.

## Explanations

### L1 human

The topological form of continuity uses only open sets and does not mention distances.
This form lets us define continuity in spaces that have no metric at all.
