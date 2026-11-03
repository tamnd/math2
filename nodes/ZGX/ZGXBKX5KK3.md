---
tag: ZGXBKX5KK3
kind: definition
name: K-theory spectrum
msc: [19D10, 55P42]
defines: 2C1M0NWPB0
uses: [X7JG1QEB9Q, ZPNXVVZY1J, 1GHF4EKBXS, TG6WHHR7CF, 2JFF5F3EGF, P976WYEFMB, 3YDPFTQTJ6]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Definition

Let $\mathcal{C}$ be a [[Waldhausen category|X7JG1QEB9Q]].
Put $S^{(0)} \mathcal{C} = \mathcal{C}$, and for $n \ge 0$ let $S^{(n+1)} \mathcal{C}$ be the $(n+1)$-fold simplicial Waldhausen category obtained by applying the [[S-construction|ZPNXVVZY1J]] to $S^{(n)} \mathcal{C}$ in each multidegree.
Let $wS^{(n)} \mathcal{C}$ be its subcategory of weak equivalences.
Since $S_0 \mathcal{C}$ is trivial and $S_1 \mathcal{C} \simeq \mathcal{C}$, the $1$-skeleton in the new simplicial direction gives maps
$$\sigma_n \colon \Sigma \abs{wS^{(n)} \mathcal{C}} \to \abs{wS^{(n+1)} \mathcal{C}}, \qquad n \ge 0.$$
The *K-theory spectrum* $K(\mathcal{C})$ is the [[spectrum|1GHF4EKBXS]] with $n$-th space $\abs{wS^{(n)} \mathcal{C}}$ and structure maps $\sigma_n$.
For a ring $R$, $K(R)$ is the K-theory spectrum of the exact category of finitely generated projective $R$-modules, with the isomorphisms as weak equivalences.

## Remarks

Waldhausen proved that the adjoint maps $\abs{wS^{(n)} \mathcal{C}} \to \Omega \abs{wS^{(n+1)} \mathcal{C}}$ are homotopy equivalences for $n \ge 1$.
Hence $K(\mathcal{C})$ is an $\Omega$-spectrum above degree $0$, its [[homotopy groups|P976WYEFMB]] are $\pi_n K(\mathcal{C}) = \pi_{n+1} \abs{wS_\bullet \mathcal{C}} = K_n(\mathcal{C})$ for $n \ge 0$, and $\pi_n K(\mathcal{C}) = 0$ for $n < 0$.

Example: for a field $k$ and $\mathcal{C}$ the finite-dimensional $k$-vector spaces with isomorphisms as weak equivalences, $\pi_0 K(\mathcal{C}) = K_0(k) \cong \Z$, through the dimension.

Non-example: the map in degree $0$, $\abs{w\mathcal{C}} \to \Omega \abs{wS_\bullet \mathcal{C}}$, is in general not a homotopy equivalence.
In the example above, $\pi_0 \abs{w\mathcal{C}}$ is the set of isomorphism classes of vector spaces, which is $\N$, while $\pi_0$ of the [[loop space|2JFF5F3EGF]] is $\Z$.
In this example the map is a group completion.

The spectrum $K(\mathcal{C})$ is connective.
Bass's [[negative K-groups|3YDPFTQTJ6]] are captured by a nonconnective variant, built by Thomason for rings and schemes.
