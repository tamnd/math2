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

The orthogonal complement of a subspace is always at least as large as the codimension of the subspace, exactly that large for a nondegenerate form, and a true direct complement exactly when the form is nondegenerate on the subspace.

Let $V$ be a vector space of finite dimension $n$ over a field $F$, let $B$ be a [[bilinear form|0P799D6AMN]] on $V$, and let $W$ be a subspace of $V$.
Let $W^\perp = \{v \in V : B(w, v) = 0 \text{ for all } w \in W\}$ be its [[orthogonal complement|05Q4JD6XEH]].

1. $\dim W + \dim W^\perp \ge n$.
2. If $B$ is [[nondegenerate|0KAN330PAH]], then $\dim W + \dim W^\perp = n$.
3. $V = W \oplus W^\perp$ if and only if the restriction of $B$ to $W \times W$ is nondegenerate.
4. If $B$ is nondegenerate and [[reflexive|M0G958M917]], then $(W^\perp)^\perp = W$.

The [[proof|3DT0AG8DFS]] applies rank-nullity to the map $V \to W^*$, $v \mapsto B(\cdot, v)|_W$.

## Remarks

### Why each hypothesis is needed

Part 2 needs nondegeneracy.
For the zero form, $W^\perp = V$ for every $W$, so $\dim W + \dim W^\perp = \dim W + n$, which exceeds $n$ when $W \ne \{0\}$.

Part 3 needs nondegeneracy on $W$ itself, and nondegeneracy on $V$ is not enough.
For $B(x, y) = x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$, which is nondegenerate, the line $W$ spanned by $(1, 1)$ has $W^\perp = W$, so $W + W^\perp$ is only a line.

Part 4 needs reflexivity.
Let $B(x, y) = x_1 y_1 + x_1 y_2 + x_2 y_2$ on $\mathbb{Q}^2$, with matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ of determinant $1$, and let $W = \operatorname{span}(e_1)$.
Then $W^\perp$ is cut out by $B(e_1, v) = v_1 + v_2 = 0$, so it is the line through $(1, -1)$.
Next, $B((1, -1), v) = v_1 + v_2 - v_2 = v_1$, so $(W^\perp)^\perp = \operatorname{span}(e_2) \ne W$.

Finite dimension is needed.
Let $V$ be the space of finite sequences with the dot product $\sum_i x_i y_i$, and let $W$ be the subspace of sequences with entry sum $0$.
A vector $v \in W^\perp$ is orthogonal to each $e_i - e_j \in W$, so $v_i = v_j$ for all $i, j$, and a finite sequence with all entries equal is $0$.
So $W^\perp = \{0\}$ and $(W^\perp)^\perp = V \ne W$, although the dot product is nondegenerate and symmetric.

### What it gives you

Part 3 is the splitting tool of the sub-area.
Each subspace on which $B$ is nondegenerate splits off as $V = W \oplus W^\perp$, and this is the main step of the [[classification of alternating forms|V8KKHKXXB3]] and of the [[Witt decomposition|BPMRSPB6GD]].
If $B$ is symmetric and $1 + 1 \ne 0$ in $F$, a nonzero $B$ has a vector $v$ with $B(v, v) \ne 0$, and induction with part 3 gives an orthogonal basis, as in the [[diagonalization of a quadratic form|0Z3FEWZ8HA]].
Part 2 bounds the totally isotropic subspaces: if $B$ is nondegenerate and $W \subseteq W^\perp$, then $\dim W \le \dim W^\perp = n - \dim W$, so $\dim W \le n / 2$.

### The converse

If $\dim W + \dim W^\perp = n$ for every subspace $W$, then $B$ is nondegenerate.
Take $W = V$: then $V^\perp$, which is the right radical, has dimension $0$, and the [[criteria for nondegeneracy|3ND2FNJ38Y]] give the claim.
Equality for a single $W$ is not enough.
For $B(x, y) = x_1 y_1$ on $F^2$ and $W = \operatorname{span}(e_1)$, we get $W^\perp = \operatorname{span}(e_2)$ and $1 + 1 = 2$, but $B$ is degenerate.

### Generalizations

For a nondegenerate pairing $V \times U \to F$ of finite-dimensional spaces, the orthogonal in $U$ of a subspace of $V$ has the complementary dimension, with the same proof.
For a nondegenerate [[sesquilinear form|054YEQ0Y8M]] the same four statements hold.
For a nondegenerate form that is not reflexive, part 4 holds with mixed complements: the left complement of $W^\perp$ is $W$.
In the example above, $B(u, (1, -1)) = u_1 + u_1 \cdot (-1) + u_2 \cdot (-1) = -u_2$, so the left complement of $W^\perp$ is $\operatorname{span}(e_1) = W$.
Without nondegeneracy, $\dim W^\perp = n - \dim W + \dim(W \cap R)$, where $R$ is the left radical $\{u : B(u, v) = 0 \text{ for all } v\}$.

## Explanations

### L1 human

The orthogonal complement of a subspace is large.
In a space of dimension $3$, the complement of a line has dimension at least $2$, because one vector gives only one condition.
For a nondegenerate form it has exactly dimension $2$.
But it may contain the line itself, and then the line and its complement do not fill the space.
They fill it exactly when the form is nondegenerate on the line.

### L2 human

We test the statement for $B(x, y) = x_1 y_1 + x_2 y_2 - x_3 y_3$ on $\mathbb{Q}^3$.
First let $W = \operatorname{span}(e_1)$, so $W^\perp$ is the plane $v_1 = 0$, and $1 + 2 = 3$.
Since $B(e_1, e_1) = 1 \ne 0$, the form is nondegenerate on $W$, and indeed $\mathbb{Q}^3 = W \oplus W^\perp$.
Next let $W' = \operatorname{span}(e_1 + e_3)$.
Then $B(e_1 + e_3, v) = v_1 - v_3$, so $W'^\perp$ is the plane $v_1 = v_3$, and again $1 + 2 = 3$.
But $B(e_1 + e_3, e_1 + e_3) = 1 - 1 = 0$, so $W' \subseteq W'^\perp$, and the sum is not direct.
This is the typical use of part 3: look for a vector $v$ with $B(v, v) \ne 0$, split off its line, and continue in the complement.
Watch out: the dimension count of part 2 holds for both lines, so it cannot tell you whether the sum is direct.

### L3 human

The map $v \mapsto B(\cdot, v)|_W$ is the isomorphism $R_B \colon V \to V^*$ followed by restriction $V^* \to W^*$, and the kernel of the restriction is the annihilator of $W$.
So for a nondegenerate form, $W^\perp$ is the preimage of the annihilator, and part 2 is the dimension formula for annihilators.
Part 4 says that $W \mapsto W^\perp$ is an involution that reverses inclusions, a polarity of the projective space $\mathbb{P}(V)$.
In Hilbert spaces the analogue of part 4 is $(W^\perp)^\perp = \overline{W}$, the closure of $W$, and the subspace $W$ of the infinite-dimensional example is dense for the length $\sqrt{\sum_i x_i^2}$.
