---
tag: 0W7NFW23RF
kind: definition
name: Sample space
msc: [60A05]
defines: 0SWXJHKJ02
uses: [0HM05N3FJD, 0SJ3RX9TXA]
sources:
  - url: https://en.wikipedia.org/wiki/Sample_space
    locator: Conditions of a sample space
inventory: [2GM8TWCDZ6]
---

## Definition

Let $E$ be a [[random experiment|0HM05N3FJD]].
A sample space of $E$ is a nonempty [[set|0SJ3RX9TXA]] $\Omega$ with two properties.
Each performance of $E$ gives exactly one element of $\Omega$.
Each element of $\Omega$ is a possible result of $E$.
The usual notation for a sample space is $\Omega$ or $S$.

## Remarks

The elements of $\Omega$ are mutually exclusive: two different elements cannot both be the result of one trial. They are also collectively exhaustive: some element is always the result.
For one toss of a coin, $\Omega = \{H, T\}$. For two rolls of a die, $\Omega = \{1, \dots, 6\}^2$ has $36$ elements.
One experiment can have more than one sample space. For a card drawn from a deck, $\Omega$ can be the set of $52$ cards or the set of the $4$ suits.
A sample space can be finite, countably infinite or uncountable. The time until a lamp fails has the sample space $[0, \infty)$.

## Explanations

### L1 human

The sample space is the list of everything that can happen in the experiment.
For a die, the list is $1, 2, 3, 4, 5, 6$. Every question about the die is then a question about this list.
