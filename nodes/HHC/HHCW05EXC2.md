---
tag: HHCW05EXC2
kind: definition
name: Alpha effect of mean-field dynamo theory
msc: [76W05, 86A25]
defines: ARBT22HW3S
uses: [T8JWCBK9M6, AFVDBT0K5C, 0NF6GQNXMY]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamo_theory
---

## Definition

Let $\mathbf{u}$ and $\mathbf{B}$ be the velocity and magnetic field of a conducting fluid with magnetic diffusivity $\eta$.
They are related by the induction equation of [[magnetohydrodynamics|T8JWCBK9M6]].
Fix an averaging operation $\langle \cdot \rangle$ (over space, time or an ensemble) that commutes with derivatives.
Write $\mathbf{u} = \overline{\mathbf{U}} + \mathbf{u}'$ and $\mathbf{B} = \overline{\mathbf{B}} + \mathbf{b}'$ with $\overline{\mathbf{U}} = \langle \mathbf{u} \rangle$ and $\overline{\mathbf{B}} = \langle \mathbf{B} \rangle$.
The *mean electromotive force* is $\boldsymbol{\mathcal{E}} = \langle \mathbf{u}' \times \mathbf{b}' \rangle$.
Assume the fluctuations are statistically homogeneous and isotropic, but not mirror symmetric, and that $\boldsymbol{\mathcal{E}}$ depends linearly on $\overline{\mathbf{B}}$ and its first derivatives.
Then
$$\boldsymbol{\mathcal{E}} = \alpha \overline{\mathbf{B}} - \beta \, \nabla \times \overline{\mathbf{B}}$$
for scalars $\alpha$ and $\beta$.
The *alpha effect* is the term $\alpha \overline{\mathbf{B}}$, and $\alpha$ is the *alpha coefficient*.

## Remarks

The mean field then obeys
$$\frac{\partial \overline{\mathbf{B}}}{\partial t} = \nabla \times \big( \overline{\mathbf{U}} \times \overline{\mathbf{B}} + \alpha \overline{\mathbf{B}} \big) + (\eta + \beta) \nabla^2 \overline{\mathbf{B}},$$
where $\nabla \times$ is the [[curl|0NF6GQNXMY]] and $\alpha, \beta$ are taken constant.
The term $\beta$ is the turbulent diffusivity.
In the first-order smoothing approximation with correlation time $\tau$, $\alpha \approx -\tfrac{\tau}{3} \langle \mathbf{u}' \cdot (\nabla \times \mathbf{u}') \rangle$, minus a third of $\tau$ times the mean kinetic helicity.
Example: with constant $\alpha \neq 0$, $\overline{\mathbf{U}} = 0$ and $\eta + \beta = \eta_T$, the field $\overline{\mathbf{B}} = e^{\gamma t}(\sin kz, \cos kz, 0)$ satisfies $\nabla \times \overline{\mathbf{B}} = k \overline{\mathbf{B}}$, and the equation gives $\gamma = \alpha k - \eta_T k^2$, which is positive for $0 < k < \alpha/\eta_T$ when $\alpha > 0$; this is an $\alpha^2$ dynamo.
Non-example: for mirror-symmetric turbulence $\alpha = 0$, and with $\overline{\mathbf{U}} = 0$ only the diffusive term remains, so the mean field decays.
The theory was developed by Steenbeck, Krause and Rädler in 1966; see [[dynamo theory|AFVDBT0K5C]].
