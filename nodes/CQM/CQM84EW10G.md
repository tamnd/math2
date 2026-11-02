---
tag: CQM84EW10G
kind: concept
name: Ultrafilter on a Boolean algebra
msc: ["06E05", "03G05"]
specializes: [Z15FXM9WM1]
sources:
  - url: https://en.wikipedia.org/wiki/Ultrafilter
---

## Summary

An ultrafilter on a [[Boolean algebra|0XADJKM699]] $B$ is a proper filter of $B$ that is maximal among proper filters.
Equivalently, it is a filter that contains exactly one of $a$ and $\neg a$ for every $a \in B$.
Ultrafilters are the same as homomorphisms from $B$ onto the two-element Boolean algebra, and they are the points of the [[Stone space|ZV38HA5PAQ]] of $B$.
For the power set of a set $X$ one gets the [[ultrafilters|J64Y3JC0RE]] on $X$.

## Explanations

### L1 human

An ultrafilter picks out the elements of a Boolean algebra that count as "true" in one consistent way of deciding everything.
It decides every element: either $a$ is true or $\neg a$ is, never both.
If $a$ and $b$ are true, so is "$a$ and $b$", and anything above a true element is true.
In the algebra of subsets of a finite set, every ultrafilter consists of the subsets that contain one fixed point.
