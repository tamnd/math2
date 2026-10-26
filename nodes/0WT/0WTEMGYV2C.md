---
tag: 0WTEMGYV2C
kind: statement
role: theorem
name: Cantor's theorem
msc: ["03E10"]
uses: [0BC7KX51Z8, 0XKH881BZ7, 0JTGRV4WT4]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor's_theorem
    locator: lead section
same_as:
  wikidata: Q474881
  wikipedia: Cantor's theorem
---

## Statement

Let $A$ be a [[set|0SJ3RX9TXA]] and let $f \colon A \to \mathcal{P}(A)$ be a [[function|0XHDTE5YMZ]] to the [[power set|0BC7KX51Z8]] of $A$.
Then $f$ is not [[surjective|0XKH881BZ7]].
So $|A| < |\mathcal{P}(A)|$.

## Remarks

Proof: let $D = \{a \in A \mid a \notin f(a)\}$. If $D = f(d)$ for some $d \in A$, then $d \in D$ if and only if $d \notin D$, a contradiction.
The map $a \mapsto \{a\}$ is an injection, so $|A| \le |\mathcal{P}(A)|$, and the inequality is strict.
It follows that there is no largest cardinal. The proof is a form of the [[diagonal argument|0XCH8QVDCQ]], and it is close to [[Russell's paradox|0HESMMSYEG]].

## Explanations

### L1 human

For each set, its set of subsets is strictly larger.
For a set with $3$ elements, this is $3 < 8$.
For infinite sets, it gives an endless tower of larger and larger infinities.
