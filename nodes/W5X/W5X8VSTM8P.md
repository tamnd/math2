---
tag: W5X8VSTM8P
kind: statement
role: fact
name: Horton's laws of stream networks
msc: [86A05, 05C05]
uses: [0Y0JGC2K9T, 062D9KXJB1]
about: [2XGF4FECN5]
sources:
  - url: https://en.wikipedia.org/wiki/Strahler_number
---

## Statement

Model a river network as a [[rooted tree|0Y0JGC2K9T]] whose root is the outlet and whose leaves are the sources.
Give each edge its Strahler order, and give source streams order $1$.
Where streams meet, let $k$ be the largest order of the streams above.
The stream below has order $k$ if only one stream above has order $k$, and order $k + 1$ if two or more do.
A stream of order $\omega$ is a maximal path of edges of order $\omega$.
Let $\Omega$ be the order of the outlet stream.
For $1 \le \omega \le \Omega$, let $N_\omega$ be the number of streams of order $\omega$.
Let $\bar L_\omega$ be their mean length and $\bar A_\omega$ the mean area that they drain.
For natural river networks the following hold approximately.

1. Law of stream numbers: the bifurcation ratio $R_B = N_\omega / N_{\omega+1}$ is nearly the same for all $\omega$, so $N_\omega \approx R_B^{\Omega - \omega}$.
2. Law of stream lengths: the ratio $R_L = \bar L_{\omega+1} / \bar L_\omega$ is nearly the same for all $\omega$.
3. Law of stream areas: the ratio $R_A = \bar A_{\omega+1} / \bar A_\omega$ is nearly the same for all $\omega$.

## Remarks

These are empirical laws found by measuring real basins, not theorems; the third law is often attributed to Schumm rather than Horton.
Observed bifurcation ratios usually lie between about $3$ and $5$.
Take the perfect binary [[tree|062D9KXJB1]] of depth $k$, with one outlet edge attached at the root.
Every branching joins two streams of equal order.
So the outlet stream has order $k + 1$ and $N_\omega = 2^{k + 1 - \omega}$, and the law of stream numbers holds exactly with $R_B = 2$.
Random tree models of river networks also produce the law of stream numbers, which suggests that it reflects the statistics of branching trees more than the physics of erosion.

## Explanations

### L1 human

Small streams join into larger ones, and larger ones join into rivers.
Horton's laws say that, going up one step in this hierarchy, the number of streams drops by roughly the same factor each time.
At the same time, their length and drained area grow by roughly fixed factors.
So a river network looks like a geometric sequence of levels.

### L2 human

The Strahler order is a purely combinatorial invariant of a rooted tree, and the laws are statements about how the counts per order decay.
Because the ratios are constant, plots of $\log N_\omega$, $\log \bar L_\omega$ and $\log \bar A_\omega$ against $\omega$ are close to straight lines.
Their slopes give $R_B$, $R_L$ and $R_A$.
Combining the laws of lengths and areas leads to power laws between stream length and drained area, such as [[Hack's law|3T47DSDX7S]], and to fractal descriptions of river networks.
