---
tag: T1KR4KPX8P
kind: object
name: Mathieu groups
msc: [20D08, 20B20]
uses: [0YMYMNQ0QZ, BDJ1AX4XBB, 0AYMP41THN, 0K1SCPBNKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Mathieu_group
same_as:
  wikidata: Q934200
  wikipedia: Mathieu group
---

## Description

The Mathieu groups are five finite [[simple groups|0YMYMNQ0QZ]], written $M_{11}$, $M_{12}$, $M_{22}$, $M_{23}$ and $M_{24}$.
Each $M_n$ is a permutation group on $n$ points.
Their orders are:

1. $\abs{M_{11}} = 7920 = 2^4 \cdot 3^2 \cdot 5 \cdot 11$,
2. $\abs{M_{12}} = 95040 = 2^6 \cdot 3^3 \cdot 5 \cdot 11$,
3. $\abs{M_{22}} = 443520 = 2^7 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11$,
4. $\abs{M_{23}} = 10200960 = 2^7 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11 \cdot 23$,
5. $\abs{M_{24}} = 244823040 = 2^{10} \cdot 3^3 \cdot 5 \cdot 7 \cdot 11 \cdot 23$.

They are sporadic groups: they belong to none of the infinite families of finite simple groups.

## Remarks

The Mathieu groups are highly [[multiply transitive|BDJ1AX4XBB]].
$M_{11}$ is sharply $4$-transitive on $11$ points, and $M_{12}$ is sharply $5$-transitive on $12$ points.
$M_{22}$ is $3$-transitive on $22$ points, $M_{23}$ is $4$-transitive on $23$ points, and $M_{24}$ is $5$-transitive on $24$ points.
Apart from the symmetric and alternating groups, $M_{11}$, $M_{12}$, $M_{23}$ and $M_{24}$ are the only finite $4$-transitive groups.
The [[stabiliser|0AYMP41THN]] of a point in $M_{24}$ is $M_{23}$, and the stabiliser of a point in $M_{23}$ is $M_{22}$; likewise the stabiliser of a point in $M_{12}$ is $M_{11}$.
$M_{24}$ is the [[automorphism group|0K1SCPBNKJ]] of the Steiner system $S(5, 8, 24)$ and of the extended binary Golay code, and $M_{12}$ is the automorphism group of the Steiner system $S(5, 6, 12)$.
They were the first sporadic simple groups to be found, by Émile Mathieu in the nineteenth century.

## Explanations

### L1 human

Most finite simple groups come in infinite families, like the alternating groups.
The Mathieu groups are five exceptions that do not fit any family.
They are permutation groups on $11$, $12$, $22$, $23$ and $24$ points, and they are surprisingly symmetric.
For example, $M_{24}$ can move any $5$ of its $24$ points to any other $5$ points, in any order.
They are also the symmetry groups of remarkable combinatorial objects, such as the Golay code used in error correction.
