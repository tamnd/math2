---
records:
    - id: F1CEGF3RZE
      kind: monograph
      title: Algebra
      creators:
        - name: Serge Lang
          role: author
      date: "2002"
      expressions:
        - key: e1
          kind: edition
          date: "2002"
          ids:
            doi: 10.1007/978-1-4613-0041-0
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2002"
              ids:
                isbn:
                    - "9781461265511"
                    - "9781461300410"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4613-0041-0
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: F1CYVYK7YB
      kind: preprint
      title: Ehrhart Properties under Operations on Lattice Polytopes
      creators:
        - name: Feihu Liu
          role: author
      date: "2026-10-05"
      subjects:
        - system: arxiv
          code: math.HO
        - system: arxiv
          code: math.CO
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-05"
          ids:
            arxiv: "2610.06338"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.06338"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
