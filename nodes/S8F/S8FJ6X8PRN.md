---
tag: S8FJ6X8PRN
kind: definition
name: Toda bracket
msc: [55Q35, 55Q45]
defines: 30K7VF7QBB
uses: [T9DG8DDE75, SMEV5BSQ5S, F2F143KQ2M, 2VD7GR64JJ]
sources:
  - url: https://en.wikipedia.org/wiki/Toda_bracket
---

## Definition

Let $W$, $X$, $Y$, $Z$ be [[pointed spaces|T9DG8DDE75]], and let $f \colon W \to X$, $g \colon X \to Y$, $h \colon Y \to Z$ be pointed maps such that $g \circ f$ and $h \circ g$ are [[null-homotopic|SMEV5BSQ5S]].
Let $CW = (W \times [0, 1]) / (W \times \set{1} \cup \set{w_0} \times [0, 1])$ be the reduced cone on $W$, with $W$ included as $W \times \set{0}$.

1. Choose a pointed null-homotopy of $g \circ f$, that is, a map $A \colon CW \to Y$ that restricts to $g \circ f$ on $W$.
2. Choose a pointed null-homotopy of $h \circ g$, that is, a map $B \colon CX \to Z$ that restricts to $h \circ g$ on $X$.
3. The maps $h \circ A \colon CW \to Z$ and $B \circ Cf \colon CW \to Z$ both restrict to $h \circ g \circ f$ on $W$.
   Gluing them along $W$ gives a map from two cones on $W$ glued along their bases, which is the reduced [[suspension|2VD7GR64JJ]] $\Sigma W$, to $Z$.

The *Toda bracket* $\langle h, g, f \rangle$ is the set of [[homotopy classes|F2F143KQ2M]] of all maps $\Sigma W \to Z$ obtained in this way, over all choices of $A$ and $B$.

## Remarks

Changing the choices of $A$ and $B$ changes the result by an element of $h_* [\Sigma W, Y] + (\Sigma f)^* [\Sigma X, Z]$.
This subgroup of $[\Sigma W, Z]$ is the *indeterminacy*, and $\langle h, g, f \rangle$ is a coset of it.
The bracket depends only on the homotopy classes of $f$, $g$, $h$.

Example: in the stable homotopy groups of spheres, let $2$ denote twice the identity and $\eta$ the stable Hopf map in degree $1$.
Then $2 \eta = 0$, so $\langle 2, \eta, 2 \rangle$ is defined, and it equals $\set{\eta^2}$ in degree $2$.

Non-example: for the identity $\iota$ of $S^n$, the composite $\iota \circ \iota$ is not null-homotopic, so $\langle \iota, \iota, \iota \rangle$ is not defined.

Some authors use the opposite order of the gluing, which changes the bracket by a sign.
