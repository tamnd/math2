---
tag: HDQS5JAEVK
kind: definition
name: Coroot
msc: ["17B22", "17B20"]
defines: XV6Q01FVAS
uses: [AVVV93CASN, 0NB0AWGJBW]
sources:
  - url: https://en.wikipedia.org/wiki/Root_system
---

## Definition

Let $\Phi$ be a [[root system|AVVV93CASN]] in a Euclidean space $E$ with [[inner product|0NB0AWGJBW]] $(\cdot, \cdot)$.
The *coroot* of a root $\alpha \in \Phi$ is the vector
$$\alpha^\vee = \frac{2\alpha}{(\alpha, \alpha)} \in E.$$
The set $\Phi^\vee = \set{\alpha^\vee : \alpha \in \Phi}$ is the set of coroots.

## Remarks

With this notation $\langle \beta, \alpha \rangle = (\beta, \alpha^\vee)$, and the reflection in the hyperplane orthogonal to $\alpha$ is $s_\alpha(x) = x - (x, \alpha^\vee) \alpha$.
Example: in $B_2 = \set{\pm e_1, \pm e_2, \pm e_1 \pm e_2}$ in $\R^2$, the coroot of $e_1$ is $2 e_1$, and the coroot of $e_1 + e_2$ is $e_1 + e_2$, since $(e_1 + e_2, e_1 + e_2) = 2$.
So $\Phi^\vee = \set{\pm 2e_1, \pm 2e_2, \pm e_1 \pm e_2}$, a root system of type $C_2$.
Non-example: in $B_2$ the vector $e_1$ is not the coroot of $e_1$, since $(e_1, e_1) = 1$ and so $e_1^\vee = 2e_1$; a root equals its coroot only when $(\alpha, \alpha) = 2$.
Many authors see $\alpha^\vee$ instead as the linear form $x \mapsto 2(x, \alpha)/(\alpha, \alpha)$ on $E$, an element of the dual space $E^*$.
In general $\Phi^\vee$ is a root system, the *dual* or *inverse* root system, and $(\alpha^\vee)^\vee = \alpha$.

## Explanations

### L1 human

The coroot of a root is the same arrow rescaled so that its inner product with the root is $2$.
It is the natural tool to write the reflection in the mirror orthogonal to the root.
