---
tag: KX0B3AWD5H
kind: statement
role: theorem
name: Toponogov's theorem
msc: [53C20, 53C23]
uses: [7CBT4SM83Y, 1X42JAA349, NSYMQMHPDN, B4QR306D8G, 1VM1AQT956]
about: [1X42JAA349]
sources:
  - url: https://en.wikipedia.org/wiki/Toponogov%27s_theorem
same_as:
  wikidata: Q7825061
  wikipedia: Toponogov's theorem
---

## Statement

Let $(M, g)$ be a connected complete [[Riemannian manifold|7CBT4SM83Y]] of dimension $n \ge 2$ whose [[sectional curvature|1X42JAA349]] satisfies $K \ge k$ for a real number $k$.
Let $M_k^2$ be the simply connected complete surface of constant curvature $k$, a [[space form|1VM1AQT956]].
Let $p \in M$, and let $\gamma_1, \gamma_2$ be minimizing unit-speed [[geodesics|NSYMQMHPDN]] starting at $p$, of lengths $\ell_1, \ell_2$, that make the angle $\alpha \in [0, \pi]$ at $p$.
If $k > 0$, assume $\ell_1, \ell_2 \le \pi / \sqrt{k}$.
Let $\bar\gamma_1, \bar\gamma_2$ be unit-speed geodesics in $M_k^2$ starting at a point $\bar p$, of lengths $\ell_1, \ell_2$, that make the angle $\alpha$ at $\bar p$.
Then
$$d\bigl(\gamma_1(\ell_1), \gamma_2(\ell_2)\bigr) \le \bar d\bigl(\bar\gamma_1(\ell_1), \bar\gamma_2(\ell_2)\bigr),$$
where $d$ is the [[Riemannian distance|B4QR306D8G]] of $M$ and $\bar d$ that of $M_k^2$.

## Remarks

This is the hinge form of the theorem.
An equivalent form compares the angles of a geodesic triangle with minimizing sides in $M$ with those of the triangle with the same side lengths in $M_k^2$.
Each angle in $M$ is at least the corresponding angle in $M_k^2$.
The proof starts from the Rauch comparison theorem, which gives the result for short hinges, and extends it to all hinges by a subdivision argument that uses completeness.

Example: if $K \ge 0$, compare with the Euclidean plane.
Then for two minimizing geodesics of lengths $\ell_1, \ell_2$ from $p$ at angle $\alpha$, the endpoints are at distance at most $\sqrt{\ell_1^2 + \ell_2^2 - 2 \ell_1 \ell_2 \cos\alpha}$, the value given by the law of cosines.
On the round sphere, for $0 < \alpha < \pi$, the distance is strictly smaller, since triangles on a sphere are fatter than flat triangles.

## Explanations

### L1 human

On a space that curves at least as much as a model surface, triangles are "fatter" than in the model.
Two paths that leave a point at a given angle end up closer together than they would in the model.

### L2 human

Toponogov's theorem turns a lower curvature bound into a statement about distances only, without derivatives.
This is why it is the basis of many global results such as the soul theorem and the Grove–Shiohama diameter sphere theorem.
Its conclusion is also used as the definition of a lower curvature bound for metric spaces, which leads to Alexandrov spaces.
