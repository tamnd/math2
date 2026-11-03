---
tag: HMXJS7QFQN
kind: statement
role: proposition
name: Anderson's theory of faulting
msc: [86A60, 86A15]
uses: [M6ZWV4Y29A, Q5CF1Z6179, KG2XWEMJ30, DED41X44XM, AGM7AKCGPG]
about: [Q5CF1Z6179]
sources:
  - url: https://en.wikipedia.org/wiki/Anderson%27s_theory_of_faulting
same_as:
  wikidata: Q109544744
  wikipedia: Anderson's theory of faulting
---

## Statement

Let the stress in the upper crust be given by a [[Cauchy stress tensor|KG2XWEMJ30]] with [[principal stresses|M6ZWV4Y29A]] $\sigma_1 \geq \sigma_2 \geq \sigma_3$, compression positive.
Assume the Earth's surface is free of shear traction, so that one principal direction is vertical.
Assume new faults form according to the [[Mohr–Coulomb criterion|Q5CF1Z6179]] with coefficient of internal friction $\mu = \tan \phi$, $0 < \phi < 90^\circ$.
Then faults form on planes that contain the $\sigma_2$ direction and make the angle $45^\circ - \phi/2$ with the $\sigma_1$ direction, and:

1. if $\sigma_1$ is vertical, the faults are normal faults dipping at $45^\circ + \phi/2$;
2. if $\sigma_2$ is vertical, the faults are vertical strike-slip faults;
3. if $\sigma_3$ is vertical, the faults are reverse (thrust) faults dipping at $45^\circ - \phi/2$.

## Remarks

Proof idea: a free surface has zero shear traction, so the vertical is an eigenvector of the stress tensor.
Take a plane whose normal lies in the $\sigma_1 \sigma_3$ plane at angle $\beta$ to $\sigma_1$.
Its normal and shear stresses lie on [[Mohr's circle|DED41X44XM]] of $\sigma_1, \sigma_3$.
The Coulomb quantity $\tau - \mu \sigma_n$ is largest when $2\beta = 90^\circ + \phi$.
The intermediate stress $\sigma_2$ does not enter, so the failure plane contains the $\sigma_2$ direction, and it makes the angle $90^\circ - \beta = 45^\circ - \phi/2$ with $\sigma_1$.
Example: with $\mu = 0.6$, $\phi \approx 31^\circ$, so normal faults dip at about $60^\circ$ and thrust faults at about $30^\circ$, as often observed.
The theory is named after E. M. Anderson, who set it out in his work on the dynamics of faulting.
It describes new faults in homogeneous rock; slip on old weak faults of other orientations is not covered.

## Explanations

### L1 human

Near the ground, one of the three main squeezing directions in rock must point straight up.
Which one it is decides the kind of fault that forms.
If the strongest squeeze is vertical, the crust is being stretched and blocks slide down along steep normal faults.
If the weakest squeeze is vertical, the crust is being shortened and blocks are pushed up along shallow thrust faults.
If the middle one is vertical, blocks slide sideways past each other.

### L2 human

The theory combines a boundary condition, the traction-free surface, with the Mohr–Coulomb failure law.
It turns the observed type and dip of faults into information about the orientation of stress in the crust.
With [[Byerlee's law|AGM7AKCGPG]] for friction on existing faults, it also bounds the ratio of the largest and smallest principal stresses that the crust can support.
