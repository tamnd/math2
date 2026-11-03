---
tag: MZPYYMSVEJ
kind: definition
name: Lumped-element thermal model
msc: [80A19, 34A30]
defines: EB1DQP2E0K
uses: [J821AD6YTE, SYYGZ18FF5, ZYJRK1RVP5, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Lumped-element_model
---

## Definition

Let a solid body have volume $V$, surface area $A$, density $\rho$ and specific [[heat capacity|SYYGZ18FF5]] $c$.
Let it exchange heat with a fluid at constant temperature $T_\infty$.
Let $h > 0$ be the [[heat transfer coefficient|J821AD6YTE]] on its surface.
The *lumped-element thermal model* assumes that the temperature of the body is uniform, equal to $T(t)$ at time $t$.
It is the [[ordinary differential equation|0NT64JV96A]]
$$\rho \, c \, V \, \frac{dT}{dt} = -h A \left(T - T_\infty\right).$$

## Remarks

The solution with $T(0) = T_0$ is $T(t) = T_\infty + (T_0 - T_\infty) e^{-t / \tau}$, with time constant $\tau = \rho c V / (h A)$.
Indeed $T'(t) = -(T_0 - T_\infty) e^{-t/\tau} / \tau = -(T - T_\infty) / \tau$, which is the equation divided by $\rho c V$.

Example: a ball with $\tau = 100$ seconds, $T_0 = 80$ and $T_\infty = 20$ degrees Celsius reaches $20 + 60 e^{-1} \approx 42$ degrees Celsius after $100$ seconds.

Non-example: a thick block of wood cooled in strong wind has a large [[Biot number|ZYJRK1RVP5]].
Its centre stays much hotter than its surface, so the uniform temperature assumption fails.

The usual criterion for the model is $\mathrm{Bi} < 0.1$ with length $V / A$.
