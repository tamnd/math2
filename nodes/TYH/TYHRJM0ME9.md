---
tag: TYHRJM0ME9
kind: counterexample
name: Witsenhausen's counterexample
msc: ["93E20", 49N30, "93A14"]
uses: [DJB8MAV5BH, TMEKPXMC7V, 07RXBVTVZB, 0TTDGTEFMN]
sources:
  - url: https://en.wikipedia.org/wiki/Witsenhausen%27s_counterexample
same_as:
  wikidata: Q8028527
  wikipedia: Witsenhausen's counterexample
---

## Counterexample

Fix constants $k > 0$ and $\sigma > 0$.
Let $x_0$ be [[normal|07RXBVTVZB]] with mean $0$ and variance $\sigma^2$, and let $v$ be standard normal and independent of $x_0$.
The first controller sees $x_0$ and applies $u_1 = \gamma_1(x_0)$, which gives the state $x_1 = x_0 + u_1$.
The second controller sees only the noisy value $y = x_1 + v$ and applies $u_2 = \gamma_2(y)$, which gives the final state $x_2 = x_1 - u_2$.
The goal is to choose Borel functions $\gamma_1$ and $\gamma_2$ that minimize
$$J(\gamma_1, \gamma_2) = E\big[k^2 u_1^2 + x_2^2\big].$$
The dynamics are linear, the noise is Gaussian and the cost is quadratic, as in the [[linear-quadratic-Gaussian problem|DJB8MAV5BH]].
But the second controller does not know what the first one knew, so the information structure is not classical.
Witsenhausen showed in 1968 that for some values of $k$ and $\sigma$ no pair of affine functions $\gamma_1, \gamma_2$ is optimal.

A check in the regime $k \sigma = 1$, $\sigma \to \infty$:

1. Affine policies. With $\gamma_1(x_0) = (\lambda - 1) x_0$, the state $x_1 = \lambda x_0$ is Gaussian, and the best $\gamma_2$ is the [[conditional mean|0TTDGTEFMN]] $E[x_1 \mid y]$, with error $\lambda^2 \sigma^2 / (1 + \lambda^2 \sigma^2)$.
So the best affine cost is $\min_{\lambda} \big[(\lambda - 1)^2 + \lambda^2 \sigma^2/(1 + \lambda^2 \sigma^2)\big]$ when $k \sigma = 1$, and this minimum tends to $1$ as $\sigma \to \infty$.
2. A nonlinear policy. Let $\gamma_1(x_0) = \sigma \sgn(x_0) - x_0$, so that $x_1 = \pm \sigma$ with probability $1/2$ each, and let $\gamma_2(y) = \sigma \tanh(\sigma y)$, which is $E[x_1 \mid y]$.
The first cost is $k^2 \sigma^2 E[(1 - \abs{z})^2] = 2\big(1 - \sqrt{2/\pi}\big) \approx 0.404$, where $z$ is standard normal.
The second cost is the error of telling $+\sigma$ from $-\sigma$ in unit noise, and it tends to $0$ as $\sigma \to \infty$.

So for $\sigma$ large and $k = 1/\sigma$, the nonlinear pair costs about $0.404$, while every affine pair costs close to $1$ or more.

## Remarks

In the classical linear-quadratic-Gaussian problem, the [[separation principle|TMEKPXMC7V]] makes linear feedback of the state estimate optimal.
The example shows that this conclusion depends on the information structure and not only on linearity, Gaussian noise and quadratic cost.
The first controller benefits from signaling: by moving $x_1$ to one of two well separated points it makes the state easy to estimate for the second controller.
Witsenhausen also proved that an optimal pair exists; no closed form for it is known.

## Explanations

### L1 human

Two people act on the same quantity in turn.
The first sees it exactly and may change it at a cost; the second sees it through noise and must cancel it.
The obvious idea is to use linear rules, as linear rules are optimal in so many similar problems.
But the first person can do better by pushing the quantity to one of two far-apart values, which the second can then recognize despite the noise.
This simple problem showed that in decentralized control, optimal rules can be nonlinear and very hard to find.
