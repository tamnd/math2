---
tag: ~8ee3dcf9
kind: statement
role: theorem
name: Liouville's formula
aliases: [abel-jacobi-liouville-identity]
msc: [34A30]
uses: [~65b51670, ~ffb8bb7b]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%27s_formula
    locator: Statement of Liouville's formula
same_as:
  wikidata: Q1827325
  wikipedia: Liouville's formula
---

## Statement

Let $I$ be an open interval, let $A : I \to \mathbb{R}^{n \times n}$ be continuous, and let $\Phi : I \to \mathbb{R}^{n \times n}$ be a differentiable function with $\Phi'(t) = A(t)\, \Phi(t)$ for each $t \in I$.
Then for each $t_0, t \in I$,
$$\det \Phi(t) = \det \Phi(t_0)\, \exp\left( \int_{t_0}^{t} \operatorname{tr} A(s)\, ds \right),$$
where $\operatorname{tr} A(s)$ is the trace of $A(s)$.

## Remarks

So $\det \Phi(t)$ is zero at each point of $I$ or at no point of $I$. This shows that a [[fundamental matrix|~65b51670]] is invertible everywhere if it is invertible at one point.
For a constant matrix $A$, the formula gives $\det e^{tA} = e^{t \operatorname{tr} A}$.
For the system that comes from $y'' + p y' + q y = 0$, the trace is $-p$, and the formula is [[Abel's identity|~91dbf9e4]].

## Explanations

### L1 human

The determinant of $\Phi$ is the volume spanned by $n$ solutions.
The formula says how this volume changes in time: its rate of growth is the trace of $A$.
