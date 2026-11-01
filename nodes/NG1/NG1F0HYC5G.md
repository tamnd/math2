---
tag: NG1F0HYC5G
kind: definition
name: Discriminant of a number field
msc: [11R29, 11R04]
defines: E0VZTNPJXA
uses: [MWBDFS2KJ5, 00KDZRW4C0, 0KZDNGA561]
sources:
  - url: https://en.wikipedia.org/wiki/Discriminant_of_an_algebraic_number_field
    locator: Definition
---

## Definition

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] of degree $n = [K : \Q]$, and let $\mathcal{O}_K$ be its ring of integers.
Let $\omega_1, \ldots, \omega_n$ be an integral basis of $K$, that is, a basis of $\mathcal{O}_K$ as a free $\Z$-module.
Let $\sigma_1, \ldots, \sigma_n$ be the $n$ field embeddings $K \to \C$.
The *discriminant* of $K$ is the number
$$d_K = \Big(\det\big(\sigma_i(\omega_j)\big)_{1 \le i, j \le n}\Big)^2,$$
where $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

The value does not depend on the integral basis or on the order of the embeddings.
Two integral bases differ by a matrix in $\mathrm{GL}_n(\Z)$, whose determinant is $\pm 1$.
Reordering the rows changes only the sign of the determinant.
An equivalent form is $d_K = \det\big(\operatorname{Tr}_{K/\Q}(\omega_i \omega_j)\big)$, where the field trace $\operatorname{Tr}_{K/\Q}(\alpha)$ is the [[trace|0KZDNGA561]] of the $\Q$-linear map $x \mapsto \alpha x$ on $K$.
The field trace of an algebraic integer is an integer, so $d_K$ is an integer.
It is never $0$, and its sign is $(-1)^{r_2}$, where $r_2$ is the number of pairs of complex conjugate embeddings.

Example: for $K = \Q(i)$ the basis $1, i$ of $\Z[i]$ gives $\det \begin{pmatrix} 1 & i \\ 1 & -i \end{pmatrix} = -2i$, so $d_K = -4$.
More generally, for a squarefree integer $d \ne 1$, the discriminant of $\Q(\sqrt{d})$ is $d$ if $d \equiv 1 \pmod 4$ and $4d$ otherwise.

Non-example: the basis $1, 2i$ gives $\det \begin{pmatrix} 1 & 2i \\ 1 & -2i \end{pmatrix}^2 = (-4i)^2 = -16$.
This is not $d_{\Q(i)}$, because $1, 2i$ is a basis of the subring $\Z[2i]$ and not of the whole ring of integers $\Z[i]$.
