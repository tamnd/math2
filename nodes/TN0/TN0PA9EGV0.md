---
tag: TN0PA9EGV0
kind: example
name: Directed percolation
msc: [82C43, 60K35, 82B43]
instance_of: [BH7YPXCYDK]
uses: [MP8VSZK19A]
sources:
  - url: https://en.wikipedia.org/wiki/Directed_percolation
same_as:
  wikidata: Q5280413
  wikipedia: Directed percolation
---

## Example

Let $\mathcal L = \set{(x, t) \in \Z \times \Z_{\ge 0} : x + t \text{ even}}$.
Draw an oriented edge from each $(x, t) \in \mathcal L$ to $(x - 1, t + 1)$ and to $(x + 1, t + 1)$.
Let $p \in [0, 1]$, and declare each oriented edge open with probability $p$, independently, as in [[bond percolation|BH7YPXCYDK]].
The cluster $C$ of the origin is the set of points reached from $(0, 0)$ by a path of open edges that follows the orientation.
Along such a path the time coordinate $t$ only increases.
*Directed bond percolation* in $1 + 1$ dimensions asks whether $C$ is infinite with positive probability, that is, whether the set $C_t = \set{x : (x, t) \in C}$ is nonempty for all $t$.

Check of a lower bound for the threshold: each point of $C_t$ has $2$ outgoing edges, so $\mathbb{E} \abs{C_{t+1}} \le 2p \, \mathbb{E} \abs{C_t}$.
Hence $\mathbb{E} \abs{C_t} \le (2p)^t \to 0$ for $p < 1/2$, and $C$ is finite almost surely.
So the critical value $p_c$ satisfies $p_c \ge 1/2$.

## Remarks

The [[percolation threshold|MP8VSZK19A]] of this model is not known exactly; numerical estimates give $p_c \approx 0.6447$.
It is strictly larger than the threshold $1/2$ of undirected bond percolation on the square lattice, since the orientation removes paths.
Reading $t$ as time, $C_t$ is the set of active sites of a growth process, and the empty set is an absorbing state.
The [[contact process|9RVKQJQ5JJ]] is its continuous-time analogue.
Many models with a phase transition into a single absorbing state are believed to share the critical exponents of directed percolation.

## Explanations

### L1 human

Water seeps down through a porous rock, and it can only flow downward, never up.
Each small channel is open or blocked at random.
Directed percolation asks whether water entering at one point on top can reach arbitrarily deep layers.
Because the water cannot turn back up, it needs more open channels than in ordinary percolation, so the critical density is higher.
The same model describes the spreading of an epidemic in time, where infected sites can only infect at later times.
