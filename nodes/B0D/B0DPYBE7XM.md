---
tag: B0DPYBE7XM
kind: proof
name: Proof of Apollonius's theorem from the parallelogram law
msc: [51M04]
proves: 0NAKHQ9XYY
uses: [0S706JBZBG, 0NPPGHQNXQ, 0XKBKGTCPC, 026HPGYGS4]
sources:
  - url: https://en.wikipedia.org/wiki/Apollonius%27s_theorem
    locator: Statement and relation to other theorem
---

## Proof

We write the two sides from $A$ as a sum and a difference of two vectors.

1. By the definition of the [[midpoint|0S706JBZBG]], $D = B + \frac{1}{2}(C - B)$.
2. Let $m = D - A$ and $w = B - D$. By step 1, $w = -\frac{1}{2}(C - B)$ and $C - D = \frac{1}{2}(C - B) = -w$.
3. Then $B - A = (D - A) + (B - D) = m + w$ and $C - A = (D - A) + (C - D) = m - w$.
4. With the [[Euclidean distance|0NPPGHQNXQ]] and the [[length|0XKBKGTCPC]], $\abs{AB} = \norm{m + w}$, $\abs{AC} = \norm{m - w}$, $\abs{AD} = \norm{m}$ and $\abs{BD} = \norm{w}$.
5. $\R^n$ with the dot product is an inner product space with the norm $\norm{\cdot}$. By the [[parallelogram law|026HPGYGS4]], $\norm{m + w}^2 + \norm{m - w}^2 = 2 \norm{m}^2 + 2 \norm{w}^2$.
6. By step 4, this is $\abs{AB}^2 + \abs{AC}^2 = 2 \left( \abs{AD}^2 + \abs{BD}^2 \right)$.

## Idea

Seen from $A$, the vertices $B$ and $C$ sit at $m + w$ and $m - w$. Here $m$ goes to the midpoint and $w$ is half the side $BC$. The parallelogram law for $m$ and $w$ is then exactly the theorem.
