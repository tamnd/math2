---
tag: RRWDAKDMJQ
kind: example
name: Distributivity fails in the subspace lattice of the plane
msc: ["81P10", "06C15"]
topics: [NJB94B39QK]
audience: research
instance_of: [2E9DMB7A6Q]
uses: [2E9DMB7A6Q, TWEYQ0XAY4, 0T36P6TXQ6, 0B8KZRT28M]
sources:
  - url: https://plato.stanford.edu/entries/qt-quantlog/
    locator: Quantum Logic and Probability Theory (SEP entry), section 1.2
  - url: https://en.wikipedia.org/wiki/Quantum_logic
    locator: Introduction
---

## Example

Let $H = \R^2$ with the standard inner product, and let $\mathcal{L}(\R^2)$ be its [[quantum logic|TWEYQ0XAY4]].
Every subspace of $\R^2$ is closed, so $\mathcal{L}(\R^2)$ consists of $0 = \set{0}$, the lines through the origin, and $1 = \R^2$.
Take three lines:
$$a = \set{(s, 0) : s \in \R}, \qquad b = \set{(0, t) : t \in \R}, \qquad c = \set{(t, t) : t \in \R}.$$

Claim: $a \wedge (b \vee c) = a$, but $(a \wedge b) \vee (a \wedge c) = 0$.
So the [[distributive law|0T36P6TXQ6]] $x \wedge (y \vee z) = (x \wedge y) \vee (x \wedge z)$ fails in $\mathcal{L}(\R^2)$.

1. The vectors $(0, 1) \in b$ and $(1, 1) \in c$ are linearly independent. So $b + c = \R^2$, and $b \vee c = \R^2$.
2. Hence $a \wedge (b \vee c) = a \cap \R^2 = a$.
3. Let $v \in a \cap b$. Then $v = (s, 0) = (0, t)$, so $s = t = 0$. So $a \wedge b = 0$.
4. Let $v \in a \cap c$. Then $v = (s, 0) = (t, t)$, so $t = 0$ and $s = 0$. So $a \wedge c = 0$.
5. Hence $(a \wedge b) \vee (a \wedge c) = 0 \vee 0 = 0$.
6. Since $(1, 0) \in a$, $a \neq 0$. By steps 2 and 5, the two sides differ.

The dual law fails as well.

7. As in steps 3 and 4, $b \wedge c = 0$, so $a \vee (b \wedge c) = a$.
8. As in step 1, $a \vee b = \R^2$ and $a \vee c = \R^2$, so $(a \vee b) \wedge (a \vee c) = \R^2 \neq a$.

## Remarks

The [[orthogonal projections|0B8KZRT28M]] onto $a$ and $c$ are
$$P_a = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad P_c = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \qquad P_a P_c = \frac{1}{2}\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} \neq \frac{1}{2}\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix} = P_c P_a.$$
So $a$ and $c$ do not commute, and the failure involves incompatible propositions.
By contrast, $P_a P_b = 0 = P_b P_a$, and $\set{0, a, b, 1}$ is a Boolean algebra with $a^\perp = b$.
The same lines work in any real or complex Hilbert space of dimension at least $2$: take two orthonormal vectors $e_1, e_2$ and the lines through $e_1$, $e_2$ and $e_1 + e_2$.
In [[quantum logic|2E9DMB7A6Q]] terms, "$a$ and ($b$ or $c$)" holds for the state $(1, 0)$, but neither "$a$ and $b$" nor "$a$ and $c$" holds for any state.

## Explanations

### L1 human

Take three different lines through the origin in the plane: the two axes and the diagonal.
"The $y$-axis or the diagonal" is the whole plane, because together they span it.
So "the $x$-axis and (the $y$-axis or the diagonal)" is the $x$-axis.
But the $x$-axis meets each of the other lines only in the origin, so the other side is just the origin.

### L2 human

The join of subspaces is a span, not a union.
A vector of $a$ lies in the span $b \vee c$, although it lies in neither $b$ nor $c$.
This is the step that breaks distributivity; with unions of sets, it cannot happen.
A trap is to check distributivity only on the axes, which commute and form a Boolean algebra.
