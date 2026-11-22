---
tag: H75GS7QVPB
kind: statement
role: lemma
name: Linear dependence lemma
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [0CRMGPAH83]
uses: [0EVHJFTG9Z, 0HR573CHNM]
proofs: [KGFAG81ZNC]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_independence
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 2A
---

## Statement

In a dependent list, some vector is built from the earlier ones, and you can remove it without losing anything.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $v_1, \dots, v_m \in V$ with $m \ge 1$.

1. If the family $(v_1, \dots, v_m)$ is [[linearly dependent|0EVHJFTG9Z]], then there is an index $k$ with $v_k \in \operatorname{span}(v_1, \dots, v_{k-1})$. For $k = 1$ this means $v_1 = 0$.
2. For every index $k$ as in part 1, removing $v_k$ does not change the [[span|0HR573CHNM]]:
$$\operatorname{span}(v_1, \dots, v_{k-1}, v_{k+1}, \dots, v_m) = \operatorname{span}(v_1, \dots, v_m).$$
3. The family is linearly dependent if and only if some $v_j$ lies in the span of the vectors $v_i$ with $i \ne j$.
4. If $(v_1, \dots, v_m)$ is linearly independent and $v \notin \operatorname{span}(v_1, \dots, v_m)$, then $(v_1, \dots, v_m, v)$ is linearly independent.

## Remarks

### A check with numbers

Take $v_1 = (1, 0)$, $v_2 = (0, 1)$ and $v_3 = (2, 3)$ in $\mathbb{R}^2$.
They satisfy the nontrivial relation $2 v_1 + 3 v_2 - v_3 = 0$, so they are dependent.
The last vector with a nonzero coefficient is $v_3$, and solving for it gives $v_3 = 2 v_1 + 3 v_2$, which is part 1 with $k = 3$.
Removing $v_3$ leaves $(1, 0)$ and $(0, 1)$, which still span $\mathbb{R}^2$, as part 2 says.
For part 4, start from the independent family $(v_1)$ and add $v_2$, which is not a multiple of $v_1$; the result is independent.

### Why each hypothesis is needed

The proof divides by a nonzero coefficient, so the scalars must form a field.
Over the ring $\mathbb{Z}$, the family $(2, 3)$ is dependent, since $3 \cdot 2 - 2 \cdot 3 = 0$, but $3$ is not an integer multiple of $2$ and $2$ is not an integer multiple of $3$.
So parts 1 and 3 fail for modules over $\mathbb{Z}$.

In part 4, the condition $v \notin \operatorname{span}(v_1, \dots, v_m)$ cannot be dropped.
The family $((1, 0))$ is independent, but adding $(2, 0)$, which lies in its span, gives the dependent family $((1, 0), (2, 0))$.

### What it gives you

Part 2 is the tool for shrinking a spanning list: as long as the list is dependent, remove a vector that lies in the span of the earlier ones, and the span stays the same.
A finite spanning list therefore shrinks to a basis, which is [[every spanning set contains a basis|06MRNP4BNT]].
Part 4 is the tool for growing an independent list: add a vector outside the span, and independence is kept.
In a finite-dimensional space this gives the [[extension to a basis|0M4SXE5WW3]].
The [[Steinitz exchange lemma|08ZDRN6H41]] uses parts 1 and 2 at each step of its exchange.

### The converse

Part 3 is already an equivalence.
Part 4 also has a converse: if $(v_1, \dots, v_m, v)$ is independent, then $v \notin \operatorname{span}(v_1, \dots, v_m)$, because otherwise part 3 would make the longer family dependent.

### Generalizations

The lemma holds for infinite families, with finite combinations, because each argument uses only one finite relation at a time.
In the language of [[matroids|PX31ZNYS3Z]], part 4 is the augmentation step that lets an independent set grow toward a basis.

## Explanations

### L1 human

If some vectors are dependent, then one of them can be built from the ones before it.
That vector is redundant: throw it away, and you can still build everything you could build before.
In the other direction, if a new vector cannot be built from an independent list, then adding it keeps the list independent.

### L2 human

Here is a typical use: find a smaller spanning list for $\operatorname{span}((1, 1, 0), (0, 1, 1), (1, 2, 1), (1, 0, 0))$ in $\mathbb{R}^3$.
Go through the list from left to right.
The vector $(0, 1, 1)$ is not a multiple of $(1, 1, 0)$, so keep it.
The vector $(1, 2, 1)$ equals $(1, 1, 0) + (0, 1, 1)$, so it lies in the span of the earlier vectors, and part 2 lets us remove it.
The vector $(1, 0, 0)$ is not in the span of the first two, because every $a(1, 1, 0) + b(0, 1, 1) = (a, a + b, b)$ with first entry $1$ and third entry $0$ has $a = 1$, $b = 0$ and second entry $1$, not $0$.
So by part 4 the list $(1, 1, 0)$, $(0, 1, 1)$, $(1, 0, 0)$ is independent, and it spans the same space as the original four vectors.
Watch out: which vector you remove depends on the order of the list, but the span left over does not.

### L3 human

The lemma is the linear algebra form of the exchange property of the span: if $w$ is in the span of $S \cup \{v\}$ but not of $S$, then $v$ is in the span of $S \cup \{w\}$.
This property, together with the fact that span is a closure operator, is all that the theory of bases and dimension needs.
For modules over rings it fails, which is why modules can have minimal generating sets of different sizes and no basis at all.
