---
tag: 07EH4R3RVQ
kind: statement
role: proposition
name: Composition of surjections is surjective
aliases: [surjective-comp]
msc: ["03E20"]
uses: [0XKH881BZ7, 07HF9YCWPP]
sources:
  - url: https://en.wikipedia.org/wiki/Surjective_function
    locator: Composition and decomposition
---

## Statement

Let $f \colon A \to B$ and $g \colon B \to C$ be [[surjective functions|0XKH881BZ7]].
Then the [[composition|07HF9YCWPP]] $g \circ f \colon A \to C$ is surjective.

## Remarks

Proof: let $c \in C$. Since $g$ is surjective, $c = g(b)$ for some $b \in B$. Since $f$ is surjective, $b = f(a)$ for some $a \in A$. Then $c = (g \circ f)(a)$.
A partial converse holds: if $g \circ f$ is surjective, then $g$ is surjective. The function $f$ need not be surjective.
Together with [[the result for injections|01FPXMTBX1]], this shows that a composition of [[bijections|0SNQEF7Z53]] is a bijection.

## Explanations

### L1 human

To reach a point $c$ of $C$, first find a point of $B$ that $g$ sends to $c$.
Then find a point of $A$ that $f$ sends to that point of $B$.
