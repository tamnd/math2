---
tag: ETMAPNQY7T
kind: statement
role: lemma
name: Szemerédi regularity lemma
msc: [05C35, 05D99]
uses: [00C0BR7D7H, 08QMKTWF9T]
about: [SC5QB5F4TE]
sources:
  - url: https://en.wikipedia.org/wiki/Szemerédi_regularity_lemma
same_as:
  wikidata: Q1295910
  wikipedia: Szemerédi regularity lemma
---

## Statement

Let $G$ be a finite simple [[graph|00C0BR7D7H]] with vertex set $V$.
For disjoint nonempty sets $X, Y \subseteq V$, let $e(X, Y)$ be the number of edges with one end in $X$ and one in $Y$, and let $d(X, Y) = e(X, Y) / (|X| |Y|)$.
Let $\varepsilon > 0$.
A pair $(A, B)$ of disjoint nonempty sets is *$\varepsilon$-regular* if $\abs{d(X, Y) - d(A, B)} \le \varepsilon$ whenever $X \subseteq A$, $Y \subseteq B$, $|X| \ge \varepsilon |A|$ and $|Y| \ge \varepsilon |B|$.
A [[partition|08QMKTWF9T]] $V = V_1 \cup \cdots \cup V_k$ is *equitable* if any two parts differ in size by at most $1$.

For every $\varepsilon > 0$ and every integer $m \ge 1$ there is an integer $M = M(\varepsilon, m)$ with the following property.
Let $G$ have at least $m$ vertices.
Then $G$ has an equitable partition $V_1, \ldots, V_k$ of its vertex set with $m \le k \le M$.
In this partition, all but at most $\varepsilon k^2$ of the pairs $(V_i, V_j)$ with $i < j$ are $\varepsilon$-regular.

## Remarks

The proof uses an energy, the mean square of the densities $d(V_i, V_j)$, which lies between $0$ and $1$.
If the current partition has too many irregular pairs, the sets $X, Y$ that witness irregularity are used to refine it.
Then the energy increases by at least a fixed amount depending on $\varepsilon$.
So the process stops after a bounded number of steps.
Each step multiplies the number of parts by an exponential, so $M$ is a tower of exponentials of height polynomial in $1/\varepsilon$.
Gowers showed that bounds of tower type are necessary.

The lemma comes with a counting lemma: if parts $V_1, V_2, V_3$ are pairwise $\varepsilon$-regular with densities at least $\delta$ and $\varepsilon$ is small compared with $\delta$, then they span many triangles.
Together they prove the [[triangle removal lemma|XMS1QRAQZC]] and the [[Erdős–Stone theorem|XZF9BFJFXB]].

## Explanations

### L1 human

Every large graph, however messy, can be cut into a bounded number of pieces of equal size so that between most pairs of pieces the edges look random.
"Look random" means that the edge density is about the same between any two large subsets of the two pieces.
The number of pieces depends only on the accuracy you ask for, not on the size of the graph.

### L2 human

The lemma replaces a huge graph by a small weighted "reduced graph" on the parts, with the densities as weights.
Questions about copies of a fixed small graph can then be answered in the reduced graph through the counting lemma.
This is the route to the [[triangle removal lemma|XMS1QRAQZC]], to [[Roth's theorem|E7H8NWXESF]], and to the [[Erdős–Stone theorem|XZF9BFJFXB]].
Szemerédi first proved a version for bipartite graphs as a step towards [[Szemerédi's theorem|B23B0QEMN5]] on arithmetic progressions.
The limit object of this point of view is the [[graphon|QMJ5PNSF9X]].
