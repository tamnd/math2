---
tag: ~eb292eed
kind: example
name: Every subgroup of the quaternion group is normal, but the group is not abelian
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0CB0DX5BVV]
illustrates: [0JPDTEDCFD]
uses: [0NRJGW864D, 3C53TD, 0V547YQRMV, 0DZ93493VN]
sources:
  - url: https://en.wikipedia.org/wiki/Quaternion_group
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Examples
---

## Example

Let $Q_8 = \{1, -1, i, -i, j, -j, k, -k\}$ be the [[quaternion group|0NRJGW864D]].
Its multiplication rules are $(-1)^2 = 1$, $i^2 = j^2 = k^2 = -1$, $ij = k$, $jk = i$, $ki = j$, $ji = -k$, $kj = -i$ and $ik = -j$.
The element $-1$ commutes with each element, and $(-1)x = -x$.
We show that each subgroup of $Q_8$ is [[normal|0CB0DX5BVV]], but $Q_8$ is not abelian.

1. $ij = k$ and $ji = -k$, and $k \ne -k$. So $Q_8$ is not abelian.
2. The element $-1$ has order $2$. For $x \in \{\pm i, \pm j, \pm k\}$, $x^2 = -1$ and $x^4 = 1$, so $x$ has order $4$.
3. By [[Lagrange's theorem|3C53TD]], a subgroup of $Q_8$ has order $1$, $2$, $4$ or $8$.
4. A subgroup of order $2$ is $\{1, x\}$ with $x$ of order $2$. By step 2, the only one is $\{1, -1\}$.
5. A subgroup $H$ of order $4$ has $3$ elements different from $1$. At most one of them is $-1$, so $H$ contains some $x$ of order $4$.
6. Then $H$ contains the $4$ powers $1$, $x$, $-1$ and $-x$ of $x$, so $H = \langle x \rangle$. This gives $\langle i \rangle$, $\langle j \rangle$ and $\langle k \rangle$, because $\langle -x \rangle = \langle x \rangle$.
7. So the subgroups of $Q_8$ are $\{1\}$, $\{\pm 1\}$, $\langle i \rangle$, $\langle j \rangle$, $\langle k \rangle$ and $Q_8$.
8. $\{1\}$ and $Q_8$ are normal, because $g\{1\}g^{-1} = \{1\}$ and $gQ_8g^{-1} = Q_8$ for each $g$.
9. $\{\pm 1\}$ is normal, because $g(-1)g^{-1} = -gg^{-1} = -1$ for each $g$. In fact $\{\pm 1\}$ is the [[centre|0DZ93493VN]] of $Q_8$.
10. $\langle i \rangle$, $\langle j \rangle$ and $\langle k \rangle$ have order $4$, so they have index $8 / 4 = 2$. They are normal, because [[subgroups of index two are normal|0V547YQRMV]].
11. So all six subgroups of $Q_8$ are normal.

## Remarks

Step 10 can also be checked by hand.
For example, $jij^{-1} = -i$ by the computation in [[conjugate elements|0DXD4QSZ8A]], so conjugation sends $\langle i \rangle$ to $\langle i \rangle$.
This example shows that the converse of [[subgroups of abelian groups are normal|0JPDTEDCFD]] is false.
A group in which each subgroup is normal is a Dedekind group.
A non-abelian Dedekind group is a Hamiltonian group, and $Q_8$ is the smallest one.
It has order $8$, and each group of order less than $8$ with all subgroups normal is abelian.

## Explanations

### L1 human

In an abelian group, all subgroups are normal, because conjugation moves nothing.
One may think that the converse holds: if no subgroup moves, the group must be abelian.
The quaternion group shows that this is wrong.
Conjugation does move some elements of $Q_8$: it sends $i$ to $-i$.
But it never moves a whole subgroup, because $i$ and $-i$ are in the same subgroup.

### L2 human

The method in steps 3 to 7 is a standard way to list all subgroups of a small group.
Lagrange's theorem gives the possible orders.
The orders of the elements then decide which subgroups exist.
After the list, the test for normality is short, because most subgroups have index $2$ or lie in the centre.
A common error is to think that "each subgroup is normal" means that each element commutes with each other element.
Normality of $\langle i \rangle$ says only that $g\langle i \rangle g^{-1} = \langle i \rangle$ as a set, and $jij^{-1} = -i \ne i$.
