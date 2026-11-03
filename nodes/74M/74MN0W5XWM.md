---
tag: 74MN0W5XWM
kind: concept
name: Harmonic analysis on the adeles
msc: [11R56, 43A25, 11F70]
specializes: [5E6KB3V8R0]
sources:
  - url: https://en.wikipedia.org/wiki/Adele_ring
---

## Summary

Harmonic analysis on the adeles is Fourier analysis on the [[adele ring|SEH68BA1QQ]] $\mathbb{A}_K$ of a number field $K$, seen as a [[locally compact abelian group|ZR09S9R3AW]].
It rests on three facts.
The group $\mathbb{A}_K$ carries a [[Haar measure|VY0HXD3GC4]].
It is isomorphic to its own [[Pontryagin dual|FMW57WNPDB]] through a character that is trivial on $K$.
The subgroup $K$ is discrete, and the quotient $\mathbb{A}_K / K$ is compact.
These facts give a [[Poisson summation formula|GARGJYSGFG]] for the lattice $K$ in $\mathbb{A}_K$.
This is the method of [[Tate's thesis|QYW79XKJTP]], which proves the functional equations of the L-functions of [[Hecke characters|R65XKHN4D1]].
It is also the setting of the modern theory of [[automorphic forms|3C73HND6XA]].

## Explanations

### L1 human

The adeles of $\Q$ put the real numbers and all the $p$-adic numbers side by side in one big ring.
Fourier analysis works on each of these pieces separately, and harmonic analysis on the adeles glues the pieces into one theory.
The rational numbers sit inside the adeles like the integers sit inside the real line: as a discrete grid with a compact quotient.
So the classical sum $\sum_{n \in \Z} f(n) = \sum_{n \in \Z} \widehat{f}(n)$ has an adelic analogue, a sum over all rational numbers.
For example, the function that is the Gaussian $e^{-\pi x^2}$ at the real place and the indicator of $\Z_p$ at each prime $p$ is its own Fourier transform.
Summing it over $\Q$ only picks up the integers, because a rational number lies in every $\Z_p$ exactly when it is an integer.
Replacing $e^{-\pi x^2}$ by $e^{-\pi t x^2}$ for $t > 0$, the adelic formula becomes the classical theta identity $\sum_{n \in \Z} e^{-\pi t n^2} = t^{-1/2} \sum_{n \in \Z} e^{-\pi n^2 / t}$.
