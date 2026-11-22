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

We compute the [[orthogonal group|WWK2E8BRGF]] of degree $1$,
$$O(1) = \{ Q \in M_1(\R) : Q^{\mathsf{T}} Q = I_1 \}.$$

1. A real $1 \times 1$ matrix is $Q = (a)$ with $a \in \R$, and its transpose is $Q^{\mathsf{T}} = (a)$.
2. The condition $Q^{\mathsf{T}} Q = I_1$ reads $a^2 = 1$.
3. So $a = 1$ or $a = -1$, and $O(1) = \{ (1), (-1) \}$.
4. The group law is multiplication of numbers, and $(-1)(-1) = 1$, so $O(1)$ is a group of order $2$.
5. The determinant of $(a)$ is $a$, so $SO(1) = \{ (1) \}$ is the trivial group.

## Remarks

The element $(-1)$ is the map $x \mapsto -x$ of the line, and it is the [[reflection|06BRDF3F0E]] in the hyperplane $\{0\}$ of $\R$.
So $O(1)$ consists of the identity and one reflection, and it is isomorphic to $\Z/2\Z$.
Its two elements are its two connected components, the smallest case of the two components of $O(n)$.

The picture changes as soon as $n = 2$: the group $O(2)$ contains a rotation $R(\theta)$ for every angle $\theta$, so it is infinite.
It also changes over $\C$.
The complex $1 \times 1$ matrices $(z)$ with $\bar{z} z = 1$ form the whole unit circle, so [[the unitary group of degree one|1Y63SY7537]] is infinite as well.

## Explanations

### L1 human

On the number line, only two moves keep every distance and keep the point $0$ in place.
One move does nothing.
The other move sends each number to its negative, so $3$ goes to $-3$ and $-2$ goes to $2$.
So the orthogonal group of the line has exactly two elements.

### L2 human

The same method finds the rotations of the plane, and it shows why degree $1$ is so small.
For $Q = (a)$ there is one entry and one condition $a^2 = 1$, so only finitely many solutions exist.
For a $2 \times 2$ matrix there are four entries and three independent conditions, two lengths and one dot product, so one free parameter remains, the angle.
Watch out: $O(1)$ is not the circle group.
The real numbers of absolute value $1$ are only $1$ and $-1$, while the circle group needs complex numbers.
