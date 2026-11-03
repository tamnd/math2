---
tag: 3HWDYB2FJ3
kind: definition
name: Radar cross-section
msc: [78A45, 78A50]
defines: 8W1NT1V97S
uses: [8BQYB8H5CT, NM024G378A]
sources:
  - url: https://en.wikipedia.org/wiki/Radar_cross_section
---

## Definition

Let a bounded target be illuminated by a time-harmonic electromagnetic [[plane wave|NM024G378A]] with electric field amplitude $\abs{E_i}$.
Let $E_s(R\hat{x})$ be the scattered electric field at distance $R$ from the target in the direction $\hat{x}$.
The *radar cross-section* in the direction $\hat{x}$ is
$$\sigma(\hat{x}) = \lim_{R \to \infty} 4\pi R^2 \frac{\abs{E_s(R\hat{x})}^2}{\abs{E_i}^2}.$$
It is *monostatic* when $\hat{x}$ points back toward the transmitter, and *bistatic* otherwise.

## Remarks

The limit exists because the scattered field decays like $1/R$ in the far field.
In terms of the far-field vector amplitude $F$, with $E_s(R\hat{x}) \approx F(\hat{x}) e^{ikR}/R$, one has $\sigma(\hat{x}) = 4\pi \abs{F(\hat{x})}^2 / \abs{E_i}^2$.
It is often given in decibels relative to one square metre (dBsm).

Example: a perfectly conducting sphere of radius $a \gg \lambda$ has monostatic radar cross-section close to $\pi a^2$.
A flat perfectly conducting plate of area $A$, large compared with $\lambda^2$, seen at normal incidence has $\sigma \approx 4\pi A^2 / \lambda^2$.
For $A = 1$ m$^2$ and $\lambda = 3$ cm this is about $1.4 \times 10^4$ m$^2$, far larger than the physical area.

Non-example: the quantity $4\pi R^2 \abs{E_s}^2 / \abs{E_i}^2$ at a fixed finite distance $R$ in the near field is not the radar cross-section, since it still depends on $R$.
