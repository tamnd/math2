---
tag: TJHVHD5SH5
kind: example
name: Dimer model
msc: [82B20, 05C70, 05B45]
instance_of: [PAEME5EQRM]
uses: [00C0BR7D7H, 0NHK9MFFW9, 83PJCPB9VA]
sources:
  - url: https://en.wikipedia.org/wiki/Domino_tiling
---

## Example

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]] with at least one [[perfect matching|0NHK9MFFW9]], and let $w \colon E \to (0, \infty)$ be edge weights.
A configuration is a perfect matching $M$ of $G$, also called a dimer covering.
Each edge of $M$ is a dimer, and each vertex is covered by exactly one dimer.
The *dimer model* on $(G, w)$ is the probability measure on perfect matchings given by
$$\mathbb{P}(M) = \frac{1}{Z} \prod_{e \in M} w(e), \qquad Z = \sum_{M} \prod_{e \in M} w(e).$$
With all weights equal to $1$, it is the uniform measure on perfect matchings, and $Z$ is their number.

## Remarks

When $G$ is the grid graph of a region of unit squares, a perfect matching is the same as a [[domino tiling|83PJCPB9VA]] of the region.
Kasteleyn, and independently Temperley and Fisher, found in 1961 that the number of domino tilings of an $m \times n$ rectangle is
$$\prod_{j=1}^{\ceil{m/2}} \prod_{k=1}^{\ceil{n/2}} \left( 4 \cos^2 \frac{\pi j}{m + 1} + 4 \cos^2 \frac{\pi k}{n + 1} \right).$$
Check for $m = n = 2$: the only factor is $4 \cdot \frac14 + 4 \cdot \frac14 = 2$, and a $2 \times 2$ square has exactly $2$ domino tilings.
Check for $m = 2$, $n = 3$: the factors are $1 + 2 = 3$ and $1 + 0 = 1$, giving the $3$ tilings of a $2 \times 3$ rectangle.
For an $m \times n$ rectangle with $m, n \to \infty$, $\frac{1}{mn} \log(\text{number of tilings}) \to G_{\mathrm{Cat}}/\pi \approx 0.2916$, where $G_{\mathrm{Cat}}$ is Catalan's constant.
On planar graphs $Z$ is a [[Pfaffian|NH5HWBPWS9]], by the [[FKT algorithm|A6SPEDH8BK]], which makes the model exactly solvable.

## Explanations

### L1 human

Place dominoes on a board so that every square is covered exactly once, and pick a tiling at random.
More generally, pair up the vertices of a graph along its edges, every vertex used once.
Dimer models model molecules that occupy two neighbouring sites, and their random tilings show striking large-scale shapes, such as the arctic circle.
