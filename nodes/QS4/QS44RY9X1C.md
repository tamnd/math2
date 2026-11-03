---
tag: QS44RY9X1C
kind: example
name: Dual groups of the integers and the real line
msc: [43A40, 22B05, 43A70]
instance_of: [FMW57WNPDB]
uses: [04EAFVFTF7, H1WNVN5V7F, RG15F0TWPW, QTVC6F2P9D]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Example

Let $\mathbb{T} = \set{z \in \C : \abs{z} = 1}$ be the [[circle group|04EAFVFTF7]].

The integers.
Give $\Z$ the discrete topology.
A [[character|H1WNVN5V7F]] $\chi \colon \Z \to \mathbb{T}$ is fixed by $z = \chi(1)$, since $\chi(n) = \chi(1)^n = z^n$.
Conversely, for every $z \in \mathbb{T}$ the map $n \mapsto z^n$ is a character, and it is continuous because $\Z$ is discrete.
On a discrete group, the [[compact-open topology|RG15F0TWPW]] is the topology of pointwise convergence on finite sets, and $z_k^n \to z^n$ for all $n$ exactly when $z_k \to z$.
So $\chi \mapsto \chi(1)$ is an isomorphism of topological groups $\widehat{\Z} \cong \mathbb{T}$.

The real line.
For $\xi \in \R$, the map $\chi_\xi(x) = e^{i \xi x}$ is a continuous character of $(\R, +)$, since $e^{i\xi(x + y)} = e^{i\xi x} e^{i\xi y}$.
Every continuous homomorphism $\chi \colon \R \to \mathbb{T}$ lifts, through the covering map $t \mapsto e^{it}$, to a continuous additive map $\R \to \R$, which has the form $x \mapsto \xi x$; so $\chi = \chi_\xi$.
Distinct $\xi$ give distinct characters, and $\chi_{\xi_k} \to \chi_\xi$ uniformly on compact sets exactly when $\xi_k \to \xi$.
So $\xi \mapsto \chi_\xi$ is an isomorphism of topological groups $\R \cong \widehat{\R}$.

These two computations, with $\widehat{\mathbb{T}} \cong \Z$, illustrate the [[Pontryagin duality theorem|QTVC6F2P9D]]: the dual of $\widehat{\Z} \cong \mathbb{T}$ is $\Z$ again, and $\R$ is self-dual.

## Explanations

### L1 human

The characters of a group are its pure waves.
On the integers, a wave is fixed by one number $z$ on the unit circle: the factor by which it turns at each step.
So the dual of $\Z$ is the circle.
On the real line, a wave $e^{i\xi x}$ is determined by its frequency $\xi$, which can be any real number, so the dual of $\R$ is $\R$ itself.
These are the duals behind Fourier series on the circle and the Fourier transform on the line.
