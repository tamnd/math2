---
tag: V7K1SXPGQY
kind: example
name: Self-dual group
msc: [43A40, 43A70]
illustrates: [FMW57WNPDB]
uses: [ZR09S9R3AW, H1WNVN5V7F, 03VFZ2WETT, BT6T702C28, 04EAFVFTF7]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Example

A [[locally compact abelian group|ZR09S9R3AW]] $G$ is *self-dual* if it is isomorphic, as a topological group, to its [[Pontryagin dual|FMW57WNPDB]] $\widehat{G}$.

1. The real line $\R$ is self-dual. For $\xi \in \R$ let $\chi_\xi(x) = e^{2\pi i \xi x}$. Each $\chi_\xi$ is a continuous [[character|H1WNVN5V7F]], and $\chi_{\xi + \eta} = \chi_\xi \chi_\eta$. Every continuous character of $\R$ has this form, and $\xi \mapsto \chi_\xi$ is a homeomorphism onto $\widehat{\R}$ with the compact-open topology.
2. The group $\Z/n\Z$ of [[integers modulo n|03VFZ2WETT]] is self-dual. For $k \in \Z/n\Z$ let $\chi_k(a) = e^{2\pi i k a / n}$. This is well defined, it is a character, and $k \mapsto \chi_k$ is an injective homomorphism. A character $\chi$ is determined by $\chi(1)$, which is an $n$-th root of unity, so all $n$ characters arise.
3. The [[p-adic numbers|BT6T702C28]] $\Q_p$ are self-dual. Here $\psi(x) = e^{2\pi i \set{x}_p}$, where $\set{x}_p$ is the $p$-adic fractional part, is a character, and $a \mapsto (x \mapsto \psi(ax))$ is an isomorphism $\Q_p \to \widehat{\Q_p}$.
4. Finite products of self-dual groups are self-dual, since the dual of a finite product is the product of the duals. So $\R^n$ is self-dual, and every finite abelian group is self-dual, being a product of cyclic groups.

Non-example: the [[circle group|04EAFVFTF7]] $\mathbb{T}$ is not self-dual.
Its dual is $\Z$, via $n \mapsto (z \mapsto z^n)$, and $\Z$ is countable and discrete, while $\mathbb{T}$ is uncountable.
Likewise $\Z$ is not self-dual.

## Explanations

### L1 human

For a self-dual group, the group and its set of waves look the same.
On the real line, waves are labelled by their frequency, and the frequencies again form a real line.
That is why the Fourier transform on $\R$ takes functions on $\R$ to functions on $\R$.
On the circle this fails: the waves on the circle are labelled by whole numbers, so Fourier series turn functions on a circle into sequences.
