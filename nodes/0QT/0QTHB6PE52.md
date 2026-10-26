---
tag: 0QTHB6PE52
kind: statement
role: theorem
name: The group of units of Z/pZ is cyclic
msc: [11A07, 20K01]
uses: [0F8X8ZRQ53, 0B85Q41RP6, 0S7495H4HM]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n
    locator: Structure
  - url: https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n
    locator: Notation
---

## Statement

Let $p$ be a prime number.
Then the group $(\mathbb{Z}/p\mathbb{Z})^\times$ is [[cyclic|0KVGH0J5B3]] of order $p - 1$.

## Remarks

So $(\mathbb{Z}/p\mathbb{Z})^\times$ is isomorphic to the additive group $\mathbb{Z}/(p-1)\mathbb{Z}$, but no simple general formula for a generator is known.
A generator is a primitive root modulo $p$, and there are $\varphi(p - 1)$ of them.
For $p = 7$, the powers of $3$ modulo $7$ are $1, 3, 2, 6, 4, 5$, so $3$ is a primitive root modulo $7$.
More generally, $(\mathbb{Z}/n\mathbb{Z})^\times$ is cyclic if and only if $n$ is $1$, $2$, $4$, $p^k$ or $2 p^k$ for an odd prime $p$. Gauss first proved this.

## Explanations

### L1 human

For a prime $p$, one residue modulo $p$ has powers that give all the nonzero residues.
Such a residue is a primitive root.
So the multiplicative group modulo $p$ is cyclic.
