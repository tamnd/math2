---
tag: 0NRJGW864D
kind: object
name: Quaternion group
aliases: [q8]
msc: [20D15]
uses: [G5S1M9, 0S7Y9Q990Q]
sources:
  - url: https://en.wikipedia.org/wiki/Quaternion_group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Quaternion_group
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Quaternion_group
    locator: Compared to dihedral group
same_as:
  wikidata: Q1335680
  wikipedia: Quaternion group
---

## Description

The quaternion group $Q_8$ is the set $\{1, -1, i, -i, j, -j, k, -k\}$ of quaternions, with quaternion multiplication as the operation.
The multiplication follows from the rules $i^2 = j^2 = k^2 = ijk = -1$, where $-1$ commutes with each element.
These rules give $ij = k$, $jk = i$, $ki = j$ and $ji = -k$, $kj = -i$, $ik = -j$.
The group has order $8$, and it is not [[abelian|082GHNPJ53]].

## Remarks

The element $-1$ is the only element of order $2$, and the six elements $\pm i, \pm j, \pm k$ have order $4$.
The [[centre|0DZ93493VN]] and the [[commutator subgroup|0ASGSTXSBW]] of $Q_8$ are both $\{1, -1\}$, and $Q_8 / \{1, -1\}$ is the [[Klein four-group|0PMRQJVTME]].
Each subgroup of $Q_8$ is [[normal|0CB0DX5BVV]], although $Q_8$ is not abelian.
The groups $Q_8$ and $D_4$ are not isomorphic, because $D_4$ has five elements of order $2$.

## Explanations

### L1 human

The quaternion group is a small group of order $8$ in which the elements do not commute.
You can think of $i$, $j$, $k$ as three square roots of $-1$ whose products go around in a circle.
It is a good test case, because many simple guesses about groups fail for it.
