---
tag: 0PDBVPP233
kind: counterexample
name: A4 has no subgroup of order 6
aliases: [converse-of-lagranges-theorem-fails-for-the-alternating-group-a4]
msc: ["20D60"]
topics: [1VHQWXC64D]
audience: ug1
uses: [0Z5905Q73D, 0515A6D2Y1, 0X1JXT47GA, 3C53TD, 03DEH43F4H, 0DTXBQPA2S, 0V547YQRMV, 0CB0DX5BVV, 0PMRQJVTME, 0JM7PA288B, 082GHNPJ53, AWWM9RWETX, Y9CB5P4YCS]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange's_theorem_(group_theory)
    locator: Existence of subgroups of given order
  - url: https://en.wikipedia.org/wiki/Lagrange's_theorem_(group_theory)
    locator: Counterexample of the converse of Lagrange's theorem
  - book: isbn:9780471433347
    locator: Section 3.2
---

## Counterexample

The converse of [[Lagrange's theorem|3C53TD]] would say this: if $G$ is a finite group and $d$ is a positive divisor of $|G|$, then $G$ has a subgroup of order $d$.
This is false.
Let $A_4$ be the [[alternating group|0Z5905Q73D]] of the even permutations of $\{1, 2, 3, 4\}$, with permutations composed from right to left.
It has order $12$, and $6$ divides $12$, but $A_4$ has no subgroup of order $6$.

1. The elements of $A_4$ are the identity $e$, the three double transpositions $(1\,2)(3\,4)$, $(1\,3)(2\,4)$, $(1\,4)(2\,3)$, and the eight $3$-cycles. There are $4 \cdot 2 = 8$ three-cycles, because a $3$-cycle is given by the point that it fixes and one of two directions. The count is $1 + 3 + 8 = 12$.
2. Suppose that $H$ is a [[subgroup|0X1JXT47GA]] of $A_4$ with $|H| = 6$. Then the [[index|0DTXBQPA2S]] is $[A_4 : H] = 12 / 6 = 2$.
3. Claim: $g^2 \in H$ for each $g \in A_4$. If $g \in H$, then $g^2 \in H$, because $H$ is closed under products.
4. Let $g \notin H$. There are only two [[left cosets|03DEH43F4H]], $H$ and $gH$. Suppose $g^2 \notin H$. Then $g^2 \in gH$, so $g^2 = gh$ for some $h \in H$.
5. We cancel $g$ on the left and get $g = h \in H$. This contradicts $g \notin H$. So $g^2 \in H$, and the claim holds.
6. Let $c$ be a $3$-cycle. Then $c^3 = e$, so $c = c^4 = (c^2)^2$. Thus $c$ is the square of the element $c^2$ of $A_4$.
7. By steps 3 and 6, each of the eight $3$-cycles lies in $H$. With $e$, the subgroup $H$ has at least $9$ elements.
8. This contradicts $|H| = 6$. So $A_4$ has no subgroup of order $6$.

## Remarks

### A second proof

This proof uses normal subgroups and conjugation.

1. Suppose $|H| = 6$. A subgroup of index $2$ is [[normal|0V547YQRMV]], so $gHg^{-1} = H$ for each $g \in A_4$.
2. The group $H$ has an element $t$ of order $2$. The elements $x \neq x^{-1}$ of $H$ come in pairs $\{x, x^{-1}\}$, and $e$ is its own inverse. So the $6 - 1 = 5$ other elements cannot all lie in pairs, and some $t \neq e$ has $t = t^{-1}$.
3. The elements of order $2$ in $A_4$ are the double transpositions, by step 1 of the counterexample. So $t$ is a double transposition.
4. Let $c = (1\,2\,3)$. For each permutation $\sigma$, the conjugate $c \sigma c^{-1}$ replaces each number $a$ in the cycles of $\sigma$ by $c(a)$.
5. So conjugation by $c$ sends $(1\,2)(3\,4) \mapsto (2\,3)(1\,4)$, $(1\,4)(2\,3) \mapsto (2\,4)(3\,1)$ and $(1\,3)(2\,4) \mapsto (2\,1)(3\,4)$.
6. Thus $t$, $ctc^{-1}$ and $c^2tc^{-2}$ are the three double transpositions. By step 1, all three lie in $H$.
7. Then $H$ contains the [[Klein four-group|0PMRQJVTME]] $V = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$ as a subgroup.
8. By Lagrange's theorem, $4$ divides $6$. This is false, so no such $H$ exists.

### Partial converses

The converse of Lagrange's theorem holds in these cases.

- [[Cauchy's theorem|0JM7PA288B]]: for each prime $p$ that divides $|G|$, there is a subgroup of order $p$.
- The [[Sylow theorems|FESTJ0K9TX]]: for each prime power $p^k$ that divides $|G|$, there is a subgroup of order $p^k$.
- Each finite [[abelian group|082GHNPJ53]] has a subgroup of each order that divides $|G|$.
- Each finite [[supersolvable group|AWWM9RWETX]] has a subgroup of each order that divides $|G|$. Groups with this property are called [[CLT groups|Y9CB5P4YCS]].

### How the example sits among small groups

Each group of order less than $12$ has a subgroup of each order that divides its order.
So $A_4$ is the smallest group for which the converse fails.
The other four groups of order $12$ have a subgroup of order $6$.
The [[symmetric group|0515A6D2Y1]] $S_4$ contains $A_4$, and it has a subgroup of each order that divides $24$.
So a group with this property can have a subgroup without it.

## Explanations

### L1 human

Lagrange's theorem says which sizes a subgroup can have.
It does not promise that each allowed size occurs.
The group $A_4$ has $12$ elements, and $6$ is an allowed size, but no subgroup has $6$ elements.
The reason is that $A_4$ has $8$ elements of order $3$, and a subgroup of size $6$ would need to contain all of them.
That is more than $6$ elements.

### L2 human

We check step 6 for $c = (1\,2\,3)$.

1. We compute $c^2 = (1\,3\,2)$, because $c$ sends $1 \mapsto 2 \mapsto 3$.
2. We compute $(c^2)^2 = (1\,3\,2)(1\,3\,2) = (1\,2\,3)$, because $(1\,3\,2)$ sends $1 \mapsto 3 \mapsto 2$.
3. So $c = (c^2)^2$ is a square, and a subgroup of index $2$ must contain it.

The typical use of this example is to stop a false argument of the form "$d$ divides $|G|$, so take a subgroup of order $d$".
Such a subgroup exists only under extra conditions, such as those in the partial converses above.
A trap is to think that the converse fails only for large or complicated groups.
The group $A_4$ has only $12$ elements.
