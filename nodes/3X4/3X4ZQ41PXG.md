---
tag: 3X4ZQ41PXG
kind: problem
name: Ten martini problem
msc: [47B36, 81Q10, 47A10]
uses: [D08SKTH2T2, BMKATJ802A]
about: [D08SKTH2T2]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_Mathieu_operator
history:
  posed_by: Barry Simon
  first_stated: "1982"
---

## Problem

For real numbers $\lambda, \alpha, \theta$, let $H_{\lambda,\alpha,\theta}$ be the [[almost Mathieu operator|D08SKTH2T2]] on $\ell^2(\Z)$.
A Cantor set in $\R$ is a nonempty compact set with no isolated points and with empty interior.
Is the [[spectrum|BMKATJ802A]] of $H_{\lambda,\alpha,\theta}$ a Cantor set for every irrational $\alpha$, every $\lambda \ne 0$ and every $\theta$?

## Remarks

The answer is yes.
Avila and Jitomirskaya proved it in a paper titled "The Ten Martini Problem", published in the Annals of Mathematics in 2009.
Before that, Bellissard and Simon showed that the spectrum is a Cantor set for a generic set of pairs $(\lambda, \alpha)$.
The name comes from Mark Kac, who offered ten martinis for a solution; Barry Simon gave the problem this name in his list of problems on almost periodic Schrödinger operators.

## Explanations

### L1 human

A Cantor set is like the [[middle-thirds Cantor set|0BXNDZFQME]]: a closed set full of gaps at every scale, with no intervals inside it and no isolated points.
The problem asks whether the possible energies of an electron in a quasi-periodic chain always form such a set.
Its solution shows that quasi-periodicity, however weak, breaks the spectrum into infinitely many pieces at every scale.
