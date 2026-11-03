---
tag: ECJMS4VDTF
kind: example
name: Friedmann–Lemaître–Robertson–Walker metric
msc: ["83F05", "83C15"]
instance_of: [BY4QYYS788]
uses: [Q8MSCRDFAT, 1VM1AQT956, 63ZKC7AFX2]
sources:
  - url: https://en.wikipedia.org/wiki/Friedmann%E2%80%93Lema%C3%AEtre%E2%80%93Robertson%E2%80%93Walker_metric
same_as:
  wikidata: Q742982
  wikipedia: Friedmann–Lemaître–Robertson–Walker metric
---

## Example

Let $I \subseteq \R$ be an open interval, let $a \colon I \to (0, \infty)$ be a smooth function, and let $k \in \R$.
Let $(\Sigma, \gamma_k)$ be the complete simply connected three-dimensional [[space form|1VM1AQT956]] of constant sectional curvature $k$.
The *Friedmann–Lemaître–Robertson–Walker (FLRW) metric* on $M = I \times \Sigma$ is
$$ds^2 = -dt^2 + a(t)^2 \, \gamma_k,$$
in units with $c = 1$.
In comoving coordinates $(\chi, \theta, \phi)$ on $\Sigma$ one has
$$\gamma_k = d\chi^2 + S_k(\chi)^2 \left( d\theta^2 + \sin^2\theta \, d\phi^2 \right),$$
where $S_k(\chi) = \sin(\sqrt{k}\,\chi)/\sqrt{k}$ if $k > 0$, $S_k(\chi) = \chi$ if $k = 0$, and $S_k(\chi) = \sinh(\sqrt{-k}\,\chi)/\sqrt{-k}$ if $k < 0$.

Check that it is a Lorentzian metric: $\gamma_k$ is positive definite, so $g$ has signature $(-,+,+,+)$ at every point.
Check the [[cosmological principle|Q8MSCRDFAT]] for $u = \partial_t$ and the slices $\Sigma_t = \set{t} \times \Sigma$: every isometry $\psi$ of the space form gives an isometry $(t, x) \mapsto (t, \psi(x))$ of $g$.
The complete simply connected space form has isometries that move any point to any other point.
It also has isometries that fix a point and rotate any tangent direction to any other one.
So both homogeneity and isotropy hold.

## Remarks

The function $a$ is the scale factor; the metric says nothing about its form until one imposes the Einstein equations, which become the Friedmann equations.
With $a$ constant and $k = 0$ the metric is Minkowski space.
The curves $x = \text{const}$ are timelike geodesics, and $t$ is the proper time along them.

## Explanations

### L1 human

The FLRW metric describes a universe whose space is the same everywhere, but whose size can change with time.
The single function $a(t)$ says how all distances between galaxies at rest grow or shrink together.
Space itself can be flat, like ordinary three-dimensional space, curved like a sphere, or curved like a saddle.
It is the metric behind all of standard cosmology.
