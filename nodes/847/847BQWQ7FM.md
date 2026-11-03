---
tag: 847BQWQ7FM
kind: definition
name: Gamma-convergence derivation of plate models
msc: [74K20, 49J45, 74B20]
defines: 576B3924C9
uses: [NW9MM370A5, ZHK2EVRD90]
sources:
  - url: https://en.wikipedia.org/wiki/Γ-convergence
---

## Definition

Let $S \subset \R^2$ be a bounded Lipschitz domain and, for $h > 0$, let $\Omega_h = S \times (-h/2, h/2)$ be a plate of thickness $h$.
Let $W \colon \R^{3 \times 3} \to [0, \infty]$ be the stored energy density of a [[hyperelastic material|ZHK2EVRD90]].
The elastic energy per unit thickness of a deformation $v \colon \Omega_h \to \R^3$ is
$$E_h(v) = \frac{1}{h} \int_{\Omega_h} W(\nabla v) \, dx.$$
For a deformation $y$ of the fixed domain $\Omega_1$, set $I_h(y) = E_h(v)$, where $v(x_1, x_2, x_3) = y(x_1, x_2, x_3 / h)$.
Fix a topology on deformations in which sequences $y_h$ with bounded scaled energy $h^{-\beta} I_h(y_h)$ are compact.
A *Γ-convergence derivation of a plate model* is the choice of an exponent $\beta \ge 0$ and the computation of the [[Γ-limit|NW9MM370A5]]
$$I = \Gamma\text{-}\lim_{h \to 0} h^{-\beta} I_h.$$
The functional $I$, which depends only on a map from $S$ to $\R^3$, is the energy of the derived plate model.

## Remarks

Take $\beta = 2$ and a frame-indifferent material $W$ that vanishes exactly on the rotation group $SO(3)$ and grows quadratically with the distance to $SO(3)$.
Then the limit is the nonlinear bending theory of plates.
Its domain is the set of $W^{2,2}$ isometric immersions $u \colon S \to \R^3$, and $I(u) = \frac{1}{24} \int_S Q_2(\nabla u^T \nabla \nu) \, dx'$.
Here $\nu$ is the unit normal of $u(S)$, and $Q_2$ is a quadratic form computed from the second derivative of $W$ at the identity.
The key tool for this result is the geometric rigidity estimate of Friesecke, James and Müller.
For $\beta = 0$ the limit is a membrane theory, in which bending costs no energy.
A non-example is the classical derivation of the [[Kirchhoff–Love plate|9E6E0SCEYA]] by assuming that normals stay normal: it postulates the form of the deformation instead of proving the convergence of minimizers.

## Explanations

### L1 human

Write down the energy of a thin slab, rescale the thickness to one, divide by the right power of the thickness, and let the thickness go to zero.
What remains is a functional of the mid-surface alone.
That functional is the plate model, and Γ-convergence guarantees that its minimizers describe the thin three-dimensional body.
