---
tag: F81SBDRKJK
kind: definition
name: Dugdale strip-yield model
msc: [74R20, 74R10, 74C05]
defines: HAGWE563VF
uses: [7P2EGHZM7Q, 8D619PN75J, AS7WQTM99W]
sources:
  - url: https://en.wikipedia.org/wiki/Fracture_mechanics
---

## Definition

Consider an infinite thin plate in [[plane stress|AS7WQTM99W]], of an elastic–perfectly plastic material with yield stress $\sigma_Y$.
Let it contain a straight crack $\abs{x_1} < a$ on the $x_1$-axis.
Let it be loaded by a remote tension $\sigma$ perpendicular to the crack, with $0 < \sigma < \sigma_Y$.
The *Dugdale strip-yield model* replaces the plastic zones by two strips $a \le \abs{x_1} < a + \rho$ on the crack line.
It solves the linear elastic problem for a fictitious crack $\abs{x_1} < a + \rho$ such that:

1. the faces of the fictitious crack are free of traction on $\abs{x_1} < a$;
2. on the strips $a \le \abs{x_1} < a + \rho$ the faces carry a closing normal traction equal to $\sigma_Y$;
3. the length $\rho$ is chosen so that the total mode I [[stress intensity factor|8D619PN75J]] at the tips $x_1 = \pm(a + \rho)$ is zero.

## Remarks

Clause 3 gives the plastic zone length through
$$\frac{a}{a + \rho} = \cos\left( \frac{\pi \sigma}{2 \sigma_Y} \right).$$
Check for small loads: $\cos x \approx 1 - x^2/2$ gives $\rho \approx \frac{\pi^2 \sigma^2 a}{8 \sigma_Y^2} = \frac{\pi}{8} \left( \frac{K_I}{\sigma_Y} \right)^2$ with $K_I = \sigma \sqrt{\pi a}$, so the plastic zone is small compared with $a$.
As $\sigma \to \sigma_Y$, $\rho \to \infty$, which describes general yielding of the plate.
The opening of the fictitious crack at the physical tip $x_1 = a$ is $\delta = \frac{8 \sigma_Y a}{\pi E} \ln \sec\left( \frac{\pi \sigma}{2 \sigma_Y} \right)$, with $E$ the Young's modulus.
Non-example: the Irwin plastic zone correction, which only shifts the elastic crack tip by a length proportional to $(K_I / \sigma_Y)^2$, does not impose clause 2 and is not the Dugdale model.

## Explanations

### L1 human

Lengthen the crack by a strip on each side, and hold the faces of the strips together with the yield stress.
Choose the strip length so that the stress at the new tips is finite.
That is the Dugdale model of a plastic zone.
