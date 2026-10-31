---
records:
    - id: TJKBDR3S78
      kind: monograph
      title: Introduction to the Mathematics of Finance
      creators:
        - name: Steven Roman
          role: author
      date: "2004"
      expressions:
        - key: e1
          kind: edition
          date: "2004"
          ids:
            doi:
                - 10.1007/978-1-4419-9005-1
                - 10.1007/978-1-4614-3582-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2004"
              ids:
                isbn:
                    - "9780387213644"
                    - "9781441990051"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2012"
              ids:
                isbn:
                    - "9781461435815"
                    - "9781461435822"
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
          native_id: 10.1007/978-1-4419-9005-1
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4614-3582-2
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
