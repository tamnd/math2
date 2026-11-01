---
tag: MPYQ39P01F
kind: statement
role: theorem
name: Pólya enumeration theorem
msc: [05A15, "05E18"]
uses: [0WCY42EV9V, 0YQPZB5Q1G, 0YWDAZPRPQ]
about: [0WCY42EV9V, 0YQPZB5Q1G]
sources:
  - url: https://en.wikipedia.org/wiki/P%C3%B3lya_enumeration_theorem
same_as:
  wikidata: Q1037559
  wikipedia: Pólya enumeration theorem
---

## Statement

Let $G$ be a finite group that [[acts|0WCY42EV9V]] on a finite set $X$ with $\abs{X} = d$.
For $g \in G$ and $1 \le j \le d$, let $c_j(g)$ be the number of [[cycles|0YWDAZPRPQ]] of length $j$ of the permutation $x \mapsto g x$ of $X$.
The *cycle index* of the action is the polynomial
$$Z_G(t_1, \ldots, t_d) = \frac{1}{\abs{G}} \sum_{g \in G} t_1^{c_1(g)} t_2^{c_2(g)} \cdots t_d^{c_d(g)}.$$
Let $C$ be a finite set of colours, and let $G$ act on the set $C^X$ of maps $f \colon X \to C$ by $(g f)(x) = f(g^{-1} x)$.

1. The number of [[orbits|0YQPZB5Q1G]] of $G$ on $C^X$ is $Z_G(m, m, \ldots, m)$, where $m = \abs{C}$.
2. Treat the colours $c \in C$ as commuting variables, and give $f$ the weight $\prod_{x \in X} f(x)$, which is constant on orbits. Then the sum of the weights of the orbits is $Z_G(p_1, p_2, \ldots, p_d)$ with $p_j = \sum_{c \in C} c^j$.

## Remarks

Proof idea: by [[Burnside's lemma|0Z47M1B2VS]], the number of orbits is the average number of colourings fixed by an element $g$.
A colouring is fixed by $g$ exactly when it is constant on each cycle of $g$, so $g$ fixes $m^{c_1(g) + \cdots + c_d(g)}$ colourings.
The weighted form follows from a weighted Burnside lemma in the same way, since a cycle of length $j$ with colour $c$ contributes $c^j$.

Example: colour the $4$ beads of a necklace black or white, up to rotation.
The rotation group $C_4$ has cycle index $\frac{1}{4}(t_1^4 + t_2^2 + 2 t_4)$.
With $m = 2$ this gives $\frac{1}{4}(16 + 4 + 4) = 6$ necklaces.
With colours $b$ and $w$, the weighted form gives $b^4 + b^3 w + 2 b^2 w^2 + b w^3 + w^4$, so $2$ of the necklaces have two beads of each colour.

The group acts on the positions $X$, not on the colours.
If one also allows permutations of the colours, the count changes, and the theorem has to be replaced by a version for the product group.

## Explanations

### L1 human

Pólya's theorem counts colourings when two colourings that differ by a symmetry count as the same.
Typical examples are necklaces up to rotation, or colourings of the faces of a cube up to turning the cube.
One first records how each symmetry moves the positions, in the cycle index.
Then one substitutes the number of colours, or the colours themselves, and reads off the answer.

### L2 human

The theorem refines [[Burnside's lemma|0Z47M1B2VS]] by keeping track of how many times each colour is used.
It counts unlabelled structures, such as isomorphism classes of graphs or chemical isomers, by letting the symmetric group act on positions.
In the [[symbolic method|JP11D90EJC]], the multiset and cycle constructions for unlabelled classes are instances of the same idea.
The cycle index of the symmetric group $S_d$ acting on $d$ points is $\sum_{\lambda} p_\lambda / z_\lambda$, a sum over the partitions $\lambda$ of $d$.
Here $p_\lambda = \prod_j t_j^{m_j}$ and $z_\lambda = \prod_j j^{m_j} m_j!$, where $m_j$ is the number of parts of $\lambda$ equal to $j$.
With $t_j$ read as power sums, this links the theorem to [[symmetric functions|PAJEHWXW6M]].
