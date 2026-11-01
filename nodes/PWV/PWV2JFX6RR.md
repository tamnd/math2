---
tag: PWV2JFX6RR
kind: conjecture
name: Erdős–Hajnal conjecture
msc: [05C55, 05C69]
uses: [00C0BR7D7H, 0EREPBVG2G, 0BYX1D7C2E, 08ANQHHG3P]
about: [0EREPBVG2G]
sources:
  - url: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Hajnal_conjecture
same_as:
  wikidata: Q16974940
  wikipedia: Erdős–Hajnal conjecture
history:
  posed_by: "Paul Erdős and András Hajnal"
  first_stated: "1989"
---

## Statement

For every finite [[graph|00C0BR7D7H]] $H$ there is a constant $\varepsilon(H) > 0$ with the following property.
Let $G$ be a graph with $n$ vertices that has no [[induced subgraph|0EREPBVG2G]] isomorphic to $H$.
Then $G$ has a [[clique|0BYX1D7C2E]] or an [[independent set|08ANQHHG3P]] with at least $n^{\varepsilon(H)}$ vertices.

## Remarks

Without the hypothesis on $H$, only a logarithmic bound holds.
Every graph on $n$ vertices has a clique or an independent set of size at least $\tfrac12 \log_2 n$, by [[Ramsey's theorem|00TQV3F5S4]].
Random graphs show that this order $\log n$ cannot be improved in general.
Erdős and Hajnal proved that excluding $H$ gives a bound of the form $e^{c\sqrt{\log n}}$ with $c > 0$ depending on $H$.
The conjecture is known for all graphs $H$ with at most four vertices.
For $H$ the path on four vertices it is easy: such graphs are perfect, so the product of the clique number and the independence number is at least $n$.
The conjecture is open in general; the path on five vertices was settled only in 2023.

## Explanations

### L1 human

Ramsey theory says that every large graph has a fairly large set of vertices that are all joined or all unjoined.
In general this set may be tiny, about the logarithm of the number of vertices.
The conjecture says that forbidding any one fixed pattern as an induced subgraph forces a much larger such set, a power of the number of vertices.
