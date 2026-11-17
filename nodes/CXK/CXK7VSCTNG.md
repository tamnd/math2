---
tag: CXK7VSCTNG
kind: example
name: A normal subgroup of P that is not its core in S4
msc: ["20B30"]
topics: [E1506A5A55]
audience: ug2
not_instance_of:
  - target: 0GETX79CJN
    note: K is normal in the subgroup P of order 8, but it is not normal in S4
uses: [0515A6D2Y1, 0CB0DX5BVV, 0V547YQRMV, 0ZTGMDNVTB]
sources:
  - url: https://en.wikipedia.org/wiki/Core_(group_theory)
    locator: The normal core
---

## Example

In the [[symmetric group|0515A6D2Y1]] $S_4$, compose permutations from right to left.
Let $P = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3), (1\,2), (3\,4), (1\,3\,2\,4), (1\,4\,2\,3)\}$, a subgroup of order $8$.
Let $K = \{e, (1\,2), (3\,4), (1\,2)(3\,4)\}$.
Then $K$ is normal in $P$, but $K$ is not the [[normal core|0GETX79CJN]] of $P$ in $S_4$.

1. $K$ is a subgroup of $P$ of index $2$. By [[the index two theorem|0V547YQRMV]], $K$ is a [[normal subgroup|0CB0DX5BVV]] of $P$.
2. Conjugation by $(2\,3)$ sends $(1\,2)$ to $(1\,3)$, and $(1\,3) \notin K$. So $K$ is not normal in $S_4$.
3. The normal core of $P$ is normal in $S_4$. By step 2, $K$ is not the core.
4. In fact $K$ is not even contained in the core. The core is $V_4 = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$, and $(1\,2) \notin V_4$.

## Remarks

The core of $K$ itself in $S_4$ is $\{e\}$.
The conjugates $(2\,3)K(2\,3)^{-1} = \{e, (1\,3), (2\,4), (1\,3)(2\,4)\}$ and $(2\,4)K(2\,4)^{-1} = \{e, (1\,4), (2\,3), (1\,4)(2\,3)\}$ meet $K$ only in $e$.
But the core of $K$ in $P$ is $K$, because $K$ is normal in $P$.
So the core depends on the large group.
Normality is not transitive: $K \trianglelefteq P$ and $P$ is a subgroup of $S_4$, but $K$ is not normal in $S_4$.

## Explanations

### L1 human

The subgroup $K$ fits well inside the smaller group $P$.
In $P$ it is normal.
But inside the whole of $S_4$, a renaming of the numbers moves $K$ to a different subgroup.
The normal core must survive every renaming in $S_4$, so $K$ fails.

### L2 human

The test for the core has two parts: the subgroup must lie in $P$, and it must be normal in $S_4$.
$K$ passes the first part and fails the second part.
One conjugate is enough to show the failure, as in step 2.
A common error is to think that "normal in a normal subgroup" means "normal".
Here $P$ is not normal in $S_4$, but even a chain $K \trianglelefteq P \trianglelefteq G$ does not give $K \trianglelefteq G$ in general.
For example, in $S_4$ the chain $\{e, (1\,2)(3\,4)\} \trianglelefteq V_4 \trianglelefteq S_4$ has a first subgroup that is not normal in $S_4$.
