---
tag: J4SZVFBHS5
kind: statement
role: proposition
name: Orthogonal complement of the column space is the null space of the transpose
msc: ["15A03", "15A18"]
topics: [S6559D61BP]
audience: ug1
about: [03AJKXH1AV, 0PQ2GGY1QV]
uses: [03AJKXH1AV, 0PQ2GGY1QV, 0W809K6AW0, 0XJXTBCB2T]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-2.xml#L878
    locator: src/section6-2.xml:878
---

## Statement

A vector is orthogonal to every output of a real matrix exactly when the transpose sends it to zero.
Let $A$ be an $m \times n$ real matrix with [[transpose|0W809K6AW0]] $A^{\mathsf{T}}$, and use the dot product on $\mathbb{R}^m$.
Then the [[orthogonal complement|0XJXTBCB2T]] of the [[column space|03AJKXH1AV]] of $A$ is the [[null space|0PQ2GGY1QV]] of $A^{\mathsf{T}}$:
$$\operatorname{Col}(A)^\perp = \operatorname{Null}(A^{\mathsf{T}}).$$

## Remarks

### Why each hypothesis is needed

The equality of sets holds over every field, if $\operatorname{Col}(A)^\perp$ is read as the set of $y$ with $y^{\mathsf{T}} b = 0$ for all $b \in \operatorname{Col}(A)$.
What needs the real numbers is the word complement, that is, $\operatorname{Col}(A) \cap \operatorname{Null}(A^{\mathsf{T}}) = \{0\}$.
Over $\mathbb{F}_2$, let $A$ be the column $(1, 1)$; then $A^{\mathsf{T}} y = y_1 + y_2$, so $\operatorname{Null}(A^{\mathsf{T}})$ is spanned by $(1, 1)$ and equals $\operatorname{Col}(A)$.

Over $\mathbb{C}$, the Hermitian product calls for the [[conjugate transpose|0DXKE10PHF]], and the statement becomes $\operatorname{Col}(A)^\perp = \operatorname{Null}(A^*)$.
With $A^{\mathsf{T}}$ it fails: for the column $(1, i)$, the vector $y = (1, i)$ satisfies $A^{\mathsf{T}} y = 1 + i^2 = 0$, but $y$ lies in $\operatorname{Col}(A)$ and its Hermitian product with itself is $2$.

### What it gives you

Applied to $A^{\mathsf{T}}$ in place of $A$, the statement gives $\operatorname{Row}(A)^\perp = \operatorname{Null}(A)$, since the column space of $A^{\mathsf{T}}$ is the [[row space|069MCGX635]] of $A$.
With the dimension of the complement it gives $\mathbb{R}^m = \operatorname{Col}(A) \oplus \operatorname{Null}(A^{\mathsf{T}})$, which is part 3 of the [[theorem on the four fundamental subspaces|73DVECPAT6]].
For a worked use, take $A$ with columns $(1, 0, 1)$ and $(0, 1, 1)$.
Then $A^{\mathsf{T}} y = (y_1 + y_3, y_2 + y_3)$, so $\operatorname{Null}(A^{\mathsf{T}})$ is the line through $(-1, -1, 1)$, which is the normal line of the plane $\operatorname{Col}(A)$, given by $b_3 = b_1 + b_2$.

### The converse

Taking complements once more gives $\operatorname{Col}(A) = \operatorname{Null}(A^{\mathsf{T}})^\perp$, because $W^{\perp\perp} = W$ for every subspace $W$ of $\mathbb{R}^m$ by the [[dimension of the orthogonal complement|0E2NYPVSP9]].
This direction is the [[Fredholm alternative|4HH8C9V8JQ]]: $Ax = b$ has a solution if and only if $b$ is orthogonal to every solution of $A^{\mathsf{T}} y = 0$.

### Generalizations

For a linear map $T \colon V \to W$ between finite-dimensional inner product spaces, $(\operatorname{im} T)^\perp = \ker T^*$, where $T^*$ is the [[adjoint|0R9NMSM1ZP]].
Over any field, the annihilator of $\operatorname{im} T$ in the dual space $W^*$ is the kernel of the [[dual map|0AZ5ARP287]].

## Explanations

### L1 human

A vector $y$ is orthogonal to the column space exactly when it is orthogonal to each column of $A$.
The dot product of $y$ with column $j$ of $A$ is entry $j$ of $A^{\mathsf{T}} y$.
So $y$ is orthogonal to all columns exactly when $A^{\mathsf{T}} y = 0$.

### L2 human

The left null space of $A$ is the set of normal vectors to the column space.
In the example with columns $(1, 0, 1)$ and $(0, 1, 1)$, the column space is a plane in $\mathbb{R}^3$, and $(-1, -1, 1)$ is orthogonal to both columns: $-1 + 0 + 1 = 0$ and $0 - 1 + 1 = 0$.
Its equation $-b_1 - b_2 + b_3 = 0$ is the test for $b$ to be in the column space.
Watch out: the left null space lives in $\mathbb{R}^m$, the space of outputs, while the null space of $A$ lives in $\mathbb{R}^n$.

### L3 human

Over any field, the left null space is the annihilator of the column space under the standard pairing $(y, b) \mapsto y^{\mathsf{T}} b$ of $F^m$ with itself.
This pairing is nondegenerate, so the annihilator has dimension $m - \operatorname{rank} A$, and taking the annihilator twice gives back the column space.
Over $\mathbb{R}$ the pairing is also positive definite, so the annihilator meets the column space only in $0$ and is a complement of it.
