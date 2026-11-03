---
tag: NXJ2PDFDCM
kind: definition
name: Multi-compartment model in pharmacokinetics
msc: [92C45, 34A30]
defines: GTD06WV20A
uses: [0NT64JV96A, 0VD9ZSWWJG, 020M04FN1H]
sources:
  - url: https://en.wikipedia.org/wiki/Multi-compartment_model
---

## Definition

Let $n \ge 1$ be the number of compartments, and let $x_i(t) \ge 0$ be the amount of drug in compartment $i$ at time $t$.
For $i \ne j$, let $k_{ij} \ge 0$ be the rate constant of transfer from compartment $j$ to compartment $i$.
Let $k_{0j} \ge 0$ be the rate constant of elimination from compartment $j$, and let $u_i(t) \ge 0$ be the dosing rate into compartment $i$.
The *linear multi-compartment model* is the system of [[ordinary differential equations|0NT64JV96A]]
$$\frac{dx_i}{dt} = \sum_{j \ne i} k_{ij}\, x_j - \Big(k_{0i} + \sum_{j \ne i} k_{ji}\Big) x_i + u_i(t), \qquad i = 1, \dots, n.$$

## Remarks

In [[matrix|0VD9ZSWWJG]] form, $\dot x = K x + u$, where $K$ has nonnegative off-diagonal entries and column sums $-k_{0j} \le 0$.
Without dosing, $x(t) = e^{tK} x(0)$ with the [[matrix exponential|020M04FN1H]], so each $x_i$ is a combination of exponentials in the eigenvalues of $K$.
Example: the two-compartment model $\dot x_1 = -(k_{10} + k_{21}) x_1 + k_{12} x_2$, $\dot x_2 = k_{21} x_1 - k_{12} x_2$ is of this form with $k_{20} = 0$; after a bolus dose its plasma amount is $x_1(t) = A e^{-\alpha t} + B e^{-\beta t}$ with $\alpha > \beta > 0$ when $k_{10}, k_{12}, k_{21} > 0$.
Non-example: an elimination rate $V_{\max} x_1 / (K_m + x_1)$ of Michaelis–Menten type is nonlinear in $x_1$, so a model with it is not a linear compartment model.
The measured concentration is $x_i / V_i$, where $V_i$ is the volume of distribution of compartment $i$.
