---
tag: P2HKS3K7T2
kind: definition
name: Splitting field of a central simple algebra
msc: [16K50, 16K20]
defines: NVD7R0T835
uses: [5HRKJBAY2V, NNXSP5KKAC, 0EQWVHF3W5, 1735VGRT2P, 0FHVPRAE60]
sources:
  - url: https://en.wikipedia.org/wiki/Central_simple_algebra
---

## Definition

Let $K$ be a field and let $A$ be a [[central simple algebra|5HRKJBAY2V]] over $K$ of [[degree|NNXSP5KKAC]] $n$.
Let $L$ be a [[field extension|0EQWVHF3W5]] of $K$.
The field $L$ is a *splitting field* of $A$, or *splits* $A$, if there is an isomorphism of $L$-algebras
$$A \otimes_K L \cong M_n(L).$$
Here $\otimes_K$ is the [[tensor product of algebras|1735VGRT2P]] and $M_n(L)$ is the [[matrix ring|0FHVPRAE60]] of $n \times n$ matrices over $L$.

## Remarks

Example: $\C$ splits $\mathbb{H}$ over $\R$.
Indeed, $\mathbb{H} \otimes_\R \C$ is central simple of dimension $4$ over $\C$, and the only such algebra is $M_2(\C)$, since $\C$ is algebraically closed.

Non-example: $\R$ itself does not split $\mathbb{H}$, since $\mathbb{H} \otimes_\R \R \cong \mathbb{H}$ is a division algebra and $M_2(\R)$ has zero divisors.

$A$ is split over $K$ itself exactly when $A \cong M_n(K)$.
An algebraic closure of $K$ splits every central simple algebra over $K$, and so does a suitable finite Galois extension of $K$.
Every maximal subfield of a central division algebra $D$ is a splitting field of $D$.
