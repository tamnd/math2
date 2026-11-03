---
tag: 8RTXDZAPRJ
kind: definition
name: Alfvén wave
msc: [76W05, 76X05, "76E25"]
defines: 8CQDTE19FW
uses: [ZSA13P8P81, T8JWCBK9M6, 2JZ0C15A9C]
sources:
  - url: https://en.wikipedia.org/wiki/Alfvén_wave
---

## Definition

Consider incompressible [[ideal MHD|ZSA13P8P81]] with constant density $\rho_0 > 0$, linearised about the state of rest in the uniform field $B_0 \mathbf{e}_z$ with $B_0 > 0$.
Let $\mu_0$ be the magnetic permeability and define the *Alfvén speed* $v_A = B_0 / \sqrt{\mu_0 \rho_0}$.
An *Alfvén wave* is a solution of the linearised system of the following form.
The velocity $\mathbf{u}$ and the field perturbation $\mathbf{b}$ are perpendicular to $\mathbf{e}_z$, and
$$\mathbf{u} = \mathbf{U} \cos(\mathbf{k} \cdot x - \omega t), \qquad \mathbf{b} = -\frac{B_0 (\mathbf{k} \cdot \mathbf{e}_z)}{\omega} \, \mathbf{U} \cos(\mathbf{k} \cdot x - \omega t),$$
with $\mathbf{U} \perp \mathbf{e}_z$, $\mathbf{U} \perp \mathbf{k}$, and frequency given by the dispersion relation
$$\omega^2 = v_A^2 \, (\mathbf{k} \cdot \mathbf{e}_z)^2.$$

## Remarks

Check for $\mathbf{k} = k \mathbf{e}_z$ and $\mathbf{U} = U \mathbf{e}_x$: the linearised equations are $\rho_0 \partial_t \mathbf{u} = -\nabla p^* + (B_0/\mu_0) \partial_z \mathbf{b}$ and $\partial_t \mathbf{b} = B_0 \partial_z \mathbf{u}$, where $p^*$ is the total pressure perturbation.
With $p^* = 0$ and $\mathbf{b} = b \, \mathbf{e}_x \cos(kz - \omega t)$, the second gives $\omega b = -k B_0 U$, and the first gives $\rho_0 \omega U = -k B_0 b / \mu_0$; together $\omega^2 = k^2 B_0^2 / (\mu_0 \rho_0)$.
For $\omega = k v_A$ this gives $\mathbf{b} = -\sqrt{\mu_0 \rho_0} \, \mathbf{u}$.
The group velocity is $\pm v_A \mathbf{e}_z$ for every $\mathbf{k}$, the sign being that of $\omega / (\mathbf{k} \cdot \mathbf{e}_z)$, so energy always travels along the background field.
Non-example: if $B_0 = 0$, then $v_A = 0$ and there is no oscillation; the perturbation does not propagate.
In compressible MHD there are also the fast and slow magnetosonic waves, which compress the fluid and are different from Alfvén waves.
