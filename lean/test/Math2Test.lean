import Math2

/-!
# Golden tests of the m2 attribute

`lake test` builds this file. Each `#guard_msgs` block fails the build when the messages change.
-/

open Math2.Meta

/-- info: true -/
#guard_msgs in
#eval isTag "7K3QX2"

/-- info: true -/
#guard_msgs in
#eval isTag ("~" ++ "3fa94c01")

/-- info: false -/
#guard_msgs in
#eval isTag "7K3QXI"

/-- info: false -/
#guard_msgs in
#eval isTag ("~" ++ "3FA94C01")

/-- error: "7K3" is not a tag or a provisional id. -/
#guard_msgs in
@[m2 "7K3"] theorem bad_tag : True := trivial

/-- error: Math2.Match.lagrange is already bound to 3C53TD. -/
#guard_msgs in
attribute [m2 "7K3QX2"] Math2.Match.lagrange

/-- info: [(`Math2.Match.lagrange, "3C53TD")] -/
#guard_msgs in
#eval return (bindings (← Lean.getEnv)).toList.map fun (b : Binding) => (b.decl, b.tag)
