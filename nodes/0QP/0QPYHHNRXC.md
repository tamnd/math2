---
tag: 0QPYHHNRXC
kind: statement
role: theorem
name: Von Dyck's theorem
msc: [20F05]
uses: [0QZCY9PE3Q, 0CDWKDYWN6, 0GJ83E78A5, 0HV9Y7WG5R]
sources:
  - url: https://en.wikipedia.org/wiki/Presentation_of_a_group
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Free_group
    locator: Universal property
---

## Statement

Let $G = \langle S \mid R \rangle$, let $H$ be a [[group|G5S1M9]], and let $f \colon S \to H$ be a function.
Let $\varphi \colon F_S \to H$ be the homomorphism with $\varphi(s) = f(s)$ for each $s \in S$.
If $\varphi(r) = e$ for each $r \in R$, then there is exactly one [[group homomorphism|0JYTG5K9Y4]] $\psi \colon G \to H$ with $\psi(s N) = f(s)$ for each $s \in S$.

## Remarks

Here $N$ is the normal closure of $R$ in $F_S$, so $G = F_S / N$.
The proof combines the [[universal property of the free group|0CDWKDYWN6]] with the [[universal property of the quotient group|0GJ83E78A5]], because $N \subseteq \ker \varphi$.
If the elements $f(s)$ generate $H$, then $\psi$ is surjective, so $H$ is a quotient of $G$.
The name refers to Walther von Dyck, who gave the first systematic study of group presentations in the early 1880s.

## Explanations

### L1 human

To map a presented group to another group, choose the images of the generators.
If these images obey all the relations, then the choice gives exactly one homomorphism.
You do not need to check anything else.
