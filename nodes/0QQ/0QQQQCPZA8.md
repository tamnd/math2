---
tag: 0QQQQCPZA8
kind: statement
role: corollary
name: Number of odd-degree vertices is even
msc: [05C07]
uses: [0T0F6CCS9W, 0XAP8WHNES]
sources:
  - url: https://en.wikipedia.org/wiki/Handshaking_lemma
    locator: Definitions and statement
  - url: https://github.com/oscarlevin/discrete-book/blob/a8e4949bc45daf100930c1182983778f56ab689f/ptx/sec_gt-intro.ptx#L945
    locator: ptx/sec_gt-intro.ptx:945
---

## Statement

Let $G$ be a finite [[graph|0JD5C82QMB]].
Then the number of vertices of $G$ with odd [[degree|0T0F6CCS9W]] is even.

## Remarks

It follows from the [[handshaking lemma|0XAP8WHNES]]: the sum of all degrees is even, so it has an even number of odd terms.
Thus no graph has exactly one vertex of odd degree. For example, no graph has the degrees $3, 2, 2, 2$.

## Explanations

### L1 human

The total of all degrees is even, because it is twice the number of edges.
A sum of whole numbers is even only if it has an even number of odd terms.
