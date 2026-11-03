---
tag: VXEK7KC7FZ
kind: statement
role: proposition
name: Murray's law
msc: [76Z05, 92C35, 92C10]
uses: [P27AH8WRRC, NM5Q4845Z4, T4ZV12BVHN]
about: [P27AH8WRRC]
sources:
  - url: https://en.wikipedia.org/wiki/Murray's_law
same_as:
  wikidata: Q6939074
  wikipedia: Murray's law
---

## Statement

Consider a network of rigid cylindrical vessels that carry a [[Newtonian fluid|T4ZV12BVHN]] of [[viscosity|NM5Q4845Z4]] $\mu > 0$ in steady laminar [[Poiseuille flow|P27AH8WRRC]].
For a vessel of length $\ell$ and radius $r$ carrying the volume flow rate $Q$, let the cost be
$$P(r) = \frac{8 \mu \ell Q^2}{\pi r^4} + b \, \pi r^2 \ell,$$
with a constant $b > 0$.
The first term is the power needed to drive the flow, and the second is a maintenance cost proportional to the volume of fluid.

1. For fixed $Q$ and $\ell$, the cost $P$ has a unique minimum over $r > 0$, at the radius with $Q = \frac{\pi}{4} \sqrt{b/\mu} \, r^3$.
2. Suppose every vessel has this optimal radius, and a parent vessel of radius $r_0$ splits into daughter vessels of radii $r_1, \dots, r_n$.
   Then conservation of the flow rate gives
   $$r_0^3 = r_1^3 + \cdots + r_n^3.$$

## Remarks

By Poiseuille's law the pressure drop is $\Delta p = 8 \mu \ell Q / (\pi r^4)$, so the pumping power is $Q \Delta p$, the first term of $P$.
Then $P'(r) = -32 \mu \ell Q^2/(\pi r^5) + 2 b \pi r \ell$, which vanishes exactly when $Q^2 = \pi^2 b r^6/(16 \mu)$; $P'$ is negative before and positive after this point, so it is the unique minimum.
Part 2 follows from $Q_0 = Q_1 + \cdots + Q_n$ and $Q_k \propto r_k^3$ with the same constant.
Example: a vessel splitting into two equal daughters has $r_1 = r_2 = 2^{-1/3} r_0 \approx 0.79 \, r_0$.
The hypotheses matter: for turbulent flow or for vessels with very different costs, the same optimisation gives a different exponent.
Cecil D. Murray derived the law in 1926 for blood vessels.

## Explanations

### L1 human

Narrow blood vessels make the heart work harder, but wide vessels hold more blood, which the body must make and maintain.
Murray asked what radius balances these two costs.
The answer is that the flow through a vessel should be proportional to the cube of its radius.
So at each branching the cube of the parent's radius equals the sum of the cubes of the children's radii.

### L2 human

It is a simple optimisation built on the Hagen–Poiseuille law, and it is a basic example of optimal transport networks in biology.
Since $Q \propto r^3$, the mean speed $Q / (\pi r^2)$ is proportional to $r$, and the wall shear stress $4 \mu Q / (\pi r^3)$ is the same in all vessels of an optimal network.
