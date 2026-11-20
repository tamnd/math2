---
tag: D9VHRJRMAS
kind: example
name: The orthogonal group of degree one
msc: ["15B10", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [WWK2E8BRGF]
uses: [0QRBVFJ50X, 0N0PXCTYA7]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_group
    locator: lead section
---

## Example

We compute $O(1) = \set{Q \in M_1(\R) : Q^TQ = I_1}$, the [[orthogonal group|WWK2E8BRGF]] of degree $1$.

1. A $1 \times 1$ real matrix is $Q = (a)$ with $a \in \R$, and $Q^T = (a)$.
2. The condition $Q^TQ = I_1$ says $a^2 = 1$.
3. So $a = 1$ or $a = -1$, and $O(1) = \set{(1), (-1)}$.
4. The group law is multiplication: $(-1)(-1) = 1$. So $O(1)$ is a group of order $2$.
5. The element $(1)$ has determinant $1$, and $(-1)$ has determinant $-1$. So $SO(1) = \set{(1)}$.

## Remarks

- The map $x \mapsto -x$ of $\R$ is the [[reflection|06BRDF3F0E]] in the hyperplane $\set{0}$. So $O(1)$ is the identity and one reflection.
- $O(1)$ is isomorphic to $\Z/2\Z$, and its two elements are the two connected components of $O(1)$.
- For $n = 2$, the group $O(2)$ is infinite: it contains every rotation $R(\theta)$.
- Over $\C$, the analogous group $U(1)$ is the whole unit circle $\set{z : \abs{z} = 1}$, see [[this example|1Y63SY7537]].

## Explanations

### L1 human

On the number line, only two moves keep all distances and the point $0$ fixed.
One move does nothing.
The other move sends each number to its negative, for example $3$ to $-3$.
So the orthogonal group of the line has two elements.

### L2 human

The worked computation is in the Example.
The same method finds $SO(2)$: the conditions $Q^TQ = I$ and $\det Q = 1$ give the rotation matrices.
A trap: $O(1)$ is not the circle group, because real $1 \times 1$ matrices of length $1$ are only $\pm 1$.
