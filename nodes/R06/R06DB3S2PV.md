---
tag: R06DB3S2PV
kind: statement
role: theorem
name: Space hierarchy theorem
msc: [68Q15]
uses: [FDNFGKEEJR, VRZ9H4EZ6V, 7RH189REV7, T9NTRY93ZT, PFKWV5SFF5]
about: [FDNFGKEEJR]
sources:
  - url: https://en.wikipedia.org/wiki/Space_hierarchy_theorem
same_as:
  wikidata: Q7572588
  wikipedia: Space hierarchy theorem
---

## Statement

Let $f \colon \N \to \N$ be a function with $f(n) \ge \log_2 n$ for all $n \ge 1$.
Suppose that $f$ is space-constructible, that is, the binary form of $f(n)$ can be computed from $1^n$ in $O(f(n))$ space.
Then there is a language that a deterministic Turing machine decides in space $O(f(n))$ but that no deterministic Turing machine decides in space $o(f(n))$.
In terms of [[space complexity|FDNFGKEEJR]], $\mathrm{DSPACE}(g(n)) \subsetneq \mathrm{DSPACE}(f(n))$ for every function $g$ with $g(n) = o(f(n))$.

## Remarks

The proof is a diagonalization.
A machine $D$, on input $w$, marks off $f(\abs{w})$ cells and simulates the machine encoded by $w$ on $w$ within that space.
It then answers the opposite.
A machine using space $o(f(n))$ is simulated within the bound on long enough inputs, so it cannot decide the same language as $D$.
Richard Stearns, Juris Hartmanis and Philip Lewis proved the theorem in 1965.

Consequences: $\mathrm{L} \subsetneq \mathrm{PSPACE}$, where L is the class [[L|VRZ9H4EZ6V]] and PSPACE is the class [[PSPACE|T9NTRY93ZT]].
By [[Savitch's theorem|PFKWV5SFF5]], [[NL|7RH189REV7]] lies in $\mathrm{DSPACE}((\log n)^2)$, so also $\mathrm{NL} \subsetneq \mathrm{PSPACE}$.
The space-constructibility hypothesis is needed: without it, the Borodin gap theorem gives functions $f$ with $\mathrm{DSPACE}(f(n)) = \mathrm{DSPACE}(2^{f(n)})$.

## Explanations

### L1 human

More memory lets a computer solve more problems.
For any reasonable bound $f$, some problem can be solved with memory about $f(n)$ but not with noticeably less.
So the space classes form a strict ladder.

### L2 human

The space hierarchy is tighter than the time hierarchy, because simulating a machine costs only a constant factor in space but a logarithmic factor in time.
It is one of the few unconditional separations of complexity classes.
It shows that at least one of the inclusions $\mathrm{L} \subseteq \mathrm{P} \subseteq \mathrm{NP} \subseteq \mathrm{PSPACE}$ is strict, though it does not say which.
