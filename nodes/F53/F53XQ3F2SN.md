---
tag: F53XQ3F2SN
kind: statement
role: theorem
name: Blum's speedup theorem
msc: [68Q15, 03D15]
uses: [KZSB5E471K, 758EYCN27B]
about: [KZSB5E471K]
sources:
  - url: https://en.wikipedia.org/wiki/Blum%27s_speedup_theorem
same_as:
  wikidata: Q1751105
  wikipedia: Blum's speedup theorem
---

## Statement

Let $\varphi_0, \varphi_1, \ldots$ be an acceptable numbering of the partial [[computable functions|KZSB5E471K]] $\N \to \N$.
Let $\Phi_0, \Phi_1, \ldots$ be a Blum complexity measure for it: each $\Phi_i$ is a partial function $\N \to \N$ such that

1. $\Phi_i(x)$ is defined if and only if $\varphi_i(x)$ is defined;
2. the set of triples $(i, x, m)$ with $\Phi_i(x) = m$ is decidable.

Let $r \colon \N \times \N \to \N$ be a total computable function.
Then there is a total computable function $f \colon \N \to \set{0, 1}$ with the following property.
For every index $i$ with $\varphi_i = f$ there is an index $j$ with $\varphi_j = f$ and
$$r\big(x, \Phi_j(x)\big) \le \Phi_i(x) \quad \text{for all but finitely many } x.$$

## Remarks

The running time of a [[Turing machine|758EYCN27B]] program, $\Phi_i(x)$ = the number of steps of program $i$ on input $x$, is a Blum complexity measure, and so is the space used.
For example, take $r(x, t) = 2^t$.
The theorem gives a function $f$ such that every program for $f$ can be replaced by another program for $f$ that is exponentially faster on almost all inputs.
So $f$ has no fastest program, even up to a large factor.
The proof is a diagonal construction that cancels programs which run too fast on chosen inputs.
The function $f$ built in the proof is artificial, and the theorem says nothing about natural problems.

## Explanations

### L1 human

One might expect every computable problem to have a best algorithm, perhaps up to small changes.
Manuel Blum showed in 1967 that this fails: some problems can be sped up again and again.
Any program for such a problem can be beaten by another program, which in turn can be beaten, without end.
The speedup can be as large as one likes, for example exponential.

### L2 human

The theorem works for any Blum complexity measure, so it is a fact about abstract complexity, not about Turing machines in particular.
It shows that the complexity of a function cannot always be defined as the cost of a best program.
Complexity classes are therefore defined by resource bounds, as in the [[time hierarchy theorem|A6D1D67GHA]], rather than by optimal algorithms.
The gap theorem of Borodin is another result of abstract complexity theory with a similar flavour.
