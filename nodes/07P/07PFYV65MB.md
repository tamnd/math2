---
tag: 07PFYV65MB
kind: statement
role: theorem
name: Heine–Borel theorem
aliases: [heine-borel-theorem]
msc: ["54E45"]
uses: [00R0X1WGPX, 0G5AV9Q4RR, 0P953MG05E, 0E1MMCAY5B]
sources:
  - url: https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem
    locator: History
same_as:
  wikidata: Q253214
  wikipedia: Heine–Borel theorem
---

## Statement

Let $n \ge 1$ be an integer and give $\mathbb{R}^n$ the [[Euclidean metric|0E1MMCAY5B]].
A subset $K$ of $\mathbb{R}^n$ is [[compact|00R0X1WGPX]] if and only if $K$ is [[closed|0G5AV9Q4RR]] and [[bounded|0P953MG05E]].

## Remarks

The direct part holds in each metric space: [[compact subsets of a metric space are bounded|0R7BTEWCJ2]], and they are closed.
The converse uses the completeness of $\mathbb{R}$. A bounded set lies in a cube $[-M, M]^n$, which is compact. A closed subset of a compact set is compact.
The converse fails in general metric spaces. In the space of bounded real sequences with the sup metric, the closed unit ball is closed and bounded but not compact.
Metric spaces in which closed bounded sets are compact are the [[proper metric spaces|0Z4V98VN5E]].

## History

Dirichlet used finite subcovers of a closed interval in his 1852 lectures, to prove that continuous functions on such intervals are uniformly continuous.
Émile Borel stated and proved a version for countable covers in 1895. Cousin, Lebesgue and Schoenflies later extended it to arbitrary covers.

## Explanations

### L1 human

In $\mathbb{R}^n$, you can recognize compact sets by two easy tests: they contain their limit points and they fit in a ball.
For example, the closed disc and the sphere are compact, but the open disc and the whole plane are not.
