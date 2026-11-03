---
tag: 9MS4X2KC1H
kind: definition
name: Thermal runaway
msc: ["80A25", "80A19", 34A34]
defines: 1BSB9NDCWF
uses: [0P97V20RW7, 075VBY4K4X]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_runaway
---

## Definition

Consider a body with uniform temperature $T(t)$ and heat capacity $C > 0$.
Let $T_0 \in \R$, and let $G \colon [T_0, \infty) \to \R$ and $L \colon [T_0, \infty) \to \R$ be continuously differentiable.
Here $G(T)$ is the rate of heat production and $L(T)$ the rate of heat loss of the body at temperature $T$.
The temperature solves the [[ordinary differential equation|0P97V20RW7]]
$$C \frac{dT}{dt} = G(T) - L(T)$$
with the [[initial condition|075VBY4K4X]] $T(0) = T_0$.
The body is in *thermal runaway* from $T_0$ if $G(T) > L(T)$ for every $T \ge T_0$.
Equivalently, $G(T_0) > L(T_0)$ and there is no steady state $T^* \ge T_0$ with $G(T^*) = L(T^*)$.

## Remarks

In thermal runaway the solution is strictly increasing and unbounded on its maximal interval of existence.
Indeed, if it stayed bounded, it would converge to a limit $T_\infty \ge T_0$ with $G(T_\infty) = L(T_\infty)$, which is excluded.
Example: in the dimensionless Semenov model, $G(\theta) = \psi e^{\theta}$ and $L(\theta) = \theta$ with $\theta_0 = 0$ and a constant $\psi > 0$.
For $\psi = 1$ the condition holds, since $e^{\theta} > \theta$ for all $\theta$.
The temperature even blows up in finite time, because $\int_0^\infty d\theta / (e^\theta - \theta) < \infty$.
Non-example: for $\psi = 1/10$, one has $G(1) = e/10 < 1 = L(1)$, so the condition fails at $\theta = 1$.
Then $G - L$ changes sign on $[0, 1]$, there is a steady state there, and the temperature stays below it.
The word is also used more loosely for any rapid, self-accelerating rise of temperature.
