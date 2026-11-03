---
tag: V82XMG8WPE
kind: statement
role: fact
name: Von Mises yield criterion
msc: [74C05]
uses: [CWWCEXZ8BH, X8AKXSA2RV, M6ZWV4Y29A, KG2XWEMJ30]
about: [CWWCEXZ8BH]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Mises_yield_criterion
same_as:
  wikidata: Q1319519
  wikipedia: Von Mises yield criterion
---

## Statement

Let an isotropic ductile material have yield stress $\sigma_y > 0$ in uniaxial tension.
Let $\sigma$ be the [[Cauchy stress tensor|KG2XWEMJ30]] at a point, $s = \sigma - \tfrac13 (\tr \sigma) I$ its [[deviatoric part|X8AKXSA2RV]], and $J_2 = \tfrac12 s : s$ the second invariant of $s$.
The von Mises criterion states that the material begins to yield at the point when
$$\sqrt{3 J_2} = \sigma_y.$$
In terms of the [[principal stresses|M6ZWV4Y29A]] $\sigma_1, \sigma_2, \sigma_3$ this reads
$$\sqrt{\tfrac12\left((\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2\right)} = \sigma_y.$$

## Remarks

The criterion is a constitutive assumption confirmed by experiments on metals, not a theorem.
The quantity $\sigma_{vM} = \sqrt{3J_2}$ is the von Mises equivalent stress; the [[yield surface|CWWCEXZ8BH]] $\sigma_{vM} = \sigma_y$ is a circular cylinder about the line $\sigma_1 = \sigma_2 = \sigma_3$.
Hydrostatic pressure has no effect, since $J_2$ does not change when a multiple of $I$ is added to $\sigma$.
Check in uniaxial tension, $\sigma_1 = \sigma$, $\sigma_2 = \sigma_3 = 0$: the left side is $\abs{\sigma}$, so yielding starts at $\sigma = \sigma_y$, as it should.
In pure shear, $\sigma_1 = \tau$, $\sigma_2 = 0$, $\sigma_3 = -\tau$: the left side is $\sqrt{3}\abs{\tau}$, so the shear yield stress is $\sigma_y / \sqrt{3}$.
$J_2$ is proportional to the elastic energy of distortion, the part of the strain energy that changes shape but not volume.
So the criterion is also called the distortion energy criterion.

## Explanations

### L1 human

The rule says that a metal starts to deform permanently when a certain combination of its stresses reaches the yield stress measured in a tensile test.
The combination measures how much the stress tries to change the shape of a small cube, and ignores how much it squeezes it uniformly.
So a metal under huge uniform pressure does not yield, while shear makes it yield easily.

### L2 human

The criterion is the standard yield condition for metals in engineering design and in finite element codes.
Combined with the associated flow rule it gives the Prandtl–Reuss equations, in which the plastic strain rate is parallel to the deviatoric stress and plastic flow keeps the volume constant.
It is smooth everywhere, which makes it easier to use than the Tresca criterion.
When both are matched in uniaxial tension, the Tresca hexagon lies inside the von Mises circle, and the two differ by at most about $15$ percent.
