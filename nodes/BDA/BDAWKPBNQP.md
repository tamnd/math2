---
tag: BDAWKPBNQP
kind: statement
role: theorem
name: Selberg trace formula
msc: [11F72, 58J50, 30F35]
uses: [VNJWSCVP6V, X6XGGH5FPW, 5K0N8QMV6Q, F4NWZNTRMD, 0BQAA2BK3Q, NSYMQMHPDN, 0DEBXAJ5SA]
about: [F4NWZNTRMD, VNJWSCVP6V]
sources:
  - url: https://en.wikipedia.org/wiki/Selberg_trace_formula
same_as:
  wikidata: Q3077649
  wikipedia: Selberg trace formula
---

## Statement

Let $\Gamma \subset \mathrm{PSL}_2(\R)$ be a torsion-free [[Fuchsian group|VNJWSCVP6V]] such that $X = \Gamma \backslash \mathbb H$ is compact, where $\mathbb H$ is the [[upper half-plane|X6XGGH5FPW]] with the hyperbolic metric $(dx^2 + dy^2)/y^2$.
Let $0 = \lambda_0 < \lambda_1 \le \lambda_2 \le \cdots$ be the [[eigenvalues|0BQAA2BK3Q]] of the [[Laplace–Beltrami operator|F4NWZNTRMD]] $\Delta = -y^2 (\partial_x^2 + \partial_y^2)$ on $X$, repeated with multiplicity, and write $\lambda_j = \tfrac14 + r_j^2$ with $r_j \in \C$.
Let $h$ be an even function, holomorphic on a strip $\abs{\operatorname{Im} r} \le \tfrac12 + \varepsilon$ with $\varepsilon > 0$, such that $\abs{h(r)} \le C (1 + \abs{r})^{-2-\varepsilon}$ there.
Let $g(u) = \frac{1}{2\pi} \int_{-\infty}^{\infty} h(r) e^{-iru} \, dr$.
Then
$$\sum_{j=0}^{\infty} h(r_j) = \frac{\operatorname{area}(X)}{4\pi} \int_{-\infty}^{\infty} r \, h(r) \tanh(\pi r) \, dr + \sum_{\gamma} \sum_{k=1}^{\infty} \frac{\ell(\gamma)}{2 \sinh(k \ell(\gamma)/2)} \, g(k \ell(\gamma)),$$
where $\gamma$ runs over the primitive oriented closed [[geodesics|NSYMQMHPDN]] of $X$ and $\ell(\gamma)$ is the length of $\gamma$.
All sums and integrals converge absolutely.

## Remarks

The closed geodesics of $X$ correspond to the nontrivial [[conjugacy classes|0DEBXAJ5SA]] of $\Gamma$, and $k \ell(\gamma)$ is the length of the $k$-th power.
The proof computes the trace of an integral operator on $L^2(X)$ in two ways.
The kernel $\sum_{\sigma \in \Gamma} k(z, \sigma w)$ is built from a point-pair invariant $k$ whose spectral transform is $h$.
Expanding in eigenfunctions gives the left side; integrating the kernel over the diagonal and grouping $\sigma$ by conjugacy classes gives the right side, with the identity giving the area term.
Example: $h(r) = e^{-t(r^2 + 1/4)}$ with $t > 0$ gives the trace of the heat kernel $\sum_j e^{-t \lambda_j}$, and the area term behaves like $\operatorname{area}(X)/(4\pi t)$ as $t \to 0$.
This yields Weyl's law: the number of $\lambda_j \le T$ is asymptotic to $\operatorname{area}(X) \, T / (4\pi)$.
For non-compact $X$ of finite area, such as $\mathrm{SL}_2(\Z) \backslash \mathbb H$, the formula needs extra terms from the cusps and from the continuous spectrum.

## Explanations

### L1 human

On a compact hyperbolic surface there are two natural lists of numbers.
One list is the frequencies at which the surface can vibrate, the eigenvalues of the Laplacian.
The other is the lengths of the closed geodesics, the loops that a light ray could travel forever.
The Selberg trace formula is an exact identity that links the two lists.

### L2 human

The formula is a non-abelian analogue of the Poisson summation formula, which links a lattice in $\R$ with its dual lattice.
It gives the prime geodesic theorem, the analytic properties of the Selberg zeta function, and Weyl's law for $X$.
Applied to congruence subgroups with Hecke operators inserted, it links Maass forms with arithmetic, and it is the prototype of the Arthur–Selberg trace formula.
