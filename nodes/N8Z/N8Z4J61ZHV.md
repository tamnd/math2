---
tag: N8Z4J61ZHV
kind: example
name: Cauchy-Schwarz by reduction to unit vectors
msc: ["00A35", "15A63"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [DX2H7AD66G]
uses: [DX2H7AD66G, 0RFWW56Y22, 0S52TNNTH9, 0XPR1E85W0, M2FAMD9HZN]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy–Schwarz_inequality
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Homogeneous_function
    locator: lead section
---

## Example

We prove the [[Cauchy-Schwarz inequality|0RFWW56Y22]] in [[Euclidean space|0XPR1E85W0]] $\mathbb{R}^n$:
$$\lvert u \cdot v \rvert \le \lVert u \rVert \, \lVert v \rVert \quad \text{for all } u, v \in \mathbb{R}^n,$$
where $u \cdot v$ is the [[dot product|0S52TNNTH9]] and $\lVert u \rVert = \sqrt{u \cdot u}$.
The proof is a [[reduction to a special case|DX2H7AD66G]]: the case of unit vectors.

1. Case $u = 0$ or $v = 0$: then $u \cdot v = 0$ and the right side is $0$, so the inequality reads $0 \le 0$.
2. Now let $u \neq 0$ and $v \neq 0$, so $\lVert u \rVert > 0$ and $\lVert v \rVert > 0$. Let $\hat u = u / \lVert u \rVert$ and $\hat v = v / \lVert v \rVert$, the [[normalizations|M2FAMD9HZN]] of $u$ and $v$. Then $\lVert \hat u \rVert = \lVert \hat v \rVert = 1$.
3. By bilinearity of the dot product, $\hat u \cdot \hat v = \frac{u \cdot v}{\lVert u \rVert \, \lVert v \rVert}$. So the claim for $u$ and $v$ is equivalent to $\lvert \hat u \cdot \hat v \rvert \le 1$.
4. It remains to prove the special case: $\lvert x \cdot y \rvert \le 1$ for unit vectors $x$ and $y$.
5. Expand: $\lVert x - y \rVert^2 = x \cdot x - 2\, x \cdot y + y \cdot y = 2 - 2\, x \cdot y$. Since a squared length is not negative, $x \cdot y \le 1$.
6. In the same way, $\lVert x + y \rVert^2 = 2 + 2\, x \cdot y \ge 0$, so $x \cdot y \ge -1$.
7. Steps 5 and 6 give $\lvert x \cdot y \rvert \le 1$. With $x = \hat u$ and $y = \hat v$, step 3 gives the claim for $u$ and $v$.

A numerical check with $u = (3, 4)$ and $v = (1, 2)$: $u \cdot v = 3 + 8 = 11$, $\lVert u \rVert = 5$ and $\lVert v \rVert = \sqrt 5$.
So $\lvert u \cdot v \rvert = 11 \le 5 \sqrt 5 \approx 11.18$, and $\hat u \cdot \hat v = \tfrac{11}{5 \sqrt 5} \approx 0.984 \le 1$.

## Remarks

1. The reduction works because both sides are homogeneous of degree $1$ in $u$ and in $v$ separately. Replacing $u$ by $su$ with $s > 0$ multiplies both sides by $s$.
2. The excluded case of step 1 is necessary: the zero vector has no normalization.
3. Equality holds in the special case exactly when $x = y$ or $x = -y$, by steps 5 and 6. So equality holds in general exactly when $u$ and $v$ are linearly dependent.
4. The same proof works in each real inner product space, since it uses only bilinearity, symmetry and $\lVert w \rVert^2 \ge 0$.
5. Other proofs of the inequality, for example with a discriminant, are collected in [[this node|6NB1CYDTNK]].

## Explanations

### L1 human

The inequality compares the dot product of two arrows with the product of their lengths.
If we make one arrow twice as long, both sides double, so the comparison does not change.
So we may shrink or stretch both arrows to length $1$ before we compare.
For two arrows of length $1$, the claim is that the dot product lies between $-1$ and $1$.
This follows because the arrows $x - y$ and $x + y$ have lengths whose squares are $2 - 2\, x \cdot y$ and $2 + 2\, x \cdot y$, and squares are not negative.

### L2 human

We follow the steps for $u = (1, 1, 0)$ and $v = (2, 0, 2)$ in $\mathbb{R}^3$.

1. $u \cdot v = 2$, $\lVert u \rVert = \sqrt 2$ and $\lVert v \rVert = \sqrt 8 = 2 \sqrt 2$.
2. $\hat u = \tfrac{1}{\sqrt 2} (1, 1, 0)$ and $\hat v = \tfrac{1}{\sqrt 2} (1, 0, 1)$, so $\hat u \cdot \hat v = \tfrac12$.
3. Step 3 of the example predicts $\hat u \cdot \hat v = \frac{2}{\sqrt 2 \cdot 2 \sqrt 2} = \tfrac12$, which agrees.
4. $\lVert \hat u - \hat v \rVert^2 = 2 - 2 \cdot \tfrac12 = 1$. Directly, $\hat u - \hat v = \tfrac{1}{\sqrt 2} (0, 1, -1)$, whose squared length is $\tfrac12 \cdot 2 = 1$.
5. So $\lvert u \cdot v \rvert = 2 \le \sqrt 2 \cdot 2 \sqrt 2 = 4$.

The typical use is an inequality whose two sides scale in the same way, where unit vectors simplify the algebra.
A trap is to divide by $\lVert u \rVert$ without first treating $u = 0$.
