module

public import Math2.Cert.Interval
public import Math2.Cert.LRAT
public import Math2.Cert.Pratt
public import Math2.Meta.Attr
public import Math2.Meta.Match

/-!
# Math2

This is the root module of the math2 Lean library.

The library holds only the statements and proofs that Mathlib does not have. A node that Mathlib already proves has no Lean code here. It has only a binding in its node file.

The files in `Math2/Cert/` are checkers of certificates, each with a proof that it is sound. A computation node uses them to reach E5.

Each file in this library is a module. Do not add a file without the `module` header.
-/
