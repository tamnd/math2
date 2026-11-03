---
tag: ST1PFA7B8A
kind: statement
role: theorem
name: Arctic circle theorem
msc: [82B20, 05B45, 60C05]
uses: [83PJCPB9VA]
about: [83PJCPB9VA]
sources:
  - url: https://en.wikipedia.org/wiki/Aztec_diamond
---

## Statement

Let $n \ge 1$ be an integer.
The *Aztec diamond* $A_n$ of order $n$ is the union of the unit squares $[a, a+1] \times [b, b+1]$ with $a, b \in \Z$ inside the region $\abs{x} + \abs{y} \le n + 1$.
Fix a [[domino tiling|83PJCPB9VA]] of $A_n$.
Its four polar regions are the regions next to the four corners of $A_n$ in which all dominoes are parallel and form a brick-wall pattern.
The rest of $A_n$ is the temperate region.
Let $T_n$ be a domino tiling of $A_n$ chosen uniformly at random.
Let $E_{n, \varepsilon}$ be the event that the boundary of the temperate region of $T_n$, scaled by $1/n$, lies within distance $\varepsilon$ of the circle $x^2 + y^2 = 1/2$.
Then for every $\varepsilon > 0$, the probability of $E_{n, \varepsilon}$ tends to $1$ as $n \to \infty$.

## Remarks

The circle $x^2 + y^2 = 1/2$ is the circle inscribed in the square $\abs{x} + \abs{y} \le 1$, the scaled limit of $A_n$.
So with high probability the tiling is frozen outside the inscribed circle and disordered inside it.
The theorem is due to Jockusch, Propp and Shor.
Their proof uses domino shuffling, a random growth procedure that builds a uniform tiling of $A_{n+1}$ from one of $A_n$, and analyses the polar regions as an interacting particle system.
The number of domino tilings of $A_n$ is $2^{n(n+1)/2}$, a result of Elkies, Kuperberg, Larsen and Propp.
Later work found the fluctuations of the boundary, which are governed by the Airy process.

## Explanations

### L1 human

Tile a diamond-shaped region of squares with dominoes at random.
Near the four corners the dominoes line up in rigid brick patterns, as if frozen.
In the middle they point every which way.
The theorem says that for large diamonds the border between the frozen and the disordered parts is very nearly a perfect circle.

### L2 human

It is a model case for the variational principle of Cohn, Kenyon and Propp for dimer models.
It shows that boundary conditions can affect a [[dimer model|TJHVHD5SH5]] deep in the bulk, unlike many short-range models.
Similar arctic curves appear for random lozenge tilings of hexagons.
