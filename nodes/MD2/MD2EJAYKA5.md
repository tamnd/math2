---
tag: MD2EJAYKA5
kind: definition
name: Prandtl–Reuss equations
msc: [74C05]
defines: CE3FTDBTGJ
uses: [A3V75E17RS, 80NPDZSKBT, V82XMG8WPE, X8AKXSA2RV, V56XAESDNE, J2GWW1NPTC, PPXM3HCN6Y]
sources:
  - url: https://en.wikipedia.org/wiki/Flow_plasticity_theory
---

## Definition

Consider an isotropic material at small strains with [[shear modulus|J2GWW1NPTC]] $G$, [[bulk modulus|PPXM3HCN6Y]] $K$ and yield stress $\sigma_y > 0$.
Let $\sigma$ be the stress, $s = \sigma - \tfrac13 (\tr \sigma) I$ its [[deviatoric part|X8AKXSA2RV]] and $J_2 = \tfrac12 s : s$.
The *Prandtl–Reuss equations* are
$$\dot\varepsilon = \dot\varepsilon^e + \dot\varepsilon^p, \qquad \dot\varepsilon^e = \frac{\dot s}{2G} + \frac{\tr \dot\sigma}{9K} I, \qquad \dot\varepsilon^p = \dot\lambda \, s,$$
together with the [[von Mises condition|V82XMG8WPE]] $\sqrt{3 J_2} \le \sigma_y$ and the conditions $\dot\lambda \ge 0$, and $\dot\lambda = 0$ unless $\sqrt{3J_2} = \sigma_y$.

## Remarks

The elastic part is the rate form of [[Hooke's law|V56XAESDNE]].
The plastic part is the [[associated flow rule|80NPDZSKBT]] for the von Mises yield function, so the equations form a [[flow plasticity model|A3V75E17RS]].
Since $\tr s = 0$, plastic flow does not change the volume.
In perfect plasticity, the deviatoric part of the equations gives $\dot s = 2G(\dot e - \dot\lambda s)$, where $\dot e$ is the deviatoric part of $\dot\varepsilon$.
The consistency condition $s : \dot s = 0$ during plastic loading then gives $\dot\lambda = \dfrac{s : \dot\varepsilon}{s : s}$.
Example: in pure shear with $\sigma_{12} = \tau$ at yield, $\tau = \sigma_y / \sqrt3$, and $\dot\varepsilon_{12} = \dot\tau / (2G) + \dot\lambda \tau$.
Non-example: the Lévy–Mises equations $\dot\varepsilon = \dot\lambda s$ drop the elastic part, so they describe a rigid perfectly plastic material and are not the Prandtl–Reuss equations.

## Explanations

### L1 human

The strain rate is the elastic rate from Hooke's law plus a plastic rate parallel to the deviatoric stress.
The plastic rate is zero unless the stress is on the von Mises yield surface.
