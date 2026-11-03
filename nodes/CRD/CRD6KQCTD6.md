---
tag: CRD6KQCTD6
kind: example
name: Mixmaster universe
msc: ["83F05", "83C75", "83C15"]
instance_of: [H7PS83YCER]
uses: [Q86TANYYX4, JRNNE88P5F, 45AE2YXWT3, 04P2RJ4WPS]
sources:
  - url: https://en.wikipedia.org/wiki/Mixmaster_universe
same_as:
  wikidata: Q3551264
  wikipedia: Mixmaster universe
---

## Example

Let $\omega^1, \omega^2, \omega^3$ be left-invariant one-forms on the group $SU(2) \cong S^3$.
Assume $d\omega^1 = \omega^2 \wedge \omega^3$ and its cyclic permutations.
Then their dual vector fields span the Lie algebra of [[Bianchi type IX|Q86TANYYX4]].
The *mixmaster universe* is the family of vacuum metrics, with $\Lambda = 0$, of the form
$$ds^2 = -dt^2 + a(t)^2 (\omega^1)^2 + b(t)^2 (\omega^2)^2 + c(t)^2 (\omega^3)^2$$
on $I \times S^3$.
Here $a, b, c$ are positive functions of $t$, and the speed of light is $1$.
The Einstein equations reduce to a system of ordinary differential equations for $a$, $b$ and $c$.

Check that each slice $t = \text{const}$ is homogeneous.
The left-invariant forms are invariant under the left action of $SU(2)$ on itself.
This action is transitive, so it gives isometries of the metric that move any point of a slice to any other.
When $a = b = c$ the slices are round three-spheres, as in a closed Friedmann–Lemaître–Robertson–Walker model; in general they are anisotropic.

## Remarks

Toward the initial [[singularity|45AE2YXWT3]], a generic solution passes through an infinite sequence of epochs.
In each epoch it is close to a [[Kasner metric|JRNNE88P5F]] with exponents
$$p_1 = \frac{-u}{1 + u + u^2}, \qquad p_2 = \frac{1 + u}{1 + u + u^2}, \qquad p_3 = \frac{u(1 + u)}{1 + u + u^2},$$
for a parameter $u \ge 1$; one checks $p_1 + p_2 + p_3 = 1$ and $p_1^2 + p_2^2 + p_3^2 = 1$.
In the approximation of Belinski, Khalatnikov and Lifshitz, one epoch follows another by $u \mapsto u - 1$ while $u \ge 2$, and a new era begins by $u \mapsto 1/(u - 1)$ when $1 < u < 2$.
So the lengths of the successive eras are the partial quotients of the [[continued fraction|04P2RJ4WPS]] expansion of the initial $u$, which makes the dynamics chaotic.
The name was given by Charles Misner.

## Explanations

### L1 human

The mixmaster universe is a closed universe that is the same at every place but expands at different rates in different directions.
Going back toward the Big Bang, it does not shrink smoothly: it oscillates, squeezing in one direction while stretching in another, and then switching directions, infinitely many times.
The pattern of switches follows the digits of a continued fraction, so it looks random.
It is the standard example of chaotic behaviour near a cosmological singularity.
