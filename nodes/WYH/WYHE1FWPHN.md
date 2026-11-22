---
tag: WYHE1FWPHN
kind: example
name: A linear map from R² to R³ has no determinant
msc: [15A04, 15A15]
topics: [DTBK11SR77]
audience: ug2
not_instance_of:
  - target: 0X0HQYSZ0K
    note: the map T(x, y) = (x, y, 0) from R^2 to R^3 is not an endomorphism, and its 3 × 2 matrices have no determinant
uses: [03F5KP94K0, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of an endomorphism
---

## Example

Let $T \colon \mathbb{R}^2 \to \mathbb{R}^3$ be the linear map $T(x, y) = (x, y, 0)$, which places the plane inside space.
This map has no determinant, and we check the condition that fails.

1. The [[definition|03F5KP94K0]] applies only to an endomorphism, a linear map from a space to the same space.
2. The domain of $T$ has dimension $2$ and the codomain has dimension $3$, so $T$ is not an endomorphism.
3. In the standard bases the columns of the [[matrix of $T$|0YYMY95FWS]] are $T(1, 0) = (1, 0, 0)$ and $T(0, 1) = (0, 1, 0)$:
$$\begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}.$$
4. Every matrix of $T$ has $3$ rows and $2$ columns, whatever bases we choose, and a $3 \times 2$ matrix has no determinant.

## Remarks

Could we still assign some number to $T$ in a useful way?
Let $\pi(x, y, z) = (x, y)$ be the projection from $\mathbb{R}^3$ to $\mathbb{R}^2$.
Then $\pi \circ T$ is the identity of $\mathbb{R}^2$, with determinant $1$.
In the other order, $T \circ \pi$ is the map $(x, y, z) \mapsto (x, y, 0)$ of $\mathbb{R}^3$, which kills $(0, 0, 1)$, so its determinant is $0$.
If $T$ and $\pi$ had numbers $d$ and $e$ that multiply under composition, we would need $ed = 1$ and $de = 0$ at once, which is impossible.

Equal dimensions are not enough either.
For the identity of $\mathbb{R}^2$, take the basis $e_1, e_2$ on the domain and $2e_1, e_2$ on the codomain.
Since $e_1 = \tfrac{1}{2}(2 e_1)$, the matrix is $\operatorname{diag}(\tfrac{1}{2}, 1)$, with determinant $\tfrac{1}{2}$, while the standard basis on both sides gives $1$.
So a map $V \to W$ between different spaces has no well-defined determinant unless extra structure is given, such as a chosen volume form on each space.

## Explanations

### L1 human

A determinant needs a square matrix.
A map from the plane into space has a matrix with $3$ rows and $2$ columns, which is not square.
So the question "what is its determinant?" has no answer.

### L2 human

The remark gives the deeper reason.
The two composites of $T$ with the projection have determinants $1$ and $0$, so no number for $T$ could make the product rule hold.
Watch out: for a map between two spaces of the same dimension we also need one basis that serves both sides, and that only makes sense when the two spaces are the same.
