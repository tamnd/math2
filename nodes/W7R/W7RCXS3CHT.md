---
tag: W7RCXS3CHT
kind: example
name: Stiefel manifold
msc: [55R10, 57R22]
instance_of: [F45VQ47GPV]
sources:
  - url: https://en.wikipedia.org/wiki/Stiefel_manifold
---

## Example

Let $1 \le k \le n$.
The real Stiefel manifold $V_k(\R^n)$ is the set of orthonormal $k$-frames in $\R^n$:
$$V_k(\R^n) = \set{(v_1, \ldots, v_k) \in (\R^n)^k : \ip{v_i}{v_j} = \delta_{ij} \text{ for all } i, j},$$
with the [[subspace topology|0WS9P12FQR]] of $(\R^n)^k$.
It is a compact [[smooth manifold|F45VQ47GPV]] of dimension $nk - k(k+1)/2$.

Check: $V_k(\R^n)$ is closed and bounded in $(\R^n)^k$, hence compact.
It is the level set of the map $(v_1, \ldots, v_k) \mapsto (\ip{v_i}{v_j})_{i \le j}$ to the space of symmetric $k \times k$ matrices at the identity matrix, and this value is regular.
The space of symmetric $k \times k$ matrices has dimension $k(k+1)/2$, which gives the dimension.

## Remarks

Special cases: $V_1(\R^n) = S^{n-1}$, and $V_n(\R^n)$ is the orthogonal group $O(n)$.
For $V_2(\R^3)$ the dimension is $6 - 3 = 3$, and indeed $(v_1, v_2) \mapsto (v_1, v_2, v_1 \times v_2)$ identifies it with the rotation group $SO(3)$.

Stiefel manifolds give standard [[fiber bundles|CX4M8K61AB]].
The map $V_k(\R^n) \to S^{n-1}$, $(v_1, \ldots, v_k) \mapsto v_1$, is a fiber bundle with fiber $V_{k-1}(\R^{n-1})$.
The map $V_k(\R^n) \to G_k(\R^n)$ that sends a frame to the subspace it spans is a [[principal $O(k)$-bundle|8E37E74XVP]] over the Grassmannian.
Using these bundles one shows that $V_k(\R^n)$ is $(n - k - 1)$-connected; as $n \to \infty$, the bundle $V_k(\R^\infty) \to G_k(\R^\infty)$ becomes the [[universal bundle|1HDH716Z24]] for $O(k)$.

## Explanations

### L1 human

A point of the Stiefel manifold $V_k(\R^n)$ is a list of $k$ unit vectors in $\R^n$ that are all perpendicular to each other.
For one vector, this is just a point of the unit sphere.
For two perpendicular unit vectors in space, the third vector of a right-handed frame is fixed by the first two.
So these pairs correspond to the rotations of space.
The question whether the sphere $S^{n-1}$ has $k$ independent tangent vector fields is the question whether the bundle $V_{k+1}(\R^n) \to S^{n-1}$ has a section.
