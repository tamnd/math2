---
tag: FB79N7AHZA
kind: example
name: Integers modulo n form a cyclic group
msc: [20A05]
instance_of: [0KVGH0J5B3, 082GHNPJ53]
illustrates: [04RG02S6BA]
uses: [03VFZ2WETT, 0B85Q41RP6]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_group
    locator: Integer and modular addition
---

## Example

Let $n \ge 1$. The [[integers modulo $n$|03VFZ2WETT]], $\mathbb{Z}/n\mathbb{Z} = \{0, 1, \dots, n-1\}$, form a group under addition modulo $n$.
Each element $k$ is the sum $1 + 1 + \dots + 1$ of $k$ copies of $1$. Thus $1$ is a generator, and the group is [[cyclic|0B85Q41RP6]] of order $n$.
Addition modulo $n$ is commutative, so the group is abelian. This agrees with the result that [[cyclic groups are abelian|04RG02S6BA]].
