---
tag: 0WHCA4SVP2
kind: concept
name: Invariant factors and elementary divisors
msc: [20K01, 20K25]
sources:
  - url: https://en.wikipedia.org/wiki/Finitely_generated_abelian_group
    locator: Primary decomposition
  - url: https://en.wikipedia.org/wiki/Finitely_generated_abelian_group
    locator: Invariant factor decomposition
  - url: https://en.wikipedia.org/wiki/Elementary_divisors
    locator: lead section
---

## Summary

Let $G$ be a finitely generated [[abelian group|082GHNPJ53]], and write $G \cong \mathbb{Z}^n \oplus \mathbb{Z}/k_1\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/k_u\mathbb{Z}$ with $1 < k_1 \mid k_2 \mid \cdots \mid k_u$.
The integers $k_1, \ldots, k_u$ are the invariant factors of $G$.
In the other form $G \cong \mathbb{Z}^n \oplus \mathbb{Z}/q_1\mathbb{Z} \oplus \cdots \oplus \mathbb{Z}/q_t\mathbb{Z}$, the prime powers $q_1, \ldots, q_t$ are the elementary divisors of $G$.

## Remarks

The [[structure theorem|0RY0B72XAS]] says that the rank $n$, the invariant factors and the elementary divisors are unique, and that they determine $G$ up to isomorphism.
The elementary divisors are the prime power factors of the invariant factors. For example, the invariant factors $2, 12$ give the elementary divisors $2, 4, 3$.
For a finite group $G$, the product of the invariant factors is $|G|$, and the largest invariant factor $k_u$ is the [[exponent|0ZDW0H0VX4]] of $G$.
The same terms are used for finitely generated modules over a principal ideal domain.

## Explanations

### L1 human

There are two standard ways to write a finitely generated abelian group as a sum of cyclic groups.
The invariant factors are orders that divide each other.
The elementary divisors are prime power orders.
