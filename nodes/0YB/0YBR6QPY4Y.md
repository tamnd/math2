---
tag: 0YBR6QPY4Y
kind: example
name: Groups of order pq
msc: [20D20]
uses: [0Q8DGAZSJ4, 0M3PYJ3TSE, 0Q2MVQ7JMT, 08FDFEF8D1]
sources:
  - url: https://en.wikipedia.org/wiki/Sylow_theorems
    locator: Cyclic group orders
---

## Example

Let $p < q$ be prime numbers such that $p$ does not divide $q - 1$, and let $G$ be a group of order $pq$.
The number $n_q$ divides $p$ and satisfies $n_q \equiv 1 \pmod q$, so $n_q = 1$, because $p < q$.
The number $n_p$ divides $q$ and satisfies $n_p \equiv 1 \pmod p$; since $p \nmid q - 1$, $n_p = 1$.
So $G$ has a [[normal|0CB0DX5BVV]] subgroup $P$ of order $p$ and a normal subgroup $Q$ of order $q$.
They meet only in $e$, so $G$ is the [[internal direct product|0VBZH90R1A]] of $P$ and $Q$.
Thus $G \cong \mathbb{Z}/p\mathbb{Z} \times \mathbb{Z}/q\mathbb{Z} \cong \mathbb{Z}/pq\mathbb{Z}$, and $G$ is cyclic.
For example, each group of order $15$ is cyclic.
If $p$ divides $q - 1$, there is also a group of order $pq$ that is not cyclic, for example the dihedral group $D_3$ of order $6$.
