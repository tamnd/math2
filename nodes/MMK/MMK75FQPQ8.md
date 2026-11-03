---
tag: MMK75FQPQ8
kind: definition
name: Spontaneous magnetization
msc: [82B20, 82B26, 82D40]
defines: JPCEWASHGQ
uses: [R0KGM32QN6, FPYQWE8X12, XSA203109Z]
sources:
  - url: https://en.wikipedia.org/wiki/Spontaneous_magnetization
---

## Definition

Let $d \ge 1$, and consider the ferromagnetic [[Ising model|R0KGM32QN6]] on $\Z^d$ with nearest-neighbour coupling $J > 0$, inverse temperature $\beta \ge 0$ and field $h \in \R$.
For a finite box $\Lambda \subset \Z^d$, let $\langle \cdot \rangle_{\Lambda, \beta, h}$ be the Gibbs expectation with free boundary condition.
Let $m(\beta, h) = \lim_{\Lambda \uparrow \Z^d} \langle \sigma_0 \rangle_{\Lambda, \beta, h}$ be the magnetization in the [[thermodynamic limit|FPYQWE8X12]].
The *spontaneous magnetization* is
$$m^*(\beta) = \lim_{h \to 0^+} m(\beta, h).$$

## Remarks

The limit over boxes exists, and $h \mapsto m(\beta, h)$ is nondecreasing, so the limit as $h \to 0^+$ exists.
The value $m^*(\beta)$ equals $\langle \sigma_0 \rangle^+_\beta$, the magnetization of the infinite-volume state with plus boundary condition.
It is the [[order parameter|XSA203109Z]] of the transition: for $d \ge 2$ there is a critical $\beta_c \in (0, \infty)$ with $m^*(\beta) = 0$ for $\beta < \beta_c$ and $m^*(\beta) > 0$ for $\beta > \beta_c$.

Example: on $\Z^2$, Yang proved in 1952 that $m^*(\beta) = \big(1 - \sinh(2\beta J)^{-4}\big)^{1/8}$ for $\sinh(2\beta J) > 1$, and $m^* = 0$ otherwise.
Near $\beta_c$ this gives $m^* \sim (\beta - \beta_c)^{1/8}$, so the critical exponent is $\beta = 1/8$.

Non-example: the magnetization $m(\beta, h)$ at a fixed $h > 0$ is positive at every temperature.
It is a response to the field, not spontaneous, because the limit $h \to 0^+$ has not been taken.
In dimension $d = 1$, $m^*(\beta) = 0$ for every $\beta$, so there is no spontaneous magnetization at any positive temperature.
