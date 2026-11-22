---
tag: ENNMQ30X9F
kind: example
name: The orthogonal complement is not the annihilator
msc: ["15A04", "15A63"]
topics: [9K7FFF26QR]
audience: ug2
not_instance_of:
  - target: 0ASHNYF7AG
    note: the orthogonal complement of a line in R^2 is a subspace of R^2 that depends on the inner product, while the annihilator is a subspace of the dual space that needs no inner product
uses: [0R6M158SQ9, 0XJXTBCB2T, 0NB0AWGJBW, 0S52TNNTH9, 04GYPXDXNH]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Inner product spaces
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Quotient spaces and annihilators
---

## Example

Let $V = \mathbb{R}^2$ and let $U$ be the line spanned by $u = (1, 1)$.
We compare the [[annihilator|0R6M158SQ9]] $U^0$ with the [[orthogonal complement|0XJXTBCB2T]] $U^\perp$ for two different [[inner products|0NB0AWGJBW]].

1. The annihilator. A form $ax + by$ vanishes on $U$ exactly when it vanishes at $u$, that is, when $a + b = 0$. So $U^0 = \mathbb{R} \cdot (x - y)$, a line in the dual space $(\mathbb{R}^2)^*$.
2. The complement for the [[dot product|0S52TNNTH9]]. A vector $v$ is perpendicular to $u$ when $v \cdot u = v_1 + v_2 = 0$. So $U^\perp = \mathbb{R} \cdot (1, -1)$, a line in $\mathbb{R}^2$.
3. A second inner product. Let $G = \operatorname{diag}(1, 2)$ and put
$$\langle v, w \rangle_G = v^{\mathsf{T}} G w = v_1 w_1 + 2 v_2 w_2.$$
This is symmetric and bilinear, and $\langle v, v \rangle_G = v_1^2 + 2 v_2^2 > 0$ for $v \ne 0$, so it is an inner product.
4. The complement for $G$. Now $\langle v, u \rangle_G = v_1 + 2 v_2$, so $U^{\perp_G} = \mathbb{R} \cdot (2, -1)$. Check: $2 + 2 \cdot (-1) = 0$. This is a different line in $\mathbb{R}^2$.
5. Step 1 used no inner product, so the annihilator is the same in both cases.

So the orthogonal complement is not the annihilator in two ways.
It lies in $V$ and not in $V^*$, and it changes when the inner product changes, while $U^0$ does not.

## Remarks

The two notions are linked by the [[Riesz map|04GYPXDXNH]] $v \mapsto \langle v, \cdot \rangle$ of the chosen inner product, which sends each vector to a form.
This map is an isomorphism $V \to V^*$ in finite dimension, and it sends $U^\perp$ onto $U^0$.

We can check this in both cases.
For the dot product, the vector $(1, -1)$ goes to the form $w \mapsto w_1 - w_2$, which is $x - y \in U^0$.
For $G$, the vector $(2, -1)$ goes to the form
$$w \mapsto 2 w_1 + 2 \cdot (-1) \cdot w_2 = 2(w_1 - w_2),$$
which is $2(x - y) \in U^0$.
So each inner product picks a different line of vectors, and its own Riesz map carries that line onto the same line of forms.

Since the Riesz map is an isomorphism, the two dimensions agree: $\dim U^\perp = \dim U^0 = \dim V - \dim U = 1$.
In an infinite-dimensional inner product space the Riesz map need not be onto $V^*$, and then the two notions can have different sizes.

## Explanations

### L1 human

The orthogonal complement of a line in the plane is the perpendicular line, and "perpendicular" depends on how you measure angles.
The annihilator of the line is the set of linear equations that hold on it, and equations need no angles.
With the usual angles the perpendicular line matches the equation $x - y = 0$ in a natural way.
With other angles the perpendicular line moves, but the equation stays the same.

### L2 human

To pass from the annihilator to an orthogonal complement, choose an inner product and invert its Riesz map.
Start from the form $x - y$, which spans $U^0$.
For the dot product, the vector $v$ with $v \cdot w = w_1 - w_2$ for all $w$ is $v = (1, -1)$.
For $G$, we need $v_1 w_1 + 2 v_2 w_2 = w_1 - w_2$ for all $w$, so $v_1 = 1$ and $v_2 = -\tfrac{1}{2}$.
The vector $(1, -\tfrac{1}{2})$ is half of $(2, -1)$, so it spans the same line $U^{\perp_G}$ as in step 4.
The typical use is to keep the two notions apart when a space has no preferred inner product.
Watch out: if you write $U^\perp$ for both, you may start to treat the annihilator as a subspace of $V$.
