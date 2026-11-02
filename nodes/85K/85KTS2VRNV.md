---
tag: 85KTS2VRNV
kind: definition
name: Siegel modular form
msc: [11F46, 32N10]
defines: MXPTXV340K
uses: [5PTYE97PF6, X12FS2JAP0, GWKN5VG78A, 507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Siegel_modular_form
---

## Definition

Let $g \ge 1$ and $k$ be integers, and let $\mathbb{H}_g$ be the [[Siegel upper half-space|5PTYE97PF6]] of degree $g$.
Let $\Gamma_g = Sp(2g, \Z)$ be the group of integer matrices in the [[symplectic group|X12FS2JAP0]] $Sp(2g, \R)$.
A *Siegel modular form* of degree $g$ and weight $k$ is a function $f \colon \mathbb{H}_g \to \C$ such that:

1. $f$ is [[holomorphic|507C34W0ZT]] in the $g(g+1)/2$ entries $Z_{ij}$, $i \le j$, of $Z$;
2. $f\big((AZ + B)(CZ + D)^{-1}\big) = \det(CZ + D)^k f(Z)$ for all $Z \in \mathbb{H}_g$ and all $\begin{pmatrix} A & B \\ C & D \end{pmatrix} \in \Gamma_g$;
3. if $g = 1$, $f$ is holomorphic at the cusp: $f$ is bounded on $\set{Z : \operatorname{Im} Z \ge 1}$.

## Remarks

For $g = 1$ this is the definition of a [[modular form|GWKN5VG78A]] of weight $k$ for $SL_2(\Z)$.
For $g \ge 2$ the Koecher principle shows that conditions 1 and 2 imply boundedness on every set $\set{Z : \operatorname{Im} Z \ge c I_g}$ with $c > 0$, so no condition at the cusp is needed.
Every Siegel modular form has a Fourier expansion $f(Z) = \sum_T a(T) e^{2\pi i \operatorname{tr}(TZ)}$, over half-integral symmetric matrices $T \ge 0$.
Forms of weight $k$ for subgroups of finite index of $\Gamma_g$, and vector-valued forms, are defined in the same way.

Example: a constant function $f = c$ is a Siegel modular form of weight $0$, since condition 2 reads $c = \det(CZ + D)^0 c$.
Example: let $S$ be a positive definite even unimodular integer matrix of size $m$.
The theta series $\theta_S(Z) = \sum_{X} e^{\pi i \operatorname{tr}(X^T S X Z)}$, over all integer $m \times g$ matrices $X$, is a Siegel modular form of weight $m/2$.

Non-example: the $j$-invariant $j(z)$ is holomorphic on $\mathbb{H}_1$ and satisfies condition 2 with $k = 0$.
But $j(z) = e^{-2\pi i z} + 744 + \cdots$ is unbounded on $\operatorname{Im} z \ge 1$, so condition 3 fails.
