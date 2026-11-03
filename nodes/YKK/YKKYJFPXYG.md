---
tag: YKKYJFPXYG
kind: object
name: International Geomagnetic Reference Field
msc: [86A25, 33C55]
uses: [PGPW2Y7GPD, Z13HPJFV1F, JXVMPHF681]
sources:
  - url: https://en.wikipedia.org/wiki/International_Geomagnetic_Reference_Field
same_as:
  wikidata: Q3656071
  wikipedia: International Geomagnetic Reference Field
---

## Description

The *International Geomagnetic Reference Field* (IGRF) is a standard mathematical model of the main part of [[Earth's magnetic field|Z13HPJFV1F]].
It is issued by the International Association of Geomagnetism and Aeronomy (IAGA).
It gives the internal potential in the form of [[Gauss's spherical harmonic analysis|PGPW2Y7GPD]]:
$$V(r, \theta, \phi, t) = a \sum_{n=1}^{N} \sum_{m=0}^{n} \Bigl(\frac{a}{r}\Bigr)^{n+1} \bigl(g_n^m(t) \cos m\phi + h_n^m(t) \sin m\phi\bigr) P_n^m(\cos\theta).$$
Here $a = 6371.2$ km is the reference radius, and $P_n^m$ are the Schmidt semi-normalised associated Legendre functions.
The field is $B = -\nabla V$.
The coefficients are tabulated at epochs five years apart and interpolated linearly in time between them.
For the most recent epoch, the model gives [[secular variation|JXVMPHF681]] coefficients $\dot g_n^m, \dot h_n^m$, and $g_n^m(t) = g_n^m(T_0) + (t - T_0)\, \dot g_n^m$ for the following five years, and likewise for $h_n^m$.
For epochs from 2000 on, the main field is truncated at degree $N = 13$, which gives $N(N + 2) = 195$ coefficients per epoch.
The secular variation is truncated at degree $8$, and earlier epochs use degree $10$ for the main field.

## Remarks

The count of coefficients follows from $\sum_{n=1}^{N} (2n + 1) = N^2 + 2N$.
The model is revised every five years, using observatory and satellite data, and earlier provisional epochs are replaced by definitive ones when better data become available.
The truncation at degree $13$ removes most of the crustal field, which dominates the spectrum at higher degrees.
The IGRF is used for navigation, for removing the main field from magnetic survey data, and for computing geomagnetic coordinates.

## Explanations

### L1 human

The IGRF is a table of numbers agreed by geophysicists worldwide, from which anyone can compute the Earth's magnetic field at any place and date.
It packs the field into about two hundred coefficients of spherical harmonics per date, and it is updated every five years because the field slowly changes.
