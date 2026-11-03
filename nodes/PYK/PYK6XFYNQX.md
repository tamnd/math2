---
tag: PYK6XFYNQX
kind: concept
name: Hopcroft–Karp algorithm
msc: [05C70, 05C85, 68W40]
sources:
  - url: https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm
same_as:
  wikidata: Q1516988
  wikipedia: Hopcroft–Karp algorithm
---

## Summary

The Hopcroft–Karp algorithm finds a maximum [[matching|0MJ04A50QW]] in a [[bipartite graph|0ZVQKTRKVQ]].
Like simpler methods, it enlarges the matching along augmenting paths, but in each phase it uses many shortest augmenting paths at once.
Only $O(\sqrt{n})$ phases are needed, which gives the running time $O(m \sqrt{n})$ on $n$ vertices and $m$ edges.

## Explanations

### L1 human

Suppose some workers can each do certain jobs, and every job needs one worker.
A matching pairs workers with jobs they can do, using each worker and each job at most once.
An augmenting path is a chain of swaps that frees room for one more pair: it starts at an idle worker and ends at an open job.
The algorithm finds the shortest such chains, applies as many non-overlapping ones as it can at once, and repeats.
For two workers who can both do job $1$, and one of them also job $2$, the algorithm ends with both workers busy.
