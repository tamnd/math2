---
tag: 0NS0TDA4E2
kind: statement
role: proposition
name: Characteristic function of the normal distribution
msc: ["60E10"]
uses: [0MYDNRT7PP, 07RXBVTVZB, 0B1G4E21G7]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_distribution
    locator: Fourier transform and characteristic function
---

## Statement

Let $\mu \in \mathbb{R}$, let $\sigma^2 > 0$ and let $X \sim \mathcal{N}(\mu, \sigma^2)$. Then for each $t \in \mathbb{R}$,
$$\varphi_X(t) = E\left[e^{itX}\right] = \exp\left(i \mu t - \tfrac{1}{2} \sigma^2 t^2\right).$$
In particular, the standard normal distribution has $\varphi(t) = e^{-t^2/2}$.

## Remarks

One proof: the [[moment-generating function|0B1G4E21G7]] $E[e^{zX}] = \exp(\mu z + \sigma^2 z^2/2)$ holds for real $z$. Both sides are entire functions of $z$, so the identity extends to all complex $z$, and one puts $z = it$.
Another proof: $\varphi(t) = e^{-t^2/2}$ for $\mathcal{N}(0, 1)$ is the solution of $\varphi'(t) = -t \varphi(t)$ with $\varphi(0) = 1$. Integration by parts gives this differential equation.
So the standard normal density is, up to the factor $\sqrt{2\pi}$, its own Fourier transform.

## Explanations

### L1 human

The characteristic function of a normal variable is again a bell-shaped function.
A narrow normal distribution, with small $\sigma$, has a wide characteristic function, and conversely.
