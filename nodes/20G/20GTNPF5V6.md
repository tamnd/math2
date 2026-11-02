---
tag: 20GTNPF5V6
kind: statement
role: theorem
name: Berger's classification of holonomy groups
msc: [53C29]
uses: [WHDZ3MK56B, 7CBT4SM83Y, CAZYGE1T4E, PAA93R4WYD]
about: [WHDZ3MK56B]
sources:
  - url: https://en.wikipedia.org/wiki/Holonomy
---

## Statement

Let $(M, g)$ be a simply connected Riemannian manifold of dimension $n$ with [[Levi-Civita connection|CAZYGE1T4E]] $\nabla$, and let $p \in M$.
Assume that the [[holonomy group|WHDZ3MK56B]] $\mathrm{Hol}_p(\nabla)$ acts irreducibly on $T_pM$, and that $(M, g)$ is not locally [[symmetric|PAA93R4WYD]], that is, $\nabla R \ne 0$ for its curvature tensor $R$.
Then $\mathrm{Hol}_p(\nabla)$, as a subgroup of $\mathrm{O}(T_pM) \cong \mathrm{O}(n)$, is conjugate to one of the following:

1. $\mathrm{SO}(n)$;
2. $\mathrm{U}(m)$, with $n = 2m \ge 4$;
3. $\mathrm{SU}(m)$, with $n = 2m \ge 4$;
4. $\mathrm{Sp}(k) \cdot \mathrm{Sp}(1)$, with $n = 4k \ge 8$;
5. $\mathrm{Sp}(k)$, with $n = 4k \ge 8$;
6. $G_2$, with $n = 7$;
7. $\mathrm{Spin}(7)$, with $n = 8$.

## Remarks

Berger's proof combines the Ambrose–Singer theorem with the Bianchi identity: the holonomy algebra must be spanned by curvature-type tensors.
Berger checked which irreducible subgroups of $\mathrm{SO}(n)$ admit enough of them while allowing $\nabla R \ne 0$.
Berger's original list also contained $\mathrm{Spin}(9)$ in dimension $16$; later work showed that such a metric is locally symmetric, so this case drops out.
All seven groups do occur; the existence of metrics with holonomy $G_2$ and $\mathrm{Spin}(7)$ was shown much later, first locally by Bryant and then on compact manifolds by Joyce.
The hypotheses are needed.
By the de Rham decomposition theorem, a reducible holonomy splits $M$ locally as a product.
A locally symmetric space can have the holonomy of its isotropy group, which is not in this list in general.
The geometric meaning: $\mathrm{U}(m)$ gives Kähler manifolds, $\mathrm{SU}(m)$ Ricci-flat Kähler (Calabi–Yau) manifolds, $\mathrm{Sp}(k)$ hyperkähler manifolds, and $\mathrm{Sp}(k)\cdot\mathrm{Sp}(1)$ quaternion-Kähler manifolds.

## Explanations

### L1 human

Every curved space has a holonomy group, which records how directions turn when carried around loops.
For a typical space this is the whole rotation group.
Berger's theorem says that, apart from products and highly symmetric spaces, only seven kinds of holonomy group can occur.
Each smaller group on the list comes with a special kind of geometry.

### L2 human

The theorem organises much of modern Riemannian geometry: each group on the list defines a class of manifolds with special holonomy and parallel tensors.
For example holonomy in $\mathrm{U}(m)$ means there is a parallel complex structure, which is the Kähler condition.
The groups $\mathrm{SU}(m)$, $\mathrm{Sp}(k)$, $G_2$ and $\mathrm{Spin}(7)$ force Ricci-flatness, and these are the geometries used in string theory compactifications.
Together with the de Rham decomposition and Cartan's classification of symmetric spaces, it describes the holonomy of every simply connected complete Riemannian manifold.
