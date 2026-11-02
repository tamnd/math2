---
tag: VS2PSX14C8
kind: concept
name: Complete elliptic integral of the second kind
msc: ["33E05"]
specializes: [NXMCYGCB59]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_integral
    locator: Complete elliptic integral of the second kind
---

## Summary

The complete elliptic integral of the second kind is the function $E(k) = \int_0^{\pi/2} \sqrt{1 - k^2\sin^2\theta}\,d\theta$ of the modulus $k$.
It gives the perimeter of an ellipse: an ellipse with semi-major axis $a$ and eccentricity $e$ has perimeter $4aE(e)$.
Together with the [[complete integral of the first kind|RM54CPPE12]] it enters [[Legendre's relation|8GSKDNZ4TK]].

## Explanations

### L1 human

A circle of radius $a$ has perimeter $2\pi a$, but there is no such simple formula for an ellipse.
The perimeter of an ellipse is four times the length of a quarter arc, and the quarter arc is $a E(e)$.
For a circle $e = 0$, and $E(0) = \pi/2$ gives back $2\pi a$.
For a flat ellipse squeezed to a segment of length $2a$, $e = 1$ and $E(1) = 1$, so the perimeter is $4a$, the segment traced there and back.
