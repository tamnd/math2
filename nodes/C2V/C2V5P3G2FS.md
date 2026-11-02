---
tag: C2V5P3G2FS
kind: example
name: Kuramoto model
msc: [34C15, 34D06, 92B25]
instance_of: [0673D85QKZ]
uses: [YP1PMW0HE3]
sources:
  - url: https://en.wikipedia.org/wiki/Kuramoto_model
same_as:
  wikidata: Q604374
  wikipedia: Kuramoto model
---

## Example

Let $N \ge 2$, let $K \ge 0$ be a coupling strength, and let $\omega_1, \ldots, \omega_N \in \R$ be natural frequencies.
The *Kuramoto model* is the [[autonomous system|0673D85QKZ]] for phases $\theta_1, \ldots, \theta_N \in \R / 2\pi\Z$:
$$\theta_i' = \omega_i + \frac{K}{N} \sum_{j=1}^{N} \sin(\theta_j - \theta_i), \qquad i = 1, \ldots, N.$$
Each oscillator turns at its own speed and is pulled towards the phases of the others.

For $N = 2$ the phase difference $\psi = \theta_2 - \theta_1$ satisfies
$$\psi' = (\omega_2 - \omega_1) - K \sin \psi.$$
If $K > 0$ and $K \ge \abs{\omega_2 - \omega_1}$, this equation has an equilibrium $\psi^*$ with $\sin \psi^* = (\omega_2 - \omega_1)/K$.
Then the two oscillators lock their phases at the difference $\psi^*$ and turn at the common speed $(\omega_1 + \omega_2)/2$.
If $K < \abs{\omega_2 - \omega_1}$, then $\psi' \ne 0$ always, and the phases drift apart.

## Remarks

The degree of synchrony is measured by the order parameter $r e^{i\phi} = \frac{1}{N} \sum_j e^{i \theta_j}$, with $0 \le r \le 1$.
With it the equations become $\theta_i' = \omega_i + K r \sin(\phi - \theta_i)$, so each oscillator couples only to the mean field.
In the limit $N \to \infty$ with frequencies drawn from a symmetric unimodal density $g$, a partially synchronized state with $r > 0$ appears when $K$ exceeds $K_c = 2 / (\pi g(0))$.
For the Lorentzian density $g(\omega) = \gamma / (\pi(\gamma^2 + \omega^2))$ this gives $K_c = 2\gamma$, and the stationary order parameter is $r = \sqrt{1 - K_c/K}$ for $K > K_c$.

Kuramoto introduced the model in 1975.
It is the basic model of [[synchronization|YP1PMW0HE3]] of oscillators in physics, chemistry and biology.

## Explanations

### L1 human

Picture many runners on a circular track, each with a favourite speed, and each slightly attracted to the others.
If the attraction is weak, they spread out and run independently.
If it is strong enough, a group forms that runs together, and the group grows as the attraction increases.
The Kuramoto model is the simplest equation that shows this sudden onset of collective rhythm, seen in fireflies flashing together and in pacemaker cells of the heart.
