---
tag: VSX1B8H71A
kind: definition
name: Choked flow
msc: [76N15]
defines: 83Z3E8HMQ1
uses: [SH8FHGTMSE, GFHJ858AN1, SN4J6KP03C, FJC2GMVARF]
sources:
  - url: https://en.wikipedia.org/wiki/Choked_flow
---

## Definition

Consider steady, quasi-one-dimensional, [[isentropic|SH8FHGTMSE]] flow of an ideal gas through a duct with cross-section area $A(x)$.
The minimal area is $A^*$, at the throat, and the gas comes from a reservoir with stagnation pressure $p_0$ and stagnation temperature $T_0$.
Let $\gamma$ be the ratio of specific heats and $R$ the specific gas constant.
The mass flow rate $\dot m$ satisfies
$$\dot m \le \dot m_{\max} = A^* p_0 \sqrt{\frac{\gamma}{R T_0}} \left(\frac{2}{\gamma + 1}\right)^{(\gamma + 1)/(2(\gamma - 1))}.$$
The flow is *choked* when $\dot m = \dot m_{\max}$, which happens exactly when the [[Mach number|GFHJ858AN1]] at the throat equals $1$.

## Remarks

The bound comes from writing $\dot m = \rho u A$ in terms of the local Mach number $M$ with the isentropic relations: the mass flux $\rho u$ is largest at $M = 1$.
Example: air, $\gamma = 1.4$, flows from a tank through a converging nozzle.
The flow chokes when the outside pressure falls to $p^* = p_0 \left(\frac{2}{\gamma + 1}\right)^{\gamma/(\gamma - 1)} \approx 0.528\, p_0$, and below that pressure $\dot m$ stays equal to $\dot m_{\max}$.
Non-example: with outside pressure $0.8\, p_0$, the exit flow is subsonic, its Mach number is below $1$, and $\dot m < \dot m_{\max}$.
More generally, a steady [[compressible flow|FJC2GMVARF]] in a duct is called choked when it reaches $M = 1$ at a section.
It then carries the largest mass flow allowed by the upstream state.
Friction and heat addition in a constant-area duct can also cause choking.
