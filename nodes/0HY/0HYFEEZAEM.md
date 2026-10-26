---
tag: 0HYFEEZAEM
kind: statement
role: proposition
name: Injective iff it has a left inverse
msc: ["03E20"]
uses: [0PVG1CRAJN, 02486SD328]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_function
    locator: Left inverses
---

## Statement

Let $A$ be a nonempty set, let $B$ be a set and let $f \colon A \to B$ be a [[function|0XHDTE5YMZ]].
Then $f$ is [[injective|0PVG1CRAJN]] if and only if $f$ has a [[left inverse|02486SD328]].

## Remarks

The hypothesis that $A$ is nonempty is necessary. The empty function from $\varnothing$ to a nonempty set is injective, but there is no function from a nonempty set to $\varnothing$.
To build a left inverse, fix $a_0 \in A$. Send each $b = f(a)$ to $a$, and send each $b \notin f(A)$ to $a_0$.

## Explanations

### L1 human

An injective function loses no information, so you can go back from each value to its unique input.
The values that $f$ never takes can go anywhere, and you need one point $a_0$ to send them to.
