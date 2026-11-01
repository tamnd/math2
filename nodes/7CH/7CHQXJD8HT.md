---
tag: 7CHQXJD8HT
kind: definition
name: Theta function
msc: [11F27, 14K25, "33E05"]
defines: 2F5CYQJVAF
uses: [X6XGGH5FPW, 09FTAET5Z4, 0NAHXR1FRH, 0J0FCWV32D]
sources:
  - url: https://en.wikipedia.org/wiki/Theta_function
---

## Definition

Let $\mathbb{H}$ be the [[upper half-plane|X6XGGH5FPW]].
The *Jacobi theta function* is the function $\vartheta \colon \C \times \mathbb{H} \to \C$ given by
$$\vartheta(z, \tau) = \sum_{n = -\infty}^{\infty} \exp(\pi i n^2 \tau + 2 \pi i n z).$$
Its value at $z = 0$ is the theta constant $\theta(\tau) = \vartheta(0, \tau) = \sum_{n \in \Z} e^{\pi i n^2 \tau}$.

## Remarks

For $\operatorname{Im} \tau > 0$ the terms decay like $e^{-\pi n^2 \operatorname{Im} \tau}$ times a factor locally bounded in $z$, so the series converges absolutely and locally uniformly.
So $\vartheta$ is [[holomorphic|0NAHXR1FRH]] in both variables.
It satisfies $\vartheta(z + 1, \tau) = \vartheta(z, \tau)$ and $\vartheta(z + \tau, \tau) = \exp(-\pi i \tau - 2 \pi i z)\, \vartheta(z, \tau)$.
Check of the second rule: replace $n$ by $m - 1$ and use $n^2 + 2n = (n + 1)^2 - 1$.
The theta constant satisfies $\theta(-1/\tau) = \sqrt{-i\tau}\, \theta(\tau)$, by the Poisson summation formula.
Example: $\theta(\tau)^4 = \sum_{n \ge 0} r_4(n) e^{\pi i n \tau}$, where $r_4(n)$ counts the ways to write $n$ as a sum of four squares.
Non-example: for real $\tau$ the series diverges, because every term has absolute value $1$ when $z$ is also real; this is why $\tau$ must lie in $\mathbb{H}$.
Other authors use the nome $q = e^{\pi i \tau}$ and the four functions $\vartheta_1, \ldots, \vartheta_4$; the function above is then $\vartheta_3$.
