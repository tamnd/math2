---
tag: 0FF2FJ8CH2
kind: statement
role: theorem
name: Universal property of the quotient topology
msc: [54B15]
uses: [0V8046R0P9, 0SY9ECQ19Q, 07HF9YCWPP]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(topology)
    locator: Properties
---

## Statement

Let $X$ be a [[topological space|0CNQXVBHCX]], let $\sim$ be an equivalence relation on $X$, and give $X / {\sim}$ the [[quotient topology|0V8046R0P9]], with quotient map $q \colon X \to X / {\sim}$.
Let $Y$ be a topological space and let $g \colon X / {\sim} \to Y$ be a function.
Then $g$ is [[continuous|0SY9ECQ19Q]] if and only if the [[composition|07HF9YCWPP]] $g \circ q \colon X \to Y$ is continuous.

## Remarks

Proof of the converse: for $V$ open in $Y$, the set $q^{-1}(g^{-1}(V)) = (g \circ q)^{-1}(V)$ is open in $X$. Thus $g^{-1}(V)$ is open in the quotient.
So each continuous map $f \colon X \to Y$ that is constant on each class gives a unique continuous map $g$ with $f = g \circ q$.
For example, $t \mapsto (\cos 2\pi t, \sin 2\pi t)$ is constant on the classes of $\mathbb{R} / \mathbb{Z}$, so it gives a continuous map from $\mathbb{R} / \mathbb{Z}$ to the circle.

## Explanations

### L1 human

To define a continuous map on a quotient space, define a continuous map on the original space that takes the same value on glued points.
The map then passes to the quotient.
