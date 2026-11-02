---
tag: 4T72ZP5XHF
kind: example
name: Mumford–Shah functional
msc: [49J45, 94A08, 49Q20]
illustrates: [NW9MM370A5]
uses: [Q1TGZK8RN6, 0ZCK8DQYN1, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Mumford–Shah_functional
same_as:
  wikidata: Q17144601
  wikipedia: Mumford–Shah functional
---

## Example

Let $\Omega \subseteq \R^2$ be a bounded open set, the image domain.
Let $g \in L^\infty(\Omega)$ be a grey-level image, and let $\alpha, \beta > 0$ be parameters.
For a relatively [[closed set|0ZCK8DQYN1]] $K \subseteq \Omega$ and a function $u \in C^1(\Omega \setminus K)$, the *Mumford–Shah functional* is
$$E(u, K) = \int_{\Omega \setminus K} \abs{\nabla u}^2 \, dx + \alpha \int_{\Omega \setminus K} (u - g)^2 \, dx + \beta \, \mathcal{H}^1(K).$$
Here $\mathcal{H}^1$ is the one-dimensional [[Hausdorff measure|Q1TGZK8RN6]], the length of $K$.
A minimizing pair $(u, K)$ gives a smoothed image $u$ and a set of edges $K$.

Check on a simple image: let $D$ be a closed disc of radius $r$ in $\Omega$, and let $g = \mathbf{1}_D$.
The pair $u = g$, $K = \partial D$ has no gradient term and no fidelity term, so $E(u, K) = 2 \pi \beta r$.
The pair $u = 0$, $K = \emptyset$ has energy $\alpha \pi r^2$.
So for $\alpha > 2\beta/r$ the first pair is cheaper than the second, and for $\alpha < 2\beta/r$ the second is cheaper.
Large weights on fidelity favour keeping the edge, and small weights favour erasing it.

## Remarks

The functional was proposed by David Mumford and Jayant Shah for image segmentation.
It is a free discontinuity problem: the unknown set $K$ is where $u$ may jump.
Ennio De Giorgi, Michele Carriero and Antonio Leaci proved the existence of minimizers.
Their method first solves a weak form, where $u$ is a special function of bounded variation and $K$ is its jump set.
Luigi Ambrosio and Vincenzo Maria Tortorelli approximated it, in the sense of [[Γ-convergence|NW9MM370A5]], by elliptic functionals of two smooth functions, which is the basis of many numerical methods.

## Explanations

### L1 human

An image has smooth regions separated by sharp edges.
The Mumford–Shah functional looks for a clean image $u$ that stays close to the given image $g$.
The clean image must be smooth away from a set of edges, and the total length of the edges must be small.
Each wish has a weight, and the best compromise gives both a cleaned image and a drawing of its contours.
For a white disc on a black background, the answer depends on the weights: either the circle is kept as an edge, or the disc is wiped out.
