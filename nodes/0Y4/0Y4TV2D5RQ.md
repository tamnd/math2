---
tag: 0Y4TV2D5RQ
kind: statement
role: theorem
name: Brooks' theorem
msc: [05C15]
uses: [0KNAN9F27P, 0C5M7AM6FH]
sources:
  - url: https://en.wikipedia.org/wiki/Brooks'_theorem
    locator: Formal statement
same_as:
  wikidata: Q512897
  wikipedia: "Brooks' theorem"
---

## Statement

Let $G$ be a finite connected simple [[graph|0JD5C82QMB]] with [[maximum degree|0KNAN9F27P]] $\Delta$.
Suppose that $G$ is not a [[complete graph|03WKB2H474]] and not a [[cycle graph|0QQ0F12962]] of odd length.
Then $\chi(G) \le \Delta$.

## Remarks

A [[greedy colouring|04AAKZNXHD]] gives $\chi(G) \le \Delta + 1$ for every graph. Brooks' theorem improves this bound by $1$ in all other cases.
The two exceptions need $\Delta + 1$ colours: $\chi(K_n) = n$ with $\Delta = n - 1$, and an odd cycle has $\chi = 3$ with $\Delta = 2$.

## History

R. Leonard Brooks published the theorem in 1941.

## Explanations

### L1 human

If each vertex has at most $\Delta$ neighbours, then $\Delta + 1$ colours are always enough.
Brooks' theorem says that $\Delta$ colours are enough, except for complete graphs and odd cycles.
