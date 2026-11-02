---
tag: H03BGDDF0N
kind: definition
name: Sinc function
msc: ["33B10", "94A12"]
defines: P1T98BECWR
uses: [08WFZP6P89]
sources:
  - url: https://en.wikipedia.org/wiki/Sinc_function
---

## Definition

The *sinc function* is the function $\operatorname{sinc} \colon \R \to \R$ given by
$$\operatorname{sinc} x = \begin{cases} \dfrac{\sin x}{x} & \text{if } x \ne 0, \\ 1 & \text{if } x = 0, \end{cases}$$
where $\sin$ is the [[sine function|08WFZP6P89]].
The *normalised sinc function* is $x \mapsto \operatorname{sinc}(\pi x)$.

## Remarks

The value at $0$ makes the function continuous, since $\frac{\sin x}{x} \to 1$ as $x \to 0$.
In fact $\operatorname{sinc} x = \sum_{k \ge 0} \frac{(-1)^k x^{2k}}{(2k+1)!}$, so it extends to an entire even function.

Example: $\operatorname{sinc}(\pi/2) = \frac{1}{\pi/2} = \frac{2}{\pi}$, and the zeros of $\operatorname{sinc}$ are the points $k\pi$ with $k$ a non-zero integer.

Non-example: the function equal to $\frac{\sin x}{x}$ for $x \ne 0$ and to $0$ at $x = 0$ is not the sinc function; it fails the second clause and is not continuous at $0$.

The improper integral $\int_{-\infty}^{\infty} \operatorname{sinc} x\, dx = \pi$ converges, but $\operatorname{sinc}$ is not Lebesgue integrable on $\R$.
Some authors, mainly in signal processing, write $\operatorname{sinc}$ for the normalised version; Mathlib's `Real.sinc` is the unnormalised one above.
