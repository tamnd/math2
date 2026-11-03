---
tag: 12EPT5G5QV
kind: definition
name: Zeldovich–von Neumann–Döring detonation model
msc: [76L05, 80A25, 76V05]
defines: 8KJJKCR26M
uses: [FBR0PYYJJ7, FRVV0NHBXT, S4XMYJ3V42, RW0JK9VDZE]
sources:
  - url: https://en.wikipedia.org/wiki/ZND_detonation_model
---

## Definition

Consider a gas mixture with one irreversible reaction, described by a progress variable $\lambda \in [0, 1]$, with $\lambda = 0$ unburnt and $\lambda = 1$ burnt, and heat of reaction $q > 0$.
The reaction rate is a given function $\omega(p, v, \lambda) \ge 0$ of the pressure, the specific volume and $\lambda$.
The *ZND model* of a [[detonation|FBR0PYYJJ7]] with speed $D$ is a steady planar flow, seen in a frame moving with the front.
It consists of the following parts.

1. Ahead of the front, the unburnt gas is uniform, with state $(p_1, v_1)$ and $\lambda = 0$.
2. At the front there is a non-reacting [[shock wave|FRVV0NHBXT]]. Its jump conditions take the gas to the von Neumann state on the Rayleigh line $p - p_1 = -m^2 (v - v_1)$, where $m = D / v_1$.
3. Behind the shock there is a reaction zone, where the one-dimensional reactive [[Euler equations|RW0JK9VDZE]] hold. In this zone the gas moves along the same Rayleigh line, and $\lambda$ grows from $0$ to $1$ by $d\lambda / dt = \omega$ along particle paths.

## Remarks

In the reaction zone the state at progress $\lambda$ lies on the intersection of the Rayleigh line with the partial Hugoniot curve with heat release $\lambda q$.
At $\lambda = 1$ the gas reaches the full reactive Hugoniot curve.
A steady solution reaching $\lambda = 1$ exists for $D \ge D_{CJ}$ under the usual convexity assumptions, and for $D = D_{CJ}$ the final state is the Chapman–Jouguet state, where the flow is sonic.

Example: take a mixture whose rate $\omega$ is positive for $\lambda < 1$, and the Chapman–Jouguet speed.
In the ZND wave the pressure jumps at the shock to the von Neumann spike.
Then it decreases monotonically to the Chapman–Jouguet pressure as $\lambda$ increases to $1$.

Non-example: the Chapman–Jouguet model, which treats the detonation as a single discontinuity from the unburnt to the burnt state, has no reaction zone and fails clause 3.
