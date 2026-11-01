---
tag: GQ0X3R3WM2
kind: concept
name: Toeplitz operator
msc: [47B35, 30H10]
sources:
  - url: https://en.wikipedia.org/wiki/Toeplitz_operator
same_as:
  wikidata: Q7812935
  wikipedia: Toeplitz operator
---

## Summary

A Toeplitz operator on the [[Hardy space|PNNNFJVF6W]] $H^2$ multiplies a function by a bounded symbol $\varphi$ on the circle and then projects back onto $H^2$.
In the basis $1, z, z^2, \ldots$ its matrix is the infinite [[Toeplitz matrix|GKY2WSHE26]] of the Fourier coefficients of $\varphi$, constant along diagonals.
Toeplitz operators link operator theory with complex analysis: their spectra, Fredholm indices and invertibility are read from the symbol.

## Explanations

### L1 human

Think of $H^2$ as the functions on the circle whose Fourier series has no negative terms.
Multiplying by a function $\varphi$ may create negative terms, so you throw them away.
What remains is the Toeplitz operator $T_\varphi$.
With $\varphi(e^{it}) = e^{it}$ nothing is thrown away and $T_\varphi$ is the shift $f \mapsto z f$.
With $\varphi(e^{it}) = e^{-it}$ the constant term is lost and one gets the backward shift.
