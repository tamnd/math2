---
tag: 0Z1G2F8DGY
kind: statement
role: proposition
name: Power series of complex cosine
aliases: [taylor-series-of-cosine]
msc: [33B10]
uses: [0A7YDKRNR6, 054VXHMCA3]
sources:
  - url: https://en.wikipedia.org/wiki/Sine_and_cosine
    locator: Series and polynomials
---

## Statement

For each $z \in \mathbb{C}$, the series $\sum_{n \ge 0} (-1)^n z^{2n} / (2n)!$ converges absolutely, and
$$\cos z = \sum_{n=0}^{\infty} (-1)^n \frac{z^{2n}}{(2n)!} = 1 - \frac{z^2}{2!} + \frac{z^4}{4!} - \cdots,$$
where $\cos$ is the [[complex cosine|0A7YDKRNR6]].

## Remarks

Proof: put $iz$ and $-iz$ in the series of the [[complex exponential|054VXHMCA3]] and add. The terms with odd powers cancel, and $i^{2n} = (-1)^n$.
In the same way, $\sin z = \sum_{n \ge 0} (-1)^n z^{2n+1} / (2n+1)!$ for each $z \in \mathbb{C}$.
The series shows that $\cos$ is an even function: $\cos(-z) = \cos z$.

## Explanations

### L1 human

The series of $\cos$ has only the even powers of $e^z$'s series, with signs that alternate.
For example, $\cos(0.1) \approx 1 - 0.005 = 0.995$ from the first two terms.
