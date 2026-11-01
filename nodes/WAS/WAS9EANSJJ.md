---
tag: WAS9EANSJJ
kind: concept
name: Random walk on a group
msc: [60B15, 60G50, 20P05]
specializes: [04VZE3FZXF]
sources:
  - url: https://en.wikipedia.org/wiki/Random_walk
---

## Summary

A random walk on a group $G$ starts at the identity and multiplies by independent random elements of $G$.
All these elements are drawn from one [[probability measure|059TJN0NZ1]] $\mu$.
It is a [[Markov chain|0G48PYM96Q]] on $G$ whose transition probabilities are invariant under the group.
When $\mu$ is uniform on a symmetric generating set, it is the simple [[random walk|04VZE3FZXF]] on the [[Cayley graph|0GYQK9NDJF]].
The long-run behaviour of the walk reflects the algebra and geometry of the group.
For example, let $G$ be finitely generated and let $\mu$ be symmetric with support generating $G$.
By a theorem of Kesten, the return probabilities then decay exponentially exactly when $G$ is not [[amenable|CEAT9BESKK]].

## Explanations

### L1 human

Picture a walker on the grid of integer points in the plane who, at each step, moves one unit north, south, east or west at random.
This is a random walk on the group $\Z^2$, and it comes back to its start with probability $1$.
Shuffling a deck of cards by repeated random swaps is a random walk on the group of permutations of the cards.
The question of how many shuffles mix the deck well is a question about this random walk.
