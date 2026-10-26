---
tag: ~ade6bb45
kind: statement
role: theorem
name: Bolzano–Weierstrass theorem
msc: [40A05]
uses: [~0a464768, ~aa16cf88, ~d628ad87, ~ee839429, ~471ab2b3]
sources:
  - url: https://en.wikipedia.org/wiki/Bolzano–Weierstrass_theorem
    locator: Proof
same_as:
  wikidata: Q468391
  wikipedia: Bolzano–Weierstrass theorem
---

## Statement

Let $(a_n)$ be a [[bounded sequence|~0a464768]] of real numbers.
Then $(a_n)$ has a [[subsequence|~aa16cf88]] that converges to a real number.

## Remarks

The proof takes a [[monotone subsequence|~ee839429]]. It is bounded, so it converges by the [[monotone convergence theorem|~471ab2b3]].
The limit of the subsequence lies in each closed interval $[m, M]$ that contains all terms, by [[the preservation of non-strict inequalities|~e2316639]].
The theorem holds in $\mathbb{R}^k$ for each $k$. It says that each closed and bounded subset of $\mathbb{R}^k$ is sequentially compact.
The theorem fails in $\mathbb{Q}$. The decimal approximations of $\sqrt{2}$ are bounded, and no subsequence has a limit in $\mathbb{Q}$.

## History

Bernard Bolzano proved the result in 1817, as a lemma for the intermediate value theorem. Karl Weierstrass proved it again about fifty years later and made it a central tool of analysis.

## Explanations

### L1 human

A bounded sequence cannot run away, so its terms must crowd together somewhere.
The theorem picks infinitely many terms that approach one point of crowding.
For $(-1)^n$, the even terms form a subsequence that converges to $1$.
