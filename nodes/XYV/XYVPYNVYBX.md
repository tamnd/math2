---
tag: XYVPYNVYBX
kind: example
name: List of small groups
msc: [20D99, 20K01]
illustrates: [G5S1M9]
uses: [0KVGH0J5B3, 00HF4RJ5QN, 0JZ27DMJ5D, 0NRJGW864D, 0515A6D2Y1, 0Z5905Q73D, 0PMRQJVTME]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_small_groups
same_as:
  wikidata: Q1332566
  wikipedia: List of small groups
---

## Example

Up to isomorphism, the [[groups|G5S1M9]] of order $n \le 15$ are the following.
Here $C_n$ is the [[cyclic group|0KVGH0J5B3]] of order $n$ and $\times$ is the [[direct product|00HF4RJ5QN]].
The group $D_{2m}$ is the [[dihedral group|0JZ27DMJ5D]] of order $2m$, and $Q_8$ is the [[quaternion group|0NRJGW864D]].
The group $A_4$ is the [[alternating group|0Z5905Q73D]] on $4$ letters, and $\mathrm{Dic}_{12} = C_3 \rtimes C_4$ is the dicyclic group of order $12$.

1. Orders $1$, $2$, $3$, $5$, $7$, $11$, $13$: only $C_n$.
2. Order $4$: $C_4$ and the [[Klein four-group|0PMRQJVTME]] $C_2 \times C_2$.
3. Order $6$: $C_6$ and $D_6 \cong S_3$, the [[symmetric group|0515A6D2Y1]].
4. Order $8$: $C_8$, $C_4 \times C_2$, $C_2 \times C_2 \times C_2$, $D_8$ and $Q_8$.
5. Order $9$: $C_9$ and $C_3 \times C_3$.
6. Order $10$: $C_{10}$ and $D_{10}$.
7. Order $12$: $C_{12}$, $C_6 \times C_2$, $A_4$, $D_{12}$ and $\mathrm{Dic}_{12}$.
8. Order $14$: $C_{14}$ and $D_{14}$.
9. Order $15$: only $C_{15}$.

So the numbers of groups of orders $1, 2, \dots, 15$ are $1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1$.
For order $16$ there are already $14$ groups.

## Remarks

Groups of prime order $p$ are cyclic, which explains the first line.
For primes $p < q$, a group of order $pq$ is cyclic unless $p$ divides $q - 1$.
This explains why $15 = 3 \cdot 5$ gives only $C_{15}$, while $6$, $10$ and $14$ also give a dihedral group.
A group of order $p^2$ is abelian, so it is $C_{p^2}$ or $C_p \times C_p$, as for orders $4$ and $9$.
In each order the abelian groups are given by the [[classification of finite abelian groups|07CQR9BW3R]].

## Explanations

### L1 human

This is the start of a catalogue of all finite groups, sorted by size.
Small sizes allow few groups: a prime number of elements forces a cyclic group.
The first interesting sizes are $8$ and $12$, which already show non-abelian groups such as the quaternion group and the alternating group $A_4$.
