---
tag: 0DKMBWTD7P
kind: statement
role: lemma
name: All cosets have the same size
aliases: [cosets-have-the-same-cardinality-as-the-subgroup]
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: ug1
about: [564VVAQTNR, 03DEH43F4H, 0NE1DK7H4T]
uses: [G5S1M9, 0X1JXT47GA, 03DEH43F4H, 0NE1DK7H4T, 0GG9TVW90M, 0G0ASKNA6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Coset
    locator: Properties
  - book: isbn:9780471433347
    locator: Section 3.2
---

## Statement

Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|0X1JXT47GA]] of $G$, and let $g \in G$.
Then the map $\lambda_g \colon H \to gH$, $\lambda_g(h) = gh$, is a [[bijection|0GG9TVW90M]] onto the [[left coset|03DEH43F4H]] $gH$.
The map $\rho_g \colon H \to Hg$, $\rho_g(h) = hg$, is a bijection onto the [[right coset|0NE1DK7H4T]] $Hg$.
Thus $|gH| = |H| = |Hg|$ as [[cardinalities|0G0ASKNA6Z]], and any two cosets of $H$, left or right, have the same size.
The group $G$ and the subgroup $H$ can be infinite.

## Remarks

### Why each hypothesis is needed

- The structure $G$ must be a group, or at least have cancellation. In the monoid $(\mathbb{Z}, \cdot)$, the submonoid $H = \{1, -1\}$ has $0 \cdot H = \{0\}$, a set with one element. The map $h \mapsto 0h$ is not injective, because $0$ has no inverse.
- The bijection $s \mapsto gs$ from $S$ to $gS$ exists for each subset $S$ of a group. The hypothesis that $H$ is a subgroup is not needed for the sizes. It is needed for the cosets to form a partition of $G$.
- No finiteness is needed. In $(\mathbb{Z}, +)$, the map $h \mapsto h + 1$ is a bijection from $2\mathbb{Z}$ onto the odd integers $1 + 2\mathbb{Z}$.

### Consequences

- With the partition of $G$ into left cosets, the lemma gives [[Lagrange's theorem|3C53TD]] and the [[counting formula|04DC0SRN2K]] $|G| = [G : H] \cdot |H|$.
- The left cosets and the right cosets of $H$ all have the same size, even when the two partitions differ.
- Each coset of the trivial subgroup $\{e\}$ is a single element.

### Converse

The converse question is whether a partition of $G$ into blocks of equal size comes from a subgroup.
The answer is no.
In $\mathbb{Z}/4\mathbb{Z}$, the blocks $\{0, 1\}$ and $\{2, 3\}$ have equal size, but $\{0, 1\}$ is not a subgroup, and $\{2, 3\}$ is not a coset of a subgroup.

### Generalizations

- For a [[group action|0WCY42EV9V]], each element $g$ acts as a bijection of the set. Thus $g$ maps each subset onto a subset of the same size.
- For [[double cosets|DSBE321XMS]] $HgK$ the sizes can differ, so the lemma does not extend to them.

## Explanations

### L1 human

Multiplying by a fixed element of a group never makes two different elements equal.
The reason is that you can undo the multiplication with the inverse element.
So when you move a subgroup to a coset, no element is lost and no two elements merge.
For example, adding $1$ to each even number gives each odd number exactly once.
Thus each coset has exactly as many elements as the subgroup.

### L2 human

We check the lemma for $G = S_3$, $H = \{e, (1\,2)\}$ and $g = (1\,3)$, with permutations composed from right to left.

1. The map $\lambda_g$ sends $e$ to $(1\,3)$.
2. It sends $(1\,2)$ to $(1\,3)(1\,2) = (1\,2\,3)$.
3. The two images are different, so $\lambda_g$ is injective.
4. The image is $\{(1\,3), (1\,2\,3)\} = gH$, so $\lambda_g$ is onto $gH$.
5. Thus $|gH| = 2 = |H|$.

The typical use of the lemma is in counting arguments, together with the fact that the cosets are disjoint.

A trap is to use the lemma for structures without inverses.
In $(\mathbb{Z}, \cdot)$, multiplication by $0$ sends each set of integers to $\{0\}$.

### L3 human

The lemma says that left multiplication $\lambda_g$ is a bijection of $G$, with inverse $\lambda_{g^{-1}}$.
Thus $g \mapsto \lambda_g$ is an action of $G$ on itself, the left regular action, and [[Cayley's theorem|0151VYVX27]] comes from it.
Each bijection of a set preserves the cardinality of subsets, so the lemma is a statement about the action and not about $H$.
For topological groups, $\lambda_g$ is a homeomorphism.
A left Haar measure $\mu$ on a locally compact group satisfies $\mu(gA) = \mu(A)$, and this is the measure version of the lemma.
