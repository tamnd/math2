---
tag: 4SVMG76QCH
kind: definition
name: Entropy
msc: [80A05, 80A10]
defines: SPY89W0RJ7
uses: [T8J5XRYBZZ, 5EKTEE00FZ, AJ8M9MGZGF, CY4GJQGF06, F3DHZ45H6A]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy
---

## Definition

Let $\Sigma$ be a closed thermodynamic system, and fix an [[equilibrium|5EKTEE00FZ]] state $A_0$ of $\Sigma$ and a real number $S_0$.
For an equilibrium state $A$, choose a [[reversible process|F3DHZ45H6A]] $\gamma$ from $A_0$ to $A$.
The *entropy* of $\Sigma$ in the state $A$ is
$$S(A) = S_0 + \int_\gamma \frac{\delta Q}{T}.$$
Here $\delta Q$ is the [[heat|CY4GJQGF06]] absorbed by $\Sigma$ along $\gamma$, and $T$ is the [[thermodynamic temperature|AJ8M9MGZGF]] of $\Sigma$.

## Remarks

By the Clausius theorem, $\oint \delta Q / T = 0$ around every reversible cycle, so $S(A)$ does not depend on the choice of $\gamma$.
So $S$ is a [[state function|T8J5XRYBZZ]], and $dS = \delta Q_{\mathrm{rev}} / T$.
For $n$ moles of ideal gas expanded reversibly at constant $T$ from $V_1$ to $V_2$, $Q = nRT \ln(V_2 / V_1)$, so $\Delta S = nR \ln(V_2 / V_1)$.
The free expansion of the same gas into a vacuum is not reversible, so the formula does not apply to it.
There $Q = 0$, but $\Delta S = nR \ln(V_2 / V_1) > 0$, as computed along a reversible path.
In statistical mechanics, $S = k_B \ln \Omega$, where $\Omega$ counts the microstates and $k_B$ is the Boltzmann constant.
