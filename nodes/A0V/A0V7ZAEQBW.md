---
tag: A0V7ZAEQBW
kind: statement
role: theorem
name: Landen's transformation
msc: ["33E05"]
uses: [NXMCYGCB59, RM54CPPE12]
about: [NXMCYGCB59, RM54CPPE12]
sources:
  - url: https://en.wikipedia.org/wiki/Landen%27s_transformation
same_as:
  wikidata: Q11347570
  wikipedia: Landen's transformation
---

## Statement

Let $0 < k < 1$, let $k' = \sqrt{1 - k^2}$, and let
$$k_1 = \frac{1 - k'}{1 + k'}.$$
Let $F(\varphi, k)$ be the incomplete [[elliptic integral|NXMCYGCB59]] of the first kind and $K(k) = F(\pi/2, k)$ the [[complete one|RM54CPPE12]].

1. For real $\varphi$, put $\varphi_1 = \varphi + \arctan(k'\tan\varphi)$, where the branch of $\arctan$ is chosen so that $\varphi_1$ depends continuously on $\varphi$ and $\varphi_1 = 0$ at $\varphi = 0$. Then
$$F(\varphi, k) = \frac{1 + k_1}{2} \, F(\varphi_1, k_1).$$
2. In particular $K(k) = (1 + k_1) \, K(k_1)$.

## Remarks

Part 2 is part 1 at $\varphi = \pi/2$, where $\varphi_1 = \pi$ and $F(\pi, k_1) = 2K(k_1)$.
Proof idea for part 1: differentiate both sides in $\varphi$ and check, with $\tan(\varphi_1 - \varphi) = k'\tan\varphi$, that the integrands agree; both sides vanish at $\varphi = 0$.
Check at small $k$: then $k' \approx 1$ and $k_1 \approx k^2/4 \approx 0$, so $\varphi_1 \approx 2\varphi$ and the right side is about $\frac12 \cdot 2\varphi = \varphi = F(\varphi, 0)$.
The modulus shrinks fast: $k_1 < k^2$ for $0 < k < 1$, since $k_1 = k^2/(1 + k')^2$.
Iterating part 2 sends the modulus to $0$ quadratically and gives $K(k) = \frac{\pi}{2}\prod_{n \ge 1} (1 + k_n)$, where $k_{n+1}$ is obtained from $k_n$ as $k_1$ from $k$.
In terms of the integral $I(a, b) = \int_0^{\pi/2} d\theta / \sqrt{a^2\cos^2\theta + b^2\sin^2\theta}$, the transformation reads $I(a, b) = I\big(\frac{a + b}{2}, \sqrt{ab}\big)$, which is the step behind the [[arithmetic–geometric mean formula|E0V3N93DX8]].

## Explanations

### L1 human

Landen's transformation changes the modulus of an elliptic integral into a much smaller one, at the cost of a simple factor and a new angle.
Doing it again and again makes the modulus tend to $0$, where the integral is just the angle itself.
This is an efficient way to compute elliptic integrals.

### L2 human

The complete form $K(k) = (1 + k_1)K(k_1)$ is equivalent to the identity $K(k) = \pi / (2M(1, k'))$ with the arithmetic–geometric mean $M$.
Indeed $k_1' = 2\sqrt{k'}/(1 + k')$, and the homogeneity $M(\lambda a, \lambda b) = \lambda M(a, b)$ gives $M(1, k_1') = \frac{2}{1 + k'} M(1, k')$.
Read backwards, with $k$ in place of $k_1$, it is the ascending Landen transformation, which pushes the modulus toward $1$.
For the theta-function side, Landen's transformation corresponds to replacing the nome $q$ by $q^2$, which doubles the ratio $K'/K$.
