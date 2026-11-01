---
tag: BD1CNVV5P0
kind: statement
role: lemma
name: Varadhan's lemma
msc: [60F10]
uses: [0CQHFPGJ45, 059TJN0NZ1, MNPWBBNCAD, 140N2PQSTE, 0X3WGX95FE, 0R3H5PANRQ]
about: [Q702WCDQQ3]
sources:
  - url: https://en.wikipedia.org/wiki/Varadhan%27s_lemma
same_as:
  wikidata: Q7915395
  wikipedia: Varadhan's lemma
---

## Statement

Let $\mathcal{X}$ be a [[topological space|0CQHFPGJ45]], and let $(\mu_n)$ be a sequence of [[probability measures|059TJN0NZ1]] on $\mathcal{X}$.
Assume that $(\mu_n)$ satisfies the [[large deviation principle|MNPWBBNCAD]] with a good [[rate function|140N2PQSTE]] $I$.
Let $\varphi \colon \mathcal{X} \to \R$ be a [[continuous|0X3WGX95FE]] function that is bounded above.
Then
$$\lim_{n \to \infty} \frac{1}{n} \log \int_{\mathcal{X}} e^{n \varphi(x)} \, \mu_n(dx) = \sup_{x \in \mathcal{X}} \bigl(\varphi(x) - I(x)\bigr).$$

## Remarks

The lemma is an infinite-dimensional form of Laplace's method: the integral is dominated by the neighbourhood of the point where $\varphi - I$ is largest.
For the lower bound, take $x$ with $I(x) < \infty$ and a small open neighbourhood $G$ of $x$ on which $\varphi > \varphi(x) - \delta$; the large deviation lower bound gives $\mu_n(G) \ge e^{-n(I(x) + \delta)}$ for large $n$.
For the upper bound, cover a compact sublevel set of $I$ by finitely many small closed neighbourhoods.
Use the large deviation upper bound on each, and the bound on $\varphi$ outside.

The boundedness of $\varphi$ from above can be replaced by the tail condition
$$\lim_{M \to \infty} \limsup_{n \to \infty} \frac{1}{n} \log \int_{\set{\varphi \ge M}} e^{n \varphi} \, d\mu_n = -\infty.$$
Some such condition is needed, since otherwise rare but huge values of $e^{n\varphi}$ can dominate the integral.

Example: let $\mu_n$ be the normal law with mean $0$ and variance $1/n$, with $I(x) = x^2/2$, and let $\varphi(x) = -\abs{x - 1}$.
The lemma gives the limit $\sup_x (-\abs{x - 1} - x^2/2) = -1/2$, attained at $x = 1$.

## Explanations

### L1 human

Suppose a random quantity is very unlikely to be far from typical, with a known exponential cost $I$.
If you reward each outcome $x$ by an exponential weight $e^{n \varphi(x)}$, then the average reward grows or decays at the rate $\max(\varphi - I)$.
The winner is the outcome with the best balance between reward and probability cost.

### L2 human

Varadhan's lemma is the main tool to compute free energies and other exponential averages once a large deviation principle is known.
In statistical mechanics, the limit is the pressure and the maximisers of $\varphi - I$ are the equilibrium states.
Its converse, Bryc's theorem, recovers a large deviation principle from the limits of such exponential integrals.
