---
tag: R8PE771DDE
kind: definition
name: Linking number
msc: [57K10, 55M25]
defines: SFJ329YB9F
uses: [1A5WRCNTM3, M0Q5CFJ7ZH, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Linking_number
---

## Definition

Let $K_1$ and $K_2$ be disjoint oriented closed curves in $\R^3$, each the image of a smooth or piecewise-linear embedding of the circle.
The group $H_1(\R^3 \setminus K_2; \Z)$ of [[singular homology|M0Q5CFJ7ZH]] is infinite cyclic.
It has a preferred generator $\mu$, the class of a small circle that bounds a disc meeting $K_2$ once.
This circle is oriented by the right-hand rule with respect to the orientation of $K_2$.
The *linking number* $\operatorname{lk}(K_1, K_2)$ is the integer $m$ such that the class of $K_1$ in $H_1(\R^3 \setminus K_2; \Z)$ equals $m \mu$.

## Remarks

Equivalently, take a regular diagram of the [[link|1A5WRCNTM3]] $K_1 \cup K_2$ and give each crossing between $K_1$ and $K_2$ the sign $+1$ or $-1$ by the right-hand rule.
Then $\operatorname{lk}(K_1, K_2)$ is half the sum of these signs.
In this form one sees that $\operatorname{lk}(K_1, K_2) = \operatorname{lk}(K_2, K_1)$.

Example: in the Hopf link, the two circles cross twice in a standard diagram, and both crossings have the same sign.
So the linking number is $\pm 1$, the sign depending on the orientations.

Non-example of linking: in the unlink of two circles, the diagram has no crossings between the components, so the linking number is $0$.
The converse fails: the Whitehead link has linking number $0$, but its two components cannot be pulled apart.

For smooth curves $\gamma_1, \gamma_2$ parametrising $K_1, K_2$, the Gauss integral gives
$$\operatorname{lk}(K_1, K_2) = \frac{1}{4\pi} \oint_{\gamma_1} \oint_{\gamma_2} \frac{(\gamma_1 - \gamma_2) \cdot (d\gamma_1 \times d\gamma_2)}{\abs{\gamma_1 - \gamma_2}^3}.$$
