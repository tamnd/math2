---
tag: MAHDE6JZYT
kind: statement
role: theorem
name: Maxwell relations
msc: [80A10, 80A05]
uses: [41NHDR6MH6, F6JVQ12X43, 722RZK72P5, JXKY6C8JTA, RBG5ZBM35Y, 01V9FPBBVK, 09EGC6F8PT]
about: [MKZW03Q590]
sources:
  - url: https://en.wikipedia.org/wiki/Maxwell_relations
same_as:
  wikidata: Q187465
  wikipedia: Maxwell relations
---

## Statement

Let a closed simple system have temperature $T$, entropy $S$, pressure $p$ and volume $V$.
Suppose that its [[internal energy|F6JVQ12X43]] $U(S, V)$, [[enthalpy|722RZK72P5]] $H(S, p)$, [[Helmholtz free energy|JXKY6C8JTA]] $F(T, V)$ and [[Gibbs free energy|RBG5ZBM35Y]] $G(T, p)$ are twice continuously differentiable in their natural variables.
Then the [[partial derivatives|09EGC6F8PT]] satisfy

1. $\left(\dfrac{\partial T}{\partial V}\right)_S = -\left(\dfrac{\partial p}{\partial S}\right)_V$,
2. $\left(\dfrac{\partial T}{\partial p}\right)_S = \left(\dfrac{\partial V}{\partial S}\right)_p$,
3. $\left(\dfrac{\partial S}{\partial V}\right)_T = \left(\dfrac{\partial p}{\partial T}\right)_V$,
4. $\left(\dfrac{\partial S}{\partial p}\right)_T = -\left(\dfrac{\partial V}{\partial T}\right)_p$.

A subscript names the variable held fixed.

## Remarks

The [[fundamental relation|41NHDR6MH6]] gives $dU = T \, dS - p \, dV$, $dH = T \, dS + V \, dp$, $dF = -S \, dT - p \, dV$ and $dG = -S \, dT + V \, dp$.
So, for instance, $T = (\partial U / \partial S)_V$ and $-p = (\partial U / \partial V)_S$.
Each relation is the [[equality of mixed second derivatives|01V9FPBBVK]] of one potential: relation 1 for $U$, 2 for $H$, 3 for $F$ and 4 for $G$.
Example: for an ideal gas, $p = nRT / V$, so relation 3 gives $(\partial S / \partial V)_T = nR / V$.
Integrating, an isothermal expansion from $V_1$ to $V_2$ raises the entropy by $nR \ln(V_2 / V_1)$.

## Explanations

### L1 human

The Maxwell relations link quantities that look unrelated.
For example, how much the entropy of a gas grows when it expands at fixed temperature equals how fast its pressure rises when it is heated at fixed volume.
The second is easy to measure, the first is not.

### L2 human

The relations turn derivatives of the entropy, which cannot be measured directly, into derivatives of $p$, $V$ and $T$, which can.
With them one derives, for example, the difference $C_p - C_V = T V \alpha^2 / \kappa_T$ of the heat capacities, where $\alpha$ is the thermal expansion coefficient and $\kappa_T$ the isothermal compressibility.
For systems with more variables, such as magnetic systems or open systems, each potential gives further Maxwell relations in the same way.
