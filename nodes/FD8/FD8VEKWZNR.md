---
tag: FD8VEKWZNR
kind: definition
name: Dirichlet space
msc: [30H99, "46E22"]
defines: KWKVCSJWFB
uses: [0NAHXR1FRH, 8G5ABXRK85, 0QVNCJXRY3, 0D6KXBHKC0]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_space
---

## Definition

Let $\mathbb{D} = \set{z \in \C : \abs{z} < 1}$ be the [[unit disc|8G5ABXRK85]] and let $dA$ be area measure.
The *Dirichlet space* $\mathcal{D}$ is the set of [[holomorphic functions|0NAHXR1FRH]] $f \colon \mathbb{D} \to \C$ such that
$$\int_{\mathbb{D}} \abs{f'(z)}^2 \, dA(z) < \infty.$$
Its norm is given by $\norm{f}_{\mathcal{D}}^2 = \abs{f(0)}^2 + \frac{1}{\pi}\int_{\mathbb{D}} \abs{f'(z)}^2 \, dA(z)$.

## Remarks

For $f(z) = \sum_{n \ge 0} a_n z^n$, a [[power series|0D6KXBHKC0]] on $\mathbb{D}$, one has $\int_{\mathbb{D}} \abs{z^{n-1}}^2 dA = \pi/n$, hence $\int_{\mathbb{D}} \abs{f'}^2 \, dA = \pi\sum_{n \ge 1} n \abs{a_n}^2$ and $\norm{f}_{\mathcal{D}}^2 = \abs{a_0}^2 + \sum_{n \ge 1} n\abs{a_n}^2$.
This norm comes from an [[inner product|0QVNCJXRY3]], and $\mathcal{D}$ is a Hilbert space.
Example: $f(z) = z$ has $\int_{\mathbb{D}} \abs{f'}^2 \, dA = \pi$, the area of $f(\mathbb{D}) = \mathbb{D}$.
Non-example: $f(z) = \log(1 - z) = -\sum_{n \ge 1} z^n/n$ gives $\sum_{n \ge 1} n \cdot \frac{1}{n^2} = \sum 1/n = \infty$, so $f \notin \mathcal{D}$, although $f$ is in the Hardy space $H^2$.
If $f$ is injective, $\int_{\mathbb{D}} \abs{f'}^2 \, dA$ is the area of $f(\mathbb{D})$, since $\abs{f'}^2$ is the Jacobian determinant of $f$.
Some authors omit the term $\abs{f(0)}^2$ or replace it by $\norm{f}_{H^2}^2$; these give equivalent norms.
