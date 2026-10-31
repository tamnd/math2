---
records:
    - id: 3SD22Z0DCX
      kind: monograph
      title: 'Algebraic Combinatorics: Walks, Trees, Tableaux, and More'
      creators:
        - name: Richard P. Stanley
          role: author
      date: "2013"
      expressions:
        - key: e1
          kind: edition
          date: "2013"
          ids:
            doi:
                - 10.1007/978-1-4614-6998-8
                - 10.1007/978-3-319-77173-1
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2013"
              ids:
                isbn:
                    - "9781461469971"
                    - "9781461469988"
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2018"
              ids:
                isbn:
                    - "9783319771724"
                    - "9783319771731"
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4614-6998-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-77173-1
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
