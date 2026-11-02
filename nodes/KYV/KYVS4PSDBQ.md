---
tag: KYVS4PSDBQ
kind: definition
name: Heegaard Floer homology
msc: [57R58, 57K31, 57K18]
defines: 2WJJBN2T5P
uses: [R20TB2KEQQ, EDE9919B5R, NCKFPAGHXF]
sources:
  - url: https://en.wikipedia.org/wiki/Floer_homology
---

## Definition

Let $Y$ be a closed oriented [[3-manifold|R20TB2KEQQ]].
Let $(\Sigma, \alpha, \beta, z)$ be a pointed Heegaard diagram of $Y$ coming from a [[Heegaard splitting|EDE9919B5R]].
Here $\Sigma$ is a closed oriented surface of genus $g$.
The families $\alpha = (\alpha_1, \ldots, \alpha_g)$ and $\beta = (\beta_1, \ldots, \beta_g)$ consist of disjoint simple closed curves on $\Sigma$.
The base point $z \in \Sigma$ lies off all of these curves.
Assume the diagram is admissible, and fix a generic path of almost complex structures on the symmetric product $\mathrm{Sym}^g(\Sigma)$.

1. The tori $\mathbb{T}_\alpha = \alpha_1 \times \cdots \times \alpha_g$ and $\mathbb{T}_\beta = \beta_1 \times \cdots \times \beta_g$ are submanifolds of $\mathrm{Sym}^g(\Sigma)$ that meet transversally in finitely many points.
2. The chain complex $\widehat{CF}(\Sigma, \alpha, \beta, z)$ is the vector space over $\F_2$ with basis $\mathbb{T}_\alpha \cap \mathbb{T}_\beta$.
3. Let $x$ and $y$ be basis elements.
Consider the holomorphic disks from $x$ to $y$ with Maslov index $1$ whose domain avoids $z$.
The coefficient of $y$ in $\partial x$ is their number modulo $2$.
Disks that differ by a translation of the parameter are counted once.

The homology $\widehat{HF}(Y)$ of this complex is the *hat version of Heegaard Floer homology* of $Y$.
The versions $HF^-$, $HF^\infty$ and $HF^+$ are defined in the same way over $\F_2[U]$ or $\F_2[U, U^{-1}]$.
In them the disks may cover $z$, and the power of $U$ records how many times they do.

## Remarks

Ozsváth and Szabó proved that $\partial^2 = 0$ and that the homology does not depend, up to isomorphism, on the diagram and the other choices, so it is an invariant of $Y$.
For $Y = S^3$, the genus $1$ diagram with $\alpha$ and $\beta$ meeting in one point gives $\widehat{HF}(S^3) \cong \F_2$.
For a rational homology sphere $Y$, the dimension of $\widehat{HF}(Y)$ is at least the order of $H_1(Y; \Z)$; the spaces with equality are called L-spaces, and lens spaces are examples.
With suitable orientation choices the construction also works over $\Z$.
It is a form of Lagrangian [[Floer homology|NCKFPAGHXF]] for the pair $(\mathbb{T}_\alpha, \mathbb{T}_\beta)$.
