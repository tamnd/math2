---
tag: 0S9EK5MQPE
kind: definition
name: Continuity in R^n
msc: [26B05]
defines: 0JEJATBVD7
uses: [0XPR1E85W0, 0J8Y1NCY0K]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Continuous functions between metric spaces
---

## Definition

Let $D \subseteq \mathbb{R}^n$, let $f \colon D \to \mathbb{R}^m$, and let $a \in D$.
The function $f$ is continuous at $a$ when, for each $\varepsilon > 0$, there is a $\delta > 0$ such that $\|f(x) - f(a)\| < \varepsilon$ for each $x \in D$ with $\|x - a\| < \delta$.
Here $\|\cdot\|$ is the Euclidean norm of [[Euclidean space|0XPR1E85W0]].
The function $f$ is continuous on $D$ when it is continuous at each point of $D$.

## Remarks

Let $a$ be a limit point of $D$. Then $f$ is continuous at $a$ if and only if $\lim_{x \to a} f(x) = f(a)$, with the [[limit of a function of several variables|0J8Y1NCY0K]].
A function into $\mathbb{R}^m$ is continuous if and only if each component function is continuous.
Sums, products and compositions of continuous functions are continuous. So each polynomial in $x_1, \dots, x_n$ is continuous on $\mathbb{R}^n$.
Continuity in each variable separately is weaker: see the [[separately continuous function that is not continuous|0C0KPAKK9Y]].

## Explanations

### L1 human

A continuous function has no jumps: if you move the input a little, the output moves only a little.
In the plane, "a little" means inside a small disc, so the condition must hold for moves in every direction.
