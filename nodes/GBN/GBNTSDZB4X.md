---
tag: GBNTSDZB4X
kind: definition
name: Nonlinear susceptibility
msc: [78A60]
defines: 7N71T3FKZ6
uses: [SZA12YB8V2, ASQAH710WN, YZ7Q9DP8RT]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_optics
---

## Definition

Consider a medium of [[nonlinear optics|SZA12YB8V2]] with an instantaneous and local response.
So the [[polarization density|ASQAH710WN]] $\mathbf{P}$ at a point is a smooth function of the [[electric field|YZ7Q9DP8RT]] $\mathbf{E}$ at that point, with $\mathbf{P}(\mathbf{0}) = \mathbf{0}$.
Let $\varepsilon_0$ be the vacuum permittivity, and expand $\mathbf{P}$ in a power series:
$$P_i = \varepsilon_0 \sum_{n \ge 1} \sum_{j_1, \dots, j_n} \chi^{(n)}_{i j_1 \cdots j_n} E_{j_1} \cdots E_{j_n}.$$
Here each tensor $\chi^{(n)}$ has $3^{n+1}$ components, and it can be chosen symmetric in its last $n$ indices, since the product $E_{j_1} \cdots E_{j_n}$ is.
For $n \ge 2$, $\chi^{(n)}$ is the *nonlinear susceptibility of order $n$*.
With this choice, $\varepsilon_0 \chi^{(n)}$ is $1/n!$ times the $n$-th derivative of $\mathbf{P}$ at $\mathbf{E} = \mathbf{0}$.

## Remarks

For a dispersive medium the response depends on frequency, and one writes $\chi^{(2)}(\omega_1 + \omega_2; \omega_1, \omega_2)$ and so on, for the response at frequency $\omega_1 + \omega_2$ to fields at $\omega_1$ and $\omega_2$.

Example: if the medium is invariant under the inversion $\mathbf{r} \mapsto -\mathbf{r}$, then $\mathbf{P}(-\mathbf{E}) = -\mathbf{P}(\mathbf{E})$.
The even-order terms must then vanish, so $\chi^{(2)} = 0$, while $\chi^{(3)}$ may be non-zero.
This is the case for glass and for liquids.

Non-example: a medium whose polarization depends on the field at earlier times, with a delay, has no single instantaneous tensor $\chi^{(n)}$.
It needs the frequency-dependent form of the remark above.
