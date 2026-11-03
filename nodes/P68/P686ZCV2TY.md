---
tag: P686ZCV2TY
kind: definition
name: Rescorla–Wagner model
msc: ["91E40"]
defines: AB3662AVXX
uses: []
sources:
  - url: https://en.wikipedia.org/wiki/Rescorla–Wagner_model
---

## Definition

Let $C$ be a finite set of conditioned stimuli, called cues.
Each cue $X \in C$ has an associative strength $V_X \in \R$ and a salience $\alpha_X \in (0, 1]$.
A trial consists of a set $A \subseteq C$ of present cues and an outcome with learning rate $\beta \in (0, 1]$ and maximum strength $\lambda \ge 0$.
When the unconditioned stimulus is absent, $\lambda = 0$.
In the *Rescorla–Wagner model* the trial changes the strengths by
$$\Delta V_X = \alpha_X \beta \left(\lambda - \sum_{Y \in A} V_Y\right) \quad \text{for } X \in A,$$
and leaves $V_X$ unchanged for $X \notin A$.

## Remarks

Example: one cue with $\alpha\beta = 0.2$, $\lambda = 1$ and $V_0 = 0$ gives $V_{t+1} = V_t + 0.2(1 - V_t)$, hence $V_t = 1 - 0.8^t$, which rises to $1$.
Blocking: if $V_L = 1 = \lambda$ for a light $L$, then on trials with $A = \set{L, T}$ and $V_T = 0$ the error is $1 - 1 - 0 = 0$, so the tone $T$ learns nothing.
Non-example: the rule $\Delta V_X = \alpha_X \beta(\lambda - V_X)$, with each cue's own strength instead of the sum over present cues, is not the Rescorla–Wagner model; it cannot produce blocking.
For a single cue, extinction trials ($\lambda = 0$) make its strength decay geometrically towards $0$.
