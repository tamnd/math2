---
tag: 32VAKG7CPS
kind: definition
name: Minimal model program
msc: ["14E30"]
defines: Q8CTDCZH01
uses: [A4H4CZ2V35, W05VYY4HBR, RZ66X0NAM5, KA5890R9YM, ZJSW0HP75H, WJ5WRGG5DE]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_model_program
---

## Definition

Let $X$ be a normal [[projective variety|A4H4CZ2V35]] over a field of characteristic $0$ with $\Q$-factorial terminal singularities.
Let $K_X$ be its canonical divisor, the divisor class of the [[canonical bundle|W05VYY4HBR]].
The variety $X$ is a *minimal model* if $K_X$ is [[nef|RZ66X0NAM5]].
The *minimal model program* applied to $X$ is the following procedure.

1. If $K_X$ is nef, stop: $X$ is a minimal model.
2. Otherwise, by the [[cone theorem|ZJSW0HP75H]] there is an extremal ray $R$ of the closed cone of curves of $X$ with $K_X \cdot R < 0$.
   It has a contraction $\varphi_R \colon X \to Z$ of exactly the curves whose classes lie in $R$.
3. If $\dim Z < \dim X$, stop: $\varphi_R$ is a *Mori fibre space*.
4. If $\varphi_R$ is [[birational|KA5890R9YM]] and its exceptional locus is a divisor, replace $X$ by $Z$ and go back to step 1.
5. If $\varphi_R$ is birational and its exceptional locus has codimension at least $2$, replace $X$ by the flip $X^+$ of $\varphi_R$.
   Then go back to step 1.

## Remarks

In steps 4 and 5 the new variety again has $\Q$-factorial terminal singularities, which is why the program allows these singularities.
The program terminates when there is no infinite sequence of flips.
Flips exist in all dimensions by a theorem of Birkar, Cascini, Hacon and McKernan, and termination of flips is known in low dimensions, including dimension $3$, but open in general.
Example: for a smooth projective surface, there are no small contractions, and step 4 contracts a $(-1)$-curve by [[Castelnuovo's contraction theorem|WJ5WRGG5DE]].
The surface $\mathbb{P}^2$ is not a minimal model, since $K_{\mathbb{P}^2} \cdot \ell = -3 < 0$ for a line $\ell$.
The program stops at step 3 for it, with $Z$ a point, so $\mathbb{P}^2$ is a Mori fibre space.
A smooth curve of genus $g \ge 1$ is a minimal model, since $\deg K = 2g - 2 \ge 0$.
