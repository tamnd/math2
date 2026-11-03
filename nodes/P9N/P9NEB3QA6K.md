---
tag: P9NEB3QA6K
kind: definition
name: Reynolds decomposition
msc: [76F02, 76F55]
defines: V47TX9AFKF
uses: [VY307F8Z0S]
sources:
  - url: https://en.wikipedia.org/wiki/Reynolds_decomposition
---

## Definition

Let $f(\mathbf{x}, t)$ and $g(\mathbf{x}, t)$ be flow quantities, such as velocity components, pressure or temperature, of a [[turbulent|VY307F8Z0S]] flow.
Let $f \mapsto \bar f$ be an averaging operation (a time average, a spatial average or an ensemble average) that satisfies the Reynolds rules:

1. $\overline{f + g} = \bar f + \bar g$ and $\overline{a f} = a \bar f$ for every constant $a$;
2. $\overline{\bar f g} = \bar f \, \bar g$, and in particular $\bar{\bar f} = \bar f$;
3. $\overline{\partial f / \partial x_i} = \partial \bar f / \partial x_i$ and $\overline{\partial f / \partial t} = \partial \bar f / \partial t$.

The *Reynolds decomposition* of $f$ is $f = \bar f + f'$, where $\bar f$ is the mean and $f' = f - \bar f$ is the fluctuation.

## Remarks

From the rules, $\overline{f'} = \bar f - \bar{\bar f} = 0$, and
$$\overline{f g} = \bar f \, \bar g + \overline{f' g'}.$$
The last term, the correlation of fluctuations, is in general not zero; for velocity components it gives the Reynolds stresses.

Example: the ensemble average over a probability space of flow realisations satisfies all three rules, since expectation is linear and commutes with derivatives of smooth fields.
Non-example: a spatial filter $\bar f = G * f$ with a smooth kernel $G$, as used in large eddy simulation, is linear and commutes with derivatives.
But in general $\bar{\bar f} \neq \bar f$, so it fails rule 2 and $\overline{f'} \neq 0$.
An average over a finite time window $T$ satisfies the rules only approximately, when $T$ is long compared with the fluctuations and short compared with changes of the mean.
