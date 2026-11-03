---
tag: 45HEVXM7RD
kind: example
name: Six-vertex model
msc: [82B20, 82B23]
instance_of: [PAEME5EQRM]
uses: [00C0BR7D7H, EXX6S3K5Z5]
sources:
  - url: https://en.wikipedia.org/wiki/Ice-type_model
same_as:
  wikidata: Q5985139
  wikipedia: Ice-type model
---

## Example

Let $\Lambda$ be the $N \times N$ square grid on a torus, with $N^2$ vertices and $2N^2$ edges, and let $a, b, c > 0$.
A configuration orients every edge so that each vertex has exactly two incoming and two outgoing edges, the *ice rule*.
There are $\binom{4}{2} = 6$ ways to orient the four edges at a vertex under this rule.
They come in three pairs related by reversing all arrows.
In types 1 and 2 the arrows point right and up, or left and down.
In types 3 and 4 they point right and down, or left and up.
In types 5 and 6 both horizontal arrows point into the vertex and both vertical arrows point out, or the reverse.
In the symmetric zero-field case these pairs get the weights $a$, $b$ and $c$.
The *six-vertex model* is the probability measure on such orientations proportional to the product of the vertex weights.
Its partition function is
$$Z_N = \sum_{\text{ice configurations}} a^{n_1 + n_2} b^{n_3 + n_4} c^{n_5 + n_6},$$
where $n_k$ is the number of vertices of type $k$.

## Remarks

The behaviour depends mainly on the parameter $\Delta = (a^2 + b^2 - c^2)/(2ab)$.
The model is in a frozen ferroelectric phase for $\Delta > 1$, in a disordered critical phase for $-1 < \Delta < 1$, and in an antiferroelectric phase for $\Delta < -1$.
For $a = b = c = 1$ the partition function counts ice configurations, and $\Delta = 1/2$; its growth rate is [[Lieb's square ice constant|NXA6N97CXN]].
Lieb solved important special cases in 1967 with the [[transfer matrix method|EXX6S3K5Z5]] and the [[Bethe ansatz|S92G5M6X41]], and Sutherland extended the solution to general weights.
Its weights satisfy the [[Yang–Baxter equation|663BP8ZHS5]], which explains the solvability, and it is the classical counterpart of the XXZ quantum spin chain.

## Explanations

### L1 human

Think of water ice drawn on a square grid: each vertex is an oxygen atom, and each edge carries a hydrogen that sits closer to one end.
An arrow on each edge points toward the end where the hydrogen sits, and the ice rule says two arrows point in and two point out at every vertex.
The six local pictures get weights, and the model asks how the arrows organize over the whole grid.
