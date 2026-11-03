---
tag: C2G7Q6TSYY
kind: definition
name: Amplitude versus offset
msc: [86A15, 86A22, 74J20]
defines: GMMXM831K6
uses: [QQQJM3SA2C, JAFNCJNF6E, EEPJJHC5JZ]
sources:
  - url: https://en.wikipedia.org/wiki/Amplitude_versus_offset
---

## Definition

Let a flat interface separate two isotropic elastic media with P-speeds $\alpha_1, \alpha_2$, S-speeds $\beta_1, \beta_2$ and densities $\rho_1, \rho_2$.
Let $R_{PP}(\theta)$ be the reflection coefficient of a [[P-wave|EEPJJHC5JZ]] incident at the angle $\theta$, given by the [[Zoeppritz equations|QQQJM3SA2C]].
*Amplitude versus offset* is the dependence of $R_{PP}$ on $\theta$.
It is observed as the dependence of the reflected amplitude on the source–receiver offset in a common-midpoint gather.
*AVO analysis* estimates from it the contrasts of $\alpha$, $\beta$ and $\rho$ at the interface.

## Remarks

Let $\alpha, \beta, \rho$ be the averages of the two media and $\Delta\alpha = \alpha_2 - \alpha_1$, $\Delta\beta = \beta_2 - \beta_1$, $\Delta\rho = \rho_2 - \rho_1$.
For small contrasts the Aki–Richards approximation is
$$R_{PP}(\theta) \approx \frac12\Big(1 - 4\beta^2 p^2\Big)\frac{\Delta\rho}{\rho} + \frac{1}{2\cos^2\theta}\frac{\Delta\alpha}{\alpha} - 4\beta^2 p^2 \frac{\Delta\beta}{\beta},$$
where $p = \sin\theta/\alpha$ is the [[ray parameter|JAFNCJNF6E]] and $\theta$ is the average of the incidence and transmission angles.
Keeping terms up to $\sin^2\theta$ gives the two-term form $R_{PP}(\theta) \approx A + B\sin^2\theta$, with intercept $A = \frac12(\Delta\alpha/\alpha + \Delta\rho/\rho)$ and gradient $B = \frac12 \Delta\alpha/\alpha - 2(\beta/\alpha)^2(\Delta\rho/\rho + 2\Delta\beta/\beta)$.
The check: $4\beta^2p^2 = 4(\beta/\alpha)^2\sin^2\theta$ and $1/\cos^2\theta = 1 + \tan^2\theta \approx 1 + \sin^2\theta$.
Example: if only $\alpha$ drops across the interface, $\Delta\alpha < 0$ and $\Delta\beta = \Delta\rho = 0$, then $A < 0$ and $B < 0$, so the negative reflection grows in size with offset.
Non-example: the amplitude change caused by geometric spreading of the wavefront also depends on offset, but it is not AVO; it is removed before the analysis.
