---
tag: M2JH84VEY9
kind: statement
role: proposition
name: Dimension of the orthogonal complement for a bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
about: [01TXN7ETH2]
uses: [05Q4JD6XEH, 0KAN330PAH, 3ND2FNJ38Y, 00889YD15K, 0W4FSW1TVB, 06HTJNCMPA]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: General bilinear forms
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Reflexive bilinear forms and orthogonal vectors
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Statement

Let $V$ be a vector space of finite dimension $n$ over a field $F$, let $B$ be a [[bilinear form|0P799D6AMN]] on $V$, and let $W$ be a subspace of $V$.
Let $W^\perp = \{v \in V : B(w, v) = 0 \text{ for all } w \in W\}$ be its [[orthogonal complement|05Q4JD6XEH]].

1. $\dim W + \dim W^\perp \geq n$.
2. If $B$ is [[nondegenerate|0KAN330PAH]], then $\dim W + \dim W^\perp = n$.
3. $V = W \oplus W^\perp$ if and only if the restriction of $B$ to $W \times W$ is nondegenerate.
4. If $B$ is nondegenerate and [[reflexive|M0G958M917]], then $(W^\perp)^\perp = W$.

The [[proof|3DT0AG8DFS]] applies rank-nullity to the map $V \to W^*$, $v \mapsto B(\cdot, v)|_W$.

## Remarks

### Why each hypothesis is needed

- Part 2 needs nondegeneracy. For the zero form, $W^\perp = V$ for every $W$, and $\dim W + \dim V > n$ when $W \neq \{0\}$.
- Part 3 does not follow from nondegeneracy of $B$ on $V$. For $B(x, y) = x_1 y_1 - x_2 y_2$ on $\R^2$ and $W = \operatorname{span}(1, 1)$, $B$ is nondegenerate, but $W^\perp = W$.
- Part 4 needs reflexivity. Let $B(x, y) = x_1 y_1 + x_1 y_2 + x_2 y_2$ on $\Q^2$, which is nondegenerate but not reflexive, and let $W = \operatorname{span}(e_1)$. Then $W^\perp$ is the line through $(1, -1)$, and the right complement of this line is $\operatorname{span}(e_2) \neq W$.
- Finite dimension is needed. In an infinite-dimensional inner product space, a dense proper subspace $W$ has $W^\perp = \{0\}$, so $(W^\perp)^\perp \neq W$.

### Consequences

- Each subspace $W$ on which $B$ is nondegenerate splits off: $V = W \oplus W^\perp$. This is the main step in the [[classification of alternating forms|V8KKHKXXB3]] and in the [[Witt decomposition|BPMRSPB6GD]].
- For a nondegenerate form, a totally isotropic subspace $W$, with $W \subseteq W^\perp$, has $\dim W \leq n / 2$.
- If $B$ is symmetric with $\operatorname{char} F \neq 2$, induction with part 3 gives an orthogonal basis. This is the diagonalization theorem for quadratic forms.

### Converse

If $\dim W + \dim W^\perp = n$ for every subspace $W$, then $B$ is nondegenerate.
Take $W = V$: then $V^\perp$, the right radical, has dimension $0$.
Equality for a single $W$ does not suffice.
For $B(x, y) = x_1 y_1$ on $F^2$ and $W = \operatorname{span}(e_1)$, we get $W^\perp = \operatorname{span}(e_2)$ and $1 + 1 = 2$, but $B$ is degenerate.

### Generalizations

For a nondegenerate pairing $V \times U \to F$ with $\dim V = \dim U$, the orthogonal of a subspace of $V$ in $U$ has the complementary dimension.
For a nondegenerate sesquilinear form the same statements hold, with the same proof.
For a nondegenerate form that is not reflexive, part 4 holds with mixed complements: the left complement of $W^\perp$ is $W$.
Without nondegeneracy, $\dim W^\perp = n - \dim W + \dim(W \cap {}^\perp V)$, where ${}^\perp V$ is the left radical.

## Explanations

### L1 human

The orthogonal complement of a subspace is large: its dimension is at least the dimension of the space minus the dimension of the subspace.
For a nondegenerate form it has exactly that dimension.
But it need not be a complement in the usual sense, because it can meet the subspace.
It is a true complement exactly when the form is nondegenerate on the subspace.

### L2 human

We test the statement for $B(x, y) = x_1 y_1 + x_2 y_2 - x_3 y_3$ on $\Q^3$.

1. Let $W = \operatorname{span}(e_1)$. Then $W^\perp$ is the plane $v_1 = 0$, and $1 + 2 = 3$.
2. $B(e_1, e_1) = 1 \neq 0$, so $B$ is nondegenerate on $W$, and indeed $\Q^3 = W \oplus W^\perp$.
3. Let $W' = \operatorname{span}(e_1 + e_3)$. Then $W'^\perp$ is the plane $v_1 - v_3 = 0$, and $1 + 2 = 3$ again.
4. $B(e_1 + e_3, e_1 + e_3) = 1 - 1 = 0$, so $B$ is zero on $W'$, and $W' \subseteq W'^\perp$. The sum is not direct.

The typical use is part 3: find a vector $v$ with $B(v, v) \neq 0$ or a plane on which $B$ is nondegenerate, split it off, and continue on the complement.
A trap: the dimension formula of part 2 holds for every subspace, even when $W \cap W^\perp \neq \{0\}$.

### L3 human

The map $v \mapsto B(\cdot, v)|_W$ is the composite of the isomorphism $V \to V^*$ with the restriction $V^* \to W^*$, and the kernel of the restriction is the annihilator of $W$.
So, for a nondegenerate form, $W^\perp$ is the image of the annihilator of $W$, and part 2 is the dimension formula for annihilators.
Part 4 says that $W \mapsto W^\perp$ is an involution that reverses inclusions, which gives a polarity of the projective space $\mathbb{P}(V)$.
