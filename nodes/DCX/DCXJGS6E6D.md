---
tag: DCXJGS6E6D
kind: statement
role: theorem
name: FKG inequality
msc: ["60E15", 06D99, 05D05]
uses: [0HM0HQCK6N, 0A7KV2WB7A, 4085B8A528, W1YH3YD3S4]
about: [0HM0HQCK6N]
sources:
  - url: https://en.wikipedia.org/wiki/FKG_inequality
same_as:
  wikidata: Q1784730
  wikipedia: FKG inequality
---

## Statement

Let $L$ be a finite [[distributive lattice|0HM0HQCK6N]] with join $\vee$ and meet $\wedge$.
Let $\mu \colon L \to [0, \infty)$ be log-supermodular, that is, $\mu(x \vee y) \, \mu(x \wedge y) \ge \mu(x) \, \mu(y)$ for all $x, y \in L$.
Let $f, g \colon L \to \R$ be [[increasing|0A7KV2WB7A]]: $x \le y$ implies $f(x) \le f(y)$ and $g(x) \le g(y)$.
Then
$$\Big( \sum_{x \in L} f(x) g(x) \mu(x) \Big) \Big( \sum_{x \in L} \mu(x) \Big) \ge \Big( \sum_{x \in L} f(x) \mu(x) \Big) \Big( \sum_{x \in L} g(x) \mu(x) \Big).$$

## Remarks

When $\mu$ is a probability measure, the inequality reads $\mathbb{E}[f g] \ge \mathbb{E}[f] \, \mathbb{E}[g]$: increasing functions are positively correlated.
It follows from the [[Ahlswede–Daykin inequality|4085B8A528]].
Adding a constant to $f$ or to $g$ does not change the difference of the two sides, so one may assume $f, g \ge 0$.
Then the four functions $f \mu$, $g \mu$, $f g \mu$ and $\mu$ satisfy $f(x) \mu(x) \, g(y) \mu(y) \le f(x \vee y) g(x \vee y) \mu(x \vee y) \, \mu(x \wedge y)$, by monotonicity and log-supermodularity, and Ahlswede–Daykin with both sets equal to $L$ gives the result.

Example: a product measure on the lattice of subsets of $\set{1, \ldots, n}$ satisfies the hypothesis with equality, and the theorem becomes the [[Harris inequality|W1YH3YD3S4]].
If $f$ is increasing and $g$ is decreasing, the inequality reverses.
Log-supermodularity cannot be dropped.
On $\set{0, 1}^2$, the measure giving mass $1/2$ to each of $(1, 0)$ and $(0, 1)$ is not log-supermodular.
For it, the increasing indicators of $\set{x_1 = 1}$ and $\set{x_2 = 1}$ are negatively correlated.

## Explanations

### L1 human

Imagine random configurations in which "more" of one thing tends to come with "more" of another.
The FKG inequality makes this precise: if the weights favour combining configurations, then any two increasing quantities are positively correlated.
For instance, in a random graph, being connected and containing a triangle tend to happen together.

### L2 human

The inequality was proved by Fortuin, Kasteleyn and Ginibre for models of statistical mechanics such as the Ising model with ferromagnetic interactions, whose Gibbs measures are log-supermodular.
In combinatorics and probability it is used to compare probabilities of monotone events in random graphs and percolation.
The Harris inequality is its product-measure case, and the Holley inequality is a two-measure generalization.
The XYZ inequality for linear extensions of posets is proved with it.
