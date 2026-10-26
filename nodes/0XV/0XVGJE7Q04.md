---
tag: 0XVGJE7Q04
kind: statement
role: proposition
name: The principal logarithm is holomorphic off the branch cut
aliases: [derivative-of-the-logarithm]
msc: [33B10]
uses: [0YKY4M3KRQ, 06JYC06JHY, 0DG0Z72CQD, 054VXHMCA3]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_logarithm
    locator: The derivative of the complex logarithm
  - url: https://en.wikipedia.org/wiki/Complex_logarithm
    locator: The principal value as an inverse function
---

## Statement

Let $S = \mathbb{C} \setminus (-\infty, 0]$ be the slit plane, the complement of the standard [[branch cut|06JYC06JHY]].
Let $\operatorname{Log}$ be the [[principal branch|0YKY4M3KRQ]] of the logarithm.
Then $\operatorname{Log}$ is [[holomorphic|0DG0Z72CQD]] on $S$, and
$$\operatorname{Log}'(z) = \frac{1}{z}$$
for each $z \in S$.

## Remarks

Proof idea: on $S$, $\operatorname{Log}$ is continuous and it is the inverse of the [[complex exponential|054VXHMCA3]] on the strip $\{w : -\pi < \operatorname{Im} w < \pi\}$. The inverse function rule gives $\operatorname{Log}'(z) = 1 / e^{\operatorname{Log} z} = 1/z$.
$\operatorname{Log}$ is not continuous at the points of $(-\infty, 0)$. For $x < 0$, its values tend to $\ln|x| + i\pi$ from above the axis and to $\ln|x| - i\pi$ from below.

## Explanations

### L1 human

Away from the cut along the negative real axis, the principal logarithm behaves like the real logarithm: its derivative is $1/z$.
On the cut itself, the angle jumps from about $\pi$ to about $-\pi$, so the function is not even continuous there.
