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

We prove the [[Cauchy-Schwarz inequality|0RFWW56Y22]] in [[Euclidean space|0XPR1E85W0]] $\mathbb{R}^n$,
$$\lvert u \cdot v \rvert \le \lVert u \rVert \, \lVert v \rVert \quad \text{for all } u, v \in \mathbb{R}^n,$$
where $u \cdot v$ is the [[dot product|0S52TNNTH9]] and $\lVert u \rVert = \sqrt{u \cdot u}$.
The proof is a [[reduction to a special case|DX2H7AD66G]], the case of unit vectors.

1. If $u = 0$ or $v = 0$, both sides are $0$.
2. Otherwise let $\hat u = u / \lVert u \rVert$ and $\hat v = v / \lVert v \rVert$, the [[normalizations|M2FAMD9HZN]] of $u$ and $v$, which have length $1$.
3. By bilinearity, $\hat u \cdot \hat v = \frac{u \cdot v}{\lVert u \rVert \, \lVert v \rVert}$, so the claim is equivalent to $\lvert \hat u \cdot \hat v \rvert \le 1$.
4. For unit vectors $x$ and $y$, $\lVert x - y \rVert^2 = x \cdot x - 2\, x \cdot y + y \cdot y = 2 - 2\, x \cdot y \ge 0$, so $x \cdot y \le 1$.
5. In the same way, $\lVert x + y \rVert^2 = 2 + 2\, x \cdot y \ge 0$, so $x \cdot y \ge -1$.
6. With $x = \hat u$ and $y = \hat v$, steps 4 and 5 give $\lvert \hat u \cdot \hat v \rvert \le 1$, and step 3 gives the claim.

Check with $u = (3, 4)$ and $v = (1, 2)$: $u \cdot v = 11$, $\lVert u \rVert = 5$, $\lVert v \rVert = \sqrt 5$, and $11 \le 5 \sqrt 5 \approx 11.18$.

## Remarks

The reduction works because both sides are homogeneous of degree $1$ in $u$ and in $v$ separately: replacing $u$ by $su$ with $s > 0$ multiplies both sides by $s$.
Step 1 is necessary, because the zero vector has no normalization.

Steps 4 and 5 also give the case of equality.
For unit vectors, $\lvert x \cdot y \rvert = 1$ exactly when $x = y$ or $x = -y$, so in general equality holds exactly when $u$ and $v$ are linearly dependent.
The proof uses only bilinearity, symmetry and $\lVert w \rVert^2 \ge 0$, so it works in every real inner product space.
Other proofs, for example by a discriminant, appear in [[proofs of the Cauchy-Schwarz inequality|6NB1CYDTNK]].

## Explanations

### L1 human

The inequality compares the dot product of two arrows with the product of their lengths.
If you make one arrow twice as long, both sides double, so the comparison does not change.
So you may shrink or stretch both arrows to length $1$ first.
For two arrows of length $1$, the claim is that the dot product lies between $-1$ and $1$.
That holds because $x - y$ and $x + y$ have squared lengths $2 - 2\, x \cdot y$ and $2 + 2\, x \cdot y$, and squares are not negative.

### L2 human

We follow the steps for $u = (1, 1, 0)$ and $v = (2, 0, 2)$ in $\mathbb{R}^3$.

1. $u \cdot v = 2$, $\lVert u \rVert = \sqrt 2$ and $\lVert v \rVert = 2 \sqrt 2$.
2. $\hat u = \tfrac{1}{\sqrt 2} (1, 1, 0)$ and $\hat v = \tfrac{1}{\sqrt 2} (1, 0, 1)$, so $\hat u \cdot \hat v = \tfrac12$, which matches $\frac{2}{\sqrt 2 \cdot 2 \sqrt 2} = \tfrac12$.
3. $\lVert \hat u - \hat v \rVert^2 = 2 - 2 \cdot \tfrac12 = 1$, and directly $\hat u - \hat v = \tfrac{1}{\sqrt 2} (0, 1, -1)$ has squared length $1$.
4. So $\lvert u \cdot v \rvert = 2 \le 4 = \lVert u \rVert \, \lVert v \rVert$.

The method fits an inequality whose two sides scale in the same way, where unit vectors simplify the algebra.
Watch out: treat $u = 0$ before you divide by $\lVert u \rVert$.
