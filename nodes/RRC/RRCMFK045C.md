---
tag: RRCMFK045C
kind: counterexample
name: Long branch attraction
msc: [92B10, 62P10]
uses: [GXYN4CQF0Y, 5624H8KWKK]
sources:
  - url: https://en.wikipedia.org/wiki/Long_branch_attraction
same_as:
  wikidata: Q2870169
  wikipedia: Long branch attraction
---

## Counterexample

Take the unrooted binary [[phylogenetic tree|5624H8KWKK]] $T = ab|cd$ on four taxa.
Leaves $a, b$ join an internal vertex $u$, leaves $c, d$ join an internal vertex $v$, and the interior edge joins $u$ and $v$.
Let a binary character evolve along $T$ under the symmetric two-state model.
The state at $u$ is uniform on $\set{0, 1}$, and along each edge it flips independently with a probability that depends on the edge.
The two long edges $ua$ and $vc$ have flip probability $p \in (0, 1/2)$.
The three short edges $ub$, $vd$ and $uv$ have flip probability $q \in (0, 1/2)$.
The data are $m$ independent characters from this model.

On four taxa only three patterns matter for [[maximum parsimony|GXYN4CQF0Y]].
They are $xxyy$ (the states of $a, b$ are equal, the states of $c, d$ are equal, and the two differ), $xyxy$ and $xyyx$.
A pattern $xxyy$ has score $1$ on $ab|cd$ and score $2$ on the other two trees, and similarly for the other patterns.
So maximum parsimony picks the tree whose pattern occurs most often.

As $q \to 0$ with $p$ fixed, the probabilities of $xxyy$ and of $xyyx$ tend to $0$, since both need a flip on a short edge.
The probability of $xyxy$ tends to $p^2 > 0$: it occurs when both long edges flip and no short edge does.
So for $q$ small enough, $xyxy$ is the most likely of the three patterns.
By the law of large numbers, maximum parsimony then returns the wrong tree $ac|bd$ with probability tending to $1$ as $m \to \infty$.

## Remarks

The example shows that maximum parsimony is not statistically consistent: more data make it surer of the wrong tree.
The cause is that parallel changes on the two long edges look like a single shared change.
Maximum likelihood under the correct model is consistent in this setting.

## Explanations

### L1 human

On long branches many changes happen, and by chance two long branches often end up with the same state.
Parsimony reads this coincidence as shared history and groups the two long branches together, even when they are not closest relatives.
The effect is not just bad luck with small data: with more and more data the method becomes more and more sure of the wrong answer.
