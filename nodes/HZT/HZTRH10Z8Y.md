---
tag: HZTRH10Z8Y
kind: example
name: Smith–Volterra–Cantor set
msc: [28A05, 26A30]
instance_of: [0VQYCCQVJ5]
uses: [2Z2QVWZ262, 0ZCK8DQYN1, 0BXNDZFQME]
sources:
  - url: https://en.wikipedia.org/wiki/Smith%E2%80%93Volterra%E2%80%93Cantor_set
same_as:
  wikidata: Q909569
  wikipedia: Smith–Volterra–Cantor set
---

## Example

Start with $C_0 = [0, 1]$.
At step $n \ge 1$, the set $C_{n-1}$ is a union of $2^{n-1}$ disjoint closed intervals.
Remove from the middle of each of them an open interval of length $4^{-n}$, and call the result $C_n$.
The Smith–Volterra–Cantor set is $S = \bigcap_{n \ge 0} C_n$.
Then $S$ is a [[closed set|0ZCK8DQYN1]], it is [[nowhere dense|0VQYCCQVJ5]] in $\R$, and its [[Lebesgue measure|2Z2QVWZ262]] is $1/2$.

## Remarks

Step $1$ removes $(3/8, 5/8)$ and leaves $[0, 3/8] \cup [5/8, 1]$.
By induction, each of the $2^n$ intervals of $C_n$ has length $2^{-n-1} + 2^{-2n-1}$.
This is more than $4^{-n-1}$, so each removal is possible.
The total length removed is
$$\sum_{n=1}^{\infty} 2^{n-1} \cdot 4^{-n} = \frac{1}{4} \sum_{n=0}^{\infty} 2^{-n} = \frac{1}{2},$$
so $\lambda(S) = 1 - 1/2 = 1/2$.
The set $S$ is closed as an intersection of closed sets.
These lengths tend to $0$, so $S$ contains no interval; a closed set with empty interior is nowhere dense.
So a nowhere dense set can have positive measure, unlike the middle-thirds [[Cantor set|0BXNDZFQME]], which has measure $0$.
The indicator function of $S$ is bounded and discontinuous at every point of $S$, a set of positive measure, so it is not Riemann integrable.

## Explanations

### L1 human

The ordinary Cantor set removes a third of each interval at every step and ends with total length $0$.
The Smith–Volterra–Cantor set removes much smaller gaps, of length $1/4$, then $1/16$, then $1/64$, and so on.
The gaps still reach everywhere, so the set contains no interval at all.
Yet the gaps only add up to length $1/2$, so the remaining dust of points still has total length $1/2$.
