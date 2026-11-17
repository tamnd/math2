---
tag: Y9CB5P4YCS
kind: concept
name: CLT group
msc: ["20D10", "20D60"]
topics: [1VHQWXC64D]
audience: grad
specializes: [0FXJ7YFMMX]
uses: [G5S1M9, 0X1JXT47GA, 0B85S2V2DR, 3C53TD, 0JM7PA288B, 0S9ZVZ34MD, 0423TXR9AN]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Existence of subgroups of given order
  - url: https://en.wikipedia.org/wiki/Lagrange%27s_theorem_(group_theory)
    locator: Counterexample of the converse of Lagrange's theorem
---

## Summary

A finite [[group|G5S1M9]] $G$ is a CLT group if $G$ has a [[subgroup|0X1JXT47GA]] of order $d$ for each positive divisor $d$ of the [[order|0B85S2V2DR]] $|G|$.
Thus the CLT groups are the finite groups for which the converse of [[Lagrange's theorem|3C53TD]] is true.
The class shows how far the converse of Lagrange's theorem is from the truth, and it sits between the [[supersolvable|AWWM9RWETX]] and the [[solvable|0FXJ7YFMMX]] groups.

## Motivation

Lagrange's theorem says that the order of each subgroup divides $|G|$.
The natural question is whether each divisor of $|G|$ is the order of a subgroup.
The answer is no: [[the alternating group $A_4$ of order $12$ has no subgroup of order $6$|0PDBVPP233]].
But the answer is yes for many groups, for example for each cyclic group and each finite abelian group.
The CLT groups are the groups for which the answer is yes.

## Notation

The letters CLT are an abbreviation of "converse of Lagrange's theorem".
There is no special symbol for the class.

## Remarks

### Examples

- Each finite [[cyclic group|0KVGH0J5B3]] is CLT. Such a group is isomorphic to $\mathbb{Z}/n\mathbb{Z}$ for its order $n$. For each divisor $d$ of $n$, the subgroup $\langle n/d \rangle$ has order $d$, [[by this result|0423TXR9AN]].
- Each finite [[abelian group|082GHNPJ53]] is CLT, by the proof in the basic properties below. For example, the [[Klein four-group|0PMRQJVTME]] has subgroups of orders $1$, $2$ and $4$.
- Each finite [[p-group|06QYRTX9KQ]] is CLT, by the proof in the basic properties below. For example, [[the dihedral group of order 8|054SBCQ93T]] is CLT.
- The [[symmetric group|0515A6D2Y1]] $S_3$ is CLT, as [[this example|QPH0JFF17Q]] shows.
- The symmetric group $S_4$ is CLT, but it is not supersolvable, as [[this example|6WG1EF772J]] shows.

### Non-examples

- The [[alternating group|0Z5905Q73D]] $A_4$ is not CLT, because it has no subgroup of order $6$, by [[this counterexample|0PDBVPP233]]. It is solvable, so the class of CLT groups is smaller than the class of solvable groups.
- The alternating group $A_5$ is not CLT, because it has no subgroup of order $30$, as [[this example|XXT86YX1J0]] shows.
- An infinite group is not CLT, because the definition asks for a finite group.

The group $A_4$ is the smallest group that is not CLT.

### Basic properties

- Each finite abelian group is CLT, and each finite $p$-group is CLT. The proof is below.
- Each [[supersolvable group|AWWM9RWETX]] is CLT. We state this known result without proof.
- Each CLT group is [[solvable|0FXJ7YFMMX]]. We state this known result without proof. Thus no nonabelian [[simple group|0YMYMNQ0QZ]] is CLT.
- A subgroup of a CLT group need not be CLT. The group $S_4$ is CLT, but its subgroup $A_4$ is not CLT.

Thus there are strict inclusions: supersolvable groups, then CLT groups, then solvable groups.
The group $S_4$ shows that the first inclusion is strict, and the group $A_4$ shows that the second inclusion is strict.

Proof that a finite abelian group $G$ is CLT.
We use induction on $|G|$, and we let $d$ be a divisor of $|G|$.

1. If $d = 1$, the subgroup $\{e\}$ has order $d$.
2. Let $d > 1$, and let $p$ be a prime that divides $d$.
3. By [[Cauchy's theorem|0JM7PA288B]], $G$ has an element $z$ of order $p$.
4. The subgroup $Z = \langle z \rangle$ has order $p$, and it is normal, because $G$ is abelian.
5. The [[quotient group|0KYX2N69J0]] $G/Z$ is abelian of order $|G|/p$, and $d/p$ divides $|G|/p$.
6. By induction, $G/Z$ has a subgroup of order $d/p$.
7. By the [[correspondence theorem|0S9ZVZ34MD]], this subgroup is $L/Z$ for a subgroup $L$ with $Z \le L \le G$.
8. Then $|L| = |L/Z| \cdot |Z| = (d/p) \cdot p = d$.

For a finite $p$-group $G$, the same induction works with one change in steps 3 and 4.
The [[centre|0DZ93493VN]] of $G$ is nontrivial, [[by this result|0RZCTT30H5]], so Cauchy's theorem gives an element $z$ of order $p$ in the centre.
Then $\langle z \rangle$ is normal, because $z$ commutes with each element of $G$.
The quotient $G/\langle z \rangle$ is again a $p$-group, so the induction applies.

### History

The abbreviation CLT is used in the research literature.
For example, a paper of Bray from 1968 has the title "A note on CLT groups".
We could not check who first defined the class, so we give no earlier name or date.

### Common errors

- To check that a group is CLT, one must find a subgroup of each order $d$ that divides $|G|$. The [[Sylow theorems|FESTJ0K9TX]] give only the prime power orders $d$.
- A group with an element of each prime order that divides $|G|$ need not be CLT. The group $A_4$ has elements of orders $2$ and $3$, but no subgroup of order $6$.
- Solvable does not imply CLT. The group $A_4$ is solvable and not CLT.

## Explanations

### L1 human

A group of $12$ elements can only have subgroups of sizes $1$, $2$, $3$, $4$, $6$ and $12$.
These are the numbers that divide $12$.
Some groups of size $12$ have a subgroup of each of these sizes.
Such a group is a CLT group.
The rotations of a clock with $12$ hours form a CLT group: the rotations by multiples of $2$ hours form a subgroup of size $6$.
The group $A_4$ also has $12$ elements, but no subgroup of size $6$, so it is not a CLT group.

### L2 human

We check that $\mathbb{Z}/12\mathbb{Z}$ is CLT.

1. The divisors of $12$ are $1$, $2$, $3$, $4$, $6$ and $12$.
2. The subgroup $\{0\}$ has order $1$, and $\langle 6 \rangle = \{0, 6\}$ has order $2$.
3. The subgroup $\langle 4 \rangle = \{0, 4, 8\}$ has order $3$, and $\langle 3 \rangle = \{0, 3, 6, 9\}$ has order $4$.
4. The subgroup $\langle 2 \rangle = \{0, 2, 4, 6, 8, 10\}$ has order $6$, and $\langle 1 \rangle$ is the whole group, of order $12$.
5. Thus each divisor of $12$ is the order of a subgroup.

The typical use of the notion is as a test case.
A theorem that gives subgroups of given orders, such as Sylow's theorem or Hall's theorem, is a partial answer to the CLT question.

A trap is to check only the prime power divisors.
The group $A_4$ has subgroups of orders $1$, $2$, $3$, $4$ and $12$.
The only missing order is $6$, which is not a prime power.

### L3 human

The converse of Lagrange's theorem holds in pieces for all finite groups.
The [[Sylow theorems|FESTJ0K9TX]] give a subgroup of each prime power order that divides $|G|$.
For solvable groups, [[Hall's theorem|8Z8PE69SJS]] gives a [[Hall subgroup|KPWW9X14V2]] of order $d$ for each divisor $d$ of $|G|$ with $\gcd(d, |G|/d) = 1$.
A CLT group has subgroups of all orders, and the result that it is solvable shows that this condition is strong.
The proofs for abelian groups and for $p$-groups above use a normal subgroup of prime order and induction on $|G|$.
A [[supersolvable group|AWWM9RWETX]] also has a normal subgroup of prime order, and supersolvable groups are CLT.
The class of CLT groups is not closed under subgroups, as $A_4 \le S_4$ shows.
Thus the CLT property is a global property of $G$, and it does not pass to the subgroups of $G$.
