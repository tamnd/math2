---
tag: CNADH7BENS
kind: counterexample
name: Hartogs triangle
msc: [32T05, 32Q02]
uses: [AHYZMSBBNH, FF2P7ER3QT, FGSKR6ZS3Q, 4487CSC0MB, GHJC53RFBT, 6BJB149MDK]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
---

## Counterexample

The *Hartogs triangle* is the domain
$$H = \set{(z, w) \in \C^2 : \abs{z} < \abs{w} < 1}.$$
It is a bounded [[pseudoconvex|AHYZMSBBNH]] domain whose closure $\overline{H}$ has no basis of pseudoconvex neighbourhoods.

Check that $H$ is pseudoconvex.
On $H$ the function $g(z, w) = z/w$ is holomorphic with $\abs{g} < 1$.
Let
$$\varphi(z, w) = -\log\big(1 - \abs{z/w}^2\big) - \log\big(1 - \abs{w}^2\big) - \log \abs{w}.$$
The first two terms are [[plurisubharmonic|FF2P7ER3QT]], since $-\log(1 - \abs{h}^2) = \sum_{k \ge 1} \abs{h^k}^2 / k$ for a holomorphic $h$ with $\abs{h} < 1$, and the last term is pluriharmonic.
The boundary of $H$ consists of the points with $\abs{z} = \abs{w} \le 1$ and the points with $\abs{w} = 1$, $\abs{z} \le 1$.
All three terms are nonnegative on $H$.
Near the first part the first term tends to $+\infty$, except at the origin, where the last term does.
Near the second part the second term tends to $+\infty$.
So $\varphi$ is a continuous [[plurisubharmonic exhaustion function|FGSKR6ZS3Q]], and $H$ is pseudoconvex, hence a [[domain of holomorphy|4487CSC0MB]] by [[Oka's theorem|6BJB149MDK]].

Check the neighbourhoods.
Let $U$ be an open set containing $\overline{H} = \set{\abs{z} \le \abs{w} \le 1}$.
Since $\overline{H}$ is compact, $U$ contains, for some $\varepsilon > 0$, the set $\set{\abs{z} < \varepsilon, \abs{w} < 1 + \varepsilon}$ and the set $\set{\abs{z} < 1 + \varepsilon, 1 - \varepsilon < \abs{w} < 1 + \varepsilon}$.
The union of these two sets is a [[Hartogs figure|GHJC53RFBT]].
Let $f$ be holomorphic on $U$.
The Laurent series of $w \mapsto f(z, w)$ on the annulus has no negative powers when $\abs{z} < \varepsilon$.
Its coefficients are holomorphic in $z$, so by the identity theorem it has none when $\abs{z} < 1$.
So $f$ extends holomorphically to the bidisc $\set{\abs{z} < 1, \abs{w} < 1 + \varepsilon}$.
Hence any domain of holomorphy that contains $\overline{H}$ contains the whole unit bidisc, and the pseudoconvex neighbourhoods of $\overline{H}$ cannot shrink to $\overline{H}$.

## Remarks

The boundary of $H$ is not a Lipschitz graph near the origin, and this singular point is the source of the pathology.
For bounded pseudoconvex domains with smooth boundary, the closure can still fail to have a pseudoconvex neighbourhood basis.
The examples are much harder, such as the worm domains of Diederich and Fornæss.

## Explanations

### L1 human

The Hartogs triangle is the set of pairs $(z, w)$ of complex numbers with $\abs{z} < \abs{w} < 1$.
If one draws it with axes $\abs{z}$ and $\abs{w}$, it is a triangle.
It is a perfectly good domain for holomorphic functions, a domain of holomorphy.
But every domain of holomorphy that contains its closure must contain the whole unit bidisc, because holomorphic functions near the closure always extend that far.
So the closure of a domain of holomorphy need not be approximable from outside by domains of holomorphy.
