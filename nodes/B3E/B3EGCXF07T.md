---
tag: B3EGCXF07T
kind: definition
name: Cohesive zone model
msc: [74R10, 74R20, 74A45]
defines: 7P2EGHZM7Q
uses: [SNRXGRZWR5, KG2XWEMJ30]
sources:
  - url: https://en.wikipedia.org/wiki/Cohesive_zone_model
---

## Definition

Let a body contain a surface $\Gamma$ along which a crack may open.
Let $\delta = [u] \cdot \nu$ be the normal opening, that is the jump of the displacement $u$ across $\Gamma$ in the direction of the unit normal $\nu$.
A *traction–separation law* is a function $T \colon [0, \infty) \to [0, \infty)$ and a number $\delta_c > 0$ such that:

1. $T(\delta) = 0$ for $\delta \ge \delta_c$;
2. $T$ is integrable, and $G_c = \int_0^{\delta_c} T(\delta) \, d\delta$ is positive.

A *cohesive zone model* is the boundary value problem of the body with the following condition on $\Gamma$.
Wherever $\delta > 0$, the normal [[traction|KG2XWEMJ30]] $\sigma \nu \cdot \nu$ on both faces of $\Gamma$ equals $T(\delta)$.
The *cohesive zone* is the part of $\Gamma$ where $0 < \delta < \delta_c$, and the crack is fully open where $\delta \ge \delta_c$.
The number $G_c$ is the *fracture energy* and $\max T$ is the *cohesive strength*.

## Remarks

Example: the linear softening law $T(\delta) = \sigma_c (1 - \delta / \delta_c)$ for $\delta < \delta_c$ satisfies both clauses, with $G_c = \sigma_c \delta_c / 2$.
Non-example: the law $T(\delta) = \sigma_c$ for all $\delta \ge 0$ fails clause 1, since the faces would never separate completely.
The Dugdale model uses the constant law $T = \sigma_Y$ on $[0, \delta_c)$, and the Barenblatt model uses a law derived from atomic cohesion.
Tangential tractions and unloading rules are added in mixed-mode and cyclic versions of the model.

## Explanations

### L1 human

The model says how the force between two crack faces depends on how far apart they are.
The force vanishes once the opening reaches a critical value, and the work needed to get there is the fracture energy.
