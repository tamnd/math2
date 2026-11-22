---
tag: A3KBTY9JW7
kind: proof
name: Proof of the theorem on the four fundamental subspaces
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
proves: 73DVECPAT6
uses: [0EWQEYRVA8, 5NKND0CPKP, 0TZAG60ZYT, 0PDVQEP0ZC, 05HQYM0R4G, 079D68S3AW, 06HTJNCMPA, 0QW084460E, 11CSKXQNG3]
methods: [0NTF6DMVAP, MKHVRNW68H]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_linear_algebra
    locator: lead section
---

## Proof

We count dimensions with the rank and the free variables, read each equation of $Ax = 0$ as an orthogonality condition, and use $v \cdot v > 0$ for $v \ne 0$ to get the direct sums.

1. By the [[definition of rank|0EWQEYRVA8]], $\dim \operatorname{Col}(A) = r$.
2. By the [[theorem on the free variables|5NKND0CPKP]], $\dim \operatorname{Null}(A) = n - r$.
3. The rows of $A$ are the columns of $A^{\mathsf{T}}$, so $\operatorname{Row}(A) = \operatorname{Col}(A^{\mathsf{T}})$, and $\dim \operatorname{Row}(A) = \operatorname{rank} A^{\mathsf{T}} = r$ because [[row rank equals column rank|0TZAG60ZYT]].
4. The matrix $A^{\mathsf{T}}$ is $m$ columns wide and has rank $r$ by step 3, so the [[theorem on the free variables|5NKND0CPKP]] for $A^{\mathsf{T}}$ gives $\dim \operatorname{Null}(A^{\mathsf{T}}) = m - r$, which proves part 1.
5. Now let $F = \mathbb{R}$ and let $a_1, \dots, a_m \in \mathbb{R}^n$ be the rows of $A$; by the definition of the [[matrix-vector product|0PDVQEP0ZC]], entry $i$ of $Ax$ is the [[dot product|05HQYM0R4G]] $a_i \cdot x$.
6. So $Ax = 0$ if and only if $a_i \cdot x = 0$ for every $i$.
7. The dot product is linear in each argument, so $x$ is orthogonal to every $a_i$ if and only if it is orthogonal to every linear combination of them, that is, to every vector of $\operatorname{Row}(A)$.
8. Steps 6 and 7 and the [[definition of the orthogonal complement|079D68S3AW]] give $\operatorname{Null}(A) = \operatorname{Row}(A)^\perp$.
9. Steps 5 to 8 for $A^{\mathsf{T}}$ give $\operatorname{Null}(A^{\mathsf{T}}) = \operatorname{Row}(A^{\mathsf{T}})^\perp$, and $\operatorname{Row}(A^{\mathsf{T}}) = \operatorname{Col}(A)$ by step 3 for $A^{\mathsf{T}}$, which proves part 2.
10. Let $v \in \operatorname{Row}(A) \cap \operatorname{Null}(A)$; by step 8, $v$ is orthogonal to itself, so $v_1^2 + \dots + v_n^2 = 0$, and a sum of real squares is $0$ only if each square is $0$, so $v = 0$.
11. By step 10, steps 2 and 3, and the [[dimension formula for a sum|06HTJNCMPA]], $\dim(\operatorname{Row}(A) + \operatorname{Null}(A)) = r + (n - r) - 0 = n$.
12. A subspace of $\mathbb{R}^n$ of dimension $n$ is $\mathbb{R}^n$ by the theorem on the [[dimension of a subspace|0QW084460E]], so with step 10, $\mathbb{R}^n = \operatorname{Row}(A) \oplus \operatorname{Null}(A)$.
13. Steps 10 to 12 for $A^{\mathsf{T}}$, with $\operatorname{Row}(A^{\mathsf{T}}) = \operatorname{Col}(A)$, give $\mathbb{R}^m = \operatorname{Col}(A) \oplus \operatorname{Null}(A^{\mathsf{T}})$, which proves part 3.
14. Let $L \colon \operatorname{Row}(A) \to \operatorname{Col}(A)$ be $L(u) = Au$, which lands in $\operatorname{Col}(A)$ by part 1 of the [[pivot basis theorem|11CSKXQNG3]] and is linear.
15. The kernel of $L$ is $\operatorname{Row}(A) \cap \operatorname{Null}(A)$, which is $\{0\}$ by step 10, so $L$ is injective.
16. Let $b \in \operatorname{Col}(A)$; by the same part 1, $b = Ax$ for some $x \in \mathbb{R}^n$.
17. By step 12, $x = u + w$ with $u \in \operatorname{Row}(A)$ and $w \in \operatorname{Null}(A)$, so $b = Au + Aw = Au = L(u)$, and $L$ is surjective.
18. By steps 15 and 17, $L$ is a linear isomorphism from $\operatorname{Row}(A)$ onto $\operatorname{Col}(A)$, which proves part 4.

## Idea

The dimensions come from three facts already proved: the rank, the count of free variables and row rank equals column rank.
Over $\mathbb{R}$, each equation of $Ax = 0$ says that $x$ is orthogonal to one row of $A$, so the null space is the orthogonal complement of the row space.
A nonzero real vector is never orthogonal to itself, so the row space and the null space meet only in $0$.
Their dimensions add up to $n$, so together they fill $\mathbb{R}^n$.
Then $A$ forgets the null space part of each input, and what is left is a one to one map from the row space onto the column space.

## Variants

Part 3 can also be read from the theorem on the [[dimension of the orthogonal complement|0E2NYPVSP9]], $\dim W + \dim W^\perp = n$, once part 2 is known.
Over a general field, the [[dual map|0AZ5ARP287]] replaces the dot product: the [[matrix of the dual map is the transpose|0ZPB3180AY]], and the kernel of the dual map is the annihilator of the image.
This proves part 1 and the annihilator form of part 2 without any inner product, but it gives no direct sums, as the example over $\mathbb{F}_2$ in the statement shows.
