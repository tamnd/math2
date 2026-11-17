---
tag: B7BJJBV1S0
kind: example
name: The point stabilizer S_{n-1} is a maximal subgroup of S_n
msc: ["20E28", "20B30"]
topics: [BAVE5RN4EE]
audience: ug2
instance_of: [RTTRNQ4JYF]
uses: [0515A6D2Y1, RTTRNQ4JYF, 0X1JXT47GA, 0DTXBQPA2S, 0Z5905Q73D, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Maximal_subgroup
    locator: lead section
---

## Example

Let $n \geq 2$, and let $S_n$ be the [[symmetric group|0515A6D2Y1]] on $\{1, \ldots, n\}$, with products composed from right to left.
Let $H = \{\sigma \in S_n : \sigma(n) = n\}$, the stabilizer of the point $n$.
The restriction of each $\sigma \in H$ to $\{1, \ldots, n-1\}$ is a permutation of this set, and this gives an isomorphism $H \cong S_{n-1}$.
We show that $H$ is a [[maximal subgroup|RTTRNQ4JYF]] of $S_n$.

1. $H$ is a [[subgroup|0X1JXT47GA]]: $e(n) = n$, and if $\sigma(n) = \tau(n) = n$, then $\tau^{-1}(n) = n$ (apply $\tau^{-1}$ to $\tau(n) = n$), so $\sigma\tau^{-1}(n) = \sigma(n) = n$.
2. $H \neq S_n$, because the transposition $(1\,n)$ sends $n$ to $1$.
3. Let $L$ be a subgroup of $S_n$ with $H \subsetneq L$. Choose $\sigma \in L$ with $\sigma \notin H$, and put $i = \sigma(n)$. Then $i \neq n$.
4. Let $\tau \in S_n$, and put $j = \tau(n)$. We show that $\tau \in L$, by cases.
5. Case $j = n$. Then $\tau \in H \subseteq L$.
6. Case $j \neq n$. Let $\alpha = e$ if $i = j$, and $\alpha = (i\,j)$ if $i \neq j$. In both cases $\alpha(i) = j$, and $\alpha(n) = n$ because $i \neq n$ and $j \neq n$. So $\alpha \in H$.
7. In case $j \neq n$, we have $(\alpha\sigma)(n) = \alpha(i) = j = \tau(n)$. Put $\beta = (\alpha\sigma)^{-1}\tau$. Then $\beta(n) = (\alpha\sigma)^{-1}(j) = n$, so $\beta \in H$.
8. So $\tau = \alpha\sigma\beta$ with $\alpha, \beta \in H \subseteq L$ and $\sigma \in L$. Since $L$ is closed under products, $\tau \in L$.
9. By steps 5 to 8, $L = S_n$. With steps 1 and 2, $H$ is a maximal subgroup of $S_n$.

## Remarks

The [[index|0DTXBQPA2S]] of $H$ in $S_n$ is $n! / (n-1)! = n$.
The left coset $\tau H$ is the set of permutations that send $n$ to $\tau(n)$, so the $n$ cosets correspond to the $n$ possible values of $\tau(n)$.
For $n \geq 3$, the [[alternating group|0Z5905Q73D]] $A_n$ is another maximal subgroup, of index $2$: any subgroup of prime index in a finite group is maximal, by Lagrange's theorem.
So $S_n$ has maximal subgroups of index $2$ and of index $n$.
The conjugate $gHg^{-1}$ is the stabilizer of the point $g(n)$, so the $n$ point stabilizers are all maximal.
For $n \geq 3$, $H$ is not normal, because the stabilizers of $n$ and of $1$ are different.
The proof uses only that $H$ can send any point $i \neq n$ to any point $j \neq n$.
So the same proof shows that in a [[2-transitive|BDJ1AX4XBB]] permutation group, the stabilizer of a point is maximal.

## Explanations

### L1 human

Think of $n$ people in $n$ chairs, and of all the ways to rearrange them.
The subgroup $H$ is the set of rearrangements that keep the person in chair $n$ in place.
If a group of rearrangements contains $H$ and one move that takes someone else into chair $n$, then it can rearrange everybody in every way.
So no group fits strictly between $H$ and all rearrangements.

### L2 human

We check the case $n = 3$, where $H = \{e, (1\,2)\}$.

1. Let $L$ be a subgroup with $H \subseteq L \subseteq S_3$. By Lagrange's theorem, $|L|$ is a multiple of $|H| = 2$ and divides $6$, so $|L| = 2$ or $|L| = 6$.
2. If $|L| = 2$, then $L = H$. If $|L| = 6$, then $L = S_3$. So no subgroup lies strictly between $H$ and $S_3$.
3. The proof above gives the same result in another way. With $\sigma = (1\,3)$, any subgroup that contains $(1\,2)$ and $(1\,3)$ contains $(1\,2)(1\,3) = (1\,3\,2)$, so it contains elements of orders $2$ and $3$, and its order is $6$.

The typical use of this example is to see that a maximal subgroup can have a large index, here $n$, and need not be normal.
A trap: the maximal subgroups of $S_n$ are not only $A_n$ and the point stabilizers.
For example, $S_4$ also has three maximal subgroups of order $8$.
