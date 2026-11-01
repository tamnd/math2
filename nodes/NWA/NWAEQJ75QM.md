---
tag: NWAEQJ75QM
kind: definition
name: Frobenius element
msc: [11R32, 11R37]
defines: H5145REFMW
uses: [MWBDFS2KJ5, 0QMZAQ6QQ4, 0XTY86BZKY, 7X92G8CQ33, H5RC67SD24, 0CGCPX8Z70, 0DEBXAJ5SA, M54ADM0CVF]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_endomorphism
---

## Definition

Let $L/K$ be a finite [[Galois extension|0QMZAQ6QQ4]] of [[algebraic number fields|MWBDFS2KJ5]] with [[Galois group|0XTY86BZKY]] $G$, and let $\mathcal{O}_K \subseteq \mathcal{O}_L$ be the rings of integers.
Let $\mathfrak{p}$ be a nonzero prime ideal of $\mathcal{O}_K$ that is [[unramified|H5RC67SD24]] in $L$, and let $\mathfrak{P}$ be a prime ideal of $\mathcal{O}_L$ over $\mathfrak{p}$.
Let $q = N(\mathfrak{p}) = \abs{\mathcal{O}_K/\mathfrak{p}}$ be the [[norm|M54ADM0CVF]] of $\mathfrak{p}$.
The *Frobenius element* of $\mathfrak{P}$ is the unique $\sigma \in G$ such that
$$\sigma(x) \equiv x^{q} \pmod{\mathfrak{P}} \quad \text{for all } x \in \mathcal{O}_L.$$
It is written $\mathrm{Frob}_{\mathfrak{P}}$ or $\left(\frac{L/K}{\mathfrak{P}}\right)$.

## Remarks

Existence and uniqueness: such a $\sigma$ fixes $\mathfrak{P}$, so it lies in the [[decomposition group|7X92G8CQ33]] $D_{\mathfrak{P}}$.
The map from $D_{\mathfrak{P}}$ to the Galois group of the residue extension is onto, with kernel the inertia group, which is trivial because $\mathfrak{p}$ is unramified.
So exactly one element of $D_{\mathfrak{P}}$ maps to the [[Frobenius automorphism|0CGCPX8Z70]] $y \mapsto y^q$ of the residue field.
$\mathrm{Frob}_{\mathfrak{P}}$ generates $D_{\mathfrak{P}}$, and its order is the residue degree $f$.

For $\tau \in G$, $\mathrm{Frob}_{\tau(\mathfrak{P})} = \tau \, \mathrm{Frob}_{\mathfrak{P}} \, \tau^{-1}$.
So the Frobenius elements of the primes over $\mathfrak{p}$ form one [[conjugacy class|0DEBXAJ5SA]] $\mathrm{Frob}_{\mathfrak{p}}$ of $G$; if $G$ is abelian, it is a single element, the *Artin symbol* of $\mathfrak{p}$.

Example: $K = \Q$, $L = \Q(\zeta_n)$ with $\zeta_n$ a primitive $n$-th root of unity, and $p$ a prime not dividing $n$.
The automorphism $\sigma_p$ with $\sigma_p(\zeta_n) = \zeta_n^p$ satisfies $\sigma_p(x) \equiv x^p$ modulo every prime over $p$, since $(a + b)^p \equiv a^p + b^p$ modulo $p$; so $\mathrm{Frob}_p = \sigma_p$.

Non-example: in $\Q(i)/\Q$, the prime $2$ is ramified.
Both elements $\sigma$ of $G$ satisfy $\sigma(x) \equiv x^2 \pmod{(1 + i)}$, because the residue field is $\F_2$ and $i \equiv -i \equiv 1 \pmod{(1+i)}$; so there is no unique Frobenius element.
