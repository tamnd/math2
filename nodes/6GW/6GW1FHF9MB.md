---
tag: 6GW1FHF9MB
kind: definition
name: Schubert calculus
msc: [14N15, 14M15, "05E14"]
defines: FWGHMADJR4
uses: [Z014Q8KPDD, CYPA882RB9, RDT4785M4D, EBEF6PEK4N]
sources:
  - url: https://en.wikipedia.org/wiki/Schubert_calculus
---

## Definition

Let $1 \le d < n$, and let $\mathrm{Gr}(d, n)$ be the complex [[Grassmannian|CYPA882RB9]].
For each partition $\lambda$ in the $d \times (n - d)$ rectangle, let $\sigma_\lambda \in H^{2 \abs{\lambda}}(\mathrm{Gr}(d, n); \Z)$ be the class of the [[Schubert variety|Z014Q8KPDD]] $X_\lambda$.
These classes form a $\Z$-basis of the [[cohomology ring|RDT4785M4D]] $H^{*}(\mathrm{Gr}(d, n); \Z)$.
*Schubert calculus* is the computation of the structure constants $c_{\lambda \mu}^{\nu}$ in
$$\sigma_\lambda \cdot \sigma_\mu = \sum_\nu c_{\lambda \mu}^{\nu} \, \sigma_\nu,$$
and their use to count intersection points of Schubert varieties in general position.
The same name is used for the analogous computations in the [[Chow ring|EBEF6PEK4N]] and for flag varieties.

## Remarks

For Grassmannians the constants $c_{\lambda \mu}^{\nu}$ are the Littlewood–Richardson coefficients, and they are nonnegative.
The Pieri rule computes the product with $\sigma_k$, for $k = 1, \ldots, n - d$.
It says that $\sigma_k \sigma_\lambda$ is the sum of $\sigma_\nu$ over the $\nu$ obtained from $\lambda$ by adding $k$ boxes, no two in the same column.
Only the $\nu$ that fit in the $d \times (n - d)$ rectangle are counted.

Example: in $\mathrm{Gr}(2, 4)$, the Pieri rule gives $\sigma_1^2 = \sigma_2 + \sigma_{1,1}$, $\sigma_1 \sigma_2 = \sigma_1 \sigma_{1,1} = \sigma_{2,1}$ and $\sigma_1 \sigma_{2,1} = \sigma_{2,2}$.
So $\sigma_1^4 = 2 \sigma_{2,2}$, and $\sigma_{2,2}$ is the class of a point.
Hence $2$ lines in $\mathbb{P}^3$ meet four general lines.

Non-example: the count of lines meeting four lines in a common plane is not given by $\sigma_1^4$.
The four Schubert varieties are not in general position, and they meet in a positive-dimensional set.
