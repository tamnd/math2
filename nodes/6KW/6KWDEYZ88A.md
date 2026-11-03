---
tag: 6KWDEYZ88A
kind: concept
name: Online algorithm and competitive analysis
msc: [68W27, 68W40, 68Q25]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Competitive_analysis_(online_algorithm)
  - url: https://en.wikipedia.org/wiki/Online_algorithm
---

## Summary

An online algorithm receives its input one piece at a time and must act on each piece before it sees the next one.
Competitive analysis measures such an [[algorithm|9DMSG5HAQX]] by comparing its cost with the cost of an optimal offline algorithm that knows the whole input in advance.
The worst ratio of the two costs, over all inputs, is the competitive ratio.
Standard examples are paging, where the least-recently-used rule is $k$-competitive for a cache of $k$ pages, and the ski rental problem.

## Explanations

### L1 human

You go skiing but do not know how many days you will go.
Renting costs $1$ per day and buying costs $B$; with hindsight you would rent if you ski fewer than $B$ days and buy otherwise.
A sensible plan is to rent for $B - 1$ days and buy on day $B$ if you are still skiing.
This plan never pays more than about twice what the best plan in hindsight would pay, whatever the number of days.
Competitive analysis makes such "at most $c$ times the best" guarantees precise.
