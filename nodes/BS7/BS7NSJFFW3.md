---
tag: BS7NSJFFW3
kind: definition
name: Bring radical
msc: ["12E12", "33E20"]
defines: BSDCDJR6RQ
uses: [00EHX6FWC0]
sources:
  - url: https://en.wikipedia.org/wiki/Bring_radical
---

## Definition

Let $a \in \R$.
The *Bring radical* of $a$, written $\operatorname{BR}(a)$, is the unique real [[root|00EHX6FWC0]] of the polynomial $x^5 + x + a$.

## Remarks

The definition makes sense: $g(x) = x^5 + x + a$ is strictly increasing on $\R$, since $g'(x) = 5x^4 + 1 > 0$, and it tends to $\pm\infty$ as $x \to \pm\infty$, so it has exactly one real root.
Example: $\operatorname{BR}(-2) = 1$, since $1^5 + 1 - 2 = 0$; and $\operatorname{BR}(0) = 0$.
Non-example: for the polynomial $x^5 - x + a$, the derivative $5x^4 - 1$ changes sign, and for $a = 0$ there are three real roots $-1, 0, 1$, so no "unique real root" is defined in the same way.
The function $\operatorname{BR}$ is odd, continuous and strictly decreasing on $\R$.
