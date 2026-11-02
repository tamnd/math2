---
tag: XDK73D2DEA
kind: definition
name: Metric outer measure
msc: [28A12, 28A78]
defines: 3T6WG315GC
uses: [BJ314H17HC, 0VKD1TP7F3, 0QF1MZ9FRG]
sources:
  - url: https://en.wikipedia.org/wiki/Metric_outer_measure
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]].
For nonempty $A, B \subseteq X$ let $d(A, B) = \inf \set{ d(a, b) : a \in A, \ b \in B }$, an [[infimum|0QF1MZ9FRG]].
A *metric outer measure* on $X$ is an [[outer measure|BJ314H17HC]] $\mu^*$ on $X$ such that
$$\mu^*(A \cup B) = \mu^*(A) + \mu^*(B) \quad \text{whenever } A, B \subseteq X \text{ are nonempty with } d(A, B) > 0.$$

## Remarks

Example: Lebesgue outer measure $\lambda^*$ on $\R^n$ is a metric outer measure.
Let $d(A, B) = \delta > 0$.
A cover of $A \cup B$ by boxes can be refined into boxes of diameter less than $\delta$, and then no box meets both $A$ and $B$.
So the cover splits into a cover of $A$ and a cover of $B$, which gives $\ge$; subadditivity gives $\le$.
Non-example: on $\R$, put $\mu^*(\varnothing) = 0$ and $\mu^*(A) = 1$ for every nonempty $A$.
This is an outer measure, but $\mu^*(\set{0, 1}) = 1 \ne \mu^*(\set{0}) + \mu^*(\set{1})$ although $d(\set{0}, \set{1}) = 1 > 0$.
Carathéodory's theorem on metric outer measures: an outer measure on a metric space is a metric outer measure if and only if every Borel set is Carathéodory measurable for it.
