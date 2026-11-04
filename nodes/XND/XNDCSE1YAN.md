---
tag: XNDCSE1YAN
kind: proof
name: Proof that the symmetric group on five or more letters is not solvable
msc: [20F16, 20B30]
proves: 0J53NE674D
uses: [0P3KZK0FTV, 096HN851YZ, 0C093D1T4M, 0ARPRJQWZ2, 0T13HM377F, 0SQTMQTSRZ, 05Y0F9M0TS, 0RJMNEN3BJ]
sources:
  - url: https://en.wikipedia.org/wiki/Solvable_group
    locator: Non-example
---

## Proof

We argue by contradiction, through the alternating group.

1. Let $n \geq 5$. The [[alternating group|0T13HM377F]] $A_n$ is the subgroup of [[even permutations|0SQTMQTSRZ]] of the [[symmetric group|0RJMNEN3BJ]] $S_n$.
2. We compose permutations from right to left. Then $(1\,2\,3) = (1\,3)(1\,2)$ and $(3\,4\,5) = (3\,5)(3\,4)$. So both $3$-cycles are even and lie in $A_n$; here we use $n \geq 5$.
3. Let $a = (1\,2\,3)$ and $b = (3\,4\,5)$. Then $ab$ sends $3$ to $a(4) = 4$, while $ba$ sends $3$ to $b(1) = 1$. So $ab \neq ba$, and $A_n$ is not abelian.
4. By the [[simplicity of the alternating group|0ARPRJQWZ2]], $A_n$ is [[simple|0C093D1T4M]].
5. Suppose that $A_n$ is [[solvable|0P3KZK0FTV]]. Take a [[subnormal series|096HN851YZ]] $\{e\} = G_0 \trianglelefteq \cdots \trianglelefteq G_k = A_n$ with abelian factors.
6. Since $A_n \neq \{e\}$, some $G_j$ equals $A_n$ with $j \geq 1$. Let $j$ be the least such index. Then $G_{j-1} \neq A_n$.
7. The subgroup $G_{j-1}$ is normal in $G_j = A_n$. Since $A_n$ is simple and $G_{j-1} \neq A_n$, we get $G_{j-1} = \{e\}$.
8. So the factor $G_j/G_{j-1} = A_n/\{e\}$ is abelian. The map $x \mapsto x\{e\}$ is an isomorphism from $A_n$ onto $A_n/\{e\}$, so $A_n$ is abelian.
9. This contradicts step 3. So $A_n$ is not solvable.
10. If $S_n$ were solvable, then its subgroup $A_n$ would be solvable, because [[subgroups of solvable groups are solvable|05Y0F9M0TS]]. This contradicts step 9.
11. Hence $S_n$ is not solvable.

## Idea

A simple group that is not abelian cannot be solvable: any series must jump from the trivial group straight to the whole group, and that factor is not abelian. For $n \geq 5$ the group $A_n$ is such a group. A solvable $S_n$ would make its subgroup $A_n$ solvable.
