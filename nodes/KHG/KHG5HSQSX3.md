---
tag: KHG5HSQSX3
kind: problem
name: Truncated moment problem
msc: [44A60, 47A57]
uses: [CS7TWHY7JM, PR11BZQQPG, 01XAHPADBA, FQTXV6BQZG, PQ1D8FQB3E, 01MMVW8CKC, FP37BTP93K]
about: [CS7TWHY7JM, 01XAHPADBA]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_problem
history:
  posed_by: "Pafnuty Chebyshev"
  first_stated: "1874"
  notes: "Chebyshev studied bounds for integrals when finitely many moments are given in 1874, and his student Markov proved the resulting inequalities in 1884; the attribution is to this earliest known formulation. The modern existence theory was developed by Curto and Fialkow from 1991 on."
---

## Problem

Let $K$ be a closed subset of $\R$, let $n \ge 0$ be an integer, and let $m_0, m_1, \ldots, m_n$ be real numbers.

1. Existence: decide whether there is a positive Borel [[measure|PR11BZQQPG]] $\mu$ on $\R$ with [[support|FQTXV6BQZG]] in $K$ such that $\int \abs{x}^n \, d\mu(x) < \infty$ and $m_j = \int x^j \, d\mu(x)$ for $j = 0, 1, \ldots, n$.
2. Description: when such measures exist, describe all of them.

## Remarks

It is the [[moment problem|CS7TWHY7JM]] with only finitely many prescribed [[moments|01XAHPADBA]].
The solution is usually far from unique, since a finite list of moments says little about a measure.
A necessary condition for $K = \R$ and $n = 2k$: the [[Hankel matrix|PQ1D8FQB3E]] $H_k = (m_{i+j})_{i,j=0}^{k}$ is [[positive semidefinite|01MMVW8CKC]], since $c^T H_k c = \int p(x)^2 \, d\mu(x) \ge 0$ for $p(x) = \sum_{j} c_j x^j$.
This condition alone is not sufficient.
Non-example: $(m_0, m_1, m_2) = (0, 0, 1)$ gives $H_1 = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, which is positive semidefinite, but $m_0 = \mu(\R) = 0$ forces $\mu = 0$ and then $m_2 = 0$.
Example: let $\mu$ be a positive measure on $\R$ with infinite support and finite moments.
Then [[Gaussian quadrature|FP37BTP93K]] with $k$ nodes gives a measure with $k$ atoms that has the same moments $m_0, \ldots, m_{2k-1}$ as $\mu$.
Truncated problems also appear with $\R^d$ in place of $\R$, and there they are linked to cubature formulas and to positive polynomials.

## Explanations

### L1 human

In practice one can only measure finitely many moments of a distribution: its mass, its mean, its second moment, and a few more.
The truncated moment problem asks whether such a short list can come from some distribution, and which distributions fit it.
For instance, the numbers $1, 0, 1$ are the mass, mean and second moment of the distribution with weight $1/2$ at each of $-1$ and $1$.
They are also the first moments of the standard normal distribution.
A list such as $1, 0, -1$ fits no distribution at all, since an average of squares cannot be negative.
