---
tag: 7MJBYVB8WZ
kind: definition
name: Plasticity
msc: [74C05, 74C15]
defines: K8BBMTN0KV
uses: [8QS6QMJF5Z, KG2XWEMJ30, SX32X1D537, CWWCEXZ8BH]
sources:
  - url: https://en.wikipedia.org/wiki/Plasticity_(physics)
---

## Definition

Work in the small-strain setting, with [[strain tensor|8QS6QMJF5Z]] $\varepsilon(t)$ and [[stress tensor|KG2XWEMJ30]] $\sigma(t)$ at a material point, both symmetric $3 \times 3$ matrices depending on time $t$.
Let $C$ be an [[elasticity tensor|SX32X1D537]].
Let $K$ be a closed convex set of symmetric matrices with $0$ in its interior, the set of admissible stresses.
The pair $(C, K)$ defines a rate-independent *elastoplastic* material when:

1. The strain splits as $\varepsilon = \varepsilon^e + \varepsilon^p$ into an elastic strain $\varepsilon^e$ and a plastic strain $\varepsilon^p$.
2. The stress is $\sigma = C : \varepsilon^e = C : (\varepsilon - \varepsilon^p)$.
3. The stress stays admissible: $\sigma(t) \in K$ for all $t$.
4. The plastic strain can change only on the boundary of $K$, the [[yield surface|CWWCEXZ8BH]]: $\dot{\varepsilon}^p(t) = 0$ whenever $\sigma(t)$ is interior to $K$.

*Plasticity* is the behaviour described by such a model when $\varepsilon^p \ne 0$: the deformation that remains after the load is removed.

## Remarks

The model is completed by a flow rule for the direction of $\dot{\varepsilon}^p$ and, if $K$ changes with deformation, a hardening law.
Example: in one dimension, take $C = E > 0$ and $K = [-\sigma_y, \sigma_y]$.
Stretch a bar to strain $\varepsilon_1 > \sigma_y / E$: the stress stays at $\sigma_y$ and the plastic strain is $\varepsilon_1 - \sigma_y/E$.
Unloading to $\sigma = 0$ leaves the strain $\varepsilon_1 - \sigma_y / E > 0$, a permanent elongation.
Non-example: a linear elastic material corresponds to $K$ being the whole space; clause 4 then forces $\varepsilon^p$ to stay constant, so no permanent deformation arises.
Large-strain theories replace the additive split by a multiplicative decomposition of the deformation gradient.

## Explanations

### L1 human

The strain has an elastic part, which goes away when the load is removed, and a plastic part, which stays.
The plastic part can only grow when the stress reaches the yield limit.
