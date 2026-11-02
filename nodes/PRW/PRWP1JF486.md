---
tag: PRWP1JF486
kind: statement
role: theorem
name: Alexander's theorem on closed braids
msc: [57K10, 20F36]
uses: [1A5WRCNTM3, BNR4H5GCTP]
about: [1A5WRCNTM3, BNR4H5GCTP]
sources:
  - url: https://en.wikipedia.org/wiki/Braid_group
---

## Statement

Let $L$ be a tame oriented [[link|1A5WRCNTM3]] in $\R^3$.
Then there are an integer $n \ge 1$ and a braid $\beta$ in the [[braid group|BNR4H5GCTP]] $B_n$ with this property.
The link $L$ is ambient isotopic, as an oriented link, to the closure $\hat\beta$ of $\beta$.
Here $\hat\beta$ is obtained from a picture of $\beta$ in a cylinder in the following way.
The top end of each strand is joined to the bottom end in the same position, outside the cylinder and without new crossings.
All strands are oriented downward.

## Remarks

The idea of the proof is to choose an axis and to make the link wind around it in one direction.
Take a polygonal diagram of $L$ and a point $O$ of the plane off the diagram.
Each edge that runs clockwise around $O$ can be replaced by two edges that pass on the other side of $O$, so that they run counterclockwise.
After finitely many such moves every edge runs counterclockwise around $O$, and cutting along a ray from $O$ shows the link as a closed braid.
For example, the trefoil knot is the closure of $\sigma_1^3$ in $B_2$, and the Hopf link is the closure of $\sigma_1^2$ in $B_2$.
The braid $\beta$ is far from unique; the [[Markov theorem|7F3QQQ63WR]] says exactly when two braids have the same closure.

## Explanations

### L1 human

Every knot or link can be drawn as a braid whose ends are joined around the back.
Imagine a pole through the middle of the knot: you can move the string so that it always goes around the pole in the same direction.
Then the string looks like a braid that has been wrapped into a ring.

### L2 human

The theorem turns questions about links into questions about the braid groups $B_n$, which are groups with simple presentations.
Together with the [[Markov theorem|7F3QQQ63WR]], it shows that a link invariant is the same as a function on all braid groups that is unchanged by the two Markov moves.
This is how Jones first found the [[Jones polynomial|4SPC17FPXE]], from traces on representations of braid groups.
The least $n$ for which $L$ is a closed $n$-braid is called the braid index of $L$.
