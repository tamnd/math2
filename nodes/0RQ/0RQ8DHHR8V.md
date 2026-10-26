---
tag: 0RQ8DHHR8V
kind: statement
role: theorem
name: Cantor set is homeomorphic to the space of binary sequences
msc: [54F65]
uses: [0BXNDZFQME, 04S9HX3GAP, 0430ETCMKD, 0JTRSJKCFB]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor_space
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Cantor_space
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Cantor_space
    locator: Characterization
---

## Statement

Let $\{0, 1\}$ have the [[discrete topology|0S2TEHX4E1]] and let $\{0, 1\}^{\mathbb{N}}$ have the [[product topology|04S9HX3GAP]].
Then the map
$$\varphi \colon \{0, 1\}^{\mathbb{N}} \to C, \qquad \varphi((a_n)_{n \ge 1}) = \sum_{n \ge 1} \frac{2 a_n}{3^n}$$
is a [[homeomorphism|05GZ11PWRY]] onto the [[Cantor set|0BXNDZFQME]] $C$.

## Remarks

The map is a bijection, because each point of $C$ has exactly one base-3 expansion with digits in $\{0, 2\}$.
It is continuous: if two sequences agree in their first $N$ terms, their images differ by at most $3^{-N}$.
The space $\{0, 1\}^{\mathbb{N}}$ is compact by [[Tychonoff's theorem|0JTRSJKCFB]], and $C$ is Hausdorff. Thus $\varphi$ is a homeomorphism, by [[this theorem|0430ETCMKD]].
A space homeomorphic to $C$ is a Cantor space. By a theorem of Brouwer, these are exactly the nonempty compact metrizable spaces that are totally disconnected and have no isolated points.

## Explanations

### L1 human

Each point of the Cantor set is described by an infinite list of choices: left or right third, at each step.
These lists are the binary sequences, and the topology of the Cantor set matches the product topology on them.
