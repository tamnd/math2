---
tag: C2Q1RKZJ1Z
kind: definition
name: Viscoelasticity
msc: [74D05, 74D10]
defines: GCX1B3DAJN
uses: [Q4C55V47A8, HXGCGHS070, 8QS6QMJF5Z, YFTQJ7VY31]
sources:
  - url: https://en.wikipedia.org/wiki/Viscoelasticity
---

## Definition

Consider a material point with [[strain|8QS6QMJF5Z]] history $\varepsilon(s)$, $s \le t$, and [[stress|HXGCGHS070]] $\sigma(t)$ at time $t$.
The material is *viscoelastic* if its [[constitutive equation|Q4C55V47A8]] gives $\sigma(t)$ as a functional of the past strain history $\{\varepsilon(s) : s \le t\}$ that satisfies:

1. causality: $\sigma(t)$ depends only on $\varepsilon(s)$ for $s \le t$;
2. fading memory: strain at times far in the past has a vanishing effect on the present stress;
3. rate dependence: the response depends on the rate of loading, so that the material shows [[creep|YFTQJ7VY31]] under constant stress and stress relaxation under constant strain.

It is *linear viscoelastic* if moreover the functional is linear in the history and does not change under a shift of time.

## Remarks

Example: the law $\sigma(t) = \int_{-\infty}^t E e^{-(t - s)/\tau} \dot\varepsilon(s) \, ds$ with constants $E, \tau > 0$ is linear and causal, with fading memory through the decaying exponential.
It relaxes: for a strain step of size $\varepsilon_0$ at time $0$ it gives $\sigma(t) = E \varepsilon_0 e^{-t/\tau}$.
Non-example: Hooke's law $\sigma(t) = E \varepsilon(t)$ is causal and linear but has no rate dependence, since a constant strain gives a constant stress, so it is elastic and not viscoelastic.
In three dimensions the strain and stress are tensors and the linear law involves a tensor-valued relaxation function.
