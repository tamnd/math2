---
tag: EFQWRXK3HF
kind: example
name: The quaternion group modulo its centre is the Klein four-group
msc: ["20D15"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0KYX2N69J0]
uses: [0NRJGW864D, 0DZ93493VN, 0PMRQJVTME, 0CB0DX5BVV, 3C53TD]
sources:
  - url: https://en.wikipedia.org/wiki/Quaternion_group
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Examples
---

## Example

Let $Q_8 = \{\pm 1, \pm i, \pm j, \pm k\}$ be the [[quaternion group|0NRJGW864D]], with $i^2 = j^2 = k^2 = ijk = -1$.
Its [[centre|0DZ93493VN]] is $Z = \{1, -1\}$.
The [[quotient group|0KYX2N69J0]] $Q_8/Z$ is isomorphic to the [[Klein four-group|0PMRQJVTME]] $V_4$.

1. The element $-1$ commutes with every element, so $\{1, -1\} \subseteq Z$.
2. The elements $\pm i$, $\pm j$, $\pm k$ are not in $Z$. We have $ij = k$ but $ji = -k$; $jk = i$ but $kj = -i$; $ki = j$ but $ik = -j$. So each of $i$, $j$, $k$ fails to commute with some element, and so do their negatives.
3. Thus $Z = \{1, -1\}$. The centre is a [[normal subgroup|0CB0DX5BVV]], so $Q_8/Z$ is defined.
4. By [[Lagrange's theorem|3C53TD]], $Q_8/Z$ has $8/2 = 4$ elements. They are the cosets $Z = \{\pm 1\}$, $iZ = \{\pm i\}$, $jZ = \{\pm j\}$ and $kZ = \{\pm k\}$.
5. Each non-identity coset has order $2$. For example, $(iZ)^2 = i^2Z = (-1)Z = Z$, and the same holds for $j$ and $k$.
6. The product of two different non-identity cosets is the third one. We have $(iZ)(jZ) = kZ$, $(jZ)(kZ) = iZ$ and $(iZ)(kZ) = (-j)Z = jZ$.
7. Steps 5 and 6 are the multiplication rules of $V_4$. So the map $Z \mapsto e$, $iZ \mapsto a$, $jZ \mapsto b$, $kZ \mapsto c$ is an isomorphism onto $V_4 = \{e, a, b, c\}$.

## Remarks

$Q_8$ is not abelian, but its quotient by the centre is abelian.
The quotient $Q_8/Z$ is not cyclic, because no element has order $4$.
This is consistent with [[the theorem that G is abelian when G modulo its centre is cyclic|0AH9Q6YNMT]]: since $Q_8$ is not abelian, $Q_8/Z(Q_8)$ cannot be cyclic.
In the quotient, the signs are forgotten: $ij = k$ and $ji = -k$ give the same coset $kZ$.
The [[dihedral group|0JZ27DMJ5D]] $D_4$ of order $8$ also has a centre of order $2$ and a quotient isomorphic to $V_4$, although $D_4 \not\cong Q_8$.

## Explanations

### L1 human

In the quaternion group, the order of a product matters only through a sign: $ij = k$ and $ji = -k$.
The quotient by $\{1, -1\}$ forgets the signs.
After this, only four elements remain: $1$, $i$, $j$ and $k$ without signs.
Each of them squared gives $1$, and any two of $i$, $j$, $k$ multiply to the third.
This is the Klein four-group.

### L2 human

The computation has three parts: find the normal subgroup, list the cosets, and build the table.
Step 6 shows a typical feature of quotient groups: the representative can change the sign, but not the coset.
For example, $(kZ)(iZ)$ can be computed as $ki = j$ or as $(-k)(-i) = j$, and $(-k)(i) = -j$ also lies in $jZ$.
A trap is to think that the quotient of a group that is not abelian is never abelian.
Here the quotient is abelian, and the commutator subgroup $\{\pm 1\}$ of $Q_8$ is contained in $Z$.
