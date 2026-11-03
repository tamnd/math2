---
tag: 2N90MRJWMA
kind: definition
name: Adiabatic invariant
msc: [70H11]
defines: PY6R2DQN0W
uses: [0EDKGA2FAK, M3T81YNSKC]
sources:
  - url: https://en.wikipedia.org/wiki/Adiabatic_invariant
---

## Definition

Let $\Lambda \subseteq \R^k$ be open, and let $H(q, p, \lambda)$ be a smooth Hamiltonian on $V \times \Lambda$, with $V \subseteq \R^{2n}$ open.
Let $\lambda \colon [0, 1] \to \Lambda$ be smooth, and for $\varepsilon > 0$ consider the [[Hamiltonian system|0EDKGA2FAK]] with the slowly varying Hamiltonian $H\big(q, p, \lambda(\varepsilon t)\big)$ for $0 \le t \le 1/\varepsilon$.
Let $K \subseteq V$ be compact.
A function $I \colon V \times \Lambda \to \R$ is an *adiabatic invariant* (for the family $H$, the path $\lambda$ and the set $K$) when the following holds.
For every $\kappa > 0$ there is $\varepsilon_0 > 0$ such that, for every $\varepsilon \in (0, \varepsilon_0)$ and every solution $x(t) = (q(t), p(t))$ with $x(0) \in K$ that stays in $V$ for $0 \le t \le 1/\varepsilon$,
$$\abs{I\big(x(t), \lambda(\varepsilon t)\big) - I\big(x(0), \lambda(0)\big)} < \kappa \quad \text{for all } 0 \le t \le 1/\varepsilon.$$

## Remarks

Let $n = 1$.
Assume that for each frozen $\lambda$ the level curves of $H(\cdot, \lambda)$ in a region are closed curves around one equilibrium.
Assume also that the frequency of the motion on them is bounded away from $0$.
Finally, assume that the solutions stay in this region, so that they do not cross a separatrix.
Then the action $I = \frac{1}{2\pi} \oint_{H = E} p \, dq$ of the level curve through $(q, p)$ is an adiabatic invariant.
This is the basic theorem on adiabatic invariance of the [[action|M3T81YNSKC]].

Example: the oscillator $H = \frac{1}{2} p^2 + \frac{1}{2} \omega(\lambda)^2 q^2$ with $\omega > 0$.
Its level curve of energy $E$ is an ellipse of area $2 \pi E / \omega$, so its action is $I = E / \omega$.
This ratio is an adiabatic invariant.

Non-example: in the same system the energy $E$ itself is not an adiabatic invariant when $\omega$ really changes.
If $\omega$ goes slowly from $1$ to $2$, then $E / \omega$ stays nearly constant, so $E$ nearly doubles, and its change does not tend to $0$ as $\varepsilon \to 0$.
