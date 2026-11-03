---
tag: AKGV0SAD4V
kind: statement
role: theorem
name: Borel's theorem on ranks of K-groups
msc: ["11R70", "19F27", "19D50"]
uses: [4HXFKW55WJ, MWBDFS2KJ5, BBRSEM0C4H]
about: [4HXFKW55WJ]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Statement

Let $F$ be an [[algebraic number field|MWBDFS2KJ5]] with ring of integers $\mathcal{O}_F$, with $r_1$ real embeddings and $r_2$ pairs of complex conjugate non-real embeddings.
Then for $n \ge 2$ the [[rank|BBRSEM0C4H]] of the finitely generated abelian group $K_n(\mathcal{O}_F)$, the $n$-th [[K-group|4HXFKW55WJ]] of $\mathcal{O}_F$, is
$$\rank K_n(\mathcal{O}_F) = \begin{cases} 0 & \text{if } n \text{ is even}, \\ r_1 + r_2 & \text{if } n \equiv 1 \pmod 4, \\ r_2 & \text{if } n \equiv 3 \pmod 4. \end{cases}$$

## Remarks

The finite generation is Quillen's theorem, and the ranks are due to Borel.
The group $K_n(\mathcal{O}_F) \otimes \Q$ is the primitive part of the rational homology of $B\mathrm{GL}(\mathcal{O}_F)^+$.
So the ranks follow from the stable real cohomology of the arithmetic groups $\mathrm{SL}_N(\mathcal{O}_F)$.
Borel computed it with invariant differential forms on the associated symmetric spaces.
For $n \ge 2$ the map $K_n(\mathcal{O}_F) \to K_n(F)$ is an isomorphism after tensoring with $\Q$, so the same ranks hold for $K_n(F)$.

Example: for $F = \Q$, $r_1 = 1$ and $r_2 = 0$, so $K_n(\Z)$ is finite for $n \ge 2$ unless $n \equiv 1 \pmod 4$, when it has rank $1$; for instance $K_5(\Z) \cong \Z$.
For an imaginary quadratic field, $r_1 = 0$ and $r_2 = 1$, so $K_n(\mathcal{O}_F)$ has rank $1$ for every odd $n \ge 3$.

## Explanations

### L1 human

The K-groups of a ring of integers are finitely generated, so each has a rank, the number of independent elements of infinite order.
Borel found that these ranks follow a simple periodic pattern.
They are zero in even degrees.
In odd degrees they count the real and complex embeddings of the number field, in a way that depends on the degree modulo $4$.

### L2 human

The theorem extends [[Dirichlet's unit theorem|1D99CSKX6N]], which gives rank $r_1 + r_2 - 1$ for $K_1$, one less than the rank $r_1 + r_2$ in the degrees $n \equiv 1 \pmod 4$ with $n \ge 5$.
Borel also built a regulator map from $K_{2m-1}(\mathcal{O}_F)$ to a real vector space whose image is a lattice of full rank.
He related its covolume to the value of the Dedekind zeta function at $m$.
This is the starting point of the Lichtenbaum and Beilinson conjectures on special values.
