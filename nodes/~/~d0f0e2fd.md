---
tag: ~d0f0e2fd
kind: statement
role: theorem
name: Equivalent conditions for a linear isometry
aliases: [characterizations-of-linear-isometries]
msc: ["15A04", "46C05"]
topics: [AZS5BPF5H3]
audience: ug1
about: [07SJXTWVQW, 0R9NMSM1ZP]
uses: [01EK923SKP, 0KG4D8AP6G, 0717XXPWM6, 09VYHEF2VT, 0FWJ0VW561, 0ST8QF9T3T]
sources:
  - url: https://en.wikipedia.org/wiki/Isometry
    locator: Linear isometry
  - url: https://en.wikipedia.org/wiki/Unitary_operator
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 7
---

## Statement

Let $V$ and $W$ be finite-dimensional [[inner product spaces|01EK923SKP]] over $\mathbb{K} = \R$ or $\C$, with the [[induced norms|0KG4D8AP6G]].
Let $T \colon V \to W$ be a linear map, and let $T^* \colon W \to V$ be its [[adjoint|0ST8QF9T3T]].
Then the following five conditions are equivalent.

1. $T$ is a [[linear isometry|0717XXPWM6]]: $\norm{Tv} = \norm{v}$ for all $v \in V$.
2. $T$ keeps inner products: $\ip{Tu}{Tv} = \ip{u}{v}$ for all $u, v \in V$.
3. $T$ sends every [[orthonormal family|09VYHEF2VT]] of $V$ to an orthonormal family of $W$.
4. There is an [[orthonormal basis|0FWJ0VW561]] $e_1, \dots, e_n$ of $V$ such that $Te_1, \dots, Te_n$ is an orthonormal family of $W$.
5. $T^*T = I_V$, where $I_V$ is the identity map of $V$.

If $\dim V = \dim W$, then the five conditions are also equivalent to each of the following two conditions.

6. $T$ is invertible and $T^{-1} = T^*$.
7. $TT^* = I_W$.

## Remarks

### Why each hypothesis is needed

- Equal dimensions are needed for conditions 6 and 7. [[The inclusion $\iota \colon \R^2 \to \R^3$|~ed15b8e6]] satisfies conditions 1 to 5, but $\iota\iota^* \neq I$.
- Condition 7 alone does not give condition 1 when the dimensions differ. The map $\iota^* \colon \R^3 \to \R^2$, $(x, y, z) \mapsto (x, y)$, satisfies $\iota^*(\iota^*)^* = \iota^*\iota = I$, but it sends $(0, 0, 1)$ to $0$.
- In condition 4, the basis must be orthonormal. The linear map $T$ of $\R^2$ with $T(1, 0) = (1, 0)$ and $T(1, 1) = (0, 1)$ sends a basis to an orthonormal basis, but $\norm{T(1, 1)} = 1 \neq \sqrt{2}$.
- In condition 4, the family must be a basis. The projection $(x, y) \mapsto (x, 0)$ sends the orthonormal family $(1, 0)$ to an orthonormal family, but it sends $(0, 1)$ to $0$.

### Consequences

- Let $A$ be the matrix of $T$ in orthonormal bases of $V$ and $W$. Then $T$ is a linear isometry exactly when $A^*A = I$, that is, when the columns of $A$ are orthonormal.
- For $V = W = \R^n$, this gives the [[conditions for an orthogonal matrix|F7M8ZXB4P7]]. For $V = W = \C^n$, it gives the [[conditions for a unitary matrix|~2220a569]].
- A linear isometry of a finite-dimensional inner product space onto itself has an inverse that is again a linear isometry.

### Converse

The statement is a list of equivalences, so each condition implies each other condition under the given hypotheses.

### Generalizations

- Conditions 1, 2 and 3 are equivalent for any inner product spaces, with the same proof.
- For a bounded operator $T$ between Hilbert spaces, condition 1 is equivalent to $T^*T = I$. In infinite dimensions, $T^*T = I$ does not give $TT^* = I$, even for $V = W$: the unilateral shift is an example, see [[unitary operators|DJHVKR63H5]].

## Explanations

### L1 human

A linear map keeps all lengths exactly when it keeps all angles and lengths together.
It is enough to check one set of perpendicular unit arrows.
If the map sends these arrows to perpendicular unit arrows, then it keeps every length.
For example, if a map of the plane sends $(1, 0)$ to $(0, 1)$ and $(0, 1)$ to $(-1, 0)$, then it is the quarter turn, and it keeps all lengths.

### L2 human

Worked example: we test $T(x, y) = \frac{1}{13}(5x - 12y, 12x + 5y)$ on $\R^2$ with condition 4.

1. Take the standard orthonormal basis $e_1 = (1, 0)$ and $e_2 = (0, 1)$.
2. $Te_1 = \frac{1}{13}(5, 12)$ has squared norm $\frac{25 + 144}{169} = 1$.
3. $Te_2 = \frac{1}{13}(-12, 5)$ has squared norm $\frac{144 + 25}{169} = 1$.
4. $\ip{Te_1}{Te_2} = \frac{1}{169}(-60 + 60) = 0$.
5. So $Te_1, Te_2$ is orthonormal, and $T$ is a linear isometry by the theorem.

The typical use: condition 4 needs only a finite check, while condition 1 is a statement about all vectors.
A trap: condition 4 needs an orthonormal basis at the start, not only orthonormal images.

### L3 human

Condition 5 says that $T$ has a left inverse, and that this left inverse is the adjoint.
In the language of matrices with orthonormal columns, the $m \times n$ matrices $A$ with $A^*A = I_n$ form the Stiefel manifold of orthonormal $n$-frames in $\mathbb{K}^m$.
For $m = n$ these are the [[orthogonal group|~dc22fe40]] and the [[unitary group|~4244c18b]].
The difference between conditions 5 and 7 is the difference between an isometry and a unitary operator, which matters for operators on Hilbert spaces.
