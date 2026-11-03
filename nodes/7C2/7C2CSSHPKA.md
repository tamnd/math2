---
tag: 7C2CSSHPKA
kind: statement
role: proposition
name: Bekenstein bound
msc: ["83C47", "81T20", "94A17"]
uses: [ANNJ7JR36T]
about: [ANNJ7JR36T]
sources:
  - url: https://en.wikipedia.org/wiki/Bekenstein_bound
same_as:
  wikidata: Q815018
  wikipedia: Bekenstein bound
---

## Statement

Let a physical system be contained in a sphere of radius $R$ and have total energy $E$, including its rest energy.
Let $\hbar$ be the reduced Planck constant, $c$ the speed of light and $k_B$ the Boltzmann constant.
Then its entropy $S$ satisfies
$$S \le \frac{2\pi k_B R E}{\hbar c}.$$

## Remarks

Bekenstein proposed the bound in 1981, arguing from the generalised second law: lowering the system into a black hole must not decrease the total entropy.
In this form it is a physical principle, and the quantities $S$, $E$ and $R$ need careful definitions for it to become a theorem.
In 2008 Casini gave a precise version in quantum field theory and proved it from the positivity of relative entropy.
In it, $S$ is a difference of entanglement entropies and $E$ is replaced by the expectation of a modular Hamiltonian.

Example: for a Schwarzschild black hole of mass $M$, take $R = 2GM/c^2$ and $E = Mc^2$.
The right side is $2\pi k_B (2GM/c^2)(Mc^2)/(\hbar c) = 4\pi k_B G M^2/(\hbar c)$.
This is exactly the [[Bekenstein–Hawking entropy|ANNJ7JR36T]] of the black hole, so black holes saturate the bound.

## Explanations

### L1 human

The bound says that a region of a given size holding a given amount of energy can store only a limited amount of information.
Doubling the size or doubling the energy doubles the limit.
Black holes reach the limit exactly.

### L2 human

The bound connects information theory, quantum field theory and gravity.
Its gravitational constant $G$ cancels, so it can be stated in flat spacetime, which is why it could be given a precise proof in quantum field theory.
It is one of the ideas behind the holographic principle, which bounds the entropy of a region by its boundary area.
