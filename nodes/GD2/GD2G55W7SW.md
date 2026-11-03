---
tag: GD2G55W7SW
kind: definition
name: Reduced norm
msc: ["16K20", "16K50", 19B99]
defines: 2FATVDAN2E
uses: [5HRKJBAY2V, NNXSP5KKAC, NVD7R0T835, 00KDZRW4C0, KRNFEZWPY0]
sources:
  - url: https://en.wikipedia.org/wiki/Central_simple_algebra
    locator: Splitting field
---

## Definition

Let $F$ be a field and let $A$ be a [[central simple algebra|5HRKJBAY2V]] over $F$ of [[degree|NNXSP5KKAC]] $n$, so $\dim_F A = n^2$.
Let $L$ be a field extension of $F$ that is a [[splitting field|NVD7R0T835]] of $A$, with an isomorphism of $L$-algebras $\varphi \colon A \otimes_F L \to M_n(L)$.
The *reduced norm* of $a \in A$ is
$$\mathrm{Nrd}(a) = \det \varphi(a \otimes 1),$$
where $\det$ is the [[determinant|00KDZRW4C0]] of $n \times n$ matrices over $L$.

## Remarks

The value $\mathrm{Nrd}(a)$ lies in $F$ and does not depend on the choice of $L$ and $\varphi$; independence of $\varphi$ follows from the Skolem–Noether theorem.
The reduced norm is multiplicative, and $a$ is invertible in $A$ if and only if $\mathrm{Nrd}(a) \ne 0$.
It relates to the norm of left multiplication by $N(a) = \det(x \mapsto ax) = \mathrm{Nrd}(a)^n$, the determinant being taken over $F$.
Example: for $A = M_n(F)$, take $L = F$ and $\varphi$ the identity, so $\mathrm{Nrd}$ is the usual determinant.
Example: for the Hamilton quaternions $\mathbb{H}$ over $\R$, with $n = 2$ and $L = \C$, one finds $\mathrm{Nrd}(a + bi + cj + dk) = a^2 + b^2 + c^2 + d^2$.
Non-example: the map $a \mapsto \det(x \mapsto ax)$ on $\mathbb{H}$ is not the reduced norm, since it equals $(a^2 + b^2 + c^2 + d^2)^2$.
The reduced norm differs from the [[field norm|KRNFEZWPY0]] in general.
But when $A$ contains a subfield $K$ of degree $n$ over $F$, the reduced norm of $a \in K$ is the field norm $N_{K/F}(a)$.
