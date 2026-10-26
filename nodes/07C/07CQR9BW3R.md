---
tag: 07CQR9BW3R
kind: statement
role: theorem
name: Classification of finite abelian groups
aliases: [fundamental-theorem-of-finite-abelian-groups, basis-theorem-for-finite-abelian-groups]
msc: [20K01]
uses: [071DDFVG4J, 0B85Q41RP6, 085PND4KNT, 0YP7WYXF9V, 08FDFEF8D1]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_group
    locator: Classification
  - url: https://en.wikipedia.org/wiki/Finitely_generated_abelian_group
    locator: Primary decomposition
  - url: https://en.wikipedia.org/wiki/Finitely_generated_abelian_group
    locator: Invariant factor decomposition
  - url: https://en.wikipedia.org/wiki/Finitely_generated_abelian_group
    locator: History
---

## Statement

Let $G$ be a finite [[abelian group|082GHNPJ53]].
Then $G$ is [[isomorphic|08MG7H8JW5]] to a [[direct sum|00HF4RJ5QN]] $\mathbb{Z}/q_1\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/q_t\mathbb{Z}$, where each $q_i$ is a power of a prime number.
The numbers $q_1, \ldots, q_t$ are unique up to their order.
Equivalently, $G \cong \mathbb{Z}/k_1\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/k_u\mathbb{Z}$ with $1 < k_1 \mid k_2 \mid \cdots \mid k_u$, and these $k_i$ are unique.

## Remarks

The two forms are equivalent because $\mathbb{Z}/m n\mathbb{Z} \cong \mathbb{Z}/m\mathbb{Z} \oplus \mathbb{Z}/n\mathbb{Z}$ if and only if $\gcd(m, n) = 1$, as in [[this statement|08FDFEF8D1]].
Each abelian group of order $8$ is isomorphic to exactly one of $\mathbb{Z}/8\mathbb{Z}$, $\mathbb{Z}/4\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$ and $\mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z} \oplus \mathbb{Z}/2\mathbb{Z}$.
Each abelian group of order $15$ is cyclic, because $15 = 3 \cdot 5$ with $\gcd(3, 5) = 1$.
The theorem is the case of rank $0$ of the [[structure theorem for finitely generated abelian groups|0RY0B72XAS]].

## History

Leopold Kronecker proved the theorem in 1870 with a group-theoretic proof, but he did not state it in the language of groups.
His work extended an earlier result of Carl Friedrich Gauss from 1801 on quadratic forms.
Ferdinand Georg Frobenius and Ludwig Stickelberger stated and proved the theorem in the language of groups in 1878.

## Explanations

### L1 human

Each finite abelian group is built from cyclic groups.
You can choose the cyclic pieces to have prime power orders, or to have orders that divide each other.
In both forms, the pieces are unique, so this lists all finite abelian groups.
