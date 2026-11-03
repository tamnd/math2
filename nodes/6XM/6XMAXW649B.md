---
tag: 6XMAXW649B
kind: example
name: De Sitter space
msc: [83C15, 53C50, 83F05]
instance_of: [BY4QYYS788]
illustrates: [WVKKDY9V61]
uses: [G49G4R1K04, 1X42JAA349, 41S2EZ0KR3]
sources:
  - url: https://en.wikipedia.org/wiki/De_Sitter_space
same_as:
  wikidata: Q1179448
  wikipedia: De Sitter space
---

## Example

Let $n \ge 3$ and $\alpha > 0$.
Equip $\R^{n+1}$ with the [[Minkowski|G49G4R1K04]] form $\eta = -dx_0^2 + dx_1^2 + \cdots + dx_n^2$.
The *de Sitter space* $dS_n$ of radius $\alpha$ is the hyperboloid
$$dS_n = \set{x \in \R^{n+1} : -x_0^2 + x_1^2 + \cdots + x_n^2 = \alpha^2}$$
with the metric $g$ induced by $\eta$.

Check that it is a Lorentzian manifold: the coordinates $x_0 = \alpha\sinh(\tau/\alpha)$, $(x_1, \ldots, x_n) = \alpha\cosh(\tau/\alpha)\,\omega$ with $\tau \in \R$ and $\omega \in S^{n-1}$ cover the whole hyperboloid.
In them
$$g = -d\tau^2 + \alpha^2\cosh^2(\tau/\alpha)\, d\Omega_{n-1}^2,$$
where $d\Omega_{n-1}^2$ is the round metric of $S^{n-1}$, so $g$ has one negative and $n - 1$ positive directions.

The [[sectional curvature|1X42JAA349]] is constant and equal to $1/\alpha^2$, so the Ricci tensor is $R_{ab} = \frac{n-1}{\alpha^2} g_{ab}$ and $dS_n$ is an [[Einstein manifold|41S2EZ0KR3]].
Hence it solves the vacuum Einstein equations $G_{ab} + \Lambda g_{ab} = 0$ with positive [[cosmological constant|WVKKDY9V61]]
$$\Lambda = \frac{(n-1)(n-2)}{2\alpha^2},$$
which is $\Lambda = 3/\alpha^2$ in dimension $4$.
The linear maps of $\R^{n+1}$ preserving $\eta$ preserve the hyperboloid, so the isometry group contains $O(1, n)$, and $dS_n$ is maximally symmetric.
The spatial slices $\tau = \text{const}$ are spheres that shrink to radius $\alpha$ at $\tau = 0$ and then expand exponentially.

## Explanations

### L1 human

De Sitter space is the Lorentzian cousin of a sphere: it is a hyperboloid of one sheet sitting inside a flat spacetime of one more dimension.
It is a universe with no matter and a positive cosmological constant, which drives an accelerated expansion.
Every point looks the same as every other, and every direction too, so it is as symmetric as flat spacetime.
It models the inflation era of the early universe and the far future of a universe dominated by dark energy, as in the [[de Sitter universe|55ZQST8RG5]] of cosmology.
