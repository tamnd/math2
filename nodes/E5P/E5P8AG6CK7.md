---
tag: E5P8AG6CK7
kind: example
name: SU(2)
msc: ["22E15", "22C05", "20G20"]
instance_of: [9TFC6ADC1C]
uses: [CZCWFPNS4N, 263GGJFA21, 0GE4DVQKR8]
sources:
  - url: https://en.wikipedia.org/wiki/Special_unitary_group
---

## Example

The group $SU(2)$ is the [[special unitary group|CZCWFPNS4N]] for $n = 2$.
Its elements are exactly the matrices
$$U = \begin{pmatrix} a & -\bar{b} \\ b & \bar{a} \end{pmatrix}, \qquad a, b \in \C, \quad \abs{a}^2 + \abs{b}^2 = 1.$$
Check: for such a matrix, $U^* U = \begin{pmatrix} \abs{a}^2 + \abs{b}^2 & 0 \\ 0 & \abs{a}^2 + \abs{b}^2 \end{pmatrix} = I_2$ and $\det U = \abs{a}^2 + \abs{b}^2 = 1$.
Conversely, a unitary matrix with determinant $1$ has its second column determined by its first column in this way.

So the map $U \mapsto (a, b)$ identifies $SU(2)$ with the unit sphere $S^3 \subset \C^2 = \R^4$.
It is a [[compact Lie group|9TFC6ADC1C]] of dimension $3$.

## Remarks

Under the usual identification of $\C^2$ with the [[quaternions|0GE4DVQKR8]], $SU(2)$ becomes isomorphic to the group of unit quaternions.
Since $S^3$ is simply connected, $SU(2)$ is simply connected.
$SU(2)$ acts on the trace-zero Hermitian $2 \times 2$ matrices, a real vector space of dimension $3$, by $X \mapsto U X U^*$.
This action preserves $-\det X$, which is a positive definite quadratic form on that space.
It gives a surjective homomorphism $SU(2) \to SO(3)$ onto the [[rotation group|263GGJFA21]] with kernel $\set{\pm I_2}$.
So $SU(2)$ is the universal cover of $SO(3)$, and it is also the spin group $\mathrm{Spin}(3)$.
Its Lie algebra $\mathfrak{su}(2)$ has basis $i\sigma_1, i\sigma_2, i\sigma_3$, where $\sigma_1, \sigma_2, \sigma_3$ are the Pauli matrices.

## Explanations

### L1 human

$SU(2)$ is one of the smallest non-commutative compact connected Lie groups.
As a space it is the $3$-sphere, the set of points at distance $1$ from the origin in four dimensions.
Each element gives a rotation of ordinary space, and exactly two elements, $U$ and $-U$, give the same rotation.
Physicists use $SU(2)$ to describe the spin of particles such as the electron.
