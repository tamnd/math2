---
tag: ZKP5KGFWCK
kind: counterexample
name: Enflo's counterexample to the approximation problem
msc: [46B28, 46B15]
uses: [06GZ956657, 8CKE0V6ANK]
sources:
  - url: https://en.wikipedia.org/wiki/Per_Enflo
  - url: https://en.wikipedia.org/wiki/Approximation_property
---

## Counterexample

There is a separable [[Banach space|06GZ956657]] $X$ that does not have the [[approximation property|8CKE0V6ANK]].
That is, there are a compact set $K \subseteq X$ and $\varepsilon > 0$ with the following property.
Every continuous linear map $T \colon X \to X$ of finite rank satisfies $\norm{Tx - x} \ge \varepsilon$ for some $x \in K$.
Per Enflo constructed such a space; his paper appeared in Acta Mathematica in 1973.

## Remarks

The construction is an explicit but intricate combinatorial one, built from finite-dimensional blocks; it is not short enough to reproduce here.
It has two famous consequences.
First, $X$ has no Schauder basis, because a space with a Schauder basis has the approximation property.
So the basis problem, whether every separable Banach space has a Schauder basis, has a negative answer.
Second, by Grothendieck's work on the approximation property, some compact operator into $X$ is not a norm limit of finite-rank operators.
Later work showed that the spaces $\ell^p$ with $p \ne 2$ contain closed subspaces without the approximation property.

## Explanations

### L1 human

For a long time it was hoped that every reasonable Banach space could be described by coordinates, like the sequence spaces.
It was also hoped that every compact operator was a limit of matrices.
Enflo's space shows that both hopes are false.
It is a separable Banach space where the identity cannot be imitated on compact sets by finite-rank maps.
