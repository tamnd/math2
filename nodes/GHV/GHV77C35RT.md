---
tag: GHV77C35RT
kind: example
name: The matrix ring of real 2 × 2 matrices contains a copy of the complex numbers
msc: ["16S50", "15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [AB2MD5CD13]
uses: [0FHVPRAE60, 076JGP6R3T, 0BVXADM10P]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_number
    locator: Matrix representation of complex numbers
---

## Example

Multiplying a complex number by $i$ turns the plane by a quarter turn, and a quarter turn is a $2 \times 2$ matrix.
This suggests that the complex numbers sit inside the [[matrix ring|0FHVPRAE60]] $M_2(\mathbb{R})$.
Define
$$\phi(a + bi) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}, \qquad C = \{ \phi(z) : z \in \mathbb{C} \}.$$
We check that $\phi$ is an injective ring homomorphism, so $C$ is a subring of $M_2(\mathbb{R})$ that is a copy of $\mathbb{C}$.

1. Let $z = a + bi$ and $w = c + di$. The [[sum|0BVXADM10P]] is entrywise, so
$$\phi(z) + \phi(w) = \begin{pmatrix} a + c & -(b + d) \\ b + d & a + c \end{pmatrix} = \phi(z + w).$$
2. The [[product|076JGP6R3T]], row times column, is
$$\phi(z)\phi(w) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}\begin{pmatrix} c & -d \\ d & c \end{pmatrix} = \begin{pmatrix} ac - bd & -(ad + bc) \\ ad + bc & ac - bd \end{pmatrix}.$$
3. In $\mathbb{C}$, $zw = (ac - bd) + (ad + bc)i$. So the matrix of step 2 is $\phi(zw)$, and $\phi(z)\phi(w) = \phi(zw)$.
4. $\phi(1) = I$, since $a = 1$ and $b = 0$.
5. $\phi$ is injective, because $a$ and $b$ can be read off the first column of $\phi(a + bi)$.
6. By steps 1 to 5, $C$ is closed under sums and products, contains $I$, and $\phi$ is a ring isomorphism from $\mathbb{C}$ onto $C$.
7. The image of $i$ is the quarter turn $\phi(i) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, and $\phi(i)^2 = -I = \phi(-1)$, as $i^2 = -1$ demands.

## Remarks

### A check with numbers

Take $z = 1 + 2i$ and $w = 3 - i$.
Then
$$\phi(z)\phi(w) = \begin{pmatrix} 1 & -2 \\ 2 & 1 \end{pmatrix}\begin{pmatrix} 3 & 1 \\ -1 & 3 \end{pmatrix} = \begin{pmatrix} 3 + 2 & 1 - 6 \\ 6 - 1 & 2 + 3 \end{pmatrix} = \begin{pmatrix} 5 & -5 \\ 5 & 5 \end{pmatrix}.$$
In $\mathbb{C}$, $(1 + 2i)(3 - i) = 3 - i + 6i - 2i^2 = 5 + 5i$, and $\phi(5 + 5i)$ is the same matrix.

### A field inside a ring with zero divisors

The ring $M_2(\mathbb{R})$ has zero divisors, but $C$ has none.
The determinant of $\phi(a + bi)$ is $a^2 + b^2 = |z|^2$, which is positive for $z \ne 0$.
So every nonzero element of $C$ is invertible, with
$$\phi(z)^{-1} = \frac{1}{a^2 + b^2}\begin{pmatrix} a & b \\ -b & a \end{pmatrix} = \phi\Bigl(\frac{1}{z}\Bigr).$$
Hence $C$ is a field, and in particular it is commutative, although $M_2(\mathbb{R})$ is not.
Complex conjugation also has a matrix meaning: $\phi(\bar z)$ is the transpose of $\phi(z)$.

### The geometric picture

Multiplication by $z$ is a linear map of $\mathbb{C} = \mathbb{R}^2$, and its matrix in the basis $1, i$ is $\phi(z)$.
Write $z = r(\cos\theta + i \sin\theta)$ in polar form.
Then
$$\phi(z) = r \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix},$$
which is a [[rotation|HNY4CPEEJA]] by $\theta$ followed by scaling by $r$.
So multiplying complex numbers is composing rotations and scalings, which explains why the product adds the angles.

### Try it

Compute $\phi(i)\phi(1 + i)$ and compare it with $\phi(i(1 + i))$.
Answer: the product is $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} -1 & -1 \\ 1 & -1 \end{pmatrix}$, and $i(1 + i) = -1 + i$ has the same image.

## Explanations

### L1 human

Complex numbers can be written as special $2 \times 2$ real matrices: $a + bi$ becomes the matrix with rows $(a, -b)$ and $(b, a)$.
Adding and multiplying these matrices gives the same answers as adding and multiplying the complex numbers.
The number $i$ becomes the matrix of a quarter turn, and two quarter turns make a half turn, which is $-1$.

### L2 human

This is a first example of a representation: an abstract ring is sent into a matrix ring by an injective ring homomorphism, so that its elements become matrices.
The typical use is to turn a calculation in a new ring into a matrix calculation, or to see that a ring is associative because the matrix product is.
The [[quaternions|0GE4DVQKR8]] have a similar representation by $2 \times 2$ complex matrices, with $z + wj$ sent to $\begin{pmatrix} z & w \\ -\bar w & \bar z \end{pmatrix}$.
Watch out: only matrices of the special form $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ belong to $C$, and two general real matrices still need not commute.
