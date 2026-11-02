---
tag: D3A9V8DKZV
kind: example
name: Capacity of a disc and a segment
msc: [31A15, 30C85]
illustrates: [DBQXRTC0VN, V0SH1DY9FJ]
uses: [DBQXRTC0VN, DMNN7E2BYA, V0SH1DY9FJ, M6EAR1JHPP]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_radius
---

## Example

Let $D_r$ be the closed disc of radius $r > 0$ and let $S_L$ be a closed segment of length $L > 0$ in $\C$.
Their [[logarithmic capacities|DBQXRTC0VN]] are
$$\operatorname{cap}(D_r) = r, \qquad \operatorname{cap}(S_L) = L/4.$$

Check for the disc, with the [[Chebyshev constant|DMNN7E2BYA]].
Translate the disc so that its centre is $0$; capacity does not change under translations.
For a monic polynomial $p(z) = z^n + a_{n-1} z^{n-1} + \cdots + a_0$, Parseval's identity on the circle $\abs{z} = r$ gives
$$\frac{1}{2\pi} \int_0^{2\pi} \abs{p(r e^{i\theta})}^2 \, d\theta = r^{2n} + \sum_{k < n} \abs{a_k}^2 r^{2k} \ge r^{2n}.$$
So $\max_{D_r} \abs{p} \ge r^n$, with equality for $p = z^n$.
Hence the Chebyshev constant is $r$, and by the [[equality of capacity and Chebyshev constant|V0SH1DY9FJ]] the capacity is $r$.

Check for the segment.
Move it by a rotation and a translation to $[-L/2, L/2]$, which does not change capacity.
For $[-1, 1]$, the monic [[Chebyshev polynomial|M6EAR1JHPP]] $2^{1-n} T_n$ has maximum $2^{1-n}$ on the interval, and no monic polynomial of degree $n$ has a smaller maximum there.
So the Chebyshev constant of $[-1, 1]$ is $\lim_n (2^{1-n})^{1/n} = 1/2$.
Capacity scales linearly, so the segment of length $L$ has capacity $(L/2) \cdot (1/2) = L/4$.

The two results show that capacity is not a measure of area.
The segment has area zero but positive capacity $L/4$.
The disc of diameter $L$ has capacity $L/2$.

## Explanations

### L1 human

A disc of radius $r$ has capacity $r$, the same as its boundary circle, because the charge in equilibrium sits on the edge anyway.
A segment of length $L$ has capacity $L/4$.
So a thin segment can hold charge, unlike a single point, but it holds less than the disc whose diameter it is.
The computation uses the fact that capacity equals the Chebyshev constant, which is easy to find for these two shapes.
