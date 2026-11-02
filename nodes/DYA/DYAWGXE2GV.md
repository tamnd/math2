---
tag: DYAWGXE2GV
kind: example
name: James space
msc: [46B10, 46B03]
instance_of: [06GZ956657]
uses: [06GZ956657, NN8RWPC8WG, QKR3D65TTH]
sources:
  - url: https://en.wikipedia.org/wiki/James%27_space
same_as:
  wikidata: Q11829157
  wikipedia: James' space
---

## Example

Let $J$ be the set of real sequences $x = (x_n)_{n \ge 1}$ with $x_n \to 0$ and $\norm{x}_J < \infty$, where
$$\norm{x}_J = \sup \Big( \sum_{i=1}^{k-1} (x_{p_i} - x_{p_{i+1}})^2 \Big)^{1/2}.$$
The supremum runs over all $k \ge 2$ and all integers $p_1 < p_2 < \cdots < p_k$.
Then $\norm{\cdot}_J$ is a norm on $J$, and $J$ is a [[Banach space|06GZ956657]], the James space.

Check that $x_n = 1/\sqrt{n}$ lies in $J$.
For $p_1 < \cdots < p_k$, the differences $a_i = x_{p_i} - x_{p_{i+1}}$ are positive.
Then $\sum_i a_i^2 \le (\sum_i a_i)^2 = (x_{p_1} - x_{p_k})^2 \le 1$.
So $\norm{x}_J \le 1$, although $x$ is not in $\ell^2$, since $\sum_n 1/n$ diverges.

## Remarks

James built this space in 1951.
The canonical image of $J$ in its [[bidual|QKR3D65TTH]] $J^{**}$ has codimension $1$, so $J$ is not [[reflexive|NN8RWPC8WG]].
Yet $J$ is isomorphic to $J^{**}$.
So a Banach space can be isomorphic to its bidual without being reflexive.
The norm vanishes only at $0$ because $x_n \to 0$: the difference $x_p - x_q$ with $q$ large is close to $x_p$.

## Explanations

### L1 human

The norm of James space measures the total squared jumps of a sequence along any chosen subsequence.
A sequence that slides down to $0$ without wiggling has a small norm, even if it decreases slowly.
The space is famous as a counterexample: it is as big as its double dual, but not in the canonical way.
