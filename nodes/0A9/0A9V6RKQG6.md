---
tag: 0A9V6RKQG6
kind: statement
role: theorem
name: Schröder–Bernstein theorem
aliases: [cantor-bernstein-theorem, cantor-schroeder-bernstein-theorem]
msc: ["03E10"]
uses: [0PVG1CRAJN, 0SNQEF7Z53]
sources:
  - url: https://en.wikipedia.org/wiki/Schröder–Bernstein_theorem
    locator: lead section
same_as:
  wikidata: Q1033910
  wikipedia: Schröder–Bernstein theorem
---

## Statement

Let $A$ and $B$ be [[sets|0SJ3RX9TXA]].
If there are [[injective functions|0PVG1CRAJN]] $f \colon A \to B$ and $g \colon B \to A$, then there is a [[bijective function|0SNQEF7Z53]] $h \colon A \to B$.

## Remarks

In terms of cardinals: $|A| \le |B|$ and $|B| \le |A|$ imply $|A| = |B|$. So the [[order of cardinals|01GTP8M5RG]] is antisymmetric.
The proof does not use the axiom of choice.
Example: $[0, 1]$ and $[0, 1)$ are equinumerous, because each one injects into the other.

## History

Cantor stated the theorem in 1887 without a proof.
Dedekind proved it in 1887, but he did not publish the proof.
Bernstein and Schröder published proofs in 1898, and the proof of Schröder had a flaw.

## Explanations

### L1 human

If $A$ fits into $B$ and $B$ fits into $A$, then $A$ and $B$ have the same size.
For finite sets this is obvious, but for infinite sets it needs a clever construction of $h$.
