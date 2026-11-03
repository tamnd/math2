---
tag: Y32EWAATPG
kind: definition
name: Root system
msc: ["17B22", "20F55"]
defines: AVVV93CASN
uses: [0XPR1E85W0, 0NB0AWGJBW, 06BRDF3F0E]
sources:
  - url: https://en.wikipedia.org/wiki/Root_system
    locator: Definition
---

## Definition

Let $E$ be a finite-dimensional real vector space with an [[inner product|0NB0AWGJBW]] $(\cdot, \cdot)$, a [[Euclidean space|0XPR1E85W0]].
For a nonzero $\alpha \in E$, let $s_\alpha(x) = x - \frac{2 (x, \alpha)}{(\alpha, \alpha)} \alpha$ be the [[reflection|06BRDF3F0E]] in the hyperplane orthogonal to $\alpha$.
A *root system* in $E$ is a finite subset $\Phi \subseteq E$ such that:

1. $\Phi$ spans $E$ and $0 \notin \Phi$;
2. for each $\alpha \in \Phi$, the only multiples of $\alpha$ in $\Phi$ are $\alpha$ and $-\alpha$;
3. for each $\alpha \in \Phi$, the reflection $s_\alpha$ maps $\Phi$ onto $\Phi$;
4. for all $\alpha, \beta \in \Phi$, the number $\langle \beta, \alpha \rangle = \frac{2 (\beta, \alpha)}{(\alpha, \alpha)}$ is an integer.

The elements of $\Phi$ are the *roots*, and $\dim E$ is the *rank* of $\Phi$.

## Remarks

Example: let $E$ be the plane $x_1 + x_2 + x_3 = 0$ in $\R^3$, with the standard basis $\varepsilon_1, \varepsilon_2, \varepsilon_3$ of $\R^3$.
The six vectors $\varepsilon_i - \varepsilon_j$ with $i \ne j$ form the root system $A_2$, whose roots point to the corners of a regular hexagon.
They span $E$; each $s_\alpha$ swaps two coordinates, so it permutes $\Phi$; and all numbers $\langle \beta, \alpha \rangle$ lie in $\set{0, \pm 1, \pm 2}$.
Non-example: with $e_1, e_2$ orthonormal, the set $\set{\pm e_1, \pm e_2, \pm (e_1 + e_2)}$ fails clause 3, since $s_{e_1}(e_1 + e_2) = -e_1 + e_2$ is not in the set.
Some authors drop clause 2 and call the systems that satisfy it *reduced*; then $\set{\pm e_1, \pm 2 e_1}$ in $\R$ is the non-reduced system $BC_1$.
Some authors also drop the spanning condition in clause 1.

## Explanations

### L1 human

A root system is a finite set of arrows that looks the same after reflection in the mirror orthogonal to any of its arrows.
The integrality condition forces the angle between two roots that are not multiples of each other to be one of $30^\circ, 45^\circ, 60^\circ, 90^\circ$ and their supplements.
