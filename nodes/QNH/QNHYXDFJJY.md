---
tag: QNHYXDFJJY
kind: concept
name: Prolate spheroidal wave functions
msc: ["33E10", "42A38", "94A12"]
sources:
  - url: https://en.wikipedia.org/wiki/Prolate_spheroidal_wave_function
same_as:
  wikidata: Q7249549
  wikipedia: Prolate spheroidal wave function
---

## Summary

The prolate spheroidal wave functions are the bounded solutions on $[-1, 1]$ of a second-order differential equation that arises from separating variables in prolate spheroidal coordinates.
D. Slepian and H. O. Pollak found that the same functions are eigenfunctions of a time and band limiting operator.
This operator first restricts a function to $[-1, 1]$ and then removes all frequencies outside a fixed band.
So they are the [[band-limited functions|P3T104G564]] that are most concentrated on an interval.
They answer the question of how much of its energy a band-limited signal can keep in a given time window.
They are used in signal processing and spectral estimation.
See the [[definition|SDYEK7HEZQ]].

## Explanations

### L1 human

No nonzero signal can be both limited in time and limited in frequency.
One can still ask which band-limited signal puts as large a share of its energy as possible inside a given time interval.
The answer is the first prolate spheroidal wave function; the next ones give the best signals that are orthogonal to the previous ones.
When the product of the time interval and the frequency band is large, many of them keep almost all their energy inside the interval.
Their number is roughly proportional to that product.
