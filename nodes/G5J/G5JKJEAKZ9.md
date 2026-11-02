---
tag: G5JKJEAKZ9
kind: statement
role: theorem
name: Thie's theorem on multiplicity
msc: [32U25, 32C30]
uses: [WVB60RKC3Z, GB7M582M5Y, AN0BYRKNRA, ZW5A88PCPK, 360H7MD9RD]
about: [WVB60RKC3Z, GB7M582M5Y]
sources:
  - url: https://en.wikipedia.org/wiki/Lelong_number
---

## Statement

Let $\Omega \subseteq \C^n$ be open, let $A \subseteq \Omega$ be an [[analytic subset|GB7M582M5Y]] of pure [[dimension|AN0BYRKNRA]] $p \ge 1$ and let $x \in A$.
Let $\pi \colon \C^n \to \C^p$ be a generic complex linear map.
Then the restriction of $\pi$ to $A$ near $x$ is a branched covering of a neighbourhood of $\pi(x)$.
Let $m_x(A)$ be its number of sheets, the multiplicity of $A$ at $x$.
Let $\operatorname{vol}_{2p}$ denote the $2p$-dimensional volume of the set of [[regular points|ZW5A88PCPK]] of $A$.
Then
$$\lim_{r \to 0^+} \frac{\operatorname{vol}_{2p}\bigl(A \cap B(x, r)\bigr)}{\pi^p r^{2p} / p!} = m_x(A).$$
In other words, the [[Lelong number|WVB60RKC3Z]] at $x$ of the [[current|360H7MD9RD]] of integration $[A]$ equals $m_x(A)$.

## Remarks

The denominator $\pi^p r^{2p} / p!$ is the volume of a ball of radius $r$ in $\C^p = \R^{2p}$.
The proof uses a generic linear projection $\pi$, under which $A$ covers a neighbourhood of $\pi(x)$ with $m_x(A)$ sheets.
It then compares, as $r \to 0$, the volume of the part of each sheet near $x$ with the volume of its image in $\C^p$.

Example: $A = \set{z_1 z_2 = 0} \subseteq \C^2$ is the union of two lines through $0$.
The set $A \cap B(0, r)$ is two discs of area $\pi r^2$, so the ratio is $2$, and indeed a generic projection to $\C$ has two sheets.
At a regular point the multiplicity is $1$, and the ratio tends to $1$.

## Explanations

### L1 human

Near a singular point, an analytic set may look like several sheets passing through the same point.
The multiplicity counts these sheets.
The theorem says that one can count them by measuring area.
The area of the set inside a small ball is about the number of sheets times the area of a flat disc of the same radius.

### L2 human

The theorem links an algebraic invariant, the multiplicity of the local ring of $A$ at $x$, with a metric invariant, the density of $[A]$.
It is the reason why the points of multiplicity at least $c$ appear as upper level sets of Lelong numbers.
It is also the model case for Lelong numbers of general closed positive currents.
