---
tag: ZV1VB1KDV7
kind: proof
name: Proof of the exterior angle theorem from the angle sum
msc: [51M04]
proves: 0NTSE7EREA
uses: [0CTNFGYMM2, 0GJAJC6TNZ, 05MDKQBEAF, 0XKBKGTCPC, 0S52TNNTH9, 028XEQCE88, 01A8JGR4JM, 08WFZP6P89, 0CWDVN132S]
sources:
  - url: https://en.wikipedia.org/wiki/Exterior_angle_theorem
    locator: High school exterior angle theorem
---

## Proof

We show that the exterior angle and the interior angle at $C$ add up to $\pi$, and then use the angle sum.

1. Since $C$ lies strictly between $B$ and $D$, there is a real $\lambda$ with $0 < \lambda < 1$ and $C = (1 - \lambda) B + \lambda D$.
2. Then $C - B = \lambda (D - B)$ and $D - C = (1 - \lambda)(D - B)$. So $D - C = -\mu (B - C)$ with $\mu = (1 - \lambda)/\lambda > 0$.
3. The vertices of the [[triangle|0CTNFGYMM2]] are distinct, so $A \neq C$ and $B \neq C$. By step 2, also $D \neq C$. So the [[angles|0GJAJC6TNZ]] $\angle ACD$ and $\angle ACB$ are defined.
4. By the definition of the angle, with the [[dot product|0S52TNNTH9]] and the [[length|0XKBKGTCPC]],
$$\cos \angle ACD = \frac{(A - C) \cdot (D - C)}{\norm{A - C} \, \norm{D - C}} = \frac{-\mu \, (A - C) \cdot (B - C)}{\mu \, \norm{A - C} \, \norm{B - C}} = -\cos \angle ACB.$$
5. By the [[addition formula|028XEQCE88]], [[$\cos \pi = -1$ and $\sin \pi = 0$|01A8JGR4JM]], and the evenness of the [[cosine|08WFZP6P89]], $\cos(\pi - \angle ACB) = -\cos \angle ACB$.
6. Both $\angle ACD$ and $\pi - \angle ACB$ lie in $[0, \pi]$, and by steps 4 and 5 they have the same cosine.
7. The cosine is injective on $[0, \pi]$, by the uniqueness in the definition of the [[arccosine|0CWDVN132S]]. So $\angle ACD = \pi - \angle ACB$.
8. By the [[angle sum of a triangle|05MDKQBEAF]], $\pi - \angle ACB = \angle BAC + \angle CBA$.
9. Steps 7 and 8 give $\angle ACD = \angle BAC + \angle CBA$.

## Idea

The rays from $C$ to $B$ and from $C$ to $D$ point in opposite directions. So the exterior angle and the interior angle at $C$ fill a straight angle $\pi$. The other two interior angles fill the same gap, by the angle sum.
