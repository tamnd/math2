---
tag: 092S6VBECQ
kind: definition
name: Lyapunov stability
aliases: [stable-equilibrium]
msc: [34D20]
defines: 0F2SYCKDT2
uses: [0G4X36AE0X, 02903SSA48]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_stability
    locator: Definition for continuous-time systems
---

## Definition

Let $U$ be an open subset of $\mathbb{R}^n$, let $f : U \to \mathbb{R}^n$ be locally Lipschitz. Let $\varphi$ be the [[flow|02903SSA48]] of $x' = f(x)$, and let $x^* \in U$ be an [[equilibrium point|0G4X36AE0X]].
The point $x^*$ is Lyapunov stable if for each $\varepsilon > 0$ there is a $\delta > 0$ with this property. For each $x_0 \in U$ with $\|x_0 - x^*\| < \delta$, the solution $\varphi_t(x_0)$ exists for all $t \ge 0$, and $\|\varphi_t(x_0) - x^*\| < \varepsilon$ for all $t \ge 0$.
The point $x^*$ is unstable if it is not Lyapunov stable.

## Remarks

For $x' = -x$ and for $x' = 0$ on $\mathbb{R}$, the equilibrium $0$ is stable. For $x' = x$, it is unstable.
The centre of the [[harmonic oscillator|0YG0ZJPTWG]] is stable but not [[asymptotically stable|05Y1JAM3Y5]]: nearby solutions stay near, but they do not approach it.
A [[Lyapunov function|04P7B5XC22]] gives a way to prove stability without solving the equation.

## Explanations

### L1 human

An equilibrium is stable if solutions that start close to it stay close to it forever.
To stay within distance $\varepsilon$, it is enough to start within a smaller distance $\delta$.
