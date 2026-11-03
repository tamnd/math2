---
tag: MFPWPK5ZNB
kind: definition
name: Harmonic analysis on the adeles
msc: [11R56, 43A25, 11F70]
defines: 74MN0W5XWM
uses: [SEH68BA1QQ, MWBDFS2KJ5, BT5V3TSNY6, ZR09S9R3AW, VY0HXD3GC4, FMW57WNPDB, VHN5VW5Q92, CG9JEATW3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Adele_ring
---

## Definition

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] and let $\mathbb{A}_K$ be its [[adele ring|SEH68BA1QQ]], a [[locally compact abelian group|ZR09S9R3AW]] under addition.
For each [[place|BT5V3TSNY6]] $v$ of $K$, let $K_v$ be the completion at $v$, and for finite $v$ let $\mathcal{O}_v$ be its valuation ring.
*Harmonic analysis on the adeles* is the [[Fourier analysis|VHN5VW5Q92]] of $\mathbb{A}_K$ built from the following data.

1. The standard character. For $\Q$, let $\psi_\infty(x) = e^{-2\pi i x}$ on $\R$, and let $\psi_p(x) = e^{2\pi i \{x\}_p}$ on $\Q_p$, where $\{x\}_p \in \Z[1/p]$ is the $p$-adic fractional part of $x$. Put $\psi_{\Q}((x_v)_v) = \prod_v \psi_v(x_v)$, and put $\psi_K = \psi_{\Q} \circ \tr_{\mathbb{A}_K / \mathbb{A}_{\Q}}$. Then $\psi_K$ is a nontrivial continuous unitary character of $\mathbb{A}_K$ that is trivial on $K$.
2. The Schwartz–Bruhat space $\mathcal{S}(\mathbb{A}_K)$. It is spanned by the functions $f((x_v)_v) = \prod_v f_v(x_v)$ of the following kind. For each infinite $v$, $f_v$ lies in the [[Schwartz space|CG9JEATW3Q]] of $K_v \cong \R^{n_v}$. For each finite $v$, $f_v$ is locally constant with compact support. For all but finitely many $v$, $f_v = \mathbf{1}_{\mathcal{O}_v}$.
3. The self-dual [[Haar measure|VY0HXD3GC4]] $dx$ on $\mathbb{A}_K$, the unique Haar measure for which the Fourier transform
$$\widehat{f}(y) = \int_{\mathbb{A}_K} f(x)\, \psi_K(xy)\, dx$$
satisfies $\widehat{\widehat{f}}(x) = f(-x)$ for all $f \in \mathcal{S}(\mathbb{A}_K)$.

## Remarks

The basic facts of the theory are these.
The map $y \mapsto (x \mapsto \psi_K(xy))$ is an isomorphism of topological groups from $\mathbb{A}_K$ onto its [[Pontryagin dual|FMW57WNPDB]], so $\mathbb{A}_K$ is self-dual.
Under this isomorphism the annihilator of the discrete subgroup $K$ is $K$ itself.
For the self-dual measure, the compact quotient $\mathbb{A}_K / K$ has volume $1$.
The adelic Poisson summation formula states that $\sum_{\gamma \in K} f(\gamma) = \sum_{\gamma \in K} \widehat{f}(\gamma)$ for every $f \in \mathcal{S}(\mathbb{A}_K)$.

Example: on $\mathbb{A}_{\Q}$, take $f_\infty(x) = e^{-\pi x^2}$ and $f_p = \mathbf{1}_{\Z_p}$ for every prime $p$.
Then $f = \prod_v f_v$ lies in $\mathcal{S}(\mathbb{A}_{\Q})$, since every clause of item 2 holds.
The Gaussian is its own Fourier transform for $\psi_\infty$, and $\mathbf{1}_{\Z_p}$ is its own Fourier transform for $\psi_p$ and the Haar measure with $\Z_p$ of volume $1$, so $\widehat{f} = f$.
A rational number $r$ has $f(r) \ne 0$ only if $r \in \Z_p$ for all $p$, that is, $r \in \Z$.
So Poisson summation gives the trivial identity $\sum_{n \in \Z} e^{-\pi n^2} = \sum_{n \in \Z} e^{-\pi n^2}$; with $f_\infty(x) = e^{-\pi t x^2}$ it gives the theta transformation formula.

Non-example: the product of $f_\infty(x) = e^{-\pi x^2}$ and $f_p = \mathbf{1}_{p\Z_p}$ for every prime $p$ is not in $\mathcal{S}(\mathbb{A}_{\Q})$.
It fails the last clause of item 2, since $f_p \ne \mathbf{1}_{\Z_p}$ for infinitely many $p$.
Indeed the set $\prod_p p\Z_p$ has empty interior in the finite adeles, so this function is not locally constant there.
